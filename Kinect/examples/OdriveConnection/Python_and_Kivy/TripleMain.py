# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from threading import Thread
from time import sleep
import time
from odrive.enums import *  # enumerations, enums, gives each sensor numbers
import odrive
# buttons are actually buttons -1
# from pidev.Joystick import Joystick
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

sys.path.insert(1, '../../')
import pykinect_azure as pykinect
from pykinect_azure.k4a import _k4a
from pykinect_azure.k4abt import _k4abt

# Kivy Imports



from threading import Thread
from time import sleep
import keyboard
# from datetime import datetime
import pyautogui

# time = datetime



KinectIsOn = True
kivyIsOn = False
time_start = time.time()
TimerRunning = True
seconds = 0




def timer_update():
    global seconds
    global TimerRunning
    while TimerRunning:
        print(seconds)
        print(' ')
        print(' ')
        time.sleep(1)
        seconds = int(time.time() - time_start)


def Kivy_Update():
    print("You have reached a new high score, enter your name:")
    print("Seconds Passed:", seconds)
    file = open('../Testers_and_Libraries/secondsstorage.txt', 'a')
    file.write(str(seconds))
    file.close()
    global TimerRunning
    TimerRunning = False

    # https://stackoverflow.com/questions/56711424/how-can-i-count-time-in-python-3


if __name__ == '__main__':

    # dumperrors
    dump_errors(odboard)
    # define ax and ay
    ax = ODrive_Axis(odboard.axis0, 15, 10)  # currentlim, vlim
    ay = ODrive_Axis(odboard.axis1, 40, 16)  # currentlim, vlim
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
    axisshortcut = az.axis
    # homing_sensor_prox
    odboard1.config.gpio8_mode = GPIO_MODE_DIGITAL
    axisshortcut.min_endstop.config.gpio_num = 2  # pin 8 for x, 2 for y, 2 for z
    Prox_Sensor_Number = axisshortcut.min_endstop.config.gpio_num  # setting to global class Runner variable just so that I can reference it in the Thread print statements
    axisshortcut.min_endstop.config.enabled = True  # Turns sensor on, says that I am using it
    axisshortcut.min_endstop.config.offset = 1  # stops 1 rotation away from sensor
    axisshortcut.min_endstop.config.debounce_ms = 20  # checks again after 20 milliseconds if actually pressed, which is what debounce is :D
    axisshortcut.min_endstop.config.offset = -1.0 * (
        8192)  # hop back from GPIO in order to allow for function again
    odboard1.config.gpio8_mode = GPIO_MODE_DIGITAL_PULL_DOWN

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

    # cv2.namedWindow('Depth image with skeleton', cv2.WINDOW_NORMAL)
    # run the Kinect
    capture_list = []

    Thread(target=timer_update).start()  # START TIM
    while True:

        # Get capture
        capture = device.update()

        # Get body tracker frame
        body_frame = bodyTracker.update()  # LOOK HERE

        # Get the color depth image from the capture
        # ret, depth_color_image = capture.get_colored_depth_image()

        # Get the colored body segmentation
        # ret, body_image_color = body_frame.get_segmentation_image()

        # if not ret:
        #     continue

        # Combine both images
        # combined_image = cv2.addWeighted(depth_color_image, 0.6, body_image_color, 0.4, 0)

        # Draw the skeletons
        # combined_image = body_frame.draw_bodies(combined_image)  # LOOK HERE

        # Overlay body segmentation on depth image
        # cv2.imshow('Depth image with skeleton', combined_image)
        if KinectIsOn:
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

            body_list = [body_frame.get_body_skeleton(body_num) for body_num in
                         range(body_frame.get_num_bodies())]  # le code
            try:
                close_body = min(body_list, key=lambda body: body.joints[
                    26].position.xyz.z)  # grabs the minimum body according to the head z depth
            except ValueError:
                close_body = None

            if close_body != None:
                rightz = close_body.joints[15].position.xyz.z
                leftz = close_body.joints[8].position.xyz.z

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
                    ay.set_vel(0)
                    # stop if leave the frame
                if righthand < -700 or righthand > 700:
                    print("Stopping because righthand left the frame")
                    ax.set_vel(0)

                if lefthand < -700 or lefthand > 700:
                    print("Stopping because lefthand left the frame")
                    ax.set_vel(0)
                #
                # #both hands are raised
                # if lefthandy < -200 and righthandy < -200:
                #     print("upwards")
                #     az.set_vel(4)
                # #both hands are lowered
                # if lefthandy > 200 and righthandy > 200:
                #     print("downwards")
                #     az.set_vel(-4)

                print("RightZ:", rightz)
                print("LeftY:", lefthandy)
                print("RightY:", righthandy)

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

            if az.axis.min_endstop.endstop_state:  # if switch, or in this case the prox is pressed
                # clear errors will get rid of freeze man
                print('Reached Prox on GPIO', Prox_Sensor_Number)
                dump_errors(odboard1)
                odboard1.clear_errors()
                sleep(3)
                Thread(target=Kivy_Update).start()
                sleep(1)
                KinectIsOn = False

# odrv0 208D3388304B
# odrv1 2065339E304B


# Odrv1 = odrive.find_any(serial_number=serial1)
# Odrv2 = odrive.find_any(serial_number=serial2)
