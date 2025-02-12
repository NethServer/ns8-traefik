#
# Copyright (C) 2025 Nethesis S.r.l.
# SPDX-License-Identifier: GPL-3.0-or-later
#

import os
import re
import yaml
from collections.abc import Mapping

def write_yaml_config(conf, path):
    """Safely write a configuration file."""
    with open(path + '.tmp', 'w') as fp:
        fp.write(yaml.safe_dump(conf, default_flow_style=False, sort_keys=False, allow_unicode=True))
    os.rename(path + '.tmp', path)

def parse_yaml_config(path):
    """Parse a YAML configuration file."""
    with open(path, 'r') as fp:
        conf = yaml.safe_load(fp)
    return conf

def merge_yaml_structs(a, b):
    """
    Recursively merges two Python structures following these rules:
    - Scalars (int, str, etc.): `b` replaces `a`
    - Lists of scalars: Append unique values while preserving order
    - Dicts of scalars: `b` replaces values with the same keys in `a`
    - Lists of dicts or lists: `b` overrides `a`
    - Dicts of lists or dicts: `b` overrides `a`
    """
    if isinstance(a, Mapping) and isinstance(b, Mapping):
        result = a.copy()
        for key, b_value in b.items():
            if key in a:
                result[key] = merge_yaml_structs(a[key], b_value)
            else:
                result[key] = b_value
        return result
    elif isinstance(a, list) and isinstance(b, list):
        if all(isinstance(x, (int, float, str, bool, type(None))) for x in a + b):
            seen = set(a)
            return a + [x for x in b if x not in seen]  # Preserve order and avoid duplicates from `a`
        else:
            return b  # Override if not purely scalar
    else:
        return b  # Replace scalars or differing types

def replace_env_placeholders(struct):
    """
    Recursively replaces environment variable placeholders in string values.
    Placeholders follow the `envsubst` syntax: $VAR or ${VAR}.
    """
    pattern = re.compile(r'\$(\w+|\{\w+\})')
    def substitute(value):
        if isinstance(value, str):
            return pattern.sub(lambda m: os.getenv(m.group(1).strip('{}'), m.group(0)), value)
        elif isinstance(value, Mapping):
            return {k: substitute(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [substitute(v) for v in value]
        else:
            return value
    return substitute(struct)
