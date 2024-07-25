import math
from tf_transformations import euler_from_quaternion
from nav_msgs.msg import Odometry

"""classe para manipular dados de odometria"""
class OdometryHandler:
    def __init__(self):
        #inicializa as variáveis de posição e orientação.
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.yaw = 0.0

    def odom_callback(self, msg):
        #callback para receber dados de odometria e extrair posição e orientação.
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.z = msg.pose.pose.position.z
        (_, _, self.yaw) = euler_from_quaternion([
            msg.pose.pose.orientation.x, 
            msg.pose.pose.orientation.y, 
            msg.pose.pose.orientation.z, 
            msg.pose.pose.orientation.w
        ])