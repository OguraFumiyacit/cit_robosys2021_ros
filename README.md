# cit_robosys2021_ros

# 概要
txtファイルから一文ずつ表示するプログラムです。デフォルトでは般若心経を読み上げます。
txtファイルを改変すれば好きな文章を使用できます。

# 動作環境
* Raspberry Pi 3 Model B＋
* Ubuntu 20.04
* ROS noetic

# 環境構築
パッケージをROSのsrcフォルダ下にインストール。
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/OguraFumiyacit/cit_robosys2021_ros.git
$ cd ..
$ catkin_make
```

# 実行方法
1. 端末1でroscoreを立ち上げる。
```
$ roscore
```
2. 端末2のscripts下でtalker.pyを立ち上げる。
```
$ cd ~/catkin_ws/src/cit_robosys2021_ros/scripts
$ rosrun robosys2021_ros talker.py
```
3. 端末3でreader.pyを立ち上げる。
```
$ rosrun robosys2021_ros reader.py
```

# 補足
* scripture.txtを書き換えれば好きな文章を使用できます。
* talker.py内の
```rate = rospy.Rate(0.5)  #表示間隔```で表示間隔を変更できます。
