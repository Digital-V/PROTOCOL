image c2_ev1 = "evidences/butuan_5.png"
image c2_ev2 = "evidences/butuan_4.png"
image c2_ev3 = "evidences/butuan_6b.png"

default isTeamLimasawa = False

label chapter2:
    $ current_chapter = 2

    scene black
    with fade

    show text "{size=76}CHAPTER 2{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve
    play music "audio/bg_music2.mp3" fadein 1.0 volume 0.2 loop
    
    scene monument
    show c2_ev1 at Transform(xpos=1000, ypos=725, zoom=0.015)
    with fade

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5)
    pause 1.0

    jipri_ta "Narito naman tayo sa dakong kung saan matatagpuan ang monumento ukol sa pangyayari ng Sunday Mass dito sa Butuan"

    show judet normal at offscreenleft
    show judet normal at walk(position=0.2)
    pause 1.0
    
    judet_ta "Woah! Kung di ako nagkakamali ito ay ipinatayo ng pamahalaang Kastila, di ba?"

    jipri_ta "Tama. base sa history ay itinayo ito ng mga prayleng rekolekto noong 1872 upang igunita ang unang Misa na nangyari noong Abril 8, 1521."

    show jipri normal at walk(position=0.9, time=0.8)
    pause 1.0

    window hide
    hide c2_ev1
    call screen search_item(ev_c2_b1, 1000, 725, 0.015, 0.02)
    $ inventory.append(ev_c2_b1)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c2_b1)
    
    show jiperson normal at offscreenright
    show jiperson normal at walk(position=0.5)
    pause 1.0

    jiperson_ti "Pero, di naman siguro nangangahulugang dito talaga nangyari sa lugar na to ang unang Misa."

    jipri_ta "May punto kayo ngunit base kasi sa impormasyong ‘to, mismong pamahalaan na ng Kastila ang nagpatayo ng monument na ito. Kaya naman masasabi natin na dito talaga nangyari ang unang Misa. Sino pa bang mas makakaalam nito kundi ang mismong mga Kastila?"

    judet_ti "Eh, ngunit naroon din ang tanong kung mapagkakatiwalaan ba talaga mismo ang mga Kastila?"

    jipri_ta "Oh siya oh siya, dumako naman tayo sa susunod na lugar at baka mainip na kayo rito."

    show judet normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 1.2
    
    hide judet
    hide jipri
    hide jiperson

    scene seaside_road
    with fade
    
    show judet normal at offscreenleft
    show judet normal at walk(position=0.5)
    pause 1.0
    
    judet_ta "Jipri, bukod sa mga ebidensyang nakuha natin, may mga iba pa bang nagpapatunay na Butuan ang lugar ng Unang Misa?"
    
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 1.0
    
    jipri_ti "Hmm, kung 'di ako nagkakamali, may isinulat si Padre Colin, isang hesuwistang misyonaryo na naglimbag ng Labor Evangelica. Base sa kanyang ang Unang Misa mismo ay dito sa Butuan. Heto, mayro'n akong kopya kung gusto mo makita."

    $ inventory.append(ev_c2_b2)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c2_b2)
    
    show jiperson normal at offscreenright
    show jiperson normal at walk(position=0.8)
    pause 1.0

    jiperson_ta "Parang karamihan ng mga misyonaryo ay iisa lang ang sinasabi, Butuan talaga ang lugar ng Unang Misa. (Kaso bakit nga ba pare-parehas sila ng sinasabi?)"

    judet_ta "Oo nga! Pero 'di ko rin mapigilan at isipin na ano ang naging rason nila bakit Butuan ang lugar na kung saan nangyari ang Unang Misa?"

    jipri_ta "Hindi kita masisisi kung ganyan ang naiisip mo ngunit hayaan natin ang mga ebidensya ang magdikta."
    
    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 1.2
    
    hide jipri
    hide judet
    hide jiperson

    scene coastal_area
    show c2_ev3 at Transform(xpos=150, ypos=750, zoom=0.05)
    with fade

    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 1.0
    
    judet_ta "Sa wakas at narito na rin tayo sa huling dako natin!"

    show judet normal at walk(position=0.5)
    show jiperson normal at offscreenright
    show jiperson normal at walk(position=0.8)
    pause 1.0

    jiperson_ta "Grabe, ang haba ng nilakbay natin pero di ako makapagreklamo dahil sa ganda ng mga tanawin dito! Bandang don makikita mo rin ang mga barkong dumadako!"
    
    show judet normal at walk(position=0.25)
    show jiperson normal at walk(position=0.46)
    show jipri normal at offscreenright
    show jipri normal at walk(position=0.8)
    pause 1.0

    jipri_ta "Sa totoo lang, kaya ito rin ang sinadya kong gawing dulo dahil iba ang ganda rito."
    
    judet_ti "Napaisip lang ako, kung tatanggalin mo ang mga istrukturang nakikita natin ngayon, eto siguro mismo ang nakita nila Magellan noong napadpad sila dito. Imagine kung gaano mas kaganda ang tanawin nilang nakita."
    
    jipri_ta "Ah! Ngayong nabanggit mo si Magellan, isa pa sa mga naging dahilan na kung bakit Butuan ang nasabing lugar ng unang misa ay dahil dito sila dumako matapos ang laban nila sa Mactan."
    
    jiperson_ta "Siyang tunay?"
    
    jipri_ta "Tunay, tunay. Base sa kanilang paglalayag, ang mga natitirang barko ay tumungo sa baybayin ng hilaga at kanluran ng Mindanao."
    

    window hide
    hide c2_ev3
    call screen search_item(ev_c2_b3, 150, 750, 0.05, 0.06, idle_img="evidences/butuan_6b.png", hover_img="evidences/butuan_6.png")
    $ inventory.append(ev_c2_b3)
    $ play_sfx("audio/item_found.mp3", 3.0)
    call screen examine_clue(ev_c2_b3)
    
    judet_ta "Ito ba 'yung mapa ukol sa direksyon ng kanilang paglalayag?"
    
    jiperson_ti "Mukhang ito nga."
    
    jipri_ta "Ayang nakikita nyo ay ang kanilang ruta tungo rito sa Butuan."

    judet_ta "Hmm, napaka-convincing ng mga evidences nakita natin at kung ako ay magiging totoo sa inyo, hindi ko rin maiwasan na maisip na rito talaga nangyari ang unang misa. Ikaw Jiperson, ano sa tingin mo?"

    menu:
        "BUTUAN":
            $ isTeamLimasawa = False
            judet_ti "Hindi kita masisisi, talagang malakas ang mga ebidensyang nakita natin."
        "LIMASAWA":
            $ isTeamLimasawa = True
            judet_ti "Oh? Talagang di ka magpapatinag sa kabila ng mga 'yon, mainam yan na nagtitiwala ka at pinanghahawakan mo ang iyong pinaniniwalaan."

    jipri_ta "O sya, pumunta naman tayo sa susunod na lugar at panigurado mas magugustuhan nyo roon!"

    show jipri normal at walk(position=1.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=1.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=1.5, time=1.2)
    pause 1.2
    
    hide jipri
    hide jiperson
    hide judet
    
    show text "{size=76}END OF CHAPTER 2{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve
    stop music fadeout 1.0
    return