#!/usr/bin/env python
import os
import json

docker_config = '/etc/docker/daemon.json'
dict = {}
if os.path.exists(docker_config):
    with open(docker_config, 'r') as f:
        dict = json.load(f)
dict['live-restore'] = True
with open(docker_config, 'w') as f:
    json.dump(dict, f, sort_keys=True, indent=4, separators=(',', ':'))

os.system('systemctl reload docker')
