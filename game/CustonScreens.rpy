screen convo:
    $ renpy.Call_out_of_context(Goto_Chat)

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    #bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

screen Main_choice:
    style_prefix "choice"
    #Show("countdown")
    vbox:
        xalign 0.1
        yalign 0.5

        textbutton _("Talk"):
            action [Hide("countdown"), Call("talkmenu")]
        textbutton _("Cry"):
            action [Hide("countdown"), Call("cry")]
        #$ time.sleep(5)
        #Hide(Main_choice)


screen talk_choice():
    style_prefix "choice"
    vbox:
        xalign 0.9
        yalign 0.1

        textbutton _("Holy fucking fuck that body of yours is absurd"):
            action  [Hide("countdown"), Jump("absurd")]
        textbutton _("Subscribe to pewdiepie"):
            action [Hide("countdown"), Jump("pewdiepie")]
        textbutton _("Return"):
            action [Hide("countdown"), Jump("mainloop")]

screen cry_choice():
    style_prefix "choice"
    vbox:
        xalign 0.9
        yalign 0.1

        textbutton _("Cry harder"):
            action [Hide("countdown"), Jump("waa")]
        textbutton _("Kill"):
            action [Hide("countdown"), Jump("copium")]
        textbutton _("Return"):
            action [Hide("countdown"), Jump("mainloop")]
#default menuset = set()


menu chapter_1_places:
    "Where should I go?"

    "Go to class.":
        jump talkmenu

    "Go to the bar.":
        jump cry

    "Go to jail.":
        jump cry
