import asyncio
import random 
import time 
from datetime import datetime
#coroutine that simulates a download file

async def download_file(file_name):
    delay = random.randint(1,10) # Random download time 
    print(f"Starting download: {file_name} (estimated {delay}s)")
    await asyncio.sleep(delay)
    print(f"Finished download: {file_name}")
    return f"{file_name} downloaded"

async def main():
    print("Starting async downloads...\n")
    start_time = time.time()
    start_datetime = datetime.fromtimestamp(start_time)
    formatted_time = start_datetime.strftime('%H:%M:%S')
    print(f'Start time: {formatted_time}')

    # lIST OF FILES
    files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

    tasks = [ download_file(file) for file in files]

    results = await asyncio.gather(*tasks)

    print("\nAll download completed:")

    for result in results:
        print(result)
    
    end_time = time.time()
    end_datetime = datetime.fromtimestamp(end_time)
    formatted_end_time = end_datetime.strftime('%H:%M:%S')
    total_time = end_datetime - start_datetime    
    print(f'End time: {formatted_end_time} seconds')
    print(f'Final time: {total_time} seconds')
# Ejecutar el evento principal
asyncio.run(main())