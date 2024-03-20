cmake_minimum_required(VERSION 2.8.3)
project(example_ros_display)

find_package(catkin REQUIRED COMPONENTS
  rospy
  duckietown_msgs
  sensor_msgs
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)
