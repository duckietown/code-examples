#!/usr/bin/env python3

import cv2
import numpy as np
import rospy
from sensor_msgs.msg import CompressedImage
from turbojpeg import TurboJPEG

from dt_robot_utils import get_robot_name

# camera info
WIDTH: int = 640
HEIGHT: int = 480
SIZE_4MB: int = 4 * 1024 * 1024

# JPEG decoder
jpeg = TurboJPEG()

# create empty matplot window
window = "example-sensor-camera"
cv2.namedWindow(window, cv2.WINDOW_AUTOSIZE)


def callback(msg: CompressedImage):
    frame: np.ndarray = jpeg.decode(msg.data)
    # display frame
    cv2.imshow(window, frame)
    cv2.waitKey(1)


def listener():
    robot_name: str = get_robot_name()
    # initialize node
    rospy.init_node('listener', anonymous=True)
    # setup camera listener
    rospy.Subscriber(
        f"/{robot_name}/camera_node/image/compressed",
        CompressedImage,
        callback,
        buff_size=SIZE_4MB,
        queue_size=1
    )
    # keep the node alive
    rospy.spin()


if __name__ == '__main__':
    listener()
