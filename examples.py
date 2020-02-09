import asyncio

import aiohttp
from baustellen_hamburg import Baustellen


async def main():
    async with aiohttp.ClientSession() as session:

        b = Baustellen(session)

        baustellen = await b.get_baustellen()
        for baustelle in baustellen:
            print(f"There is a building site at {baustelle.coordinates}.")

            i = await b.get_informationen(baustelle.id)
            print(f"\tTitle: {i.title}")


asyncio.run(main())
