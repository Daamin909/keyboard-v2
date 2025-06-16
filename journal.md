---
title: "keyboard-v2"
author: "Daamin Ashai"
description: "a smart & cool keyboard"
created_at: "2025-06-05"
---

**Total Time Spent: 18 hours**

# keyboard-v2 - a custom keyboard

### 5th June (day 1): brainstorming & schematic

oooo this is gonna be hella fun.
i've already designed a keyboard before this but that one was a bit chunky, with this keyboard, I plan to make it very minimalistic and compact, so it becomes very portable. I also want to print the case in one piece using my own 3D printer which i'm working on right now, it has a build plate of 310mm x 310mm. Meaning I want my keeb to slightly smaller than that. I ended up choosing a 60% layout. I also want to use slide potentiometers and REs for this keyboard.

I designed the layout using kb-layout-editor, and finished the schematic for the switches. I also worked on the aligning the switches.

<image src="assets/pcb.png" width="400">

<image src="assets/schem.png" width="400">

**Time Spent:** 2 hours

### 6th June (day 2): finish pcb

after some brainstorming, i decided to not use sliders since they're pretty unfit for what i do. i ended up adding 2 REs and some noepixels on the pcb. since the mcu takes space on the top, ill put some neopixels which will have a glass/acrylic top for aesthetics. i made a VERY cool harry potter themed silkscreen and im very happy with how it turned out. routing this time way way better than my prev keyboard and i actually used a lot less vias. ill work on the case next

<image src="assets/front_3d.png" width="400">

<image src="assets/back_3d.png" width="400">

**Time Spent**: 4 hours

### 7th June (day 3): make changes to save money

i removed the neopixels since i could not source them with in India, and PCBA would probably incur a lot of customs. I switched to using a bunch of LEDs. the colors will still look cool, and id save some money on customs.

<image src="assets/new.png" width="400">

**Time Spent**: 1 hour

### 10th June (day 4): finish CAD and complete the keyboard!!

I started working on the CAD, this time it was very easy, compared to last time when I was making a keyboard 😭.
I decided on making a integrated top and plate to make it quick to print. I used the plate generator and this time it was smoother than last time. it took me a while to figure out the fastener situation, but i ended up using heatsets and kept it very hidden. I decided to go with an all - white case, and found an acrylic sheet to cover the LEDs, i also made a way to mount this sheet using some superglue. it was very fun to make this, and the renders look AWESOME.

<image src="assets/1.png" width="400">
<image src="assets/2.png" width="400">
<image src="assets/3.png" width="400">
<image src="assets/4.png" width="400">
<image src="assets/5.png" width="400">
<image src="assets/6.png" width="400">

**Time Spent**: 6 hours

### 12th June (day 5): add firmware

i did some gpt-ing since its very hard to make the firmware without having the parts with me 😭. and BOOM I had a firmware, I made a tiny little function to cycle through my LED configs and thats it!

**Time Spent:** 1 hour

### 16th June (day 6): made the case inclined

i had some second thoughts on whether I should make my case inclined or not, and here we go. after some googling, i went with a 5 degree incline, and did some magic and once again BOOM. I added the holes for the fasteners and I was done! im really proud of how this ended up looking.

<image src="assets/sus.png" width="400">

**Time Spent**: 2 hours
