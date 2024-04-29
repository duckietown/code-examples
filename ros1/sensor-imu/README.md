# Example: ROS - Sensor - IMU

This example shows how to read a robot's IMU data in ROS.

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


## 3. Expected Result

You should see the inertia measurements performed by the IMU aboard the robot printed to the console.
The detected temperature will also be printed.
