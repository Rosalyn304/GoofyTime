init python:
    import time
init:
    $ timer_range = 0
    $ timer_jump = 0

define valid_conversation = False
define next_chat = 0
define mood = 0

image monika_room = "images/cg/monika/monika_room.png"

image k_menu_art = "mod_assets/K_menu_art.png"

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

#Koto Definitions

define k = DynamicCharacter('k_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

default k_name = "Kotonoha"

image kotonoha 1a = "mod_assets/1a.png"
image kotonoha 1b = "mod_assets/1b.png"
image kotonoha 1c = "mod_assets/1c.png"
image kotonoha 1ca = "mod_assets/1ca.png"
image kotonoha 2 = "mod_assets/2.png"
image kotonoha 3 = "mod_assets/3.png"
image kotonoha 3b = "mod_assets/3b.png"
