# Pursuit-Evasion Game using Turtlebot3 in ROS
Simulating TurtleBot3 in custom worlds &amp; playing the evader-pursuer game.

This project was divided into two parts:
1. We build a custom Gazebo world environment and make the Turtlebot3 robot (Waffle_Pi) traverse through the scene.
2. We create maps of two Gazebo worlds using SLAM and deploy an object detection based node for the Turtlebot3 robot to be able to follow the evader.

## Part 1

#### Task 1: Building a custom Gazebo world

##### Description: 
The custom world environment was built using Gazebo, a software primarily used for performing robotic simulation experiments by running algorithms on a simulated robot in a custom environment and obtaining the required observations. For this specific project, the ultimate goal is to be able to simulate a pursuit evasion game in a custom world environment. As a first step, we designed a custom floor plan in the Gazebo environment using the Building Editor. This allowed us to design the outline of the sample one floor house with a living room, a kitchen, a store room and two bedrooms. All the spaces are well connected to each other and have doors leading the robot inside each of the rooms.

##### Screenshots:

![alt text](https://github.com/sbhambr1/turtlebot3_simulations/blob/master/screenshots/Screenshot%20from%202021-03-31%2019-41-43.png?raw=true)
![alt text](https://github.com/sbhambr1/turtlebot3_simulations/blob/master/screenshots/Screenshot%20from%202021-03-31%2019-42-22.png?raw=true)
![alt text](https://github.com/sbhambr1/turtlebot3_simulations/blob/master/screenshots/Screenshot%20from%202021-03-31%2019-43-19.png?raw=true)

#### Task 2 Traversing the custom Gazebo world using the Turtlebot3 robot

##### Description: 
As the second step, we operated a Turtlebot3 robot in the custom world. This allowed us to understand the motion of the robot in the custom designed environment. The custom world is launched using a launch file and the robot is simulated using a python script where the constructed ROS node published to the node ‘cmd_vel’.

##### Robot traversal video:

https://user-images.githubusercontent.com/43840095/116606960-49db8600-a8e6-11eb-91eb-1682b59b8b6c.mp4




## Part 2

#### Task 1: SLAM with GMapping in ROS

##### Description: 
Here, we use the GMapping package to create a map of the world. We use one turtlebot3 robot to traverse through the world through the teleop node. This allows us to create a map of the Gazebo world which is saved using the map_server package.

##### Screenshots:

![image](https://user-images.githubusercontent.com/43840095/116607592-0d5c5a00-a8e7-11eb-8de9-d143cd608aa1.png)


#### Task 2: Autonomous Navigation

##### Description: 
In this task of the project, we are able to launch the turtlebot3_navigation file which allows us to control the movement of the turtlebot3 robot using the GUI provided by the RVIZ framework. We can use the 2D Nav Goal feature of the RVIZ GUI to make the turtlebot3 robot move in a particular direction inside the Gazebo world map.

##### Robot traversal video:

https://user-images.githubusercontent.com/43840095/116607763-3da3f880-a8e7-11eb-957c-9bc1dbbf3299.mp4


#### Task 3 & 4: Tracking Node, and, Control Node for Pursuit

##### Description:
For the first part of the task to create a tracking node, we make use of the built-in camera module of waffle_pi turtlebot3 robot. Using the camera of the robot, we are able to receive the images of the world from the robot’s perspective. These images are in the ROS sensor-msgs/Image format and hence, need to be converted into a format that can be used as input for the opencv2 package. This step is performed using the cv_bridge package in ROS.

After the images are converted into a usable format, we use an object detection algorithm to draw bounding boxes around the human/evader that will be detected. The center of the bounding box is then calculated and then sent as a goal for the turtlebot3 robot to navigate to. For the object detection part, we use a Mobilenet_v2 network pre-trained on the COCO dataset using Single-Shot Detection (SSD) algorithm.

We increase the height of the camera pose for the turtlebot3 robot to be able to view the human’s body from behind. This allows the robot to detect and draw the bounding box around the detected evader much more efficiently than in the case when the height of the camera is unchanged. 

Note: The pre-trained model is not included in the repository but can be downloaded in the ‘~/catkin_ws/src/pursuit_evasion/src/models/’ by using the following commands:

$ wget  https://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz

$ tar -zxf ssd_mobilenet_v2_coco_2018_03_29.tar.gz

The labels for the model can be downloaded in the ‘catkin_ws/src/pursuit_evasion/src/models/research/object_detection/data/’ by using the following link: 

https://github.com/tensorflow/models/blob/master/research/object_detection/data/mscoco_label_map.pbtxt

##### References:
http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/

https://github.com/tensorflow/models/tree/master/research/object_detection

##### Demonstration Video:

https://user-images.githubusercontent.com/43840095/116608065-9a9fae80-a8e7-11eb-9185-5cf686535364.mp4




