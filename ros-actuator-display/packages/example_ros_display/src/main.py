#!/usr/bin/env python3

import time

import cv2
import numpy as np
import rospy
from cv_bridge import CvBridge
from duckietown_msgs.msg import DisplayFragment
from sensor_msgs.msg import RegionOfInterest

from dt_robot_utils import get_robot_name

# display regions
"""
|-----------------------|
|        128x16         |        Region: HEADER   Color: Yellow
|-----------------------|
|                       |
|        128x44         |        Region: BODY     Color: Blue
|-----------------------|
"""


def main():
    robot_name: str = get_robot_name()
    bridge = CvBridge()
    # initialize node
    rospy.init_node('painter', anonymous=True)
    # setup publisher
    publisher = rospy.Publisher(
        f"/{robot_name}/display_driver_node/fragments",
        DisplayFragment,
        queue_size=1,
    )
    # create empty image (128x44, for the BODY region)
    img: np.ndarray = np.zeros((44, 128), dtype=np.uint8)
    # center of the BODY region
    center_coordinates = (64, 22)
    radius = 15
    thickness = 2
    # draw a circle at the center of the region
    img = cv2.circle(img, center_coordinates, radius, 255, thickness)
    # paint the display
    while not rospy.is_shutdown():
        publisher.publish(
            DisplayFragment(
                id="example",
                region=DisplayFragment.REGION_BODY,
                page=DisplayFragment.PAGE_ALL,
                data=bridge.cv2_to_imgmsg(img, encoding="mono8"),
                location=RegionOfInterest(width=128, height=44, x_offset=0, y_offset=0),
                # z-index
                z=99,
                # expires after 1 second
                ttl=1,
            )
        )
        time.sleep(0.25)


if __name__ == '__main__':
    main()
