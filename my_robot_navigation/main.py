import rclpy
from rclpy.node import Node
from my_robot_navigation.odometry_module import *
from my_robot_navigation.laser_module import *
from my_robot_navigation.navigation_module import *

class funciona(Node):
    def __init__(self):
        #inicializa o nó e os manipuladores de odometria, laser e navegação
        super().__init__('funciona')
        self.timer = self.create_timer(0.1, self.go_to)
        
        self.odom_handler = OdometryHandler()
        self.laser_handler = LaserHandler()
        
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_handler.odom_callback, 10)
        self.laser_sub = self.create_subscription(LaserScan, 'base_scan', self.laser_handler.laser_callback, 10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        self.navigation = Navigation(self.odom_handler, self.laser_handler, self.publisher, self.get_logger())

        self.get_logger().info('Node has been started')

    def go_to(self):
        #chama a função de navegação para mover o robô em direção ao próximo ponto alvo
        self.navigation.go_to()

def main(args=None):
    #função principal para iniciar o nó
    rclpy.init(args=args)
    node = funciona()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()