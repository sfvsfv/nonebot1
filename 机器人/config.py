"""
作者：杨涵文
时间：2021/4/6
"""
''':cvar
conda activate nonebot1

conda deactivate
'''
from nonebot.default_config import *
import re
from datetime import timedelta
SUPERUSERS = {2835809579}

COMMAND_START = ['', re.compile(r'[/!]+')]
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=2)

HOST = '127.0.0.1'
PORT = 8765