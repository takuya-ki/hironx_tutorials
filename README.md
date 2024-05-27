# hironx_tutorials

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

<img src=img/gui.png width=240>

   - CUI  
     - ``ipython -i `rospack find hironx_ros_bridge`/scripts/hironx.py --host hiro012 ``  
     - `robot.checkEncoders()` after ipython openning  
     - Wait for the robot to finish moving  
     - `robot.goInitial()`

<img src=img/calibrate_comp.gif width=240>  <img src=img/initialize_comp.gif width=240>

3. Open rviz and moveit    
   - `roslaunch hironx_moveit_config moveit_planning_execution.launch`  
   - When the rviz screen comes up, the preparation has been completed  

<img src=img/rviz.gif width=280>

1. Execute demonstrations
   - `roslaunch hironx_tutorials head_banging.launch`
   - `roslaunch hironx_tutorials turn_waist.launch`
   - `roslaunch hironx_tutorials move_arms.launch`

<img src=img/head_comp.gif width=240>  <img src=img/waist_comp.gif width=240> <img src=img/arms_comp.gif width=240>

1. Shutdown the robot   
   - GUI  
     - Push `Goto power-off pose` button   
   - CUI
     - `robot.goOffPose()`  

<img src=img/off_comp.gif width=240>

## References

- [RTMROS_NEXTAGE reference (Japanese)](https://rtmros-nextage.readthedocs.io/en/latest/index.html)  
- [MoveIt! Commander reference](http://docs.ros.org/kinetic/api/moveit_commander/html/index.html)  

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)  

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
