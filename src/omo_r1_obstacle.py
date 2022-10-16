#!/usr/bin/env python3
import rospy

from obstacle_detector.msg import Obstacles
from geometry_msgs.msg import Twist

def callback(data):
    # rospy.loginfo(data.circles[1].center.x)
    n=len(data.circles)
    # rospy.loginfo(n) #  장애물 개수
    for i in range (0,n):
        v_x=data.circles[i].velocity.x
        v_y=data.circles[i].velocity.y
        c_x=data.circles[i].center.x
        c_y=data.circles[i].center.y

        v=pow(pow(v_x,2)+pow(v_y,2),0.5)

        if v >= 0.03:
            if c_x >=0:
                if c_y >=0:
                    cmd(0, -0.2)
                else:
                    cmd(0,0.2)
            else:
                if c_y >=0:
                    if c_y <=0.1:
                        cmd(0.2,0)
                        if c_x >=-0.5:
                            cmd(0,0)
                    else:
                        cmd(0, -0.2)
                else:
                    if c_y >= -0.1:
                        cmd(0.2,0)
                        if c_x >=-0.5:
                            cmd(0,0)
                    else:
                        cmd(0,0.2)

            # if c_y >= 0:
            #     if c_y<=0.1:
            #         if c_x>=-0.5 and c_x<=0:
            #             cmd(0,0)
            #         else:
            #             cmd(0.2,0)
            #     else:
            #         if c_x>=-0.5 and c_x<=0:
            #             cmd(0,0)
            #         else:
            #             cmd(0, -0.2)
            # else:
            #     if c_y>=-0.1:
            #         if c_x>=-0.5 and c_x<=0:
            #             cmd(0,0)
            #         else:
            #             cmd(0.2,0)
            #     else:
            #         if c_x>=-0.5 and c_x<=0:
            #             cmd(0, 0)
            #         else:
            #             cmd(0, 0.2)

        # elif v_y >= 0.05 or v_y <= -0.05:

        #     # d=pow(pow(c_x,2)+pow(c_y,2),0.5)
        #     # rospy.loginfo(d)
        #     if c_x >=0:
        #         if c_y >=0:
        #             cmd(0, -0.2)
        #         else:
        #             cmd(0,0.2)
        #     else:
        #         if c_y >=0:
        #             if c_y <=0.1:
        #                 cmd(0.2,0)
        #                 if c_x >=-0.5:
        #                     cmd(0,0)
        #             else:
        #                 cmd(0, -0.2)
        #         else:
        #             if c_y >= -0.1:
        #                 cmd(0.2,0)
        #                 if c_x >=-0.5:
        #                     cmd(0,0)
        #             else:
        #                 cmd(0,0.2)
            
            # if c_y >= 0:
            #     if c_y<=0.1:
            #         if c_x>=-0.5 and c_x<=0:
            #             cmd(0,0)
            #         else:
            #             cmd(0.2,0)
            #     else:
            #         if c_x>=-0.5 and c_x<=0:
            #             cmd(0,0)
            #         else:
            #             cmd(0, -0.2)
            # else:
            #     if c_y>=-0.1:
            #         if c_x>=-0.5 and c_x<=0:
            #             cmd(0,0)
            #         else:
            #             cmd(0.2,0)
            #     else:
            #         if c_x>=-0.5 and c_x<=0:
            #             cmd(0,0)
            #         else:
            #             cmd(0, 0.2)

             
def listener():

    rospy.Subscriber("/obstacles", Obstacles, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def cmd(linear, angular):
    pub=rospy.Publisher("cmd_vel", Twist, queue_size=10)

    cmd_msg=Twist()
    cmd_msg.linear.x=linear
    cmd_msg.linear.y=0
    cmd_msg.linear.z=0
    cmd_msg.angular.x=0
    cmd_msg.angular.y=0
    cmd_msg.angular.z=angular
    pub.publish(cmd_msg)

if __name__ == '__main__':
    rospy.init_node('obstacle_controller', anonymous=True)
    listener()