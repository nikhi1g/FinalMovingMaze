import sys
import cv2
from pykinect_azure.k4a import _k4a
from pykinect_azure.k4abt import _k4abt

from time import sleep
sys.path.insert(1, '../')
import pykinect_azure as pykinect

if __name__ == "__main__":

	# Initialize the library, if the library is not found, add the library path as argument
	pykinect.initialize_libraries(module_k4abt_path="/usr/lib/libk4abt.so", track_body=True)

	# Modify camera configuration
	device_config = pykinect.default_configuration
	device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_1080P
	device_config.depth_mode = pykinect.K4A_DEPTH_MODE_WFOV_2X2BINNED
	#print(device_config)

	# Start device
	device = pykinect.start_device(config=device_config)

	# Start body tracker
	bodyTracker = pykinect.start_body_tracker()

	cv2.namedWindow('Color image with skeleton',cv2.WINDOW_NORMAL)
	capture_list = []
	while True:
		
		# Get capture
		capture = device.update()

		# Get body tracker frame
		body_frame = bodyTracker.update()

		# Get the color image
		ret, color_image = capture.get_color_image()

		if not ret:
			continue

		# Draw the skeletons into the color image
		color_skeleton = body_frame.draw_bodies(color_image, pykinect.K4A_CALIBRATION_TYPE_COLOR)

		# Overlay body segmentation on depth image
		cv2.imshow('Color image with skeleton',color_skeleton)

		# close_body = 0
		# for body_num in range(body_frame.get_num_bodies()):
		#
		# 	print("body", body_num, body_frame.get_body_skeleton(body_num).joints[26].position.xyz.z)
		# 	if body_num == 0:
		# 		pass
		# 	else:
		# 		if body_frame.get_body_skeleton(close_body).joints[26].position.xyz.z > body_frame.get_body_skeleton(body_num).joints[26].position.xyz.z:
		# 			print("Current body is closest")
		# 			close_body = body_num
		# 		else:
		# 			print("Previous body is closest")
		# print("Closest z: ", body_frame.get_body_skeleton(close_body).joints[26].position.xyz.z)

		body_list = [body_frame.get_body_skeleton(body_num) for body_num in range(body_frame.get_num_bodies())]
		try:
			close_body = min(body_list, key=lambda body: body.joints[26].position.xyz.z)#grabs the minimum body according to the head z depth
		except ValueError:
			close_body = None

		_k4a.k4a_capture_release(capture.handle())
		_k4abt.k4abt_frame_release(body_frame.handle())
		# capture_list.append(body_frame.get_capture().handle())
		#
		# if len(capture_list) == 1200:
		# 	for handle_to_delete in capture_list:
		# 		print(handle_to_delete)
		# 		_k4a.k4a_capture_release(handle_to_delete)
		# 	capture_list.clear()


		# Press q key to stop
		if cv2.waitKey(1) == ord('q'):  
			break