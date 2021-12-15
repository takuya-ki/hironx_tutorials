#!/usr/bin/env python

import rospy
import moveit_commander


def main():
	rospy.init_node("moveit_command_sender")
	robot = moveit_commander.RobotCommander()
	head = moveit_commander.MoveGroupCommander("head")

	print " Robot Groups:"
	print robot.get_group_names()
	print ""
	print " Printing robot state"
	print robot.get_current_state()
	print ""

	print " Head "
	print " Reference frame: %s" % head.get_planning_frame()
	print " Reference frame: %s" % head.get_end_effector_link()
	print ""

	print "Initializing head pose"
	head.set_joint_value_target([0.0, 0.0])
	head.go()
	head_initial_joint = head.get_current_joint_values()
	print " Printing Head initial joint: "
	print head_initial_joint
	print ""

	print "Going to first pose"
	head.set_joint_value_target([0.0, 0.5])
	head.go()
	rospy.sleep(2)
	print ""

	print "Going to second pose"
	head.set_joint_value_target([0.5, -0.3])
	head.go()
	rospy.sleep(2)
	print ""

	print "Going to third pose"
	head.set_joint_value_target([-0.5, -0.3])
	head.go()
	rospy.sleep(2)
	print ""

	print "Going to fourth pose"
	head.set_joint_value_target([-0.5, 0.5])
	head.go()
	rospy.sleep(2)
	print ""

	print "Back to the Initial pose ..."
	head.set_joint_value_target(head_initial_joint)
	head.go()
	rospy.sleep(2)
	exit(0)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

