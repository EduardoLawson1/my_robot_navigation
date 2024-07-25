Trabalho Número 1: Robô Navegador

Eduardo Lawson da Silva -140598  && João Victor Acosta - 132818

Vídeo do youtube: https://youtu.be/TUnJYN1WcIk 

OBS: Foi implementado passando no segundo alvo primeiro para demorar menos a execução.

O arquivo está organizado dessa forma: 

├── src/
│   └── my_robot_navigation/
│       ├── my_robot_navigation/
│       │   ├── __init__.py
│       │   ├── odometry_module.py
│       │   ├── laser_module.py
│       │   ├── navigation_module.py
│       │   └── main.py
│       ├── package.xml
│       └── setup.py

para rodar o código é necessário  entrar na ws erodar esse comando em um terminal: 

```
ros2 launch stage_ros2 stage.launch.py world:=cave enforce_prefixes:=false one_tf_tree:=true

```
 depois disso abrir outro terminal e entrar na ws e depois rodar: 
 ```
 source install/setup.bash && colcon build && ros2 run my_robot_navigation main
 ```

 Prefiro utilizar todos os comandos juntos pois não tem perigo de esquecer de dar colcon build e também poupa tempo
