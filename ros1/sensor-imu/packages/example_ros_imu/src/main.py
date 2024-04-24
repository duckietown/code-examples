#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu, Temperature

from dt_robot_utils import get_robot_name


def data_callback(msg: Imu):
    print("""
Linear Acceleration:\n{0}

Angular Velocity:\n{1}
""".format(msg.linear_acceleration, msg.angular_velocity))


def temperature_callback(msg: Temperature):
    print(f"Temperature: {msg.temperature}")


def listener():
    robot_name: str = get_robot_name()
    # initialize node
    rospy.init_node('listener', anonymous=True)
    # setup imu listeners
    rospy.Subscriber(
        f"/{robot_name}/imu_node/data",
        Imu,
        data_callback,
    )
    rospy.Subscriber(
        f"/{robot_name}/imu_node/temperature",
        Temperature,
        temperature_callback,
    )
    # keep the node alive
    rospy.spin()


if __name__ == '__main__':
    listener()
