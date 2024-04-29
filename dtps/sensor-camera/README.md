# Example: DTPS - Sensor - Camera

This example shows how to subscribe to a continuous stream of camera frames via DTPS.

## 1. Build

Build this project using the command,

```shell
dts devel build
```

## 2. Run

Run the project using the command,

```shell
dts devel run -X -R [ROBOT_NAME]
```

**NOTE:** Make sure to replace `[ROBOT_NAME]` with the name of the robot you are using in the commands above.

**NOTE:** The `-X` flag is used to give the project permissions to open a window to show the camera feed.


### 2.1 Run against the Duckiematrix

If you want this example to connect to an instance of the Duckiematrix instead of a physical robot, find the
port number the instance of the Duckiematrix you are running is using as shown in the image below and then add
`-- -e PORT=<PORT_NUMBER>` to the `dts devel run` command above
(for example, in the example in the image below, we would add `-- -e PORT=40295`).

<p align="center" style="padding: 12px 40px 0 40px; border-left: 5px solid grey">
  <img src="./docs/figures/dtps-server-port.png" alt="Find the duckiematrix DTPS port to use"/>
</p>


## 3. Expected Result

You should see a window showing the live camera feed of the robot similar to the one below,

<p align="center">
  <img src="./docs/figures/live-stream-gui-window.png" alt="Live Stream Window"/>
</p>
