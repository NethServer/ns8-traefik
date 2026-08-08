#
# Copyright (C) 2025 Nethesis S.r.l.
# SPDX-License-Identifier: GPL-3.0-or-later
#

import agent
import os
import re
import yaml

def write_yaml_config(conf, path):
    """Safely write a configuration file."""
    with agent.safe_open(path, 'w') as fp:
        yaml.safe_dump(conf, stream=fp, default_flow_style=False, sort_keys=False, allow_unicode=True)

def parse_yaml_config(path):
    """Parse a YAML configuration file."""
    with open(path, 'r') as fp:
        conf = yaml.safe_load(fp)
    return conf
