#!/usr/bin/env python

# Software License Agreement (BSD License)

#

# Copyright (c) 2008, Willow Garage, Inc.

# All rights reserved.

#

# Redistribution and use in source and binary forms, with or without

# modification, are permitted provided that the following conditions

# are met:

#

#  * Redistributions of source code must retain the above copyright

#    notice, this list of conditions and the following disclaimer.

#  * Redistributions in binary form must reproduce the above

#    copyright notice, this list of conditions and the following

#    disclaimer in the documentation and/or other materials provided

#    with the distribution.

#  * Neither the name of Willow Garage, Inc. nor the names of its

#    contributors may be used to endorse or promote products derived

#    from this software without specific prior written permission.

#

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS

# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT

# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS

# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE

# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,

# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,

# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;

# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER

# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT

# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN

# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE

# POSSIBILITY OF SUCH DAMAGE.

#

# Revision $Id$



## Simple talker demo that published std_msgs/Strings messages

## to the 'chatter' topic

import rospy
from std_msgs.msg import String
import homehabit_manager.msg
import os

def convert(dim):
	val = dim / 10
	arrondi = round(val*2)/2
	resultat = int(arrondi * 10)
	return resultat



def envoi_lamp(ids, dimming):
	tableau = ["L1","L2","L3","L4","L"]
	i = 0
	dim_arrondi = convert(dimming)
	while i<5:
		if ids == tableau[i]:
			dim_string = str(dim_arrondi)
			print"%s"%dim_string
			monstring = "NodeUtil -DFAEEA936 -I/home/tp/NodeUtilScript/"+ids+"_"+dim_string
			os.system(monstring)
		i += 1

def callback(data):
	rospy.loginfo(rospy.get_name() + "STATE: %s    |    ID: %s    |    MODE: %s    |    DIMMING: %s", data.State, data.Id, data.Mode,data.Dimming)
	if data.Mode == "auto":
		monstring = "NodeUtil -DFAEEA936 -I/home/tp/NodeUtilScript/Auto"
		os.system(monstring)
	elif data.Mode == "manuel":
		if data.State == "off":
			envoi_lamp(data.Id,0)
		elif data.State == "on":
			envoi_lamp(data.Id, data.Dimming)



def listener():
	rospy.Subscriber('/homehabit/lamp_control', homehabit_manager.msg.PowerControlMsg, callback)
	rospy.spin()



if __name__ == '__main__':
	rospy.init_node('lamp_listener', anonymous = True)
	listener()
