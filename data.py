import asyncio
import aiohttp
import prettytable
import json

class main:
    global iyuh
    iyuh = []
    async def gas(self):
        async with aiohttp.ClientSession() as self.sessi:
            async with self.sessi.get('https://api.kawalcorona.com/indonesia') as self.respons:
                self.txt = await self.respons.text()
                self.js = json.loads(self.txt)
                self.x = prettytable.PrettyTable()
                self.x.field_names = ['negara',
                        'positif',
                        'sembuh',
                        'meninggal',
                        'dirawat']
                for one in self.js:
                    # based parse
                    for key in one:
                        iyuh.append(one[key])
                self.x.add_row(iyuh)
                print (self.x)


loop = asyncio.get_event_loop()
loop.run_until_complete(main().gas())
