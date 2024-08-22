---
layout: post
title: "Tips & Tricks: Use Incognito Mode for the OS Default Browser"
description: "Are you tired of opening the links in your main browser session exposing the data in those sessions to a chance to be stolen?"
tags: [ "tips-n-tricks", "browser", "incognito", "registry", "windows", "admin", "administration"]
image: /content/img/web-browser-colorful.webp
---

![Web Browser](/content/img/web-browser-colorful.webp){:style="display:block; margin-left:auto; margin-right:auto; max-width: 50%;"}

Hello :wave:

There's an option to open the links or in more general case, various file types from file explorer by just (double-)clicking on it, and letting the operating system do its magic behind the scenes to call the associated program (e.g. web browser).

This feature works and improves the end-user experience while using, for example, chatting software which can have copying of the links disabled in the chats\channels by admins and not showing the URLs as well, basically leaving the user with the only chance to get to content by clicking on it and letting the chatting software open the link in the internal viewer or forwarding this request to the operating system which in turn will look up its default associations.

So, it does the trick but has one tiny annoyance: it opens the associated browser in one of its main sessions.

But as any InfoSec-aware person knows, it's basically one of the dumbest things to do: to open the link without knowing where it points to in your main browsing session (in which you're probably already authenticated and have alive sessions for your social media accounts, work, and personal emails, cloud storage service or the online banking - all waiting to be stolen).

And let's not forget about the 0-days that would be more than happy to make your system 0wn3d in the automated fashion without being noticed by your OS / antivirus / DPI vendor.

But what if we want to open the associated link in the incognito session instead? It may not save us from 0-days but still, it's better than nothing. Is it possible?

Well, the OS knows what browser to open via its associations mappings. And there should exist (directly or transitively) the setting with the command line pointing to the browser's binary somewhere in the related OS settings. In general, that command line should be parameterized in order for the OS to be able to pass the URL to be opened.

The idea is to find the related starting command line and alter it with some browser-specific switches to open the browser in incognito mode. I've performed the research and here are the results at the moment of writing (for Win 10 x64):

<div style="overflow-x: scroll;" markdown="block">

| Browser | Registry Key | Registry Value | Update |
|-|-|-|-|
| Edge | `Computer\HKEY_CLASSES_ROOT\MSEdgeHTM\shell\open\command` | `"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -inprivate --single-argument %1` | `-inprivate` |
| Brave | `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\BraveHTML\shell\open\command` | `"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" -incognito --single-argument %1` | `-incognito` |
| Chrome | `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\ChromeHTML\shell\open\command` | `"C:\Program Files\Google\Chrome\Application\chrome.exe" --incognito --single-argument %1` | `--incognito` |
| Firefox | `Computer\HKEY_CLASSES_ROOT\FirefoxURL-308046B0AF4A39CB\shell\open\command` | `"C:\Program Files\Mozilla Firefox\firefox.exe" -osint -private-window "%1"` | `-private-window` |

</div>

<br/>

So, just update the registry value for your browser of choice, then set it as the default browser in the OS, and enjoy the links being opened in incognito mode :detective:.

P.S. Obviously, the specific registry keys and format of switches are subject to change by the corresponding software vendors. In case of change, use your intuition and search for `\<browser_binary_name>.exe` across the registry and look for the most promising keys by name.

:v:

<br/>

**Update:** after installing the OS updates, it turned out that the above-mentioned registry settings were reset for all browsers, so better be sure to re-apply the changes (manually or automatically)
