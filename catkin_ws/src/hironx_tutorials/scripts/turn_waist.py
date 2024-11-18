#!/usr/bin/env python

import rospy
import moveit_commander


def turn_waist():
    """Turn waist."""
    rospy.init_node("moveit_command_sender")
    robot = moveit_commander.RobotCommander()
    torso = moveit_commander.MoveGroupCommander("torso")

    rospy.loginfo("Initializing waist pose...")
    torso.set_joint_value_target([0.0])
    torso.go()
    torso_initial_joint = torso.get_current_joint_values()

    rospy.loginfo("Turnning waist to the left...")
    torso.set_joint_value_target([0.5])
    torso.go()
    rospy.sleep(rospy.Duration.from_sec(3))

    rospy.loginfo("Turnning waist to the right...")
    torso.set_joint_value_target([-0.5])
    torso.go()
    rospy.sleep(rospy.Duration.from_sec(3))

    rospy.loginfo("Back to the initial poses.")
    torso.set_joint_value_target(torso_initial_joint)
    torso.go()
    rospy.sleep(rospy.Duration.from_sec(2))


if __name__ == '__main__':
    try:
        turn_waist()
    except rospy.ROSInterruptException:
        pass
