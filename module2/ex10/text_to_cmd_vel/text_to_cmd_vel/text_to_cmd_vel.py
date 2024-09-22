import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist 

class TextToCmd(Node):

    def __init__(self):
        super().__init__('text_to_cmd_vel')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.timer = self.create_timer(1.0, self.command_callback)
        self.get_logger().info("Node initialized")

    def command_callback(self):
        msg = input()
        msg_twist = Twist()

        if msg == "turn_right":
            msg_twist.linear.x, msg_twist.linear.y, msg_twist.linear.z  = 0.0, 0.0, 0.0
            msg_twist.angular.x, msg_twist.angular.y, msg_twist.angular.z = 0.0, 0.0, 1.5
        elif msg == "turn_left":
            msg_twist.linear.x, msg_twist.linear.y, msg_twist.linear.z  = 0.0, 0.0, 0.0
            msg_twist.angular.x, msg_twist.angular.y, msg_twist.angular.z = 0.0, 0.0, -1.5
        elif msg == "move_forward":
            msg_twist.linear.x, msg_twist.linear.y, msg_twist.linear.z  = 1.0, 0.0, 0.0
            msg_twist.angular.x, msg_twist.angular.y, msg_twist.angular.z = 0.0, 0.0, 0.0
        elif msg == "move_backward":
            msg_twist.linear.x, msg_twist.linear.y, msg_twist.linear.z  = -1.0, 0.0, 0.0
            msg_twist.angular.x, msg_twist.angular.y, msg_twist.angular.z = 0.0, 0.0, 0.0
        else:
            msg_twist.linear.x, msg_twist.linear.y, msg_twist.linear.z  = 0.0, 0.0, 0.0
            msg_twist.angular.x, msg_twist.angular.y, msg_twist.angular.z = 0.0, 0.0, 0.0
            self.get_logger().info(f'Command {msg} is not recognized')
        
        self.publisher_.publish(msg_twist)
        self.get_logger().info(f'Publishing Twist message: linear={msg_twist.linear}, angular={msg_twist.angular}')


def main():
    rclpy.init()

    text_to_cmd = TextToCmd()
    rclpy.spin(text_to_cmd)
    text_to_cmd.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
