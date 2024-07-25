from sensor_msgs.msg import LaserScan

class LaserHandler:
    """classe para manipular dados do laser"""
    def __init__(self):
        #crio e inicializo a lista de dados do laser
        self.laser_data = []
    

    def laser_callback(self, msg):
        #callback para receber os dados do laser
        self.laser_data = msg.ranges