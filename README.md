# DTProject - Examples

This repository is a collection of simple DTProjects that you can use as a starting point for the development of more complex behaviors for your Duckietown robots. For further information about what a DTProject is and how to use it, we suggest you follow 
the [official tutorial](https://docs.duckietown.com/daffy/devmanual-software/beginner/dtproject/index.html).


## Structure

Each directory in this repository contains an independent DTProject. Each project is built and executed the same way, the only thing that changes is the content of their `packages/` directory, which is the place where the specific behavior is implemented.

## Examples

A detailed list of the examples stored in this repository follows,

---

### ROS - Sensor - Camera - (💬 Make it see)

This example shows how to subscribe to a continuous stream of camera frames via ROS.

> **Location:** [`./ros-sensor-camera/`](./ros-sensor-camera/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS* \
---------------- \
![badge](https://shields.io/badge/status-ready-green?&style=plastic)

* **NOTE:** This example requires a window to be opened for the live stream to be shown. Newer versions of MacOS do not support this.


---


### ROS - Actuator - LEDs - (💬 Make it blink)

This example shows how to control a vehicle's lights via ROS.

> **Location:** [`./ros-actuator-leds/`](./ros-actuator-leds/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux \
---------------- \
![badge](https://shields.io/badge/status-ready-green?&style=plastic)


---


### ROS - Actuator - Display (💬 Make it paint)

This example shows how to display a message on a robot's LCD screen in ROS.

> **Location:** [`./ros-actuator-display/`](./ros-actuator-display/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux \
---------------- \
![badge](https://shields.io/badge/status-ready-green?&style=plastic)



---


### ROS - Actuator - Wheels - (💬 Make it move)

This example shows how to control a vehicle's motors via ROS.

> **Location:** [`./ros-actuator-wheels/`](./ros-actuator-wheels/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux \
---------------- \
![badge](https://shields.io/badge/status-TODO-red?&style=plastic)


---


### ROS - Sensor - Time-of-Flight

This example shows how to measure the distance to the closest object using a robot's time-of-flight sensor in ROS.

> **Location:** [`./ros-sensor-tof/`](./ros-sensor-tof/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-ready-green?&style=plastic)


---


### ROS - Sensor - IMU

This example shows how to read a robot's IMU data in ROS.

> **Location:** [`./ros-sensor-imu/`](./ros-sensor-imu/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-ready-green?&style=plastic)


---


### ROS - Sensor - Power Button

This example shows how to detect the user input from a robot's power button in ROS.

> **Location:** [`./ros-sensor-button/`](./ros-sensor-button/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-ready-green?&style=plastic)


---


### ROS - Sensor - Wheel Encoder

This example shows how to read a robot's wheel encoder data in ROS.

> **Location:** [`./ros-sensor-wheel-encoder/`](./ros-sensor-wheel-encoder/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-ready-green?&style=plastic)