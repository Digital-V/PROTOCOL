label chapter1:
    scene street
    
    show jiperson normal:
        offscreenleft
        walk(position=0.0)
    pause 1.0

    show jiperson talking at left, shake
    jp "Paano ba yan nandito na tayo sa pag ba-bakasyunan natin para mag explore at maghanap ng evidence para sa First Mass."
    
    show jiperson normal
    show jipri normal:
        offscreenleft
        walk(position=0.5)
    pause 1.0

    show jipri talking at center, shake
    jr "Isang makasaysayang pangyayari, dalawang lugar, at mga ebidensya na parang hindi nagtutugma sa isa't-isa."
    
    show jipri normal
    show judet normal:
        offscreenright
        walk(position=1.0)
    pause 1.0

    show judet thinking at right
    jd "Gagawin ba talaga natin to? Nalipasan na to ng panahon e, kailangan pa ba natin ulit ungkatin at imbestigahan?"
    
    show judet normal
    show jipri talking at center, shake
    jr "Kaya nga tayo nandito."
    
    show jipri normal
    show judet talking at right, shake
    jd "Edi tara na! pero feeling ko sa Butuan talaga e."
    
    show judet normal
    show jipri talking at center, shake
    jr "Parang sure na sure ka ah?"
    
    show jipri normal
    show judet talking at right, shake
    jd "Feeling ko lang naman!"
    
    show judet normal
    show jipri talking at center, shake
    jr "Tignan natin. Pero hindi tayo pumunta dito para mag assume agad. Nandito tayo para alamin kung ano ba talaga ang totoong nangyari."

    show jiperson normal at walk(position=-0.5, time=1.5)
    show jipri normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5

    scene museum
    with fade

    show jipri normal:
        offscreenleft
        walk(position=0.5)
    pause 1.0

    show jipri talking at right, shake
    jr "Nandito na tayo sa museum para makakita ng pang unang evidence. O ito na pala pang unang evidence para saatin."

    show jipri normal
    
    window hide 
    call screen search_item(ev_c1_b1, 935, 525, 0.025, 0.03)
    $ inventory.append(ev_c1_b1)
    
    show screen examine_clue(ev_c1_b1)
    "Evidence Found! Isang lumang 19th century spanish colonial newspaper."
    
    show jipri talking at center, shake
    jr "May matagal nang historical tradition na nag uugnay sa Butuan sa expedition ni Magellan at sa First Mass."
    
    hide screen examine_clue 
    
    jr "So matagal na palang may connection ang Butuan sa First Mass."
    
    show jipri normal
    show judet normal:
        offscreenright
        walk(position=1.0)
    pause 1.0

    show judet thinking at right
    jd "Oo, kaya hindi rin basta-basta lang nabuo ang Butuan claim."
    
    show judet normal
    show jipri talking at center, shake
    jr "Interesting, pero kailangan pa natin makahanap ng iba pang evidence."

    show jipri normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5

    scene agusan_river
    with fade

    show jiperson normal:
        offscreenleft
        walk(position=0.0)
    pause 1.0

    show jiperson talking at left, shake
    jp "Hali na kayo pumunta naman tayo sa susunod na lugar para maka-kalap pa ng iba pang evidence dahil sa Agusan River Area maraming tao ang nagsasabi na may pinunong na involve nung panahon ni Magellan."
    
    show jiperson normal
    show judet normal:
        offscreenright
        walk(position=1.0)
    pause 1.0

    show judet talking at right, shake
    jd "O nandito na pala tayo sa Agusan River area may narinig na rin ako na pangalawang evidence."

    show judet normal
    show jipri normal:
        offscreenleft
        walk(position=0.5)
    pause 1.0

    window hide 
    call screen search_item(ev_c1_b2, 1400, 700, 0.0125, 0.0226, "evidences/butuan_3b.png") 
    $ inventory.append(ev_c1_b2)
    
    show screen examine_clue(ev_c1_b2)
    "Evidence Found! 2D Character dossier card of Rajah Siawi."

    show jipri talking at center, shake
    jr "Ito ang sinabi satin ng ibang tao, Talaga bang may connection ito sa mga narinig mo Judet?"
    
    hide screen examine_clue
    
    show jipri normal
    show jiperson talking at left, shake
    jp "May nakita pa akong evidence. May nakatalagang pinuno nang Butuan ang sangkot sa mga pangyayari noong expedition."
    
    show jiperson normal
    show jipri talking at center, shake
    jr "Kung naging sangkot ang pinuno ng butuan mas magiging convincing yung connection nila sa expedition."
    
    show jipri normal
    show judet thinking at right
    jd "Pero hindi pa rin ibig sabihin ay automatic na doon nga nangyari ang First Mass."
    
    show judet normal
    show jipri talking at center, shake
    jr "Tama. Kailangan pa rin nating tingnan kung ano mismo ang pinapatunayan at ipinapakita ng evidence."
    
    show jipri normal
    show jiperson talking at left, shake
    jp "Exactly. Yun ang dapat talaga nating alamin."

    show jiperson normal at walk(position=-0.5, time=1.5)
    show jipri normal at walk(position=-0.5, time=2)
    show judet normal at walk(position=-0.5, time=2.5)
    pause 2.5

    scene balanghai_shrine
    with fade

    show jiperson normal:
        offscreenleft
        walk(position=0.0)
    pause 1.0

    show jiperson talking at left, shake
    jp "Tayo na sa Balanghai Shrine doon daw makakakita pa tayo ng panibagong evidence."
    
    show jiperson normal
    show judet normal:
        offscreenright
        walk(position=1.0)
    pause 1.0

    show judet talking at right, shake
    jd "Oh ito na tayo sa Balanghai Shrine ayan na at pinag uusapan ng mga taga rito makinig tayo at baka maging isa rin itong evidence para sa atin at baka sakaling magamit natin ito."

    show judet normal
    show jipri normal:
        offscreenleft
        walk(position=0.5)
    pause 1.0

    window hide 
    call screen search_item(ev_c1_b3, 653, 630, 0.025, 0.03)
    $ inventory.append(ev_c1_b3)
    
    show screen examine_clue(ev_c1_b3)
    "Evidence Found! Lumang manuscript na naglalaman ng sipi mula kila Fr. Francisco Colin at Fr. Francisco Combes."

    show jiperson talking at left, shake
    jp "Last Evidence muna sa chapter na ito. May mga later historical accounts at traditions na patuloy na nag-uugnay sa First Mass sa Butuan."
    
    hide screen examine_clue
    
    show jiperson normal
    show jipri talking at center, shake
    jr "Tatlong evidence na yung nakita natin at lahat ay may connection sa Butuan."
    
    show jipri normal
    show judet talking at right, shake
    jd "Kaya hanggang dito lang tayo, malakas talaga yung Butuan side."
    
    show judet normal
    show jipri thinking at center
    jr "Sa ngayon ang masasabi kong convincing ang theory ng Butuan."
    
    show jipri normal
    show jiperson talking at left, shake
    jp "Pero hindi pa tayo tapos."
    
    show jiperson normal
    show jipri talking at center, shake
    jr "Tama ka, baka meron pa tayong makalap na iba pang evidence."
    jr "Kahit na meron na po-provide ang Butuan ay hindi ako pwedeng maniwala agad dahil may alam rin akong impormasyon tungkol sa Limasawa..."
    jr "...ngunit hindi pa ganoong karami ang nalalaman ko tungkol sa Limasawa."

    "END OF CHAPTER 1"
    
    return