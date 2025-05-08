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

def logger(order_id: int, status: Status, message: str) -> None:
    log_message = f'[order_id: {order_id}] status: {status.value} | message: {message}'
    if status == Status.CANCELED:
        logging.warning(log_message)
    elif status == Status.FINISHED:
        logging.info(log_message)
    elif status == Status.PENDING:
        logging.debug(log_message)
    else:
        logging.info(log_message)
        
