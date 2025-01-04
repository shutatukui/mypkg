#!/usr/bin/bash
# SPDX-FileCopyrightText: 2025 Tsukui Shuta
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws || { echo "Failed to change directory to $dir/ros2_ws"; exit 1; }

colcon build || { echo "colcon build failed"; exit 1; }
source $dir/.bashrc

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log || { echo "ros2 launch failed"; exit 1; }

cat /tmp/mypkg.log || { echo "Failed to read log file"; exit 1; }

#mojiretu kensaku
if grep -q 'Received fish info' /tmp/mypkg.log; then
    echo "Success: 'Received fish info' found in /tmp/mypkg.log"
    exit 0
else
    echo "Error: 'Received fish info' not found in /tmp/mypkg.log"
    exit 1
fi
