import math
from geometry_msgs.msg import Twist

class Navigation:
    """classe para controlar a navegação do robô"""
    def __init__(self, odom_handler, laser_handler, publisher, logger):
        #inicializa os manipuladores de odometria, laser, publicador e logger
        self.odom_handler = odom_handler
        self.laser_handler = laser_handler
        self.publisher = publisher
        self.logger = logger

        self.target_pos = [(10.0, -6.0), (18.0, -0.2)]
        self.current_pos = self.target_pos[0]
        self.next_point = 0

    def go_to(self):
        #movimenta em direção ao ponto alvo
        if not self.laser_handler.laser_data:
            return

        cmd_vel_msg = Twist()

        distance_x = self.current_pos[0] - self.odom_handler.x
        distance_y = self.current_pos[1] - self.odom_handler.y
        theta = math.atan2(distance_y, distance_x)
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        front_distance = min(self.laser_handler.laser_data[50:155])

        if abs(distance_x) > 0.3 or abs(distance_y) > 0.3:
            if front_distance < 0.4:
                cmd_vel_msg.linear.x = -0.5
                cmd_vel_msg.angular.z = 50.0
            else:
                cmd_vel_msg.linear.x = self.calculate_speed(distance)
                cmd_vel_msg.angular.z = self.calculate_curved_turn_rate(theta)
            self.publisher.publish(cmd_vel_msg)
        else:
            self.update_target_point(cmd_vel_msg)

    def calculate_speed(self, distance):
        #calcula a velocidade baseada na distância ao alvo
        return min(1.0, distance)

    def calculate_curved_turn_rate(self, target_theta):
        #calcula a taxa de curva baseada no ângulo theta em relação à orientação atual
        k = 0.5
        return k * (target_theta - self.odom_handler.yaw)

    def update_target_point(self, cmd_vel_msg):
        #atualiza o ponto alvo quando o robô chega ao ponto atual
        if self.next_point < (len(self.target_pos) - 1):
            self.next_point += 1
            self.current_pos = self.target_pos[self.next_point]
            self.logger.info('Chegou no ponto alvo, próximo ponto: (%.1f, %.1f)' % (self.current_pos[0], self.current_pos[1]))
            self.logger.info('Posição atual: (%.1f, %.1f)' % (self.odom_handler.x, self.odom_handler.y))
        else:
            cmd_vel_msg.linear.x = 0.0
            cmd_vel_msg.angular.z = 0.0
            self.logger.info('Chegou no ponto final!')
            self.logger.info('Posição atual: (%.1f, %.1f)' % (self.odom_handler.x, self.odom_handler.y))
            self.publisher.publish(cmd_vel_msg)
