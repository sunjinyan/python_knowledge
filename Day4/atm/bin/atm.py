import os.path

import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from  conf import setting
from core import  main

main.login()