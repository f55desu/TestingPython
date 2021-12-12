import asyncio

async def count(counter):
    print(f"Количество записей в списке: {len(counter)}")

    while True:
        await asyncio.sleep(1/100000)
        counter.append(1)

async def printEverySecond(counter):
    while True:
        await asyncio.sleep(1)
        print(f"- 1 секунда прошла. "
                f"Количество записей в списке: {len(counter)}")

async def printEvery5Seconds():
    while True:
        await asyncio.sleep(5)
        print(f"--- 5 секунд прошло. ")

async def printEvery10Seconds():
    while True:
        await asyncio.sleep(10)
        print(f"----- 10 секунд прошло. ")

async def main():
    counter = list()

    countCour = count(counter)
    printCour = printEverySecond(counter)
    print5Cour = printEvery5Seconds()
    print10Cour = printEvery10Seconds()

    asyncio.create_task(countCour)
    asyncio.create_task(printCour)
    asyncio.create_task(print5Cour)
    await print10Cour

asyncio.run(main())