#!/usr/bin/env python

import rospy
import moveit_commander


def head_banging():
    """Does head banging."""
    rospy.init_node("moveit_command_sender")
    robot = moveit_commander.RobotCommander()
    head = moveit_commander.MoveGroupCommander("head")

    rospy.loginfo("Initializing head pose...")
    head.set_joint_value_target([0.0, 0.0])
    head.go()
    head_initial_joint = head.get_current_joint_values()

    rospy.loginfo("Start head banging.")
    head.set_joint_value_target([0.0, 0.5])
    head.go()
    rospy.sleep(rospy.Duration.from_sec(2))

    head.set_joint_value_target([0.5, -0.3])
    head.go()
    rospy.sleep(rospy.Duration.from_sec(2))

    head.set_joint_value_target([-0.5, -0.3])
    head.go()
    rospy.sleep(rospy.Duration.from_sec(2))

    head.set_joint_value_target([-0.5, 0.5])
    head.go()
    rospy.sleep(rospy.Duration.from_sec(2))

    rospy.loginfo("Back to initial pose.")
    head.set_joint_value_target(head_initial_joint)
    head.go()
    rospy.sleep(rospy.Duration.from_sec(2))


if __name__ == '__main__':
    try:
        head_banging()
    except rospy.ROSInterruptException:
        pass
