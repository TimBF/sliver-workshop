#!/usr/bin/env python3

import os
import asyncio
from sliver import SliverClientConfig, SliverClient

DEFAULT_CONFIG = ""

async def main():
    config = SliverClientConfig.parse_config_file(DEFAULT_CONFIG)
    client = SliverClient(config)
    print('[*] Connected to server ...')
    await client.connect()
    sessions = await client.sessions()
    print('[*] Sessions: %r' % sessions)
    if len(sessions):
        print('[*] Interacting with session %s', sessions[0].ID)
        interact = await client.interact_session(sessions[0].ID)
        ls = await interact.ls()
        print('[*] ls: %r' % ls)

if __name__ == '__main__':
    asyncio.run(main())
