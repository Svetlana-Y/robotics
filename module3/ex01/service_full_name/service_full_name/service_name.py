from m2_ex09.srv import FullNameSumService

import rclpy
from rclpy.node import Node


class NameService(Node):

    def __init__(self):
        super().__init__('nameService')
        self.srv = self.create_service(FullNameSumService, 'create_full_name', self.create_full_name_callback)

    def create_full_name_callback(self, request, response):
        response.full_name = request.last_name + " " + request.name + " " + request.first_name
        self.get_logger().info('Incoming request\nlast_name: %s name: %s first_name %s' % (request.last_name, request.name, request.first_name))

        return response


def main():
    rclpy.init()

    name_service = NameService()

    rclpy.spin(name_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
