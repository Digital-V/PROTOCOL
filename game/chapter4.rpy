label chapter4:

    scene black
    with fade

    show text "{size=76}CHAPTER 4{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve

    scene coastal_area2
    with fade

    # EVIDENCE 1: EXPEDITION ROUTE
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.15, time=2)
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5, time=3)
    show judet normal at offscreenright
    show judet normal at walk(position=0.85, time=2)
    pause 3.0

    jiperson_ta "So ito na ba yung route ng expedition?"
    jipri_ta "Oo. Kailangan nating ikumpara ang recorded route sa lugar na pinagpipilian natin. Sa Butuan o Limasawa."
    
    window hide 
    call screen search_item(ev_c3_b4, 1400, 665, 0.035, 0.045)
    $ inventory.append(ev_c3_b4)
    
    show screen examine_clue(ev_c3_b4)
    "Evidence Found! Expedition Route map comparing Butuan and Limasawa."
    hide screen examine_clue

    judet_ti "So paano kung hindi tugma yung location sa route, ibig sabihin ba questionable na yung claim?"
    jipri_ta "Tama."

    show jipri normal at walk(position=-0.5, time=1.5)
    show jiperson normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5

    hide jiperson
    hide jipri
    hide judet

    # EVIDENCE 2: DISTANCE AND DIRECTION
    scene seaside_road
    with fade

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.15, time=2)
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5, time=3)
    show judet normal at offscreenright
    show judet normal at walk(position=0.85, time=2)
    pause 3.0

    judet_ta "May compass at distance markers dito."
    
    window hide 
    call screen search_item(ev_c3_b5, 1680, 850, 0.025, 0.035)
    $ inventory.append(ev_c3_b5)
    
    show screen examine_clue(ev_c3_b5)
    "Evidence Found! Distance and Direction compass markers."
    hide screen examine_clue

    jipri_ta "Gagamitin natin yung recorded directions at distances bilang clues."
    jiperson_ti "So hindi lang kung saan sila pumunta, pati na rin kung gaano kalayo at anong direksyon."
    judet_ti "Hmmm... and kapag pinagsama natin yung route, distance, at direction..."
    jipri_ta "...mas makikita natin kung alin ang mas consistent."

    show jipri normal at walk(position=-0.5, time=1.5)
    show jiperson normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5

    hide jiperson
    hide jipri
    hide judet

    # EVIDENCE 3: ISLAND DESCRIPTION
    scene museum
    with dissolve

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.15, time=2)
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.95, time=3)
    show judet normal at offscreenright
    show judet normal at walk(position=0.80, time=2)
    pause 3.0

    jiperson_ta "Wait, nasa Limasawa tayo?"
    jipri_ta "Oo."
    judet_ta "Ibig sabihin pwede natin ma-check dito yung ibang descriptions ng Mazua?"
    
    window hide 
    call screen search_item(ev_c3_b6, 960, 525, 0.025, 0.03)
    $ inventory.append(ev_c3_b6)
    
    show screen examine_clue(ev_c3_b6)
    "Evidence Found! Island Description showing mountains and shoreline."
    hide screen examine_clue

    jipri_ta "Sa account ni Pigafetta, ang Mazua ay inilarawan bilang isang isla."
    jiperson_ta "And Limasawa is an island."
    judet_ti "Pero sabi mo kanina, hindi sapat ang isang evidence."
    jiperson_ta "Correct. Kaya kailangan pa rin natin i-connect sa route, distance, direction, at sa original account."

    show jipri normal at walk(position=-0.5, time=1.5)
    show jiperson normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5

    hide jiperson
    hide jipri
    hide judet

    # EVIDENCE 4: HISTORICAL INVESTIGATION
    scene library
    with dissolve

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.15, time=2)
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5, time=3)
    show judet normal at offscreenright
    show judet normal at walk(position=0.85, time=2)
    pause 3.0

    judet_ta "Ito na ba yung shrine at investigation board?"
    jipri_ta "Oo. At dito natin pagsasama-samahin ang lahat."

    window hide 
    call screen search_item(ev_c3_b9, 90, 630, 0.05, 0.06)
    $ inventory.append(ev_c3_b9)
    
    show screen examine_clue(ev_c3_b9)
    "Evidence Found! Historical Investigation board connecting all clues to Limasawa."
    hide screen examine_clue

    jiperson_ti "Kapag pinag-connect natin lahat..."
    judet_ta "Mas nag-lead sa Limasawa."
    jipri_ta "Hmm... Pero kailangan nating tandaan na hindi lamang isang evidence ang nagbigay sa atin ng conclusion."
    jipri_ta "So, after reviewing all the evidence, which side are you guys?"

    # PLAYER CHOICE
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

    scene black
    with fade
    centered "{size=50}END OF CHAPTER 4!!{/size}"
    pause 2.0

    return