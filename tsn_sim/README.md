### TSN Simulator

#### UR5

##### run

1. launch a world with ur5
```bash
$ roslaunch tsn_sim ur5.launch
```

2. launch ur5 moveit planner
```bash
$ roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true
```

3. launch ur5 rviz moveit planner(optional)
```bash
$ roslaunch ur5_moveit_config moveit_rviz.launch config:=true
```

#### Baxter

##### install

1. follow [this](https://github.com/ros-planning/warehouse_ros_mongo) and [this](http://sdk.rethinkrobotics.com/wiki/MoveIt_Tutorial), make sure you can use moveit on baxter normally
2. if occurs any error, just compile moveit by yourself

##### run

1. launch a world with baxter
```bash
$ roslaunch tsn_sim baxter.launch
```

2. enable baxter(**important!**)
```bash
$ rosrun baxter_tools enable_robot.py -e
```

3. run baxter traj action server
```bash
$ rosrun baxter_interface joint_trajectory_action_server.py -l both
```

4. launch baxter rviz moveit planner(attention! left/right gripper)
```bash
$ roslaunch baxter_moveit_config demo_baxter.launch right_electric_gripper:=true left_electric_gripper:=true
```
or 
```bash
$ roslaunch baxter_moveit_config move_group.launch right_electric_gripper:=true left_electric_gripper:=true
```
if it occrus some error msg like "no semantic description" when  running the 2nd command, just run the 1st command then C-C it and run the 2nd command again.

#### Env parameters:

1. camera pose

edit `kinect::pose` `tsn_sim/worlds/table_world.world`

2. ur5 init pose

edit `spawn_gazebo_model`'s options `-x <x_coord> -y <y_coord> -z <z_coord>` in `tsn_sim/launch/ur5.launch`

3. baxter init pose

edit `spawn_gazebo_model`'s options `-x <x_coord> -y <y_coord> -z <z_coord> -R <roll_in_radian> -P <pitch_in_radin> -Y <yaw_in_radian>` in `tsn_sim/launch/baxter.launch`

4. add object

ask [@jeasinema](mailto:jeasinema@gmail.com) to do it.

#### Set object position dynamically

use this topic `/gazebo/set_model_state`
you can have a look at `script/move_object.py`

