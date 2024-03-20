#!/usr/bin/env python3

from typing import Dict

import rospy
from duckietown_msgs.msg import ButtonEvent

from dt_robot_utils import get_robot_name

EVENTS: Dict[int, str] = {
    1: "SINGLE_CLICK",
    3: "HELD_3SEC",
    10: "HELD_10SEC",
}


def callback(msg: ButtonEvent):
    event: str = EVENTS.get(msg.event, "UNKNOWN")
    print(f"Event: {event}")


def listener():
    robot_name: str = get_robot_name()
    # initialize node
    rospy.init_node('listener', anonymous=True)
    # setup button listener
    rospy.Subscriber(
        f"/{robot_name}/button_driver_node/event",
        ButtonEvent,
        callback,
    )
    # keep the node alive
    rospy.spin()


if __name__ == '__main__':
    listener()
