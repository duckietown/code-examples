# Example: ROS - Sensor - Camera

This example shows how to measure the distance to the closest object using a robot's time-of-flight sensor in ROS.

## 1. Build

Build this project using the command,

```shell
dts devel build
```

## 2. Run

Run the project using the command,

```shell
dts devel run -R [ROBOT_NAME]
```

**NOTE:** Make sure to replace `[ROBOT_NAME]` with the name of the robot you are using in the commands above.


### Expected Result

You should see the distance to the nearest obstacle in front of the robot printed to the console. When no obstacle
is detected, the message `"Too-far"` will be printed instead.
