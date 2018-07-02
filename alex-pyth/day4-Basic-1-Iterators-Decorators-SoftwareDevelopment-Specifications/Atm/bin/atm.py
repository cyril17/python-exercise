# -*- conding: utf-8 -*-

import os
import sys

# print(__file__)
# print(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(base_dir)
sys.path.append(base_dir)
print(base_dir)

from core import main

if __name__ == '__main__':
    main.login()

