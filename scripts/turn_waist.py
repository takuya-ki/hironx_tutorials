#!/usr/bin/env python

import rospy
import moveit_commander


def main():
	rospy.init_node("moveit_command_sender")
	robot = moveit_commander.RobotCommander()
	torso = moveit_commander.MoveGroupCommander("torso")

	print " Robot Groups:"
	print robot.get_group_names()
	print ""
	print " Printing robot state"
	print robot.get_current_state()
	print ""

	print " Waist "
	print " Reference frame: %s" % torso.get_planning_frame()
	print " Reference frame: %s" % torso.get_current_joint_values()
	print ""

	print "Initializing waist pose"
	torso.set_joint_value_target([0.0])
	torso.go()
	torso_initial_joint = torso.get_current_joint_values()
	print " Printing torso initial joint: "
	print torso_initial_joint
	print ""

	print "Turnning waist to the left"
	torso.set_joint_value_target([0.5])
	torso.go()
	rospy.sleep(3)
	print ""

	print "Turnning waist to the right"
	torso.set_joint_value_target([-0.5])
	torso.go()
	rospy.sleep(3)
	print ""

	print "Back to the Initial pose ..."
	torso.set_joint_value_target(torso_initial_joint)
	torso.go()
	rospy.sleep(2)
	exit(0)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

