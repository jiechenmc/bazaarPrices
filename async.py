import asyncio


async def find_divisibles(inrange, div_by):
    print(f"finding nums in range {inrange} divisible by {div_by}")
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 500_000 == 0:
            await asyncio.sleep(0.01)
    print(f"Done w/ nums in range {inrange} divisible by {div_by}")
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(500_000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))
    await asyncio.gather(divs1, divs2, divs3)
    return divs1, divs2, divs3


loop = asyncio.get_event_loop()
d1, d2, d3 = loop.run_until_complete(main())
loop.close()

print(d1)