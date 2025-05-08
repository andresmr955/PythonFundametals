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
        

#Creating asynchronous function to check the status of the inventory
async def check_inventory(item):
   logger(1, Status.START, f"Verifying inventory to {item}")
   #we are pausing to start other process
   await asyncio.sleep(random.randint(3,6))
   logger(1, Status.START, f'Inventory verifying to {item}')

   return random.choice([True, False])
#We are creating an asynchronous function to process payment

async def process_payment(order_id):
    logger(1, Status.PENDING, f"Processing payment to the order {order_id}")

    #simulate waiting time that a payment service has
    await asyncio.sleep(random.randint(3,6))
    logger(1, Status.FINISHED, f'Payment processed to the order {order_id}')
    return True

#Function to simulate an intensive work in the CPU  to calculate the cost of order
def calculate_total(items):
    logger(1, Status.START, f"Calculating the total cost to {len(item)} articles")
    time.sleep(5)
    total = sum(item['price'] for item in items) 
    logger(1, Status.FINISHED, f'Total cost calculated {total}')        
    return total