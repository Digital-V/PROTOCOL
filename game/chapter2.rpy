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

    # Evidence 1: Monument
    scene monument
    show c2_ev1 at Transform(xpos=1000, ypos=725, zoom=0.015)
    with fade

    show jipri normal:
        offscreenleft
        walk(position=0.0)
    pause 1.0

    show jipri talking
    jipri "Narito naman tayo sa dakong kung saan matatagpuan ang monumento ukol sa pangyayari ng Sunday Mass dito sa Butuan"

    show jipri normal
    show judet normal:
        offscreenright
        walk(position=1.0)
    pause 1.0
    
    show judet talking
    judet "Woah! Kung di ako nagkakamali ito ay ipinatayo ng pamahalaang Kastila, di ba?"

    show judet normal
    show jipri talking at shake
    jipri "Tama. base sa history ay itinayo ito ng mga prayleng rekolekto noong 1872 upang igunita ang unang Misa na nangyari noong Abril 8, 1521."

    window hide
    hide c2_ev1
    call screen search_item(ev_c2_b1, 1000, 725, 0.015, 0.02)
    $ inventory.append(ev_c2_b1)
    call screen examine_clue(ev_c2_b1)
    
    hide screen examine_clue
    
    show jipri normal
    show judet normal at walk(position=0.85)
    show jiperson normal:
        offscreenright
        walk(position=1.1)
    pause 0.5

    show jiperson thinking
    jiperson "Pero, di naman siguro nangangahulugang dito talaga nangyari sa lugar na to ang unang Misa."

    show jiperson normal
    show jipri talking at shake
    jipri "May punto kayo ngunit base kasi sa impormasyong 'to, mismong pamahalaan na ng Kastila ang nagpatayo ng monumentong ito. Kaya naman masasabi natin na dito talaga nangyari ang unang Misa. Sino pa bang mas makakaalam nito kundi ang mismong mga Kastila?"

    show jipri normal
    show judet thinking at shake
    judet "Eh, ngunit naroon din ang tanong kung mapagkakatiwalaan ba talaga mismo ang mga Kastila?"

    show judet normal
    show jipri talking at shake
    jipri "Oh siya oh siya, dumako naman tayo sa susunod na lugar at baka mainip na kayo rito."

    show jipri normal at walk(position=-0.5, time=2)
    show judet normal at  walk(position=-0.5, time=3)
    show jiperson normal at walk(position=-0.5, time=4)

    pause 1.0

    # Evidence 2: Historical Accounts
    scene seaside_road
    with fade
    
    show judet normal:
        offscreenright
        xalign 1.35
        walk(position=0.15, time=3)
    show jipri normal:
        offscreenright
        xalign 1.7
        walk(position=0.5, time=3)
    show jiperson normal:
        offscreenright
        xalign 2.05
        walk(position=0.85, time=3)
    pause 1.0
    
    show judet talking
    judet "Jipri, bukod sa mga ebidensyang nalakap natin, may mga iba pa bang nagpapatunay na Butuan ang lugar ng Unang Misa?"
    
    show judet normal
    show jipri thinking at shake
    jipri "Hmm, kung 'di ako nagkakamali, may isinulat si Padre Colin, isang hesuwistang misyonaryo na naglimbag ng Labor Evangelica. Base sa kanyang ang Unang Misa mismo ay dito sa Butuan. Heto, mayro'n akong kopya kung gusto mo makita."

    $ inventory.append(ev_c2_b2)
    call screen examine_clue(ev_c2_b2)

    pause 1.0
    
    show jipri normal 
    show jiperson talking at shake
    jiperson "Parang karamihan ng mga misyonaryo ay iisa lang ang sinasabi, Butuan talaga ang lugar ng Unang Misa. (Kaso bakit nga ba pare-parehas sila ng sinasabi?)"

    show jiperson normal
    show judet talking at shake
    judet "Oo nga! Pero 'di ko rin mapigilan at isipin na ano ang naging rason nila bakit Butuan ang lugar na kung saan nangyari ang Unang Misa?"

    show judet normal
    show jipri talking at shake
    jipri "Hindi kita masisisi kung ganyan ang naiisip mo ngunit hayaan natin ang mga ebidensya ang magdikta."
    
    show judet normal at  walk(position=-0.85, time=3)
    show jipri normal at walk(position=-0.5, time=3)
    show jiperson normal at walk(position=-0.15, time=3)

    pause 1.0

    # Evidence 3: Magellan's expedition
    scene coastal_area
    show c2_ev3 at Transform(xpos=150, ypos=750, zoom=0.05)
    with fade

    show judet normal:
        offscreenright
        walk(position=1.0)
    pause 1.0
    
    show judet talking
    judet "Sa wakas at narito na rin tayo sa huling dako natin!"

    show judet normal at walk(position=0.75)
    show jiperson normal:
        offscreenright
        walk(position=1.1)
    pause 1.0

    show jiperson talking
    jiperson "Grabe, ang haba ng nilakbay natin pero di naman ako nagrereklamo. Hindi ko maikakaila na maganda ang tanawin dito. Bandang don makikita mo rin ang mga barkong dumadako!"
    
    show judet normal at walk(position=0.5)
    show jiperson normal at walk(position=0.75)
    show jipri normal:
        offscreenright
        walk(position=1.1)
    pause 1.0

    show jipri talking
    jipri "Sa totoo lang, kaya ito rin ang sinadya kong gawing dulo dahil iba ang ganda rito."
    
    show jipri normal
    show judet thinking at shake
    judet "Napaisip lang ako, kung tatanggalin mo ang mga istrukturang nakikita natin ngayon, eto siguro mismo ang nakita nila Magellan noong sila'y naglayag. Hindi ko maisip kung gaano mas kaganda ang tanawin nilang nakita."
    
    show judet normal
    show jipri talking at shake
    jipri "Ah! Ngayong nabanggit mo si Magellan, isa pa sa mga naging dahilan na kung bakit Butuan ang nasabing lugar ng unang misa ay dahil dito sila dumako matapos ang laban nila sa Mactan."
    
    show jipri normal
    show jiperson talking at shake
    jiperson "Siyang tunay?"
    
    show jiperson normal
    show jipri talking at shake
    jipri "Tunay, tunay. Base sa kanilang paglalayag, ang mga natitirang barko ay tumungo sa baybayin ng hilaga at kanluran ng Mindanao."

    window hide
    hide c2_ev3
    call screen search_item(ev_c2_b3, 150, 750, 0.05, 0.06, idle_img="evidences/butuan_6b.png", hover_img="evidences/butuan_6.png")
    $ inventory.append(ev_c2_b3)
    
    call screen examine_clue(ev_c2_b3)
    hide screen examine_clue 
    pause 1.0
    
    show jipri normal
    show judet talking at shake
    judet "Ito ba 'yung mapa ukol sa direksyon ng kanilang paglalayag?"
    
    show judet normal
    show jiperson thinking at shake
    jiperson "Mukhang ito nga."
    
    show jiperson normal
    show jipri talking at shake
    jipri "Ayang nakikita nyo ay ang kanilang ruta tungo rito sa Butuan."

    show jipri normal
    show judet talking at shake
    judet "Hmm, napaka-convincing ng mga ebidensyang nakita natin at kung ako ay magiging totoo sa inyo, hindi ko rin maiwasan na maisip na rito talaga nangyari ang unang misa. Ikaw Jiperson, ano sa tingin mo?"

    menu:
        "BUTUAN":
            $ isTeamLimasawa = False
            show judet thinking at shake
            judet "Hindi kita masisisi, talagang malakas ang mga ebidensyang nakita natin."
        "LIMASAWA":
            $ isTeamLimasawa = True
            show judet thinking at shake
            judet "Oh? Talagang di ka magpapatinag sa kabila ng mga 'yon, mainam yan na nagtitiwala ka at pinanghahawakan mo ang iyong pinaniniwalaan."

    show judet normal
    show jipri talking at shake
    jipri "O sya, dako naman tayo sa susunod na lugar at panigurado mas magugustuhan nyo roon!"

    show judet normal at  walk(position=1.5, time=4)
    show jiperson normal at walk(position=1.5, time=3)
    show jipri normal at walk(position=1.5, time=2)

    pause 1.0
    
    show text "{size=76}END OF CHAPTER 2{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve

    return