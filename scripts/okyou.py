#!/usr/bin/env python3
import rospy
#from std_msgs.msg import String
from std_msgs.msg import Int32


rospy.init_node('okyou')
#pub = rospy.Publisher('input_data', String, queue_size=1)
pub = rospy.Publisher('input_data',Int32, queue_size=1)
rate = rospy.Rate(1)
n = 0

while not rospy.is_shutdown():
    #f = open('kyoten.txt', 'r')
    #str = f.readline()
    #if str == '':
    #    break
    #pub.publish(str.rstrip('\n'))
    #f.close()
    msg = Int32()
    msg.data = n
    pub.publish(n)
    n += 1
    rate.sleep()
    if n >= 17:
        n = 0
