import time
import sys
import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class MoveTurtle(Node):

    def __init__(self):
        super().__init__("move_to_goal_node")

        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.subscription = self.create_subscription(Pose, "/turtle1/pose", self._move_to_goal, 10)
        self.pose_data = Pose()
        
    def __call__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        
    def _move_to_goal(self, msg):

            twist = Twist()

            s = math.sqrt((self.x - msg.x)**2 + (self.y - msg.y)**2)
            theta = math.atan2(self.y - msg.y, self.x - msg.x) - msg.theta

            self.get_logger().info(f"Pos {s} {theta}")

            if abs(s) > 0.1:
                twist.linear.x = s * 0.7
                twist.angular.z = theta
                self.publisher.publish(twist)
            else:
                twist.angular.z = self.theta - msg.theta
                self.publisher.publish(twist)
                self.get_logger().info(f"{ msg.x} { msg.y} { msg.theta}")
                self.destroy_node()
                rclpy.shutdown()
            time.sleep(0.1) 
def main():
    rclpy.init()

    move_turtle = MoveTurtle()
    move_turtle(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))

    rclpy.spin(move_turtle)

    move_turtle.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
