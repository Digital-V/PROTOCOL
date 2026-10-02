image nhcp_document = "evidences/limasawa_10.png"

transform nhcp_pop:
    xalign 0.12
    yalign 0.65
    alpha 0.0
    zoom 0.1
    parallel:
        ease 0.4 alpha 1.0
    parallel:
        ease 0.4 zoom 0.15
#Start
label chapter5:
    $ current_chapter = 5

    scene black
    with fade

    show text "{size=76}CHAPTER 5{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve

    scene limasawa_shrine
    with fade
#Walk in, callbacks
    show jiperson normal:
        offscreenleft
        walk(position=0.0, time=2)
    show jipri normal:
        offscreenleft
        walk(position=0.5, time=2.5)
    show judet normal:
        offscreenright
        walk(position=1.0, time=2)
    pause 3.0

    jiperson_ti "Ano naman kaya ang pagbubunyag ng patotoo na Limasawa ang lugar na pinangyarihan ng Unang Misa?"
    judet_ta "Napapaisip din ako pero nae-excite rin!"
    jipri_ta "Well, ano handa na ba kayo malaman kung ano ang huling ebidensya? Makinig kayo nang mabuti."
    #callback dim for nontalking chars
    jipri_ti "Kung titignan natin pabalik, lahat ng ebidensyang nakita natin ay may katotohanan. Lahat sila, regardless kung Butuan o Limasawa, ay may kanya-kanyang punto."
    jipri_ta "Ngunit sa kadahilanang ito, nananatiling hati tuloy ang argumento ukol sa lugar ng Unang Misa."
    jipri_ta "Kaya naman, upang matigil na, ay nagsagawa ang sangay ng gobyerno, National Historical Commission of the Philippines, ng panels na binubuo ng mga eksperto sa larangang pangkasaysayan ng Pinas."

    # NHCP evidence
    show nhcp_document  at nhcp_pop zorder 0
    jipri_ta "At ang naging desisyon nila? Batay sa mga lumang tala at ebidensya, pinanindigan ng NHCP na sa Limasawa talaga naganap ang Unang Misa."

    hide nhcp_document
    with dissolve

    jipri_ta "Pero kahit may opisyal nang sagot, hindi ibig sabihing sarado na ang usapan. Ang kasaysayan kasi, puwede pang magbago kapag may mga bagong matuklasan."
    jipri_ti "Sa huli, hindi lang naman ito basta pagtatalo kung Limasawa ba o Butuan. Ang mas mahalaga, kung ano naging epekto ng pangyayaring 'to sa ating mga Pilipino ngayon."

    scene black
    with fade
    show text "{size=50}THANK YOU FOR PLAYING{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve

    scene selfie
    with fade
    pause 4.0

    scene black
    with fade

    return
#sleepy pachckecnalangss
