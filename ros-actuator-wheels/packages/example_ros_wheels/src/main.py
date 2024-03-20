#!/usr/bin/env python3

import time

import rospy
from duckietown_msgs.msg import WheelsCmdStamped

from dt_robot_utils import get_robot_name

# parameters
DURATION: float = 5.0
SPEED: float = 0.25


def stop_wheels(publisher):
    publisher.publish(WheelsCmdStamped(vel_left=0.0, vel_right=0.0))
    time.sleep(1)


def driver():
    robot_name: str = get_robot_name()
    # initialize node
    rospy.init_node('driver', anonymous=True)
    # setup publisher
    publisher = rospy.Publisher(
        f"/{robot_name}/wheels_driver_node/wheels_cmd",
        WheelsCmdStamped,
        queue_size=1,
        tcp_nodelay=True,
    )
    # stop wheels when shutting down
    rospy.on_shutdown(lambda: stop_wheels(publisher))
    # drive
    stime: float = time.time()
    while not rospy.is_shutdown() and time.time() - stime < DURATION:
        publisher.publish(WheelsCmdStamped(vel_left=SPEED, vel_right=SPEED))
        time.sleep(0.1)


if __name__ == '__main__':
    driver()
