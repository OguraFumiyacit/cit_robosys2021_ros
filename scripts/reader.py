#SPDX-License-Identifier: BSD-3.0
#Copyright (C) 2021 Fumiya Ogura, Ryuichi ueda. All rights reserved.


#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def cb(message):
    rospy.loginfo(message.data)
    #f = open('scripture.txt', 'r')
    #global n
    #n = message.data
    #str = f.readlines()[n]
    #print(str)


if __name__ == '__main__':
    rospy.init_node('reader')
    sub = rospy.Subscriber('count_up', String, cb)
    rospy.spin()
