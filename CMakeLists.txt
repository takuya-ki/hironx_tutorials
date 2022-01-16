cmake_minimum_required(VERSION 2.8.3)
project(hironx_stack)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  moveit_core
  moveit_ros_planning_interface
  tf
)

catkin_package(
  CATKIN_DEPENDS
    rospy
    std_msgs
    geometry_msgs
    moveit_core
    moveit_ros_planning_interface
    tf
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/head_banging.py scripts/turn_waist.py scripts/move_arms.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
