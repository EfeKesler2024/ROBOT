from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='gazebo_ros', executable='gazebo', output='screen'),
        Node(package='ros_gz_bridge', executable='parameter_bridge', arguments=['/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image'], output='screen'),
        Node(package='robot_state_publisher', executable='robot_state_publisher', arguments=['my_robot_description/urdf/my_robot.urdf.xacro']),
        Node(package='joint_state_publisher', executable='joint_state_publisher'),
        Node(package='rviz2', executable='rviz2', output='screen'),
        Node(package='ball_chaser', executable='ball_chaser_node.py', output='screen')
    ])

