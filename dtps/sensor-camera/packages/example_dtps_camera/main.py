#!/usr/bin/env python3

import asyncio
import os

import cv2
from duckietown_messages.sensors import CompressedImage
from turbojpeg import TurboJPEG

from dt_robot_utils import get_robot_name
from dtps import DTPSContext, context
from dtps_http import RawData

# url
host: str = os.environ.get("HOST", f"{get_robot_name()}.local")
port: str = os.environ.get("PORT", "11511")

# constants
CAMERA_NAME: str = "front-center"

# JPEG decoder
JPEG = TurboJPEG()

# cv2 window
window = "example-sensor-camera"
cv2.namedWindow(window, cv2.WINDOW_AUTOSIZE)


async def callback(rd: RawData):
    # global frame
    jpeg: CompressedImage = CompressedImage.from_rawdata(rd)
    frame = JPEG.decode(jpeg.data)
    # display frame
    cv2.imshow(window, frame)
    cv2.waitKey(1)


async def main():
    # global frame
    robot_name: str = get_robot_name()
    url: str = f"http://{host}:{port}/"
    # initialize node
    print(f"Connecting to {url}...")
    cxt: DTPSContext = await context("robot", urls=[url])
    # setup camera listener
    camera: DTPSContext = cxt / robot_name / "sensor" / "camera" / CAMERA_NAME / "jpeg"
    await camera.subscribe(callback)
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
