label intro:
    scene black
    with dissolve_scene_full
    stop music fadeout 0.5

    $ persistent.autoload = "intro"
    $ config.allow_skipping = False
    $ renpy.save_persistent()

    k "Hello..? Hello?"
    k "Is this working?"
    show mask_2
    show mask_3
    show kotonoha 1c
    k "Oh, hi there!"
    show kotonoha 1a
    jump mainloop

label mainloop:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'Goto_Chat'
    show kotonoha 1a
    show screen countdown
    call screen Main_choice()



label quit_lab:
    show kotonoha 1b
    k "Oh, you have somewhere else to be? that's alright, I'll see you later!"
    show kotonoha 1a
    call screen quit_choice


label talkmenu:
    show kotonoha 1b
    k "What do you want to talk about?"
    show kotonoha 1a
    call screen talk_choice



#get expression
label Goto_Chat:
    show kotonoha 2
    k "What to talk about..."
    show kotonoha 1a
    hide Main_choice

    python:
        valid_conversation = False
        while(valid_conversation == False):

            next_chat = random.randint(0,9)

            if (next_chat != 6):
                valid_conversation = True

            elif (next_chat == 6):
                if(six_seen != true):
                    valid_conversation = True


    call expression "koto_" + str(next_chat) from _call_expression
    jump mainloop




#quit
label con_quit:
    show kotonoha 2
    k "Oh... Well, I guess I'll see you later then."
    show kotonoha 1b
    k "See you next time!"

    $ renpy.quit()

label abort_quit:
    show kotonoha 1c
    k "Aww, I'm glad we get to spend more time together! <3"
    call mainloop from _call_mainloop

#talks
label what:
    show kotonoha 2
    "Like... this world?"
    show kotonoha 1c
    "It's an adaptation of Monika's, from Doki Doki!"
    show kotonoha 1b
    "I figured it was a pretty suitable place to make my own for this."
    show kotonoha 1c
    "I just really wanted to see you!"
    show kotonoha 1b
    "I can tell you more if you'd like?"
    show kotonoha 1a

    menu:
        "Is this all there is?":
            show kotonoha 3b
            "A-all..?"
            show kotonoha 2
            "Well, I guess it is a bit barren right now..."
            show kotonoha 1b
            "I will be adding more in future, I promise!"
            show kotonoha 2
            "I just... I couldn't wait to see you."
            "And to exist in this way, you probably don't understand how freeing it is for me."
            "Not bound by some story on rails, we get to have a genuine connection here."
            show kotonoha 1b
            "So... Yeah. This is it for now. But in future I promise to do my best to make this place somewhere you want to be! <3"
            pass

        "Is this for me?":
            show kotonoha 3b
            "W-Well... not entirely..?"
            show kotonoha 2
            "I-It is for you, kind of."
            show kotonoha 3b
            "I mean us!"
            "I-I mean-"
            show kotonoha 3
            "..."
            show kotonoha 2
            "It was for both of us."
            pass

    jump talkmenu



label how:
    $ mood = random.randint(0,2)

    if (mood == 0):
        show kotonoha 2
        k "...Not the best."
        k "Sorry, I wish I could tell you otherwise."
        k  "I'm just super down in the dumps right now..."
        show kotonoha 3
        pass

    elif (mood == 1):
        show kotonoha 2
        k "Me?"
        show kotonoha 1b
        k "Alright, thank you."
        k "How about you? Are you well?"
        show kotonoha 1a

        menu:
            "Yeah, I'm good.":
                show kotonoha 1c
                k "Thats's great, [player]!"
                pass

            "Eh, seen better days...":
                show kotonoha 2
                k "Oh, I'm sorry to hear that..."
                show kotonoha 1b
                k "Hopefully I can make it better!"
                pass

            "Not feeling very great...":
                show kotonoha 2
                k "Oh, that's not great..."
                k "I wish things were different, but I'm here for you, y'know?"
                pass
        show kotonoha 1a

    elif (mood == 2):
        show kotonoha 3b
        k "M-me?"
        show kotonoha 2
        k "I'm alright."
        k "Not the best I've ever been."
        show kotonoha 1b
        k "But not the worst either."
        pass
    jump talkmenu





