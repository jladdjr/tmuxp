#!/usr/bin/bash
tower_hostname=`python /home/vagrant/git/tmuxp/get_tower_instance.py`
sed -i 's?export TOWERKIT_BASE_URL.*?export TOWERKIT_BASE_URL='"https://${tower_hostname}"'?g' ~/.bashrc
