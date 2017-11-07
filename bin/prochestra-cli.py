#!/usr/bin/env python
import os
import sys

source_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(source_path)

if __name__ == '__main__':
    from prochestra import command_line
    exit(command_line())
