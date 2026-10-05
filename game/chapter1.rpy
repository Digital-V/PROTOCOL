image c1_ev1 = "evidences/butuan_1.png"
image c1_ev2 = "evidences/butuan_3a.png"
image c1_ev3 = "evidences/butuan_2b.png"

label chapter1:
    $ current_chapter = 1

    scene black
    with fade

    show text "{size=76}CHAPTER 1{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve
    play music "audio/bg_music.mp3" fadein 1.0 volume 0.2 loop
    
    scene street
    $ speak_order = ["jiperson", "jipri", "judet"]
    
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 1.0

    jiperson_ta "Paano ba ‘yan, nandito na tayo. Ano pang hinihintay natin? Tara na, hanapin na natin ‘yang mga ebidensya na ‘yan!"
    
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.0)
    pause 1.0

    jipri_ta "Pwede bang wait lang? Kailangan nating maging handa kasi hindi biro ang mga kailangan nating hanapin. Mahalaga at Makasaysayan. Dalawang lugar at magulong ebidensya."
    
    show judet normal at offscreenright
    show judet normal at walk(position=1.0)
    pause 1.0

    judet_ti "Gagawin ba talaga natin to? Nalipasan na to ng panahon e."
    
    jipri_ta "Kailangan eh, wala tayong choice e."
    judet_ta "Edi tara na! Pero feeling ko kasi sa Butuan talaga yun e. "
    jipri_ta "Parang sure na sure ka ah?"
    judet_ta "Feeling ko lang naman!"
    jipri_ta "Tignan natin. Kaso hindi tayo pumunta dito para mag-assume agad. Nandito tayo para alamin kung ano ba talaga yung totoong nangyari."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jipri
    hide jiperson
    hide judet

    scene museum
    $ speak_order = ["jipri", "judet", "jiperson"]
    show c1_ev1 at Transform(xpos=935, ypos=525, zoom=0.025)
    with fade

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2, time=1.75)
    pause 2.0

    window hide 
    hide c1_ev1
    call screen search_item(ev_c1_b1, 935, 525, 0.025, 0.03)
    $ inventory.append(ev_c1_b1)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c1_b1)
    
    show jipri normal at walk(position=0.5, time=1.0)
    pause 1.0

    jipri_ta "May matagal nang historical tradition ang nag-uugnay sa Butuan expedition ni Magellan at sa First Mass. Edi matagal na palang may connection ang Butuan?"
    
    show judet normal at offscreenleft
    show judet normal at walk(position=0.0)
    pause 1.0

    judet_ti "Oo, kaya hindi rin basta-basta lang nabuo ang Butuan claim."
    jipri_ta "Kaya pala hindi rin basta-basta nabuo ang Butuan claim. May laban din naman pala!"
    jipri_ta "Oo nga. Pero pa hindi rin sapat eh. Kailangan pa natin ng iba pang ebidensya."

    show jiperson normal at offscreenright
    show jiperson normal at walk(position=1.0)
    pause 1.0

    jiperson_ta "Edi tara na! May narinig ako na sa Agusan River area, may pinuno raw na na-involve noong panahon ni Magellan. "
    
    show judet normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide judet
    hide jipri
    hide jiperson
    
    scene agusan_river
    $ speak_order = ["judet", "jipri", "jiperson"]
    show c1_ev2 at Transform(xpos=1400, ypos=700, zoom=0.0125)
    with fade

    show judet normal at offscreenright
    show judet normal at walk(position=0.5)
    pause 1.0

    judet_ta "O nandito na pala tayo sa Agusan River area, may narinig na rin ako na pangalawang evidence."

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.0)
    pause 1.0

    window hide 
    hide c1_ev2
    call screen search_item(ev_c1_b2, 1400, 700, 0.0125, 0.0226, idle_img="evidences/butuan_3a.png", hover_img="evidences/butuan_3b.png") 
    $ inventory.append(ev_c1_b2)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c1_b2)
    
    show jiperson normal at offscreenright
    show jiperson normal at walk(position=1.0)
    pause 1.0

    jipri_ta " Eto na ba yun? May koneksyon ba ‘yan?"
    jiperson_ta "Teka lang, meron pa akong nahanap. May nakasulat din kasi dito na may pinuno raw sa Butuan ang kasama sa naging expedition ni Magellan. "
    jipri_ta "Kung naging bahagi ang pinuno ng Butuan, mas magiging convincing yung connection."
    judet_ti "Pero hindi pa rin sapat ‘yan para masabi nating sa Butuan nangyari ang First Mass."
    jipri_ta "Tama. Kailangan pa rin natin maging maingat sa mga ebidensya na nahahanap natin."
    jiperson_ta "May na-search ako na isa pang lugar na pwede nating puntahan para makahanap pa ng ibang ebidensya."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jipri
    hide judet
    hide jiperson

    scene balanghai_shrine
    $ speak_order = ["jiperson", "judet", "jipri"]
    show c1_ev3 at Transform(xpos=653, ypos=630, zoom=0.025)
    with fade

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 1.0
    
    show judet normal at offscreenleft
    show judet normal at walk(position=0.0)
    pause 1.0

    show jipri normal at offscreenright
    show jipri normal at walk(position=1.0)
    pause 1.0

    window hide 
    hide c1_ev3
    call screen search_item(ev_c1_b3, 653, 630, 0.025, 0.03, idle_img="evidences/butuan_2b.png", hover_img="evidences/butuan_2a.png") 
    $ inventory.append(ev_c1_b3)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c1_b3)
    
    jiperson_ta "Last na muna to. Kailangan na nating mag pahinga para may lakas tayo sa paghahanap."
    judet_ta "Okay na ‘yan! Tatlo na yan oh. "
    jipri_ta "Kaya nga. Konti na lang mako-convince na ako na sa Butuan talaga."
    jiperson_ta "Teka lang, hindi pa tayo tapos. Marami pa tayong dapat malaman."
    jipri_ta "May point ka. Magiging biased tayo kung ‘di natin aalamin kung ano’ng connection meron sa Limasawa. "

    pause 1.0
    
    show text "{size=76}END OF CHAPTER 1{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve
    stop music fadeout 1.0
    return