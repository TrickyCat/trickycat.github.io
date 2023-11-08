---
layout: post
title: "Let's Replace the Battery in ONYX BOOX MAX: Episode 2"
description: "A continuation of a concise guide on replacing the battery in an ONYX BOOX MAX e-book"
tags: ["diy", "repair", "battery", "battery replacement", "e-reader", "onyx boox", "onyx boox max"]
---

![ONYX BOOX MAX e-reader](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-intro.webp)

#### Links:

- [Episode 1]({% post_url 2023-09-30-onyx-boox-max-battery-replacement %})
- [Episode 2 (this one)]({% post_url 2023-11-08-onyx-boox-max-battery-replacement-episode-2 %})

---

After replacing the battery, the reader happily worked for a couple of weeks and reacted with a light while being charged. But suddenly, it started to show the 'Low Battery' message. My initial guess :thinking: was that the mainboard (and OS) somehow can't get the feedback from the battery to figure out its current charge level (as I ignored the white wire while connecting the new battery), but still charges it. So, I thought it should continue to work even though some software counter in the OS would eventually show the 0% charge.

And the day has come: the reader turned itself off showing the low charge level image. It didn't load when I pressed the button. And to my surprise, it did not boot even when I attached the power charger: it went into the infinite boot loop and showed the blue light. :scream:

[![drained battery](/content/binary/img/posts/2023-11-08-onyx-boox-max-battery-replacement-episode-2/01.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQWa0MCfQCq2sAM6?e=oVTMrj){:target="_blank"}

:crystal_ball: Googling on the Internet wisdom database showed that:

- the 3-wire battery should ideally be substituted with the 3-wire replacement
- if the replacement is the 2-wired one, then:
  - option 1:
    - measure the resistance of the grid between the '-' wire and the controller wire in the original battery
    - solder additional resistance element (with a value comparable to the one measured above) while wiring up the replacement battery
  - option 2:
    - reuse the 3-wired charger board of the battery

Since I hadn't got rid of the original battery and option 1 looked too complicated, I decided to follow the way #2.

**My amateur journey:**

- take the original battery and detach the small charger board from it

  [![charging board from the original battery](/content/binary/img/posts/2023-11-08-onyx-boox-max-battery-replacement-episode-2/02.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQJRNEApi5mxOyG3?e=kImJR6){:target="_blank"}

- disassemble the reader (see [Episode 1]({% post_url 2023-09-30-onyx-boox-max-battery-replacement %}))

- solder the charger board into the circuit

  [![solder the charger board into the circuit](/content/binary/img/posts/2023-11-08-onyx-boox-max-battery-replacement-episode-2/03.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQPQGaNZMY01anyB?e=HirV0J){:target="_blank"}

- attach the charger, check, and see that the behavior has changed: now it's the red light!

  [![the behavior has changed: now it’s the red light](/content/binary/img/posts/2023-11-08-onyx-boox-max-battery-replacement-episode-2/04.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQRTQXUbpsATKIa2?e=bNHMMZ){:target="_blank"}

- assemble everything back together

- attach the charger and try to load the device: it boots :relaxed:

- leave it for at least half an hour to charge the battery a bit: it now better shows the charging process in the OS

  [![operating system shows the charging process](/content/binary/img/posts/2023-11-08-onyx-boox-max-battery-replacement-episode-2/05.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQZ3DKAmlRpPwdD2?e=ulpp5c){:target="_blank"}

- turn off the charger and verify that the reader works from the battery

- voila :+1:

[![get things done](/content/binary/img/posts/2023-11-08-onyx-boox-max-battery-replacement-episode-2/06.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQci2OIvNuZMt_PO?e=DNINWt){:target="_blank"}

:v:


