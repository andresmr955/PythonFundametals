import asyncio
import logging.config
import time
import random 
import multiprocessing
import logging
import enum
from typing import Optional 
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] %(message)s')

class Status(enum.Enum):
    START = 'START ⭐'
    PENDING = 'PENDING 🚧'
    CANCELED = 'CANCELED ❌'
    FINISHED = 'FINISHED 🎉🎆'
