#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import WheelEncoderStamped

from dt_robot_utils import get_robot_name

SIDE: str = "left"


def callback(msg: WheelEncoderStamped):
    print(f"#ticks: {msg.data}")


def listener():
    robot_name: str = get_robot_name()
    # initialize node
    rospy.init_node('listener', anonymous=True)
    # setup wheel_encoder listener
    rospy.Subscriber(
        f"/{robot_name}/{SIDE}_wheel_encoder_driver_node/tick",
        WheelEncoderStamped,
        callback,
    )
    # keep the node alive
    rospy.spin()


if __name__ == '__main__':
    listener()
