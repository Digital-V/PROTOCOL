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

    scene street
    
    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5)
    pause 1.0

    jipri_ta "Isang makasaysayang pangyayari, dalawang lugar, at mga ebidensya na parang hindi nagtutugma sa isa't-isa."
    
    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.2)
    pause 1.0

    jiperson_ta "Paano ba yan nandito na tayo sa pag ba-bakasyunan natin para mag explore at maghanap ng evidence para sa First Mass."
    
    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 1.0

    judet_ti "Gagawin ba talaga natin to? Nalipasan na to ng panahon e, kailangan pa ba natin ulit ungkatin at imbestigahan?"
    
    jipri_ta "Kaya nga tayo nandito."
    judet_ta "Edi tara na! pero feeling ko sa Butuan talaga e."
    jipri_ta "Parang sure na sure ka ah?"
    judet_ta "Feeling ko lang naman!"
    jipri_ta "Tignan natin. Pero hindi tayo pumunta dito para mag assume agad. Nandito tayo para alamin kung ano ba talaga ang totoong nangyari."

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
    show c1_ev1 at Transform(xpos=935, ypos=525, zoom=0.025)
    with fade

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.5, time=1.75)
    pause 2.0

    jipri_ta "Nandito na tayo sa museum para makakita ng pang unang evidence. O ito na pala pang unang evidence para saatin."
    
    show jipri normal at walk(position=0.1, time=0.6)
    pause 0.6

    window hide 
    hide c1_ev1
    call screen search_item(ev_c1_b1, 935, 525, 0.025, 0.03)
    $ inventory.append(ev_c1_b1)
    call screen examine_clue(ev_c1_b1)
    
    jipri_ta "May matagal nang historical tradition na nag uugnay sa Butuan sa expedition ni Magellan at sa First Mass."
    jipri_ta "So matagal na palang may connection ang Butuan sa First Mass."
    
    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 1.0

    judet_ti "Oo, kaya hindi rin basta-basta lang nabuo ang Butuan claim."
    jipri_ta "Interesting, pero kailangan pa natin makahanap ng iba pang evidence."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jipri
    hide judet

    scene agusan_river
    show c1_ev2 at Transform(xpos=1400, ypos=700, zoom=0.0125)
    with fade

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 1.0

    jiperson_ta "Hali na kayo pumunta naman tayo sa susunod na lugar para maka-kalap pa ng iba pang evidence dahil sa Agusan River Area maraming tao ang nagsasabi na may pinunong na involve nung panahon ni Magellan."
    
    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 1.0

    judet_ta "O nandito na pala tayo sa Agusan River area may narinig na rin ako na pangalawang evidence."

    show judet normal at walk(position=0.99, time=0.6)
    pause 0.6

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.2)
    pause 1.0

    window hide 
    hide c1_ev2
    call screen search_item(ev_c1_b2, 1400, 700, 0.0125, 0.0226, idle_img="evidences/butuan_3a.png", hover_img="evidences/butuan_3b.png") 
    $ inventory.append(ev_c1_b2)
    call screen examine_clue(ev_c1_b2)
    
    jipri_ta "Ito ang sinabi satin ng ibang tao, Talaga bang may connection ito sa mga narinig mo Judet?"
    jiperson_ta "May nakita pa akong evidence. May nakatalagang pinuno nang Butuan ang sangkot sa mga pangyayari noong expedition."
    jipri_ta "Kung naging sangkot ang pinuno ng butuan mas magiging convincing yung connection nila sa expedition."
    judet_ti "Pero hindi pa rin ibig sabihin ay automatic na doon nga nangyari ang First Mass."
    jipri_ta "Tama. Kailangan pa rin nating tingnan kung ano mismo ang pinapatunayan at ipinapakita ng evidence."
    jiperson_ta "Exactly. Yun ang dapat talaga nating alamin."

    show jipri normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show jiperson normal at walk(position=-0.5, time=1.2)
    pause 0.4
    show judet normal at walk(position=-0.5, time=1.2)
    pause 1.2

    hide jiperson
    hide jipri
    hide judet

    scene balanghai_shrine
    show c1_ev3 at Transform(xpos=653, ypos=630, zoom=0.025)
    with fade

    show jiperson normal at offscreenleft
    show jiperson normal at walk(position=0.5)
    pause 1.0

    jiperson_ta "Tayo na sa Balanghai Shrine doon daw makakakita pa tayo ng panibagong evidence."
    
    show judet normal at offscreenright
    show judet normal at walk(position=0.8)
    pause 1.0

    judet_ta "Oh ito na tayo sa Balanghai Shrine ayan na at pinag uusapan ng mga taga rito makinig tayo at baka maging isa rin itong evidence para sa atin at baka sakaling magamit natin ito."

    show jipri normal at offscreenleft
    show jipri normal at walk(position=0.1)
    pause 1.0

    window hide 
    hide c1_ev3
    call screen search_item(ev_c1_b3, 653, 630, 0.025, 0.03, idle_img="evidences/butuan_2b.png", hover_img="evidences/butuan_2a.png") 
    $ inventory.append(ev_c1_b3)
    call screen examine_clue(ev_c1_b3)
    
    jiperson_ta "Last Evidence muna sa chapter na ito. May mga later historical accounts at traditions na patuloy na nag-uugnay sa First Mass sa Butuan."
    jipri_ta "Tatlong evidence na yung nakita natin at lahat ay may connection sa Butuan."
    judet_ta "Kaya hanggang dito lang tayo, malakas talaga yung Butuan side."
    jipri_ti "Sa ngayon ang masasabi kong convincing ang theory ng Butuan."
    jiperson_ta "Pero hindi pa tayo tapos."
    jipri_ta "Tama ka, baka meron pa tayong malikom na iba pang evidence."
    jipri_ta "Kahit na meron na po-provide ang Butuan ay hindi ako pwedeng maniwala agad dahil may alam rin akong impormasyon tungkol sa Limasawa..."
    jipri_ti "...ngunit hindi pa ganoong karami ang nalalaman ko tungkol sa Limasawa."

    pause 1.0
    
    show text "{size=76}END OF CHAPTER 1{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve
    
    return