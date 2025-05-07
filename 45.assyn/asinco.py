import asyncio

#This is coroutine function that simulates a time-consuming task
async def process_data(data):

    print("Processing data...")
    await asyncio.sleep(10)  # Simulate a time-consuming task
    print("Data processed.")
    return data * 2

#This is a coroutine function that runs the main function
async def main():
    print("Starting main function...")
    result = await process_data('file.txt')
    print("Result:", result)
    print("Main function completed.")

#This is the event loop that runs the main function
asyncio.run(main())