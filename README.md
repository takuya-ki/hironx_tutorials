# hironx_stack

ROS Kinetic metapackage for the KAWADA HIRO-NX

## Requirement

- Ubuntu 16.04  
- ROS Kinetic

## Installation

1. Connect an ethernet cable between the controller and your PC  
<img src=img/lan_port.jpg width=300>

2. Set network configuration as below  
<img src=img/hiro_network.png width=300>

3. Register hiro's IP address in /etc/hosts  
   `10.254.12.1 hiro012`

## Usage

1. Bring HIRO-NX up  
   - Push the green button placed at the back of HIRO-NX
   - If the four leds blinking in different colors keeps after 5 to 10 minutes, restart by pushing the green button
   - When the two of them blink in green and white only, the robot is ready to be controlled
   - If the red led turns on, the emergency stop button may have been pressed  
  
<img src=img/power_button.jpg width=300>  <img src=img/front.jpg width=310>

1. Calibration and initialization (choose from the following two options)  
   - GUI    
     - `$ rtmlaunch hironx_ros_bridge hironx_ros_bridge_real.launch nameserver:=hiro012`  
     - Push `joint calibration` button after GUI openning  
     - Wait for that the robot finishes moving  
     - Push `go initial pose` button  

   - CUI  
     - ``$ ipython -i `rospack find hironx_ros_bridge`/scripts/hironx.py -- --host hiro012 ``  
     - `robot.checkEncoders()` after ipython openning  
     - Wait for that the robot finishes moving  
     - `robot.goInitial()`

2. Open rviz and moveit    
   - `$ roslaunch hironx_moveit_config moveit_planning_execution.launch`  
   - When the rviz screen comes up, the preparation has been completed  

3. Execute python script
   - `$ rosrun hironx_stack head_banging.py`
   - `$ rosrun hironx_stack turn_waist.py`
   - `$ rosrun hironx_stack move_arms.py`

4. Shutdown the robot   
   - GUI  
     - Push `go power-off pose` button   
   - CUI
     - `robot.goOffPose()`  

## References

[RTMROS_NEXTAGE reference (Japanese)](https://rtmros-nextage.readthedocs.io/en/latest/index.html)  
[MoveIt! Commander reference](http://docs.ros.org/kinetic/api/moveit_commander/html/index.html)  

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)  

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