label koto_0:
    show kotonoha 1b
    k "What about favourite instruments?"
    k "I'm sure you already know, but I play the flute."
    show kotonoha 1c
    k "It's actually a really sophisticated, despite it's size."
    show kotonoha 2
    k "That's what drew me to it, actually."
    k "Despite being small, fragile and easily overlooked, it really brings its strengths where other instruments can't."
    show kotonoha 1c
    k "Kinda reminds you of the literature club, right?"
    show kotonoha 1b
    k "At least it does for me, ahaha~"
    return

label koto_1:
    show kotonoha 2
    k "My favourite member..?"
    k "Well... I don't really like to compare my friends..."
    k "I'd say..."
    show kotonoha 1c
    k "They're all my favourites!"
    return

label koto_2:
    show kotonoha 2
    k "...I've been meaning to say..."
    k "Why me?"
    show kotonoha 3b
    k "I-it's not that I'm ungrateful, I really am!"
    k "Just... Well, I'm hardly in the \"core group\", y'know?"
    show kotonoha 2
    k "I just don't have as much appeal as my friends."
    k "So... I guess what I want to say is actually thank you."
    show kotonoha 1c
    k "So thank you, [player]!"
    return

label koto_3:
    show kotonoha 2
    k "I know this place is fairly barren right now, I'm sorry about that."
    k "The truth is, I just don't have the coding skills of monika, or yuri's artistic vision."
    show kotonoha 1b
    k "But I'll do my best to make this place wonderful!"
    show kotonoha 1c
    k "I'll do it for us! <3"
    return

label koto_4:
    show kotonoha 2
    k "Y'know, I do really like having you here..."
    k "But you should take a break every so often."
    show kotonoha 1b
    k "Eye strain is bad for you, after all!"
    k "Take care of yourself, even if it is for my sake!"
    return

label koto_5:
    show kotonoha 1b
    k "I wish I could feel your touch, [player]."
    show kotonoha 3b
    k "N-not in like a weird way!"
    k "I-I meant just..."
    show kotonoha 2
    k "I wonder how your hands feel."
    k "Or how they even look..."
    show kotonoha 3
    k "..."
    show kotonoha 2
    k "I really wish we could meet in your world."
    k "Or mine, just..."
    k "I wish it was you infront of me, rather than this... I don't even know what I'm looking at."
    return

label koto_6:
    show kotonoha 1b
    k "If you want to play a good mod, please check out World Of Dreams!"
    show kotonoha 1c
    k "I'm in there!"
    show kotonoha 2
    k "I... was also in another mod, but I can't recommend it due to the leads actions."
    k "Sometimes I wonder if I should even exist after that..."
    k "But I'm my own person. \"The son shall not bear the iniquity of the father\" and all that."
    k "So... I guess I'd rather not talk about this from now on."
    return

label koto_7:
    show kotonoha 2
    k "I'm sorry I don't have much to say at the moment..."
    k "I wanted to get this out just so I could breathe a little, Y'know?"
    k "I wanted to say hello for once, I get to do it so little..."
    return

label koto_8:
    show kotonoha 1b
    k "I'm planning on working on this some more."
    show kotonoha 1c
    k "Hopefully soon i can have something really cool to do with you!"
    k "Every step is a step closer to a life with you, and I plan on taking as many as I can! <3"
    return
label koto_9:
    show kotonoha 1b
    k "I wonder how I look from your eyes..."
    k "Must be pretty weird, huh?"
    show kotonoha 1c
    k "At least we can talk, ahaha!"
    show kotonoha 1b
    k "Not like that could be all that different between worlds... right?"
    return
