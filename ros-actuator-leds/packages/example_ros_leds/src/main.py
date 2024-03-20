#!/usr/bin/env python3

import time
from typing import List

import rospy
from duckietown_msgs.msg import LEDPattern
from std_msgs.msg import ColorRGBA

from dt_robot_utils import get_robot_name

# parameters
FREQUENCY: float = 1.0
INTENSITY: float = 0.25

# colors
OFF: ColorRGBA = ColorRGBA(0, 0, 0, INTENSITY)
COLOR_RED: ColorRGBA = ColorRGBA(1, 0, 0, INTENSITY)
COLOR_GREEN: ColorRGBA = ColorRGBA(0, 1, 0, INTENSITY)
COLOR_BLUE: ColorRGBA = ColorRGBA(0, 0, 1, INTENSITY)
COLOR_WHITE: ColorRGBA = ColorRGBA(1, 1, 1, INTENSITY)

RGB_AMBER: List[float] = [1, 0.75, 0]


def regular_pattern(publisher):
    publisher.publish(
        LEDPattern(
            rgb_vals=[
                # front-left
                COLOR_WHITE,
                # rear-left
                COLOR_RED,
                # front-middle (DB1X models only)
                OFF,
                # rear-right
                COLOR_RED,
                # front-right
                COLOR_WHITE,
            ]
        )
    )
    time.sleep(1)


def blinker():
    robot_name: str = get_robot_name()
    # initialize node
    rospy.init_node('blinker', anonymous=True)
    # setup camera listener
    publisher = rospy.Publisher(
        f"/{robot_name}/led_driver_node/led_pattern",
        LEDPattern,
        queue_size=1,
        tcp_nodelay=True,
    )
    # back to default when shutting down
    rospy.on_shutdown(lambda: regular_pattern(publisher))
    # blink
    dt: float = 1.0 / FREQUENCY
    bit: int = 0
    while not rospy.is_shutdown():
        intensity: float = bit * INTENSITY
        publisher.publish(
            LEDPattern(
                rgb_vals=[ColorRGBA(*RGB_AMBER, intensity)] * 5
            )
        )
        time.sleep(dt)
        bit = 1 - bit


if __name__ == '__main__':
    blinker()
