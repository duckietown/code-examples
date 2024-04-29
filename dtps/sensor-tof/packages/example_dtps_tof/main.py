#!/usr/bin/env python3

import asyncio
import os

from duckietown_messages.sensors import Range

from dt_robot_utils import get_robot_name
from dtps import DTPSContext, context
from dtps_http import RawData

# url
host: str = os.environ.get("HOST", f"{get_robot_name()}.local")
port: str = os.environ.get("PORT", "11511")

# constants
SENSOR_NAME: str = "front_center"


async def callback(rd: RawData):
    msg: Range = Range.from_rawdata(rd)
    distance: str = f"{msg.data:.3f}m" if msg.data else "Too-far"
    print(f"Range: {distance}")


async def main():
    # global frame
    robot_name: str = get_robot_name()
    url: str = f"http://{host}:{port}/"
    # initialize node
    print(f"Connecting to {url}...")
    cxt: DTPSContext = await context("robot", urls=[url])
    # setup tof listener
    tof: DTPSContext = cxt / robot_name / "sensor" / "time_of_flight" / SENSOR_NAME / "range"
    await tof.subscribe(callback)
    # keep the node alive
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        return


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
