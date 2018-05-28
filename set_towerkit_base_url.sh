#!/usr/bin/bash
tower_hostname=`python get_tower_instance.py`
sed -i 's?export TOWERKIT_BASE_URL.*?export TOWERKIT_BASE_URL='"${tower_hostname}"'?g' ~/.bashrc
