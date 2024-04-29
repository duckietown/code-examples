# Example: DTPS - Actuator - Wheels

This example shows how to control a vehicle's motors via DTPS.

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


### 2.1 Run against the Duckiematrix

If you want this example to connect to an instance of the Duckiematrix instead of a physical robot, find the
port number the instance of the Duckiematrix you are running is using as shown in the image below and then add
`-- -e PORT=<PORT_NUMBER>` to the `dts devel run` command above
(for example, in the example in the image below, we would add `-- -e PORT=40295`).

<p align="center" style="padding: 12px 40px 0 40px; border-left: 5px solid grey">
  <img src="./docs/figures/dtps-server-port.png" alt="Find the duckiematrix DTPS port to use"/>
</p>


## 3. Expected Result

The motors should spin forward for 5 seconds.