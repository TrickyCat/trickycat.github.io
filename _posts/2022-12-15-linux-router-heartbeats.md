---
layout: post
title: "One way to send HTTPS requests from the Linux terminal"
description: "Reveal one of the OpenSSL superpowers 😉"
tags: ["linux", "openssl", "s_client", "https", "request", "bash", "terminal"]
---

Recently I needed to customize the behavior of one router allowing it to send custom heartbeat messages to a cloud service.

At glance, this sounds like a trivial task with obvious possible solutions:

- Use the router firmware's default functionality

  **:x: Stop factor:**
  
  - I need to have full control over the format and contents of the message
  
  - the router is running a custom firmware flashed: **Tomato Firmware 1.28.0000 MIPSR2-140 K26 Mini** with a tiny Linux distribution

- Then just use the cURL / wget / ...
  
  **:x: Stop factor:**
  
  There's no cURL/wget in that Linux installment and there's even no easy way to install some because there's no package manager due to limited ROM size restrictions.

- That Linux has netcat so use it to manually format the HTTP message

  **:x: Stop factor:**
  Remote service is accessible only via HTTPS and even though I can configure it to accept unencrypted HTTP too,  I don't want to. And netcat can't deal with SSL encryption.

- Looks like a hopeless situation :scream:
  
  <details>
    <summary>
      <strong>:heavy_check_mark: Solution recipe from Ron:</strong>
    </summary>
  
    <img src="/content/binary/img/ron-swanson-real-men-would-recompile-the-linux-and-add-the-missing-functionality.jpg" width="600px" alt="Real men know the answer" />
  
  </details>

---

Luckily, searching this Linux distro for all available commands ended with success: it has `openssl` :wink:.

A curious fact: its 'super power' for sending HTTPS requests is not widely 'googlable' over the Internet, that's why I decided to write it down as a reminder for myself as well as others:

```bash
openssl s_client -crlf -quiet -connect example.com:443 <<EOF
POST /heartbeat HTTP/1.1
Host: example.com
X-ApiKey: 666
Content-Type: text/plain
Content-Length: 19
Connection: Close

$(date +'%Y-%m-%d %H:%M:%S')
EOF
```

Here we're sending a manually composed HTTP message over the SSL to the `example.com` host with some example payload.

**Important note:**

`openssl s_client` is mostly a debug tool so use it wisely and ideally strive for another solution that would follow the expected behavior for invalid certificates, excerpt from the docs:

> s_client can be used to debug SSL servers.
>
> ...
>
> The s_client utility is a test tool and is designed to continue the handshake after any certificate verification errors. As a result it will accept any certificate chain (trusted or not) sent by the peer. None test applications should not do this as it makes them vulnerable to a MITM attack. This behaviour can be changed by with the `-verify_return_error` option: any verify errors are then returned aborting the handshake.

:v:
