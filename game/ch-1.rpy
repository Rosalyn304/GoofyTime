label intro:
    scene black
    with dissolve_scene_full
    show kotonoha 1a
    stop music fadeout 0.5

    $ persistent.autoload = "intro"
    $ config.allow_skipping = False
    $ renpy.save_persistent()

    show kotonoha 1b
    k "mod time bitches"
    show kotonoha 1a
    jump mainloop

label mainloop:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'Goto_Chat'
    show screen countdown
    call screen Main_choice


label talkmenu:
    show kotonoha 1b
    k "What do you want to talk about?"
    show kotonoha 1a
    call screen talk_choice

label cry:
    show kotonoha 1b
    k "crying? lil bitch boy."
    show kotonoha 1a
    call screen quit_choice





#get expression
label Goto_Chat:
    show kotonoha 1b
    k "What to talk about..."
    show kotonoha 1a
    hide Main_choice

    $ valid_conversation = False
    while(valid_conversation == False):

        $ next_chat = random.randint(0,9)

        if (next_chat != 6):
            $ valid_conversation = True

        elif (next_chat == 6 && six_seen != true):
            $ valid_conversation = True


    call expression "koto_" + str(next_chat)
    jump mainloop




#quit
label waa:
    show kotonoha 1b
    k "Oh... Well, I guess I'll see you later then."
    show kotonoha 1c
    k "Adios, manwhore!"
    $ renpy.call_in_new_context("confirm_quit")

label copium:
    k "Aww, I knew we had something together! <3"
    call mainloop

#talks
label absurd:
    "Oh? I'm to hot for you? that's pretty gay, [player]"
    jump talkmenu

label pewdiepie:
    "Fridays with peeeewdiepieeeee"
    "I get an awesome brofist"
    jump talkmenu





label koto_0:
    "What about favourite instruments?"
    "I'm sure you already know, but I play the flute."
    "It's actually a really sophisticated, despite it's size."
    "That's what drew me to it, actually."
    "Despite being small, fragile and easily overlooked, it really brings its strengths where other instruments can't."
    "Kinda reminds you of the literature club, right?"
    "At least it does for me, ahaha~"
    return

label koto_1:
    "My favourite member..?"
    "Well... I don't really like to compare my friends..."
    "I'd say..."
    "They're all my favourites!"
    return

label koto_2:
    "...I've been meaning to say..."
    "Why me?"
    "I-it's not that I'm ungrateful, I really am!"
    "Just... Well, I'm hardly in the \"core group\", y'know?"
    "I just don't have as much appeal as my friends."
    "So... I guess what I want to say is actually thank you."
    "So thank you, [player]!"
    return

label koto_3:
    "I know this place is fairly barren right now, I'm sorry about that."
    "The truth is, I just don't have the coding skills of monika, or yuri's artistic vision."
    "But I'll do my best to make this place wonderful!"
    "I'll do it for us! <3"
    return
label koto_4:
    "Y'know, I do really like having you here..."
    "But you should take a break every so often."
    "Eye strain is bad for you, after all!"
    "Take care of yourself, even if it is for my sake!"
    return

label koto_5:
    "I wish I could feel your touch, [player]."
    "N-not in like a weird way!"
    "I-I meant just..."
    "I wonder how your hands feel."
    "Or how they even look..."
    "..."
    "I really wish we could meet in your world."
    "Or mine, just..."
    "I wish it was you infront of me, rather than this... I don't even know what I'm looking at."
    return

label koto_6:
    "If you want to play a good mod, please check out World Of Dreams!"
    "I'm in there!"
    "I... was also in another mod, but I can't recommend it due to the leads actions."
    "Sometimes I wonder if I should even exist after that..."
    "But I'm my own person. \"The son shall not bear the iniquity of the father\" and all that."
    "So... I guess I'd rather not talk about this from now on."
    return

label koto_7:
    "I'm sorry I don't have much to say at the moment..."
    "I wanted to get this out just so I could breathe a little, Y'know?"
    "I wanted to say hello for once, I get to do it so little..."
    return

label koto_8:
    "I'm planning on working on this some more."
    "Hopefully soon i can have something really cool to do with you!"
    "Every step is a step closer to a life with you, and I plan on taking as many as I can! <3"
    return
label koto_9:
    "I wonder how I look from your eyes..."
    "Must be pretty weird, huh?"
    "At least we can talk, ahaha!"
    "Not like that could be all that different between worlds... right?"
    return
