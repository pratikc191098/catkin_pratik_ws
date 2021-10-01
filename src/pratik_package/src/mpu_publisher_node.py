import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

move_turtle_publisher = rospy.publisher('/turtle1/cmd_vel',Twist,queue_size=10) 
	#move_turtle_publisher is the publisher to publish on topic /turtle1/cmd_vel in Twist type 		of message

rospy.init_node('mpu_publisher_node',anonymous=True)
rate = rospy.Rate(1)
i=0
 
while not rospy.is_shutdown():
    twist= Twist()    
    twist.linear.x= 1.0
    rospy.loginfo("I publish:")
    rospy.loginfo(twist)
    move_turtle_publisher.publish(twist)
    rate.sleep()
    i=i+1     
'''def move_turtle_function():
        print("pppp")
	move_turtle_publisher = rospy.publisher('/turtle1/cmd_vel',Twist,queue_size=10) 
	#move_turtle_publisher is the publisher to publish on topic /turtle1/cmd_vel in Twist type 		of message

	rospy.init_node('mpu_publisher_node',anonymous=True)
	rate = rospy.Rate(1)

	i=0
	while not rospy.is_shutdown():
		twist= Twist()
		twist.linear.x= 1.0

if __name__ == '__main__':
	try:
            print("rg")
            move_turtle_function()
	except:
            print("xd") 
            pass'''
 

