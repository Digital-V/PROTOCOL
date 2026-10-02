image c3_ev1 = "evidences/limasawa_1a.png"
image c3_ev2 = "evidences/limasawa_2.png"
image c3_ev5 = "evidences/limasawa_8a.png"

label chapter3:
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

    scene street
    with fade

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ta "Grabe, parang ang dami na nating napuntahan. Akala ko ba simpleng investigation at pag-aaral lang 'to?"

    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ta "Simple sana kung isang lugar lang ang may claim eh."

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "At kung lahat ng evidence ay nagtuturo sa iisang direksyon at lugar."
    jiperson_ti "Pero hindi naman ganoon ang nangyayari."
    jipri_ta "Exactly."
    judet_ti "So, saan na tayo papunta ngayon?"
    jipri_ta "Sa lugar kung saan pwede natin mahanap at mabalikan ang pinakaunang account patungkol sa First Mass."

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
    call screen examine_clue(ev_c3_b1)

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ti "Wait… Mazua?"

    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ti "Huh? Hindi Butuan?"
    jipri_ta "Sa account ni Pigafetta, ang lugar ay tinawag na Mazua, at doon inilagay ang Easter Sunday Mass noong March 31, 1521."
    jiperson_ti "Pero bakit ganoon? Yung mga evidence na nakuha natin ay nagl-lead sa Butuan. Paano nangyari iyon?"
    judet_ta "Ayan, kaya hindi tayo matapos-tapos e. Yung mga evidence na nakukuha natin sumasalungat sa isa’t-isa."
    jipri_ta "Dumagdag pa yang Mazua. Hindi natin alam kung saan at ano ba ang tinutukoy nito."

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
    judet_ta "Kung Mazua yung pangalan sa original account ni Pigafetta, saan naman natin hahanapin 'yun?"

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
    call screen examine_clue(ev_c3_b2)

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 0.8
    jiperson_ta "So, dalawang possible location ulit?"
    jipri_ta "Sa investigation natin, kailangan ikumpara ang Butuan at Limasawa base sa mga historical clues."

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

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Oo. Kung may description ng lugar, pwede natin ikumpara iyon sa actual geography."

    $ inventory.append(ev_c3_b3)
    call screen examine_clue(ev_c3_b3)

    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ti "So basically, titignan natin alin sa dalawa ang tugma sa geographical features ng Mazua."
    jipri_ta "Exactly. Tama."
    jiperson_ti "Wait, parang nag-i-iba na yung approach natin."
    jipri_ta "Akala ko ako lang ang naka-pansin."
    jipri_ti "Ngayon, hinahanap na natin kung alin ang mas tugma sa description ng Mazua instead na hanapin natin mismo kung ano ang connection nito sa Butuan."

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
    jiperson_ta "Yung ruler na connected sa Butuan?"
    jipri_ti "Oo."

    $ inventory.append(ev_c3_b7)
    call screen examine_clue(ev_c3_b7)

    jipri_ti "May mga pinunong naging bahagi ng pangyayari noong expedition."
    jipri_ta "May connection ang isang ruler sa Butuan, pero may mga ibang lugar at pinuno ring involved sa mga pangyayari."
    judet_ti "So? Hindi porke connected sa Butuan yung isang ruler, ibig sabihin doon na mismo ang First Mass?"
    jipri_ta "Tama."
    jiperson_ta "Ang ruler ay evidence ng connection, pero kailangan pa rin nating patunayan ang lugar/lokasyon."

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
    jiperson_ta "Ano naman ang hahanapin natin dito?"

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 0.8
    jipri_ta "Mga historical writings. Kailangan nating kumpirmahin ang mga naunang sources at mga interpretations."
    jiperson_ti "Edi may pagkakaiba?"
    jipri_ta "Meron."

    window hide 
    hide c3_ev5
    call screen search_item(ev_c3_b8, 1475, 225, 0.040, 0.045, idle_img="evidences/limasawa_8a.png", hover_img="evidences/limasawa_8b.png")
    $ inventory.append(ev_c3_b8)
    call screen examine_clue(ev_c3_b8)

    jipri_ti "Sa account ni Pigafetta, ginamit niya ang pangalang Mazua."
    jiperson_ta "Habang may mga later historical writings na nag-uugnay nito sa Butuan."
    jipri_ta "Kailangan nating tignan kung saan nanggaling ang bawat interpretation."
    jiperson_ta "Meaning, hindi natin pwedeng paghaluin yung original account at yung mga bagong interpretation."

    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 0.8
    judet_ta "So… yung mga evidence natin sa Butuan, hindi naman pala basta-basta fake."
    jiperson_ta "Pero hindi rin natin masasabi na sapat 'iyon para masabing Butuan talaga ang Mazua."
    jipri_ta "Tama."
    judet_ti "May historical connection naman. May ruler. May traditions."
    jipri_ti "Pero may original account na nagsasabing Mazua, at kailangan pa nating malaman kung saan ba talaga 'yon."
    jipri_ta "At ngayon, alam na natin kung ano ang susunod nating gagawin."
    judet_ta "Ano naman 'yon?"
    jipri_ta "Hanapin natin kung aling lugar ang pinaka tumutugma sa lahat ng descriptions ng Mazua."
    jiperson_ta "Hmmm… *sigh* May point ka diyan."

    pause 1.0

    show text "{size=76}END OF CHAPTER 3{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve

    return