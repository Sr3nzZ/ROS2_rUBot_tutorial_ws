import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class MoveTurtle(Node):

    def __init__(self):
        super().__init__('move_turtle')

        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.get_logger().info("Start turtle robot")

    def pose_callback(self, msg):


        cmd = Twist()

        if(msg.x > 7.0 or msg.y > 7.0):
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            self.get_logger().info("Stopping turtle robot")

            self.get_logger().info(f"Final position -> x: {msg.x:.2f}, y: {msg.y:.2f}")

            self.destroy_node()
            rclpy.shutdown()

        else:
            cmd.linear.x = 0.75
            cmd.angular.z = 0.0

        self.publisher.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()