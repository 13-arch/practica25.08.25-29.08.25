from laba6_1 import worker_1
from laba6_2 import worker
from laba6_3 import task
from laba6_3 import main
import asyncio

async def main():
    first = worker_1()
    second = worker()
    third = await task()
    third_2= await main()

    
if __name__ == "__main__":
    asyncio.run(main()) 