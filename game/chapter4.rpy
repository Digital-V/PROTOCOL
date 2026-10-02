<<<<<<< HEAD
label chapter4:
    $ current_chapter = 4
    
=======
image c4_ev2 = "evidences/limasawa_5.png"
image c4_ev3 = "evidences/limasawa_6b.png"
image c4_ev4 = "evidences/limasawa_9.png"

label chapter4:
>>>>>>> 627fbbc9cbf11abf21b48c24ee9e99ec0a66f915
    scene black
    with fade

    show text "{size=76}CHAPTER 4{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve

    scene coastal_area2
    with fade

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ta "So ito na ba yung route ng expedition?"

    $ inventory.append(ev_c3_b4)
    call screen examine_clue(ev_c3_b4)

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Oo. Kailangan nating ikumpara ang recorded route sa lugar na pinagpipilian natin. Sa Butuan o Limasawa."

    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ti "So paano kung hindi tugma yung location sa route, ibig sabihin ba questionable na yung claim?"
    jipri_ta "Tama."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jiperson
    hide jipri
    hide judet

    scene seaside_road
    show c4_ev2 at Transform(xpos=1680, ypos=850, zoom=0.025)
    with fade

    show judet normal at offscreenleft
    show judet normal at walk(position=0.5)
    pause 0.8
    judet_ta "May compass at distance markers dito."

    window hide 
    hide c4_ev2
    call screen search_item(ev_c3_b5, 1680, 850, 0.025, 0.035)
    $ inventory.append(ev_c3_b5)
    call screen examine_clue(ev_c3_b5)

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Gagamitin natin yung recorded directions at distances bilang clues."

    show jiperson normal at offscreenright
    show jiperson normal at walk(position=0.8)
    pause 0.8
    jiperson_ti "So hindi lang kung saan sila pumunta, pati na rin kung gaano kalayo at anong direksyon."
    judet_ti "Hmmm... and kapag pinagsama natin yung route, distance, at direction..."
    jipri_ta "...mas makikita natin kung alin ang mas consistent."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jiperson
    hide jipri
    hide judet

    scene museum
    show c4_ev3 at Transform(xpos=960, ypos=525, zoom=0.025)
    with dissolve

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ta "Wait, nasa Limasawa tayo?"

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Oo."

    show judet normal at offscreenright
    show judet normal at walk(position=0.88)
    pause 0.8
    judet_ta "Ibig sabihin pwede natin ma-check dito yung ibang descriptions ng Mazua?"

    show judet normal at walk(position=0.92, time=0.6)
    show jiperson normal at walk(position=0.74, time=0.6)
    pause 0.6

    window hide 
    hide c4_ev3
    call screen search_item(ev_c3_b6, 960, 525, 0.025, 0.03, idle_img="evidences/limasawa_6b.png", hover_img="evidences/limasawa_6.png")
    $ inventory.append(ev_c3_b6)
    call screen examine_clue(ev_c3_b6)

    jipri_ta "Sa account ni Pigafetta, ang Mazua ay inilarawan bilang isang isla."
    jiperson_ta "And Limasawa is an island."
    judet_ti "Pero sabi mo kanina, hindi sapat ang isang evidence."
    jiperson_ta "Correct. Kaya kailangan pa rin natin i-connect sa route, distance, direction, at sa original account."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jiperson
    hide jipri
    hide judet

    scene library
    show c4_ev4 at Transform(xpos=90, ypos=630, zoom=0.05)
    with dissolve

    show judet normal at offscreenleft
    show judet normal at walk(position=0.5)
    pause 0.8
    judet_ta "Ito na ba yung shrine at investigation board?"

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Oo. At dito natin pagsasama-samahin ang lahat."

    window hide 
    hide c4_ev4
    call screen search_item(ev_c3_b9, 90, 630, 0.05, 0.06)
    $ inventory.append(ev_c3_b9)
    call screen examine_clue(ev_c3_b9)

    show jiperson normal at offscreenright
    show jiperson normal at walk(position=0.8)
    pause 0.8
    jiperson_ti "Kapag pinag-connect natin lahat..."
    judet_ta "Mas nag-lead sa Limasawa."
    jipri_ta "Hmm... Pero kailangan nating tandaan na hindi lamang isang evidence ang nagbigay sa atin ng conclusion."
    jipri_ta "So, after reviewing all the evidence, which side are you guys?"

    menu:
        "BUTUAN":
            $ historical_choice = "Butuan"
            jump chapter4_choice_result
        "LIMASAWA":
            $ historical_choice = "Limasawa"
            jump chapter4_choice_result

label chapter4_choice_result:
    jipri_ta "Interesting. Pero hindi pa tapos ang investigation."
    judet_ta "Bakit? May kulang pa ba na evidence?"
    jipri_ta "Meron."
    jipri_ta "At dito natin malalaman kung ano ang naging conclusion kung Butuan ba o Limasawa."

    pause 1.0
    
    show text "{size=76}END OF CHAPTER 4{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve

    return