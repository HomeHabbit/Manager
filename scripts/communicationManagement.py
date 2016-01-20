#!/usr/bin/env python


## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from manager.msg import GeneralPurposeCmd

def callback(data):
    print("yessssssss !")
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node so that multiple talkers can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("publication", GeneralPurposeCmd, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
