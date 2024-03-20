# Example: ROS - Actuator - Display

This example shows how to display a message on a robot's LCD screen in ROS.

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

You should see a circle appear on the display of the robot.
On exit (CTRL-C), the circle will disappear within 1 second. 
