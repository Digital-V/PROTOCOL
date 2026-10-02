label chapter3:
    $ current_chapter = 3

    scene black
    with fade
    show text "{size=76}CHAPTER 3{/size}" at truecenter
    with dissolve
    pause 3.0
    hide text
    with dissolve
    show text "{size=50}{i}Habang naglalakad papunta sa susunod na lugar...{/size}{i}"
    with dissolve
    pause 3.0
    hide text
    with dissolve
    
    scene street
    with fade
    
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.0)
    pause 1.0
    jiperson_ta "Grabe, parang ang dami na nating napuntahan. Akala ko ba simpleng investigation at pag-aaral lang 'to?"
    
    show judet normal at offscreenright
    show judet normal at walk(position=1.0)
    pause 1.0
    judet_ta "Simple sana kung isang lugar lang ang may claim eh."
    
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5)
    pause 1.0
    jipri_ta "At kung lahat ng evidence ay nagtuturo sa iisang direksyon at lugar."
    jiperson_ti "Pero hindi naman ganoon ang nangyayari."
    jipri_ta "Exactly."
    judet_ti "So, saan na tayo papunta ngayon?"
    jipri_ta "Sa lugar kung saan pwede natin mahanap at mabalikan ang pinakaunang account patungkol sa First Mass."

    show jiperson normal at walk(position=-0.5, time=1.5)
    show jipri normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5
    
    # --- MUSEUM INSTANCE 1 ---
    scene museum
    with dissolve
    
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5)
    show judet normal at offscreenright
    show judet normal at walk(position=1.0)
    pause 1.0
    
    jipri_ta "Nandito tayo ngayon para tingnan ang pinakaunang primary source ukol sa ekspedisyon."

    # Move Jipri out of the center so he doesn't block the evidence
    show jipri normal at walk(position=0.15, time=0.75)
    pause 0.75

    window hide 
    call screen search_item(ev_c3_b1, 935, 525, 0.025, 0.03)
    $ inventory.append(ev_c3_b1)
    
    show screen examine_clue(ev_c3_b1)
    "Evidence Found! Pigafetta’s Account showing the name Mazaua."
    hide screen examine_clue 

    jiperson_ti "Wait… Mazua?"
    judet_ti "Huh? Hindi Butuan?"
    jipri_ta "Sa account ni Pigafetta, ang lugar ay tinawag na Mazua, at doon inilagay ang Easter Sunday Mass noong March 31, 1521."
    jiperson_ti "Pero bakit ganoon? Yung mga evidence na nakuha natin ay nagl-lead sa Butuan. Paano nangyari iyon?"
    judet_ta "Ayan, kaya hindi tayo matapos-tapos e. Yung mga evidence na nakukuha natin sumasalungat sa isa’t-isa."
    jipri_ta "Dumagdag pa yang Mazua. Hindi natin alam kung saan at ano ba ang tinutukoy nito."

    show jipri normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5

    # --- MUSEUM INSTANCE 2 ---
    scene museum
    with fade
    
    # Show all three characters cleanly arranged on the left/middle-left so they don't block the right-side evidence
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.15)
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.99)
    show judet normal at offscreenright
    show judet normal at walk(position=0.85)
    pause 1.5
    
    judet_ta "Kung Mazua yung pangalan sa original account ni Pigafetta, saan naman natin hahanapin 'yun?"
    jipri_ta "‘Yan ang kailangan nating alamin."
    
    window hide 
    call screen search_item(ev_c3_b2, 935, 525, 0.025, 0.03)
    $ inventory.append(ev_c3_b2)
    
    show screen examine_clue(ev_c3_b2)
    "Evidence Found! Mazua Identity map with a question mark."
    hide screen examine_clue

    judet_ta "Kung Mazua yung pangalan sa original account ni Pigafetta, saan naman natin hahanapin 'yun?"
    jipri_ta "‘Yan ang kailangan nating alamin."

    # Since Jiperson is already on screen at position 0.4, he will speak without jumping to the center!
    jiperson_ta "So, dalawang possible location ulit?"
    jipri_ta "Sa investigation natin, kailangan ikumpara ang Butuan at Limasawa base sa mga historical clues."

    show jiperson normal at walk(position=-0.5, time=1.5)
    show jipri normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5
    
    scene coastal_area2
    with fade
    
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.0)
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5)
    show judet normal at offscreenright
    show judet normal at walk(position=1.0)
    pause 1.5

    window hide 
    call screen search_item(ev_c3_b3, 1015, 825, 0.025, 0.03)
    $ inventory.append(ev_c3_b3)
    
    show screen examine_clue(ev_c3_b3)
    "Evidence Found! Geographical features description card."
    hide screen examine_clue
    
    jiperson_ta "Ito ba yung geographical evidence?"
    jipri_ta "Oo. Kung may description ng lugar, pwede natin ikumpara iyon sa actual geography."
    judet_ti "So basically, titignan natin alin sa dalawa ang tugma sa geographical features ng Mazua."
    jipri_ta "Exactly. Tama."
    jiperson_ti "Wait, parang nag-i-iba na yung approach natin."
    jipri_ta "Akala ko ako lang ang naka-pansin."
    jipri_ti "Ngayon, hinahanap na natin kung alin ang mas tugma sa description ng Mazua instead na hanapin natin mismo kung ano ang connection nito sa Butuan."

    show jiperson normal at walk(position=-0.5, time=1.5)
    show jipri normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5
    
    scene seaside_road
    with fade
    
    show judet normal at offscreenright
    show judet normal at walk(position=1.0)
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5)
    pause 1.0
    
    judet_ta "Wait, bakit tayo bumalik sa Butuan side?"
    jipri_ti "May kailangan tayong linawin tungkol sa ruler evidence na nakita natin noon."
    
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.0)
    pause 1.0
    
    jiperson_ta "Yung ruler na connected sa Butuan?"
    jipri_ti "Oo."

    window hide 
    call screen search_item(ev_c3_b7, 1015, 825, 0.025, 0.03)
    $ inventory.append(ev_c3_b7)
    
    show screen examine_clue(ev_c3_b7)
    "Evidence Found! Two Rulers character dossier cards."
    hide screen examine_clue
    
    jipri_ti "May mga pinunong naging bahagi ng pangyayari noong expedition."
    jipri_ta "May connection ang isang ruler sa Butuan, pero may mga ibang lugar at pinuno ring involved sa mga pangyayari."
    judet_ti "So? Hindi porke connected sa Butuan yung isang ruler, ibig sabihin doon na mismo ang First Mass?"
    jipri_ta "Tama."
    jiperson_ta "Ang ruler ay evidence ng connection, pero kailangan pa rin nating patunayan ang lugar/lokasyon."

    show jiperson normal at walk(position=-0.5, time=1.5)
    show jipri normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5
    
    scene library
    with fade
    
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.0)
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5)
    show judet normal at offscreenright
    show judet normal at walk(position=1.0)
    pause 1.5
    
    jiperson_ta "Ano naman ang hahanapin natin dito?"
    jipri_ta "Mga historical writings. Kailangan nating kumpirmahin ang mga naunang sources at mga interpretations."
    jiperson_ti "Edi may pagkakaiba?"
    jipri_ta "Meron."

    window hide 
    call screen search_item(ev_c3_b8, 1475, 225, 0.025, 0.03)
    $ inventory.append(ev_c3_b8)
    
    show screen examine_clue(ev_c3_b8)
    "Evidence Found! Primary Sources vs. Later Tradition files."
    hide screen examine_clue
    
    jipri_ti "Sa account ni Pigafetta, ginamit niya ang pangalang Mazua."
    jiperson_ta "Habang may mga later historical writings na nag-uugnay nito sa Butuan."
    jipri_ta "Kailangan nating tignan kung saan nanggaling ang bawat interpretation."
    jiperson_ta "Meaning, hindi natin pwedeng paghaluin yung original account at yung mga bagong interpretation."
    
    scene library
    with fade
    
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.0)
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5)
    show judet normal at offscreenright
    show judet normal at walk(position=1.0)
    pause 1.5
    
    judet_ta "So… yung mga evidence natin sa Butuan, hindi naman pala basta-basta fake."
    jiperson_ta "Pero hindi rin natin masasabi na sapat 'iyon para masabing Butuan talaga ang Mazua."
    jipri_ta "Tama."
    judet_ti "May historical connection naman. May ruler. May traditions."
    jipri_ti "Pero may original account na nagsasabing Mazua, at kailangan pa nating malaman kung saan ba talaga 'yon."
    jipri_ta "At ngayon, alam na natin kung ano ang susunod nating gagawin."
    judet_ta "Ano naman 'yon?"
    jipri_ta "Hanapin natin kung aling lugar ang pinaka tumutugma sa lahat ng descriptions ng Mazua."
    jiperson_ta "Hmmm… *sigh* May point ka diyan."
    
    "END OF CHAPTER 3"
    return