image nhcp_document = "evidences/limasawa_10.png"
image chapter5_fan_art_photo = "final_art.jpg"

transform nhcp_pop:
    xalign 0.12
    yalign 0.65
    alpha 0.0
    zoom 0.1
    parallel:
        ease 0.4 alpha 1.0
    parallel:
        ease 0.4 zoom 0.15

screen chapter5_fan_art_polaroid():
    zorder 200
    add Solid("#000000")

    frame:
        xalign 0.5
        yalign 0.48
        xsize 880
        ysize 650
        background Solid("#f4efe4")
        padding (30, 28, 30, 24)

        vbox:
            spacing 0

            frame:
                xsize 820
                ysize 460
                background Solid("#d6dfd9")
                padding (0, 0)

                add "chapter5_fan_art_photo" xysize (820, 460)

            null height 22
            text "ANG ATING PAGLALAKBAY" xalign 0.5 size 30 color "#080a09"
            null height 8
            text "Tatlong imbestigador, isang di-malilimutang paglalakbay." xalign 0.5 size 20 color "#46534c"

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
    play music "audio/bg_music5.mp3" fadein 1.0 volume 0.2 loop
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

    jiperson_ti "Ano ang mga patunay na ang Limasawa ang pinagdausan ng Unang Misa?"
    judet_ta "Napapaisip din ako pero nae-excite rin!"
    jipri_ta "Well, ano handa na ba kayo malaman kung ano ang huling ebidensya? Makinig kayo nang mabuti."
    #callback dim for nontalking chars
    jipri_ti "Kung titignan natin pabalik, lahat ng ebidensyang nakita natin ay may katotohanan. Lahat sila, regardless kung Butuan o Limasawa, ay may kanya-kanyang punto."
    jipri_ta "Ngunit sa kadahilanang ito, nananatiling hati ang argumento ukol sa lugar ng Unang Misa. That's why to stop that,  nagsagawa ang sangay ng gobyerno, National History Comission of the Philippines, ng panels na binubuo ng mga eksperto sa larangang pangkasaysayan ng pinas."
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
    centered "{size=42}Sa pag-unawa sa nakaraan, hindi sapat ang pumili ng panig.\nSuriin ang ebidensya, pakinggan ang iba't ibang pananaw,\nat manatiling bukas sa mga bagong tuklas.{/size}"
    pause 2.0

    show screen chapter5_fan_art_polaroid
    with fade
    pause 10.0
    hide screen chapter5_fan_art_polaroid
    with dissolve

    centered "{size=50}THANK YOU FOR PLAYING!{/size}"
    stop music fadeout 1.0
    pause 3.0

    return
#sleepy pachckecnalangss
