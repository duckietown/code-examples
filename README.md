# Code Examples

This repository is a collection of simple DTProjects that you can use as a starting point for the development of more complex behaviors for your Duckietown robots. For further information about what a DTProject is and how to use it, we suggest you follow 
the [official tutorial](https://docs.duckietown.com/daffy/devmanual-software/beginner/dtproject/index.html).


## Content

Examples in this repository are implemented as independent DTProjects. These are then grouped together by framework.
Each project is built and executed the same way, the only thing that changes is the content of their `packages/` 
directory, which is the place where the specific behavior is implemented.

A detailed list of the examples stored in this repository follows,


## ROS1

---

### ROS1 - Sensor - Camera - (💬 Make it see)

This example shows how to subscribe to a continuous stream of camera frames via ROS1.

> **Location:** [`./ros1/sensor-camera/`](./ros1/sensor-camera/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS* \
---------------- \
![badge](https://shields.io/badge/status-untested-red?&style=plastic)

* **NOTE:** This example requires a window to be opened for the live stream to be shown. Newer versions of MacOS do not support this.


---


### ROS1 - Actuator - LEDs - (💬 Make it blink)

This example shows how to control a vehicle's lights via ROS1.

> **Location:** [`./ros1/actuator-leds/`](./ros1/actuator-leds/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux \
---------------- \
![badge](https://shields.io/badge/status-untested-red?&style=plastic)


---


### ROS1 - Actuator - Display (💬 Make it paint)

This example shows how to display a message on a robot's LCD screen in ROS1.

> **Location:** [`./ros1/actuator-display/`](./ros1/actuator-display/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux \
---------------- \
![badge](https://shields.io/badge/status-untested-red?&style=plastic)



---


### ROS1 - Actuator - Wheels - (💬 Make it move)

This example shows how to control a vehicle's motors via ROS1.

> **Location:** [`./ros1/actuator-wheels/`](./ros1/actuator-wheels/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux \
---------------- \
![badge](https://shields.io/badge/status-untested-red?&style=plastic)


---


### ROS1 - Sensor - Time-of-Flight

This example shows how to measure the distance to the closest object using a robot's time-of-flight sensor in ROS1.

> **Location:** [`./ros1/sensor-tof/`](./ros1/sensor-tof/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-untested-red?&style=plastic)


---


### ROS1 - Sensor - IMU

This example shows how to read a robot's IMU data in ROS1.

> **Location:** [`./ros1/sensor-imu/`](./ros1/sensor-imu/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-untested-red?&style=plastic)


---


### ROS1 - Sensor - Power Button

This example shows how to detect the user input from a robot's power button in ROS1.

> **Location:** [`./ros1/sensor-button/`](./ros1/sensor-button/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-untested-red?&style=plastic)


---


### ROS1 - Sensor - Wheel Encoder

This example shows how to read a robot's wheel encoder data in ROS1.

> **Location:** [`./ros1/sensor-wheel-encoder/`](./ros1/sensor-wheel-encoder/) \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-untested-red?&style=plastic)




## DTPS

---

### DTPS - Sensor - Camera - (💬 Make it see)

This example shows how to subscribe to a continuous stream of camera frames via DTPS.

> **Location:** [`./dtps/sensor-camera/`](./dtps/sensor-camera/) \
**Framework:** `DTPS` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS* \
---------------- \
![badge](https://shields.io/badge/status-todo-red?&style=plastic)

* **NOTE:** This example requires a window to be opened for the live stream to be shown. Newer versions of MacOS do not support this.


---


### DTPS - Actuator - LEDs - (💬 Make it blink)

This example shows how to control a vehicle's lights via DTPS.

> **Location:** [`./dtps/actuator-leds/`](./dtps/actuator-leds/) \
**Framework:** `DTPS` \
**Supported Robots:** Any \
**Supported OSs:** Linux \
---------------- \
![badge](https://shields.io/badge/status-todo-red?&style=plastic)


---


### DTPS - Actuator - Display (💬 Make it paint)

This example shows how to display a message on a robot's LCD screen in DTPS.

> **Location:** [`./dtps/actuator-display/`](./dtps/actuator-display/) \
**Framework:** `DTPS` \
**Supported Robots:** Any \
**Supported OSs:** Linux \
---------------- \
![badge](https://shields.io/badge/status-todo-red?&style=plastic)



---


### DTPS - Actuator - Wheels - (💬 Make it move)

This example shows how to control a vehicle's motors via DTPS.

> **Location:** [`./dtps/actuator-wheels/`](./dtps/actuator-wheels/) \
**Framework:** `DTPS` \
**Supported Robots:** Any \
**Supported OSs:** Linux \
---------------- \
![badge](https://shields.io/badge/status-todo-red?&style=plastic)


---


### DTPS - Sensor - Time-of-Flight

This example shows how to measure the distance to the closest object using a robot's time-of-flight sensor in DTPS.

> **Location:** [`./dtps/sensor-tof/`](./dtps/sensor-tof/) \
**Framework:** `DTPS` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-todo-red?&style=plastic)


---


### DTPS - Sensor - IMU

This example shows how to read a robot's IMU data in DTPS.

> **Location:** [`./dtps/sensor-imu/`](./dtps/sensor-imu/) \
**Framework:** `DTPS` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-todo-red?&style=plastic)


---


### DTPS - Sensor - Power Button

This example shows how to detect the user input from a robot's power button in DTPS.

> **Location:** [`./dtps/sensor-button/`](./dtps/sensor-button/) \
**Framework:** `DTPS` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-todo-red?&style=plastic)


---


### DTPS - Sensor - Wheel Encoder

This example shows how to read a robot's wheel encoder data in DTPS.

> **Location:** [`./dtps/sensor-wheel-encoder/`](./dtps/sensor-wheel-encoder/) \
**Framework:** `DTPS` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS \
---------------- \
![badge](https://shields.io/badge/status-todo-red?&style=plastic)
