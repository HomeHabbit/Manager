#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def generalPurpose_callback(data):
	rospy.loginfo("Msg Received")

def listener():
	rospy.init_node("HomeHabit Manager", anonymous=True)
	rospy.Subscriber("HomeHabit_GeneralPurpose", String, generalPurpose_callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
