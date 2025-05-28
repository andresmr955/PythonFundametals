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
    results = []
    result1 = await process_data('file.txt')
    results.append(result1)
    result2 = await process_data('file2.txt')
    results.append(result2)
    result3 = await process_data('file3.txt')
    results.append(result3)
    result4 = await process_data('file4.txt')
    results.append(result4)

    for result in results:
        print("Result:", result)
    print("Main function completed.")

#This is the event loop that runs the main function
asyncio.run(main())