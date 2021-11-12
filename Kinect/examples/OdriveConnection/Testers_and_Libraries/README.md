# Azure-Maze-2.0
Kinetic Maze with Azure Kinect and Python Library


## TODO: This is an old README from [previous azure kinect repo](https://github.com/dpengineering/azure-maze). Update this README to reflect new installation instructions

Note that this is a Dos Pueblos Engineering Academy project, and it is assumed that this project is running with DPEA pre-configured software, such as the python interpreter and ssh configuration (if needed). Success outside of the DPEA is not guaranteed, however individual parts relating to the Azure Kinect should be able to run outside of the project.


## Installation ##
Instructions to install the Azure Kinect SDK are from microsoft, copied here for convinience.

1. Configure the Microsoft Package Repository, and install the Azure Kinect packages (tools, headers, and body tracking):
```
 sudo apt install curl
 curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
 sudo apt-add-repository https://packages.microsoft.com/ubuntu/18.04/prod
 sudo apt-get update
 sudo apt install k4a-tools
 sudo apt install libk4a1.4-dev
 sudo apt install libk4abt1.1-dev
```
Note: requires OpenGL 4.4 and above,

When installing Azure Kinect Samples (Git submodule info):
https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues/896

if device unavailable after compiling samples, run with sudo as rules not properly set.

```
pip3 install kivy
```

2. For kivy, Pidev must be installed from https://github.com/dpengineering/RaspberryPiCommon


## Azure Kinect on Linux ##
As most Microsoft documentation is windows based, Linux usage will be documented as thoroughly as possible for future use. In general, follow instructions in the Microsoft documentation.

To launch the Azure Kinect Viewer, run `k4aviewer` in the command line.

Joints: x,y,z, measured in mm from the lens of the camera.

## How to Run ##

**If motors are needed, uncomment the motor lines from main.py**

With two monitors:
Make a terminal window on both screens.

In vis_cpp_tracker, run the trackhands script in /build/bin. If this is not compiled, go to /build and run:
```
rm -r *
cmake ..
make
```
After compiling, follow the instructions from the beginning once more.

Run the script.

On the other terminal window (on the second monitor), run ```python3 main.py```.

With one monitor: change vis_cpp_tracker/libs/k4abt_libs/window_controller_3d/WindowController3d.h line 49 to bool fullscreen = false, then follow the instructions for two monitors.

One monitor can be used with fullscreen, however there will be no way to exit.

To reset the ODrive, wait for the fan on the power supply to stop before turning the power strip back on, to ensure power to the ODrive actually cut.

## Troubleshooting ##
If the kivy screen is white, make sure for borderless Kivy to change ~/.kivy/config.ini borderless to = 1, **not** = 0!



## Reference Links ##
[Azure Kinect Samples](https://github.com/microsoft/Azure-Kinect-Samples)

[Azure Kinect SDK](https://github.com/microsoft/Azure-Kinect-Sensor-SDK)

[Azure Kinect DK Documentation](https://docs.microsoft.com/en-us/azure/kinect-dk/)

[Body Tracking SDK Reference](https://microsoft.github.io/Azure-Kinect-Body-Tracking/release/1.x.x/index.html)

[Azure Kinect Sensor SDK Reference](https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/index.html)

Installing Azure Kinect SDK: https://docs.microsoft.com/en-us/azure/kinect-dk/sensor-sdk-download 
