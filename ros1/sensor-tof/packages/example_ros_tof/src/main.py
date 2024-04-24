#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Range

from dt_robot_utils import get_robot_name

SENSOR_NAME: str = "front_center"


def callback(msg: Range):
    distance: str = f"{msg.range:.3f}m" if msg.range < msg.max_range else "Too-far"
    print(f"Range: {distance}")


def listener():
    robot_name: str = get_robot_name()
    # initialize node
    rospy.init_node('listener', anonymous=True)
    # setup tof listener
    rospy.Subscriber(
        f"/{robot_name}/{SENSOR_NAME}_tof_driver_node/range",
        Range,
        callback,
    )
    # keep the node alive
    rospy.spin()


if __name__ == '__main__':
    listener()
