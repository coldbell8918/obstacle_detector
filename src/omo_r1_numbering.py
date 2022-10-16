#!/usr/bin/env python3
import rospy

from obstacle_detector.msg import Obstacles
from geometry_msgs.msg import Twist
from obstacle_detector.msg import human
import math

def callback(data):
    cnt=0
    n=len(data.circles)
    # rospy.loginfo(n) #  장애물 개수
    for i in range (0,n):
        v_x=data.circles[i].velocity.x
        v_y=data.circles[i].velocity.y
        c_x=data.circles[i].center.x
        c_y=data.circles[i].center.y
        if cnt==0:
            c_x_p=c_x
            c_y_p=c_y
        if pow(pow(c_x-c_x_p,2)+pow(c_y-c_y_p,2),0.5)<=0.5:
            pub(n, data.circles[i])

        c_x_p=c_x
        c_y_p=c_y
    cnt+=1

             
def listener():

    rospy.Subscriber("/obstacles", Obstacles, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def pub(n, circle):
    pub=rospy.Publisher("/number", human, queue_size=10)
    obstacle=human
    for i in range (0,n):
        obstacle.id[i]=i+1
        obstacle.circles[i].velocity.x= circle.velocity.x
        obstacle.circles[i].velocity.y=circle.velocity.y
        obstacle.circles[i].center.x=circle.center.x
        obstacle.circles[i].center.y=circle.center.y
    pub.publish(obstacle)

if __name__ == '__main__':
    rospy.init_node('obstacle_number', anonymous=True)
    listener()