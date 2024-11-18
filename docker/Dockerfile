FROM ros:kinetic

RUN apt update -y && apt install -y --no-install-recommends curl lsb-release wget gnupg
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | apt-key add -

# setting environmental variables
ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y && apt install -y --no-install-recommends \
    ros-kinetic-desktop-full \
    ros-kinetic-gazebo-ros-pkgs \
    ros-kinetic-gazebo-ros-control \
    ros-kinetic-ros-control \
    ros-kinetic-ros-controllers \
    ros-kinetic-control-toolbox \
    ros-kinetic-moveit \
    ros-kinetic-moveit-visual-tools \
    ros-kinetic-effort-controllers \
    ros-kinetic-forward-command-controller \
    ros-kinetic-joint-state-controller \
    ros-kinetic-joint-trajectory-controller \
    ros-kinetic-position-controllers \
    ros-kinetic-velocity-controllers \
    ros-kinetic-tf \
    ros-kinetic-tf2-tools \
    ros-kinetic-robot-state-publisher \
    ros-kinetic-genpy \
    ros-kinetic-industrial-core \
    ros-kinetic-roslint \
    ros-kinetic-orocos-kdl \
    ros-kinetic-urdf-tutorial \
    ros-kinetic-nextage-description \
    ros-kinetic-joint-state-publisher \
    ros-kinetic-joint-state-publisher-gui \
    ros-kinetic-trac-ik-kinematics-plugin \
    ros-kinetic-rtmros-nextage \
    ros-kinetic-rtmros-hironx \
    python-catkin-tools \
    libxkbcommon-x11-0 \
    build-essential \
    libudev-dev \
    python-pip \
    net-tools \
    aptitude \
    libxcb* \
    psmisc \
    dvipng \
    byobu \
    dbus \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc

# Generates bash commands
WORKDIR /catkin_ws/src/
RUN echo "source /opt/ros/kinetic/setup.bash && source /catkin_ws/devel/setup.bash && roslaunch hironx_tutorials head_banging.launch" >> ~/.bash_history
RUN echo "source /opt/ros/kinetic/setup.bash && source /catkin_ws/devel/setup.bash && roslaunch hironx_tutorials turn_waist.launch" >> ~/.bash_history
RUN echo "source /opt/ros/kinetic/setup.bash && source /catkin_ws/devel/setup.bash && roslaunch hironx_tutorials move_arms.launch" >> ~/.bash_history
RUN echo "source /opt/ros/kinetic/setup.bash && source /catkin_ws/devel/setup.bash && roslaunch hironx_tutorials wave_arms.launch" >> ~/.bash_history

