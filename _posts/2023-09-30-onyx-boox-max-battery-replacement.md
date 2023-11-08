---
layout: post
title: "Let's Replace the Battery in ONYX BOOX MAX"
description: "A concise guide on replacing the battery in an ONYX BOOX MAX e-book"
tags: ["diy", "repair", "battery", "battery replacement", "e-reader", "onyx boox", "onyx boox max"]
---

![ONYX BOOX MAX e-reader](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/onyx-boox-max-intro.webp)

#### Links:

- [Episode 1 (this one)]({% post_url 2023-09-30-onyx-boox-max-battery-replacement %})
- [Episode 2]({% post_url 2023-11-08-onyx-boox-max-battery-replacement-episode-2 %})

---

I have an ONYX BOOX MAX ebook, it's almost A4 paper size and I have owned it for quite a while.

Recently due to its age, I noticed that the battery has degraded, and the ebook can stay alive for around one day only whereas at the beginning it lasted for weeks without recharging.

So, I decided to try to replace the battery on my own :muscle:, and to my surprise, I haven't found any good disassembly instructions for this e-reader on the internet, so I'm writing this post as a guide for others as well as for my future self.

[![preparing for the quest](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/01.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQmzmYBmisFFQp1B?e=2e0pMY){:target="_blank"}


:hammer_and_wrench: And here's the step-by-step how-to:

- raise and detach the lid cover (it's attached with thin double-sided tape or glue)

  [![detaching the lid cover](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/02.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQpq0VBtgrF8zf-M?e=JIjANu){:target="_blank"}

  [![detached lid cover](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/03.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQgfb5L8A8GuBQp4?e=gJlMBR){:target="_blank"}

- unscrew 24 screws from the front panel and lift up the panel

  [![unscrew 24 screws](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/04.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQse6YPyva_a0Lt3?e=lwYupE){:target="_blank"}

- now we have access to the internals including the battery

   - the battery dimensions are roughly 155 x 85 x 2 mm
   - and its characteristics are 3.7 V and 15.17 Wh => 4100 mAh
   - the battery is connected to the board with 3 cables
     - black and red are for the power delivery
     - and as googling over the internet suggested, the white one is used for the controller / thermistor

   [![internals view](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/05.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQ9UsPXFNV1ZBWhV?e=6xdOCV){:target="_blank"}

   [![batteries comparison](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/06.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQzmAi_YwaGisDtq?e=OjcOqT){:target="_blank"}
   
- the replacement battery I found has only 2 wires (black and red for the power delivery), so I soldered them with the corresponding wires at the connector and left the white wire unused

  [![soldering preview](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/07.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQ2zra_Kl7U04Kt9?e=p7aD1o){:target="_blank"}

- right after attaching the connector back to the board, the reader started to boot successfully

- using the double-sided tape I attach the new battery back to the panel

  [![double-sided tape on new battery](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/08.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gQ47aKm8UdTzNnLq?e=3ExCch){:target="_blank"}
  
  [![new battery on its place](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/09.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gRCsTVuWXEKuct9h?e=iX17dO){:target="_blank"}

- then I assembled everything together in reverse order

- then I attached the power charger to the reader and it started to consume the power (and it did not blow up :sweat_smile:)

- voila :+1:

  [![view of the assembled e-reader](/content/binary/img/posts/2023-09-30-onyx-boox-max-battery-replacement/10.webp)](https://1drv.ms/i/s!AqP7CryK4Xu4gRHL1Zfm2nGdfiHT?e=uJBClh){:target="_blank"}

:v:
