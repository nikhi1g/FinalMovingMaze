# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from threading import Thread
from time import sleep
from odrive.enums import *  # enumerations, enums, gives each sensor numbers
import odrive
# buttons are actually buttons -1
from pidev.Joystick import Joystick
from ODrive_Ease_Lib import *

# variables
# findodrive
odboard = odrive.find_any(serial_number='208D3388304B')
odboard.clear_errors()
odboard1 = odrive.find_any(serial_number='2065339E304B')
odboard1.clear_errors()
# setup the Kinect

import sys
import time

import cv2
from pykinect_azure.k4abt._k4abtTypes import K4ABT_JOINT_NAMES

sys.path.insert(1, '../')
import pykinect_azure as pykinect
from pykinect_azure.k4a import _k4a
from pykinect_azure.k4abt import _k4abt

if __name__ == '__main__':

    # dumperrors
    dump_errors(odboard)
    # define ax and ay
    ax = ODrive_Axis(odboard.axis0, 15, 10)  # currentlim, vlim
    ay = ODrive_Axis(odboard.axis1, 40, 10)  # currentlim, vlim
    az = ODrive_Axis(odboard1.axis0, 15, 10)
    # calibrate
    if not ax.is_calibrated():  # calibrate x (left right)
        print("calibrating x...")
        ax.calibrate_with_current_lim(25)
    if not az.is_calibrated():  # calibrate z (left right)
        print("calibrating z...")
        az.calibrate_with_current_lim(25)
    # if not self.ay.is_calibrated(): #calibrate y (top bottom)
    #     print("calibrating y...")
    #     self.ay.calibrate_with_current(60)
    # odboard.save_configuration()
    # odboard.reboot()
    # COMMENCE THE GAINZ
    ax.gainz(20, 0.16, 0.32, False)
    az.gainz(20, 0.16, 0.32, False)
    odboard.clear_errors()

    ax.idle()
    ay.idle()
    az.idle()

    sleep(10)

    # initilize the Kinect

    # Initialize the library, if the library is not found, add the library path as argument
    pykinect.initialize_libraries(module_k4abt_path="/usr/lib/libk4abt.so", track_body=True)

    # Modify camera configuration
    device_config = pykinect.default_configuration
    device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_OFF
    device_config.depth_mode = pykinect.K4A_DEPTH_MODE_WFOV_2X2BINNED
    # print(device_config)

    # Start device
    device = pykinect.start_device(config=device_config)

    # Start body tracker
    bodyTracker = pykinect.start_body_tracker()

    cv2.namedWindow('Depth image with skeleton', cv2.WINDOW_NORMAL)
    # run the Kinect
    capture_list = []
    while True:

        # Get capture
        capture = device.update()

        # Get body tracker frame
        body_frame = bodyTracker.update()  # LOOK HERE

        # Get the color depth image from the capture
        ret, depth_color_image = capture.get_colored_depth_image()

        # Get the colored body segmentation
        ret, body_image_color = body_frame.get_segmentation_image()

        if not ret:
            continue

        # Combine both images
        combined_image = cv2.addWeighted(depth_color_image, 0.6, body_image_color, 0.4, 0)

        # Draw the skeletons
        combined_image = body_frame.draw_bodies(combined_image)  # LOOK HERE

        # Overlay body segmentation on depth image
        cv2.imshow('Depth image with skeleton', combined_image)

        # print(body_frame.get_segmentation_image())

        # raised hand around -1000~1000 units

        # print("Right Hand X:", body_frame.get_body_skeleton().joints[15].position.xyz.x)
        # body_num = body_frame.get_num_bodies()
        # close_body = 0
        # for body_num in range(body_frame.get_num_bodies()):
        #
        #     print("body", body_num, body_frame.get_body_skeleton(body_num).joints[26].position.xyz.z)
        #     if body_num == 0:
        #         pass
        #     else:
        #         if body_frame.get_body_skeleton(close_body).joints[26].position.xyz.z > body_frame.get_body_skeleton(body_num).joints[26].position.xyz.z:
        #             print("Current body is closest")
        #             close_body = body_num
        #         else:
        #             print("Previous body is closest")

        body_list = [body_frame.get_body_skeleton(body_num) for body_num in range(body_frame.get_num_bodies())]
        try:
            close_body = min(body_list, key=lambda body: body.joints[
                26].position.xyz.z)  # grabs the minimum body according to the head z depth
        except ValueError:
            close_body = None

        if close_body != None:
            rightz = close_body.joints[15].position.xyz.z
            leftz =close_body.joints[8].position.xyz.z

            righthand = close_body.joints[15].position.xyz.x
            lefthand = close_body.joints[8].position.xyz.x

            righthandy = close_body.joints[15].position.xyz.y
            lefthandy = close_body.joints[8].position.xyz.y


            if lefthandy < -400 and righthandy > -100:
                print("to the LEFT!")
                ax.set_vel(3)

            if lefthandy > -100 and righthandy < -400:
                print("to the RIGHT!")
                ax.set_vel(-3)

            if -400 < lefthandy < -100 and -400 < righthandy < -100:
                print("in the MIDDLE!")
                ax.set_vel(0)
                # stop if leave the frame
            if righthand < -700 or righthand > 700:
                print("Stopping because righthand left the frame")
                ax.set_vel(0)
            if lefthand < -700 or lefthand > 700:
                print("Stopping because lefthand left the frame")
                ax.set_vel(0)

            print("RightZ:", rightz)
            print("LeftX:", lefthand)
            print("RightX:", righthand)
        # IT WORKS! TILTING MOVES IT!!!
        # yooo this is lit

        # golden

        # golden

        # try to return the nunbodies within 900

        # depthtesting


        # if leftz > 1300:
        #     print("Up?")
        #     ay.set_ramped_vel(.8, .5)
        #
        # if leftz < 800:
        #     print("Down?")
        #     ay.set_ramped_vel(-.8, .5)
        #
        # if 800 < leftz < 1300:
        #     print("Stop?")
        #     ay.set_ramped_vel(0, .5)

        # print("Left", leftz)
        # print("")
        # print("Right", rightz)
        _k4a.k4a_capture_release(capture.handle())
        _k4abt.k4abt_frame_release(body_frame.handle())

        # numbxerbodies = []
        # min = None
        #
        # for bodies in numberbodies:
                # body_frame.get_body_skeleton().joints[26].position.xyz.z = bodies()
            # get.z.skel1
            # get.z.skel2

        if cv2.waitKey(1) == ord('q'):
            ax.set_vel(0)
            ax.idle()
            break

            # append the images to the array. if the array is == 3000, then run a whilie loop that clear the array according the handle's id.

# odrv0 208D3388304B
# odrv1 2065339E304B


# Odrv1 = odrive.find_any(serial_number=serial1)
# Odrv2 = odrive.find_any(serial_number=serial2)
