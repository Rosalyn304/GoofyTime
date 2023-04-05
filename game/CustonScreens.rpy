screen convo:
    $ renpy.Call_out_of_context(Goto_Chat)

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    #bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

screen Main_choice():
    style_prefix "choice"
    #Show("countdown")
    vbox:
        xalign 0.1
        yalign 0.6

        textbutton _("Talk"):
            action [Hide("countdown"), Call("talkmenu")]
        textbutton _("Quit"):
            action [Hide("countdown"), Call("quit_lab")]
        #$ time.sleep(5)
        #Hide(Main_choice)


screen talk_choice:
    style_prefix "choice"
    vbox:
        xalign 0.9
        yalign 0.1

        textbutton _("What is this place?"):
            action  [Jump("what"), Hide("countdown")]
        textbutton _("How are you today?"):
            action [Jump("how"), Hide("countdown")]
        textbutton _("Return"):
            action [Jump("mainloop"), Hide("countdown")]

screen quit_choice:
    style_prefix "choice"
    vbox:
        xalign 0.9
        yalign 0.1

        textbutton _("Yeah, I have to go."):
            action [Jump("con_quit"), Hide("countdown")]
        textbutton _("...I can stay for a while longer."):
            action [Jump("abort_quit"), Hide("countdown")]
#default menuset = set()
