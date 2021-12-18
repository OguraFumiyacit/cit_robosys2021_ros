#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32


rospy.init_node('talker')
pub = rospy.Publisher('count_up',Int32, queue_size=1)
rate = rospy.Rate(1)
n = 0
while not rospy.is_shutdown():
    msg = Int32()
    msg.data = n
    pub.publish(n)
    count = 0
    n +=1
    with open('scripture.txt') as f:
        for line in f:
            count += 1
    if n >= count:
        n = 0
    rate.sleep()
