# -*- coding: utf-8 -*-
import asyncio
import time                                
import random 
import multiprocessing
import logging
import enum
from typing import Optional 
 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] %(message)s')

class Status(enum.Enum):
    START = 'START ☑️'
    PENDING = 'PENDING ⚠️'
    CANCELED = 'CANCELED ❌'
    FINISHED = 'FINISHED ✅'

def logger(status: Status, message: str, order_id: Optional[int] = None) -> None:

    order_id_st = f'order_id: {order_id}' if order_id is not None else "X"

    log_message = f'[{order_id_st}] status: {status.value} | message: {message}'
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
   logger(Status.PENDING, f"Verifying inventory to {item}...")
   #we are pausing to start other process
   await asyncio.sleep(random.randint(3,6))
   logger(Status.PENDING, f"Inventory verifying to {item}..." )

   return random.choice([True, False])
#We are creating an asynchronous function to process payment

async def process_payment(order_id):
    logger(Status.PENDING, f"Processing payment 💵 to the order {order_id}")

    #simulate waiting time that a payment service has
    await asyncio.sleep(random.randint(3,6))
    logger( Status.FINISHED, f'Payment processed 💲💲 to the order {order_id}' )
    return True

#Function to simulate an intensive work in the CPU  to calculate the cost of order
def calculate_total(items):
    logger( Status.START, f"Calculating 🧮 the total cost to {len(items)} articles" )
    time.sleep(5)
    total = sum(item['price'] for item in items) 
    logger( Status.FINISHED, f'Total cost calculated 🧮🏁✔️ {total}')        
    return total

async def process_order(order_id, items):
    logger(  Status.START, f'Initializing the processing of order {order_id} ...', order_id)
    #verifying inventory to each article
    inventory_checks = [check_inventory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_checks)   

    if not all(inventory_results):
        logger( Status.CANCELED, f'This product is not available', order_id) 
    print("Before pool")
    with multiprocessing.Pool() as pool:
        total = pool.apply(calculate_total, (items,)) #we add coma to be iterable
    print("After pool:")
    #process the payment asynchronous
    payment_result = await process_payment(order_id)

    if payment_result:
        logger( Status.FINISHED, F'The order was completed with success. Total {total}', order_id)
    else:
        logger( Status.CANCELED, F'Error processing this order {order_id}', order_id)

async def main():
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}]},
        {'order_id': 2, 'items': [{'name': 'Keyboard', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
        {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Cover', 'price': 20}]}
    ]

#processing multiples orders 

    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*tasks)


#Event loop

if __name__ == '__main__':
    asyncio.run(main())