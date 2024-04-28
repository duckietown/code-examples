#!/usr/bin/env python3

import os
import time
import asyncio

from duckietown_messages.actuators import DifferentialPWM

from dt_robot_utils import get_robot_name
from dtps import DTPSContext, context, PublisherInterface

# url
host: str = os.environ.get("HOST", f"{get_robot_name()}.local")
port: str = os.environ.get("PORT", "11511")

# constants
WHEELS_NAME: str = "base"
DURATION: float = 5.


async def main():
    # global frame
    robot_name: str = get_robot_name()
    url: str = f"http://{host}:{port}/"
    # initialize node
    print(f"Connecting to {url}...")
    cxt: DTPSContext = await context("robot", urls=[url])
    # setup wheels publisher
    wheels: PublisherInterface = await (cxt / robot_name / "actuator" / "wheels" / WHEELS_NAME / "pwm").publisher()
    # duty cycle at 50%
    pwm = 0.5
    # publish for 5 seconds then exit
    stime = time.time()
    try:
        while time.time() - stime <= DURATION:
            # publish
            await wheels.publish(DifferentialPWM(left=pwm, right=pwm).to_rawdata())
            await asyncio.sleep(1 / 30.)
    except asyncio.CancelledError:
        return


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
