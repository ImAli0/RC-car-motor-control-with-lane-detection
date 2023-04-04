# RC-car-motor-control-with-lane-detection

Project: RC Car Motor Control with Lane Detection powered by Raspberry Pi

Objective:
To develop a system using Raspberry Pi to control the motors of an RC car based on lane detection.

Requirements:

    Raspberry Pi (Model 3 or later)
    Pi Camera
    RC car kit
    L293D motor driver
    Jumper wires
    Breadboard
    OpenCV library
    Python programming language
    Internet connectivity

Steps:

    Connect the L293D motor driver to the Raspberry Pi using jumper wires and a breadboard.
    Connect the motors of the RC car to the motor driver.
    Connect the Pi camera to the Raspberry Pi.
    Install the OpenCV library on the Raspberry Pi.
    Develop a Python program to capture frames from the Pi camera and perform lane detection using OpenCV.
    Once the lanes are detected, calculate the error between the center of the lanes and the center of the frame.
    Use the error to adjust the speed and direction of the RC car motors.
    Repeat steps 5-7 for each frame captured by the Pi camera.

Implementation:

    Connect the L293D motor driver to the Raspberry Pi using the following wiring:

    Raspberry Pi L293D

    GPIO 17 (3.3V) -> Enable 1
    GPIO 27 -> Input 1
    GPIO 22 -> Input 2
    GPIO 23 -> Input 3
    GPIO 24 -> Input 4
    GPIO GND -> GND
    VCC (5V) -> VCC1 and VCC2

    Connect the motors of the RC car to the motor driver.

    Connect the Pi camera to the Raspberry Pi.

    Install the OpenCV library on the Raspberry Pi using the following command:

    sudo apt-get install libopencv-dev python-opencv

    Develop a Python program to capture frames from the Pi camera and perform lane detection using OpenCV.
