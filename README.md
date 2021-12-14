# robosys2021_ros_okyou

# 概要
txtファイルから一文ずつ表示するプログラムです。デフォルトでは般若心経を読み上げます。txtファイルを改変すれば好きな文章を使用できます。

# 動作環境
* Raspberry Pi 3 Model B＋
* Ubuntu 18.04
* ROS noetic

# 環境構築
パッケージをROSのsrcフォルダ下にインストール。
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/OguraFumiyacit/robosys2021_ros_okyou.git
$ cd ..
$ catkin_make
```


# 実行方法
1. 端末1でroscoreを立ち上げる。
```
$ roscore
```
2. 端末2でscripts下でokyou.pyを立ち上げる。
```
$ cd ~/catkin_ws/src/robosys2021_ros_okyou/scripts

