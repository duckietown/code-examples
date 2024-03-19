# DTProject - Examples

This repository is a collection of simple DTProjects that you can use as a starting point for the development of more complex behaviors for your Duckietown robots. For further information about what a DTProject is and how to use it, we suggest you follow 
the [official tutorial](https://docs.duckietown.com/daffy/devmanual-software/beginner/dtproject/index.html).


## Structure

Each directory in this repository contains an independent DTProject. Each project is built and executed the same way, the only thing that changes is the content of their `packages/` directory, which is the place where the specific behavior is implemented.

## Examples

A detailed list of the examples stored in this repository follows,


### ROS - Sensor - Camera (Make it see)

> **Location:** `./ros-sensor-camera` \
**Framework:** `ROS1` \
**Supported Robots:** Any \
**Supported OSs:** Linux, MacOS* \
---------------- \
![badge](https://shields.io/badge/status-ready-green?&style=plastic)

This example shows how to subscribe to a continuous stream of camera frames in ROS.

* **NOTE:** This example requires a window to be opened for the live stream to be shown. Some newer versions of MacOS will not support this.
