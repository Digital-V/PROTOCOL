image c3_ev1 = "evidences/limasawa_1a.png"
image c3_ev2 = "evidences/limasawa_2.png"
image c3_ev5 = "evidences/limasawa_8a.png"

label chapter3:
    $ current_chapter = 3

    scene black
    with fade

    show text "{size=76}CHAPTER 3{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve

    show text "{size=50}{i}Habang naglalakad papunta sa susunod na lugar...{/size}{i}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve
    play music "audio/bg_music3.mp3" fadein 1.0 volume 0.2 loop
    scene street
    with fade
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ta "Ang dami na nating naikot. Akala ko ba simpleng investigation lang yung gagawin natin? Sumasakit na ulo ko sa dami ng kailangan nating alamin."
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Simple lang dapat to e, kung iisang lugar lang ang inaaral at ine-investigate natin."
    jiperson_ti "At kung ‘di nagsasalungat yung mga ebidensya."
    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ta "Edi saan na tayo papunta ngayon?"

    jipri_ta "Kailangan nating mahanap ‘yung pinagmulan, ‘yung mismong source na magtuturo tungkol sa First Mass. "
    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jiperson
    hide jipri
    hide judet

    scene museum
    show c3_ev1 at Transform(xpos=935, ypos=525, zoom=0.025)
    with dissolve

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5)
    pause 0.8
    jipri_ta "Nandito tayo ngayon para tingnan ang pinakaunang primary source ukol sa ekspedisyon."

    show jipri normal at walk(position=0.2, time=0.6)
    pause 0.6

    window hide 
    hide c3_ev1
    call screen search_item(ev_c3_b1, 935, 525, 0.025, 0.03, idle_img="evidences/limasawa_1a.png", hover_img="evidences/limasawa_1b.png")
    $ inventory.append(ev_c3_b1)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c3_b1)

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ti "Wait lang, ano tong “Mazaua” na sinasabi niya dito? Ano yon?"

    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ti "Huh? Hindi Butuan?"
    jipri_ta "Sa account ni Pigafetta, Mazaua ang pangalan ng lugar kung saan nangyari ang Easter Sunday Mass noong March 31, 1521. "
    jiperson_ti "Ang labo! Eh 'yung mga unang ebidensya natin puro sa Butuan ang bagsak. Paano nasingit 'tong Mazua na 'to? Ano ba talaga?"
    judet_ta "Kaya hindi tayo matapos-tapos, sumasalungat 'yung ibang ebidensya sa original account. "
    jipri_ta "Oh 'di ba, dumagdag pa 'yang Mazaua. Kailangan ding alamin kung saan yan."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jiperson
    hide jipri
    hide judet

    scene museum
    show c3_ev2 at Transform(xpos=935, ypos=525, zoom=0.025)
    with fade

    show judet normal at offscreenleft
    show judet normal at walk(position=0.5)
    pause 0.8
    judet_ta "Kung Mazua yung pangalan sa original account ni Pigafetta, saan naman natin hahanapin yun?"

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "‘Yan ang kailangan nating alamin."

    show judet normal at walk(position=0.8, time=0.6)
    pause 0.6

    window hide 
    hide c3_ev2
    call screen search_item(ev_c3_b2, 935, 525, 0.025, 0.03)
    $ inventory.append(ev_c3_b2)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c3_b2)

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ta "Anak ng... edi, babalik tayo sa dalawang possible location ulit? Pagod na ako."
    jipri_ta "Ikukumpara natin ang Butuan at Limasawa base sa mga historical clues niyan."
    judet_ta "Ibig sabihin, hindi pwedeng porke't matagal nang connected ang Butuan sa First Mass eh 'yun na agad ang Mazua."
    jiperson_ta "Tama. Hindi tayo pwedeng bumase lang sa kwento-kwento o monumento. Hihimayin natin kung aling lugar sa dalawa ang mas tugma sa description ng Mazaua na 'yan."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jiperson
    hide jipri
    hide judet

    scene coastal_area2
    with fade

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ta "Ito ba yung geographical evidence?"
    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ti "Edi kailangan natin ikumpara to sa nakalagay na description ng Mazaua?"
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Exactly. Tama."
    $ inventory.append(ev_c3_b3)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c3_b3)
    jiperson_ta "Ang galing! Nag e-enjoy na ako sa investigation na to."

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
    with fade

    show judet normal at offscreenleft
    show judet normal at walk(position=0.5)
    pause 0.8
    judet_ta "Wait, bakit tayo bumalik sa Butuan side?"

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ti "May kailangan tayong linawin tungkol sa ruler evidence na nakita natin noon."

    show jiperson normal at offscreenright
    show jiperson normal at walk(position=0.8)
    pause 0.8
    jiperson_ta "Yung ruler ba na connected sa Butuan? Anong meron don? "
    jipri_ti "Oo."
    $ inventory.append(ev_c3_b7)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c3_b7)

    jipri_ti "May mga pinunong naging bahagi ng pangyayari noong expedition. May connection ‘yung isang ruler sa Butuan, pero may mga ibang ruler din na kasama sa pangyayari na yon."
    judet_ti "Oh, ngayon lahat nag m-make sense. Hindi porke’t connected sa Butuan yung isang ruler na kasama doon, ibig sabihin doon na mismo ang First Mass."
    jiperson_ta "Yung ruler, nagpapakita lang yan na may connection. Kailangan pa rin natin alamin kung saan ba talaga ‘yung mismong lugar."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jiperson
    hide jipri
    hide judet

    scene library
    show c3_ev5 at Transform(xpos=1475, ypos=225, zoom=0.025)
    with fade

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ta "Tapos ngayon, andito tayo sa puro libro? Ano naman hahalungkatin natin dito?"

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Mga historical writings. I-check niyo ‘yung mga unang sources na nakuha at ikumpara sa mga bagong interpretations."

    window hide 
    hide c3_ev5
    call screen search_item(ev_c3_b8, 1475, 225, 0.040, 0.045, idle_img="evidences/limasawa_8a.png", hover_img="evidences/limasawa_8b.png")
    $ inventory.append(ev_c3_b8)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c3_b8)

    jipri_ti "Sa account ni Pigafetta, ginamit niya ang pangalang Mazua."
    jiperson_ta "Tapos 'yung mga sumunod na chismis—este, historical writings pala, pilit na inuugnay sa Butuan 'yung lugar."
    jipri_ta "Kaya kailangan malaman kung saan galing ang bawat interpretation at kung bakit nila naisulat yon."
    jiperson_ta "Gets. Hindi natin pwedeng pagsamahin ang mga interpretation na galing sa iba’t ibang sources o account."

    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ta "Yung mga ebidensya natin sa Butuan, hindi naman pala basta-basta. May ebidensya pa rin na sumosuporta. "
    jiperson_ta "‘di rin natin masasabi na sapat ‘yon para masabing Butuan talaga ang Mazaua."
    jipri_ta "Tama."
    judet_ti "May historical connection naman. May ruler. May traditions."
    jipri_ti "Pero may original account na nagsasabing Mazua, at kailangan pa nating malaman kung saan ba talaga 'yon."
    jipri_ta "At ngayon, alam na natin kung ano ang susunod nating gagawin."
    judet_ta "Ano nang plano?"
    jipri_ta "Hanapin natin kung aling lugar ang pinakatumatugma sa lahat ng descriptions ng Mazua."

    pause 1.0

    show text "{size=76}END OF CHAPTER 3{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve
    stop music fadeout 1.0
    return