
image c4_ev2 = "evidences/limasawa_5.png"
image c4_ev3 = "evidences/limasawa_6b.png"
image c4_ev4 = "evidences/limasawa_9.png"

label chapter4:
    $ current_chapter = 4
    scene black
    with fade

    show text "{size=76}CHAPTER 4{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve
    play music "audio/bg_music4.mp3" fadein 1.0 volume 0.2 loop
    scene coastal_area2
    with fade

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ta "Ito na ba yung mismong ruta ng expedition?"

    $ inventory.append(ev_c3_b4)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c3_b4)

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Oo. Ikumpara niyo 'yung recorded route d'yan sa Butuan at Limasawa."

    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ti "Paano kung hindi tugma ‘yung location sa route, ibig sabihin ba questionable na ‘yung claim?"
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
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c3_b5)

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Gagamitin natin yung recorded directions at distances bilang clues."

    show jiperson normal at offscreenright
    show jiperson normal at walk(position=0.8)
    pause 0.8
    jiperson_ti "Ah, edi hindi lang pala basta kung saan sila napunta, susukatin din natin kung gaano kalayo at kung anong direksyon ang dinaanan nila."
    judet_ti "At kapag pinagsama natin ‘yung ruta, gano kalayo, at direksyon…"
    jipri_ta " …mas makikita kung alin ang may sense."

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
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c3_b6)

    jipri_ta "Sa account ni Pigafetta, ang Mazaua ay isang isla."
    jiperson_ta "Limasawa Island?"
    judet_ti "Ohhh, pero sabi mo kanina, hindi sapat ang isang ebidensya lang. "
    jiperson_ta "Tama. Kaya kailangan pa rin alamin at ikumpara to sa ruta, layo, direksyon, at sa description sa account ni Pigafetta. "

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
    judet_ta "Ito na ba ‘yung shrine?"

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Oo. At dito na rin pagsasama-samahin ang lahat."

    window hide 
    hide c4_ev4
    call screen search_item(ev_c3_b9, 90, 630, 0.05, 0.06)
    $ inventory.append(ev_c3_b9)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c3_b9)

    show jiperson normal at offscreenright
    show jiperson normal at walk(position=0.8)
    pause 0.8
    jiperson_ti "Kapag pinag-connect natin lahat..."
    judet_ta "Mas pumapabor sa Limasawa."
    jipri_ta "Kailangan nating tandaan na hindi lang isang ebidensya ang nagbigay ng conclusion na to."
    jipri_ta "So, after lahat ng nakita niyo, saan ginanap ang First Mass?"

    menu:
        "BUTUAN":
            $ historical_choice = "Butuan"
            jump chapter4_choice_result
        "LIMASAWA":
            $ historical_choice = "Limasawa"
            jump chapter4_choice_result

label chapter4_choice_result:
    jipri_ta "Interesting.Kaso, ‘di pa dito nagtatapos."
    judet_ta "Bakit? May kulang pa ba na ebidensya?"

    pause 1.0
    
    show text "{size=76}END OF CHAPTER 4{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve
    stop music fadeout 1.0
    return