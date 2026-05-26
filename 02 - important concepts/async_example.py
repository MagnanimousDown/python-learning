import asyncio

async def greet():
    print("starting...")
    await asyncio.sleep(2)
    print("Finished...")

asyncio.run(greet())
