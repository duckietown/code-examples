# Example: ROS - Sensor - Camera

This example shows how to read a robot's wheel encoder data in ROS.

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

You should see the number of wheel encoder ticks printed to the console. Try rotating the wheels of the robot to see 
the number of ticks increase.

**NOTE:** When you rotate the wheels, the number of ticks will only increase regardless of the direction of rotation. 
The robot normally uses the commanded command as a proxy for the direction of rotation. 
