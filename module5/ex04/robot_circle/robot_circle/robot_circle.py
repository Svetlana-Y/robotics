import time
import sys
import math
import random
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry

class RobotCircle(Node):

    def __init__(self):
        super().__init__("robot_circle")
        self.publisher = self.create_publisher(Twist, "/robot/cmd_vel", 10)
        self.subscription = self.create_subscription(Odometry, "/robot/odom", self._move_circle, 10) 
        #self.timer = self.create_timer(0.2, self._move_circle)
        
    def _move_circle(self,msg):
        twist = Twist()
        twist.linear.x = 0.7
        twist.angular.z = 0.7
        self.publisher.publish(twist)

def main():
    rclpy.init()
    robot_circle = RobotCircle()
    rclpy.spin(robot_circle)
    robot_circle.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
