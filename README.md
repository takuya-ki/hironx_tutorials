# hironx_tutorials

[![support level: community](https://img.shields.io/badge/support%20level-community-lightgray.svg)](http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![repo size](https://img.shields.io/github/repo-size/takuya-ki/hironx_tutorials)

ROS sample programs for the KAWADA HIRO-NX

## Requirement

- Ubuntu 16.04  
- ROS Kinetic

## Installation

1. Connect an ethernet cable between the controller and your PC  
   <img src=img/lan_port.jpg width=280>
2. Set network configuration as below  
   <img src=img/hironx_network.png width=280>
3. Register the IP address of the HIRO-NX in /etc/hosts  
   `10.254.12.1 hiro012`

## Usage
### Execute a demonstration

1. Launch HIRO-NX  
   - Push the green button located on the back of the HIRO-NX  
   - If the four LEDs blinking in different colors remained after 5 to 10 min, restart by pushing the green button  
   - When two of them blink only in green and white, the robot is ready to be controlled  
   - If the red LED is turned on, the emergency stop button may have been pressed  
      <img src=img/power_button.jpg width=290>  <img src=img/front.jpg width=300>
2. Caribrate and initialize all joints (select from the following two options)  
   - GUI    
     - `rtmlaunch hironx_ros_bridge hironx_ros_bridge_real.launch nameserver:=hiro012`  
     - Push `joint calibration` button after GUI openning  
     - Wait for the robot to finish moving  
     - Push `Goto init pose` button  
      <img src=img/gui.png height=180>
   - CUI  
     - ``ipython -i `rospack find hironx_ros_bridge`/scripts/hironx.py --host hiro012``  
     - `robot.checkEncoders()` after ipython openning  
     - Wait for the robot to finish moving  
     - `robot.goInitial()`  
      <img src=img/calibrate.gif height=180>  <img src=img/initializ.gif height=180>
3. Open rviz and moveit    
   - `roslaunch hironx_moveit_config moveit_planning_execution.launch`  
   - When the rviz screen comes up, the preparation has been completed  
      <img src=img/rviz.png height=180>
4. Execute demonstrations
   - `roslaunch hironx_tutorials head_banging.launch`  
   - `roslaunch hironx_tutorials turn_waist.launch`  
   - `roslaunch hironx_tutorials move_arms.launch`  
   - `roslaunch hironx_tutorials wave_arms.launch`  
      <img src=img/head_banging.gif height=180>  <img src=img/turn_waist.gif height=180> <img src=img/move_arms.gif height=180> <img src=img/wave_arms.gif height=180>

### Shutdown the robot   
   - GUI  
     - Push `Goto power-off pose` button   
   - CUI
     - `robot.goOffPose()`  
      <img src=img/offpose.gif height=180>

## References

- [RTMROS_NEXTAGE reference (Japanese)](https://rtmros-nextage.readthedocs.io/en/latest/index.html)  
- [MoveIt! Commander reference](http://docs.ros.org/kinetic/api/moveit_commander/html/index.html)  

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)  

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
