label intro:
    scene bg bedroom
    with dissolve_scene_full
    stop music fadeout 0.5

    $ persistent.autoload = "intro"
    $ config.allow_skipping = False
    $ renpy.save_persistent()

    "mod time bitches"
    jump mainloop

label mainloop:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'Goto_Chat'
    show screen countdown
    call screen Main_choice()


label talkmenu:
    "What do you want to talk about?"
    call screen talk_choice()

label cry:
    "crying? lil bitch boy."
    call screen talk_choice()





#get expression
label Goto_Chat:
    "What to talk about..."
    call expression "koto_" + str(1)
    jump mainloop






#talks
label absurd:
    "Oh? I'm to hot for you? that's pretty gay, [player]"
    jump talkmenu

label pewdiepie:
    "Fridays with peeeewdiepieeeee"
    "I get an awesome brofist"
    jump talkmenu


#crys
label waa:
    "waaaaaaaa"
    "waaaaaaaaaaaaaaaaaaaaaaa"
    "waAaAaAaAaaAaAAAaaaaAAaaaAAaAaaaAAaaaAAAAaaAaaaAA"
    "That's you right now."
    "Little bitch boy."
    jump cry

label copium:
    "I'M NOT A LITTLE PISS BABY!"
    "STOP CALLING ME A LITTLE PISS BABY!"
    "FUCK YOU!!!"
    jump cry


label koto_0:
    "test 1"
    return

label koto_1:
    "test 2"
    return

label koto_2:
    "test 3"
    return

label koto_3:
    "test 4"
    return
label koto_4:
    "test 5"
    return
