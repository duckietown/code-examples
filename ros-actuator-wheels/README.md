# Example: ROS - Actuator - LEDs

This example shows how to control a vehicle's lights via ROS.

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

You should see the LEDs of the robot turn amber and start blinking with a frequency of 1 Hz. 
On exit (CTRL-C), the initial pattern of white in the front and red in the back will be restored. 
