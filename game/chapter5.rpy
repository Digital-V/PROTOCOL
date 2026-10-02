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

    jiperson_ta "Ano namang pasabog 'to? Pa'no nila papatunayan na sa Limasawa nga talaga nangyari 'yung Unang Misa? Gusto ko na makita 'yan ah!"
    judet_ta "Napapaisip din ako pero nae-excite rin!"
    jipri_ta "Handang-handa na kayo ah. Oh heto na 'yung huli. Makinig kayo."
    #callback dim for nontalking chars
    jipri_ti "Kung titingnan natin pabalik, lahat ng ebidensyang hinimay niyo eh may katotohanan."
    jipri_ta "Kaya nga parehong may laban 'yung Butuan at Limasawa eh. Dahil hati ang usapan, 'yung NHCP o National Historical Commission of the Philippines, nagpatawag na ng mga eksperto sa history para tapusin 'yung argumento."

    # NHCP evidence
    show nhcp_document  at nhcp_pop zorder 0
    jipri_ta "At ang desisyon nila? Batay sa lumang tala at lahat ng ebidensyang tumugma... sa Limasawa talaga nangyari ang Unang Misa. 'Yan ang opisyal na stand nila."

    hide nhcp_document
    with dissolve

    jipri_ta "Pero opisyal man o hindi, baka bukas-makalawa may bago na namang ebidensya na lumitaw. Ganyan talaga ang history."
    jipri_ti "Sa huli naman, hindi lang naman ito tungkol kung saang lugar unang nagsimba. Ang mahalaga, ano 'yung naging epekto ng pangyayaring 'yon sa ating mga Pilipino hanggang ngayon. 'Di ba?"

    scene black
    with fade
    centered "{size=50}END OF CHAPTER 5.{/size}"
    pause 2.0

    return
#pachckecnalangss
