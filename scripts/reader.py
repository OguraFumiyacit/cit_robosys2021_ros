#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32


def cb(message):
    f = open('scripture.txt', 'r')
    global n
    n = message.data
    str = f.readlines()[n]
    print(str)


if __name__ == '__main__':
    rospy.init_node('reader')
    sub = rospy.Subscriber('count_up', Int32, cb)
    rospy.spin()