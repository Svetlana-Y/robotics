import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    demo_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('learning_tf2_pyy'), 'launch'),
            '/turtle_tf2_demo.launch.py']),
       launch_arguments={'target_frame': 'carrot1'}.items(),
       )

    return LaunchDescription([
        demo_nodes,
        Node(
            package='learning_tf2_pyy',
            executable='my_tf2_broadcaster',
            name='dynamic_broadcaster',
            parameters=[{'radius':LaunchConfiguration('radius', default = 1.0)},
            {'direction_of_rotation': LaunchConfiguration('direction_of_rotation', default = -1)}]
        ),
    ])
