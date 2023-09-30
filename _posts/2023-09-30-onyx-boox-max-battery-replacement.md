---
layout: post
title: "Let's Replace the Battery in ONYX BOOX MAX"
description: "A concise guide on replacing the battery in an ONYX BOOX MAX e-book"
tags: ["diy", "repair", "battery", "battery replacement", "e-reader", "onyx boox", "onyx boox max"]
---

![ONYX BOOX MAX e-reader](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-intro.webp)

I have an ONYX BOOX MAX ebook, it's almost A4 paper size and I have owned it for quite a while.

Recently due to its age, I noticed that the battery has degraded, and the ebook can stay alive for around one day only whereas at the beginning it lasted for weeks without recharging.

So, I decided to try to replace the battery on my own :muscle:, and to my surprise, I haven't found any good disassembly instructions for this e-reader on the internet, so I'm writing this post as a guide for others as well as for my future self.

[![preparing for the quest](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-01.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21115&authkey=%21AKfCdH8msb6WtKg&width=3223&height=1836){:target="_blank"}


:hammer_and_wrench: And here's the step-by-step how-to:

- raise and detach the lid cover (it's attached with thin double-sided tape or glue)

  [![detaching the lid cover](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-02.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21113&authkey=%21AKPe19fRYxFLKwU&width=3264&height=1836){:target="_blank"}

  [![detached lid cover](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-03.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21114&authkey=%21AFDOP_GK0a6WVjs&width=3264&height=1836){:target="_blank"}

- unscrew 24 screws from the front panel and lift up the panel

  [![unscrew 24 screws](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-04.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21118&authkey=%21AIWDxsMWSIzS0h4&width=2474&height=1783){:target="_blank"}

- now we have access to the internals including the battery

   - the battery dimensions are roughly 155 x 85 x 2 mm
   - and its characteristics are 3.7 V and 15.17 Wh => 4100 mAh
   - the battery is connected to the board with 3 cables
     - black and red are for the power delivery
     - and as googling over the internet suggested, the white one is used for the temperature measurements

   [![internals view](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-05.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21116&authkey=%21ADFngYb-z0OByMY&width=2537&height=1819){:target="_blank"}

   [![batteries comparison](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-06.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21117&authkey=%21AE9oMvMtIcCrnwA&width=3264&height=3672){:target="_blank"}
   
- the replacement battery I found has only 2 wires (black and red for the power delivery), so I soldered them with the corresponding wires at the connector and left the white wire unused

  [![soldering preview](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-07.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21119&authkey=%21ABHvn9Evy5P48xM&width=1836&height=3264){:target="_blank"}

- right after attaching the connector back to the board, the reader started to boot successfully

- using the double-sided tape I attach the new battery back to the panel

  [![double-sided tape on new battery](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-08.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21121&authkey=%21AEM_Cl5NakScnaM&width=3264&height=1836){:target="_blank"}
  
  [![new battery on its place](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-09.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21120&authkey=%21APyy1X0XS6iGmrU&width=2470&height=1797){:target="_blank"}

- then I assembled everything together in reverse order

- then I attached the power charger to the reader and it started to consume the power (and it did not blow up :sweat_smile:)

- voila :+1:

  [![view of the assembled e-reader](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-10.webp)](https://onedrive.live.com/embed?resid=B87BE18ABC0AFBA3%21122&authkey=%21AFtZn2XuVX8m9Ek&width=3264&height=1836){:target="_blank"}

:v:
