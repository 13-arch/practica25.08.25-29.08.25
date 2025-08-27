import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay} seconds")

async def main():
    for i in range(0, 22,2):
        list=['A', 0, 'B', 0,'C', 0,'D', 0,'E', 0,
              'F', 0,'G', 0,'H', 0,'I', 0,'G',0,'H']
        tasks = [
                asyncio.create_task(task(list[i], i))
            ]
        await asyncio.gather(*tasks)

asyncio.run(main())