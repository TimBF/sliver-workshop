# Attack Infrastructure

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63230d22-41f0-4c0e-951d-73b39b79115a/Untitled.png)

## Multiplayer mode

Sliver supports a multiplayer mode allowing multiple operators to interact with implants. The commands to enable it and create new operator accounts are only available on the sliver server console for security purposes.

```bash
[server] sliver > multiplayer

[*] Multiplayer mode enabled!
```

Operators can then be managed using the following commands.

```bash
Multiplayer:
============
  kick-operator  Kick an operator from the server
  multiplayer    Enable multiplayer mode
  new-operator   Create a new operator config file
  operators      Manage operators
```

Keep in mind, the server will listen for new connections on port 31337 which needs to be accessible to operators when connecting.

## Daemon mode

Sliver servers can be run in daemon mode, which is configured either during the server startup using the daemon parameter or by setting the daemon_mode variable in the server configuration to true.

There are two ways to start the server in daemon mode:

```bash
$ cat ~/.sliver/configs/server.json 
{
    "daemon_mode": true,
    "daemon": {
        "host": "",
        "port": 31337
    },
```

## Watchtower

Watchtower allows monitoring popular threat intel platforms for the presence of your implant, the idea being that if a blue team uploads one of your implants to virus total for example you can detect that and change your implants before being taken down. 

You will first need to edit the server configuration in server.json and restart the server.

```bash
"watch_tower": {
        "vt_api_key": "YOUR_VIRUSTTOTAL_API_KEY",
        "xforce_api_key": "YOUR_XFORCE_API_KEY",
        "xforce_api_password": "YOUR_XFORCE_API_PASSWORD"
    },
```

Monitoring can then be enabled using `monitor start`.

## Canaries

When generating an implant, you can optionally include a dns canary in the payload, which will be an unobfuscated url that can be viewed using the strings command on the implant binary.

The main purpose of this feature is to trick defenders into attempting to resolve the domain which will let us know someone has found our implant and is doing some analysis, giving us a quick warning to switch up our infrastructure before being booted of our target network.

To setup this feature you’ll need to point configure an NS record to point to sliver and have the canary domain managed by that same nameserver.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab24e2f4-871d-42de-b244-38ebb87b5b87/Untitled.png)

The domain can then be included during implant generation.

```bash
[server] sliver > generate -b localhost --canary my.canarydomain.net --skip-symbols

[*] Generating new windows/amd64 implant binary
[!] Symbol obfuscation is disabled
[*] Build completed in 5s
[*] Implant saved to /Users/tester/RATIONAL_GREAT.exe

[server] sliver > canaries

 Sliver Name      Domain                         Triggered   First Trigger   Latest Trigger
================ ============================== =========== =============== ================
 RATIONAL_GREAT   bmscu8b.my.canarydomain.net.   false       Never           Never
```

## References

- [https://github.com/BishopFox/sliver/wiki/Architecture](https://github.com/BishopFox/sliver/wiki/Architecture)
- [https://github.com/BishopFox/sliver/wiki/Daemon-Mode](https://github.com/BishopFox/sliver/wiki/Daemon-Mode)
- [https://github.com/BishopFox/sliver/wiki/Watchtower](https://github.com/BishopFox/sliver/wiki/Watchtower)
- [https://github.com/BishopFox/sliver/wiki/Multiplayer-Mode](https://github.com/BishopFox/sliver/wiki/Multiplayer-Mode)
