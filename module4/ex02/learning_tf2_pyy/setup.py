import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'learning_tf2_pyy'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='svetlana',
    maintainer_email='s.yarkova@g.nsu.ru',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'static_turtle_tf2_broadcaster = learning_tf2_pyy.static_turtle_tf2_broadcaster:main',
        'turtle_tf2_broadcaster = learning_tf2_pyy.turtle_tf2_broadcaster:main',
        'turtle_tf2_listener = learning_tf2_pyy.turtle_tf2_listener:main',
        'fixed_frame_tf2_broadcaster = learning_tf2_pyy.fixed_frame_tf2_broadcaster:main',
        'dynamic_frame_tf2_broadcaster = learning_tf2_pyy.dynamic_frame_tf2_broadcaster:main',
        'my_tf2_broadcaster = learning_tf2_pyy.my_tf2_broadcaster:main',
        ],
    },
)
