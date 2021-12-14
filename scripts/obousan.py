#!/usr/bin/env python3
import rospy
#from std_msgs.msg import String
from std_msgs.msg import Int32
def cb(message):
    #rospy.loginfo(message.data)
    f = open('kyoten.txt', 'r')
    global n
    n = message.data
    str = f.readlines()[n]
    print(str)
    
    #elif message.data == 1:
        #str = f.readlines()[1]
        #print(str)


if __name__ == '__main__':
    rospy.init_node('obousan')
    #sub = rospy.Subscriber('input_data', String, cb)
    sub = rospy.Subscriber('input_data', Int32, cb)
    rospy.spin()
