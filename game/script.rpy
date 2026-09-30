# Characters
define jp = Character("Jiperson", color="#ffcc00")
define jr = Character("Jipri", color="#00ffcc")
define jd = Character("Judet", color="#ff66b2")

image jiperson normal:
    "jiperson normal.png"
    zoom 0.2
image jiperson talking:
    "jiperson talking.png"
    zoom 0.2
image jiperson thinking:
    "jiperson thinking.png"
    zoom 0.2

image jipri normal:
    "jipri normal.png"
    zoom 0.2
image jipri talking:
    "jipri talking.png"
    zoom 0.2
image jipri thinking:
    "jipri thinking.png"
    zoom 0.2

image judet normal:
    "judet normal.png"
    zoom 0.2
image judet talking:
    "judet talking.png"
    zoom 0.2
image judet thinking:
    "judet thinking.png"
    zoom 0.2

# Animations
transform bounce:
    yoffset 0
    easein 0.1 yoffset -20
    easeout 0.1 yoffset 0

# Evidence
init python:
    class Clue:
        def __init__(self, name, visual, details):
            self.name = name
            self.visual = visual
            self.details = details

    ev_butuan_1 = Clue(
        "Historical Connection to Butuan",
        "bituanevidence1.png",
        "Historical traditions and records have long connected Butuan with Magellan's expedition and First Mass."
    )
    
    ev_butuan_3 = Clue(
        "The Ruler of Butuan",
        "bituanevidence3.png",
        "A ruler associated with Butuan was involved in events surrounding Magellan's expedition."
    )
    
    ev_butuan_4 = Clue(
        "Historical Tradition",
        "bituanevidence4.png",
        "Later historical accounts and traditions continued to associate the First Mass with Butuan."
    )

default inventory = []

# UI screens
default show_chapter_info = False
default current_evidence_page = 0

screen chapter_info_hud():
    zorder 100 
    
    imagebutton:
        xalign 0.98 yalign 0.02 
        idle Transform("BrownNormal18.png", zoom=3.0) 
        hover Transform("BrownPressed18.png", zoom=3.0) 
        action Show("evidence_menu")

screen evidence_menu():
    modal True
    
    button:
        background "#000000cc"
        xfill True
        yfill True
        action [SetVariable("current_evidence_page", 0), Hide("evidence_menu")]

    frame:
        background Transform("wooden_board.png", size=(1200, 800)) 
        xalign 0.5 yalign 0.5
        xysize (1200, 800) 
        
        # Frame padding
        padding (260, 220, 260, 200)

        vbox:
            spacing 15
            xfill True
            
            # Headers
            vbox:
                xalign 0.5
                spacing 5
                text "Evidence Log" size 40 bold True color "#3b2313" xalign 0.5
                text "[len(inventory)] / 3 Collected" size 24 color "#3b2313" xalign 0.5
            
            null height 10
            
            if len(inventory) == 0:
                text "No evidence collected yet." size 30 color "#555555" xalign 0.5 yalign 0.5
            else:
                $ current_clue = inventory[current_evidence_page]
                
                hbox:
                    spacing 25
                    add current_clue.visual ysize 160 fit "contain"
                    
                    vbox:
                        spacing 5
                        text "[current_clue.name]" size 28 bold True color "#3b2313"
                        text "[current_clue.details]" size 20 xmaximum 400 color "#000000"

            if len(inventory) > 1:
                null height 15
                hbox:
                    xalign 0.5
                    spacing 50
                    
                    if current_evidence_page > 0:
                        textbutton "< Back" action SetVariable("current_evidence_page", current_evidence_page - 1) text_color "#3b2313" text_hover_color "#FFD700" text_size 28
                    else:
                        null width 100 
                    
                    text "Page [current_evidence_page + 1] of [len(inventory)]" size 24 color "#3b2313" yalign 0.5
                    
                    if current_evidence_page < len(inventory) - 1:
                        textbutton "Next >" action SetVariable("current_evidence_page", current_evidence_page + 1) text_color "#3b2313" text_hover_color "#FFD700" text_size 28
                    else:
                        null width 100


screen examine_clue(clue_item):
    modal True 
    
    button:
        background "#00000088"
        xfill True
        yfill True
        action Hide("examine_clue")

    frame:
        background Transform("wooden_board.png", size=(1200, 800)) 
        xalign 0.5 yalign 0.35 
        xysize (1200, 800) 
        
        # Frame padding
        padding (260, 220, 260, 200) 
        
        vbox:
            spacing 15
            xfill True
            
            text "[clue_item.name]" size 35 bold True color "#3b2313" xalign 0.5
            add clue_item.visual xalign 0.5 ysize 160 fit "contain"
            text "[clue_item.details]" size 24 text_align 0.5 color "#000000" xmaximum 600 xalign 0.5

# Search screens
screen search_museum():
    if ev_butuan_1 not in inventory:
        imagebutton:
            xpos 400 ypos 300 
            idle Transform("bituanevidence1", zoom=0.2)
            hover Transform("bituanevidence1", zoom=0.22)
            action Return("found_clue")

screen search_agusan():
    if ev_butuan_3 not in inventory:
        imagebutton:
            xpos 200 ypos 450
            idle Transform("bituanevidence3", zoom=0.2)
            hover Transform("bituanevidence3", zoom=0.22)
            action Return("found_clue")

screen search_shrine():
    if ev_butuan_4 not in inventory:
        imagebutton:
            xpos 600 ypos 200
            idle Transform("bituanevidence4", zoom=0.2)
            hover Transform("bituanevidence4", zoom=0.22)
            action Return("found_clue")

# Game flow
label start:
    show screen chapter_info_hud

    call chapter1
    call chapter2
    call chapter3
    call chapter4
    call chapter5

    return

# Chapter 1
label chapter1:
    scene bg town_street
    
    show jiperson talking at left, bounce
    jp "Paano ba yan nandito na tayo sa pag ba-bakasyunan natin para mag explore at maghanap ng evidence para sa First Mass."
    
    show jiperson normal
    show jipri talking at center, bounce
    jr "Isang makasaysayang pangyayari, dalawang lugar, at mga ebidensya na parang hindi nagtutugma sa isa't-isa."
    
    show jipri normal
    show judet thinking at right
    jd "Gagawin ba talaga natin to? Nalipasan na to ng panahon e, kailangan pa ba natin ulit ungkatin at imbestigahan?"
    
    show judet normal
    show jipri talking at center, bounce
    jr "Kaya nga tayo nandito."
    
    show jipri normal
    show judet talking at right, bounce
    jd "Edi tara na! pero feeling ko sa Butuan talaga e."
    
    show judet normal
    show jipri talking at center, bounce
    jr "Parang sure na sure ka ah?"
    
    show jipri normal
    show judet talking at right, bounce
    jd "Feeling ko lang naman!"
    
    show judet normal
    show jipri talking at center, bounce
    jr "Tignan natin. Pero hindi tayo pumunta dito para mag assume agad. Nandito tayo para alamin kung ano ba talaga ang totoong nangyari."

    scene bg museum
    with fade

    show jipri talking at center, bounce
    jr "Nandito na tayo sa museum para makakita ng pang unang evidence. O ito na pala pang unang evidence para saatin."

    show jipri normal
    
    window hide 
    call screen search_museum 
    $ inventory.append(ev_butuan_1)
    
    show screen examine_clue(ev_butuan_1)
    "Nakahanap kayo ng ebidensya: Isang lumang 19th century spanish colonial newspaper."
    
    show jipri talking at center, bounce
    jr "May matagal nang historical tradition na nag uugnay sa Butuan sa expedition ni Magellan at sa First Mass."
    
    hide screen examine_clue 
    
    jr "So matagal na palang may connection ang Butuan sa First Mass."
    
    show jipri normal
    show judet thinking at right
    jd "Oo, kaya hindi rin basta-basta lang nabuo ang Butuan claim."
    
    show judet normal
    show jipri talking at center, bounce
    jr "Interesting, pero kailangan pa natin makahanap ng iba pang evidence."

    scene bg agusan_river
    with fade

    show jiperson talking at left, bounce
    jp "Hali na kayo pumunta naman tayo sa susunod na lugar para maka-kalap pa ng iba pang evidence dahil sa Agusan River Area maraming tao ang nagsasabi na may pinunong na involve nung panahon ni Magellan."
    
    show jiperson normal
    show judet talking at right, bounce
    jd "O nandito na pala tayo sa Agusan River area may narinig na rin ako na pangalawang evidence."

    show judet normal

    window hide 
    call screen search_agusan 
    $ inventory.append(ev_butuan_3)
    
    show screen examine_clue(ev_butuan_3)
    "Nakahanap kayo ng ebidensya: 2D Character dossier card of Rajah Siawi."

    show jipri talking at center, bounce
    jr "Ito ang sinabi satin ng ibang tao, Talaga bang may connection ito sa mga narinig mo Judet?"
    
    hide screen examine_clue
    
    show jipri normal
    show jiperson talking at left, bounce
    jp "May nakita pa akong evidence. May nakatalagang pinuno nang Butuan ang sangkot sa mga pangyayari noong expedition."
    
    show jiperson normal
    show jipri talking at center, bounce
    jr "Kung naging sangkot ang pinuno ng butuan mas magiging convincing yung connection nila sa expedition."
    
    show jipri normal
    show judet thinking at right
    jd "Pero hindi pa rin ibig sabihin ay automatic na doon nga nangyari ang First Mass."
    
    show judet normal
    show jipri talking at center, bounce
    jr "Tama. Kailangan pa rin nating tingnan kung ano mismo ang pinapatunayan at ipinapakita ng evidence."
    
    show jipri normal
    show jiperson talking at left, bounce
    jp "Exactly. Yun ang dapat talaga nating alamin."

    scene bg balanghai_shrine
    with fade

    show jiperson talking at left, bounce
    jp "Tayo na sa Balanghai Shrine doon daw makakakita pa tayo ng panibagong evidence."
    
    show jiperson normal
    show judet talking at right, bounce
    jd "Oh ito na tayo sa Balanghai Shrine ayan na at pinag uusapan ng mga taga rito makinig tayo at baka maging isa rin itong evidence para sa atin at baka sakaling magamit natin ito."

    show judet normal

    window hide 
    call screen search_shrine
    $ inventory.append(ev_butuan_4)
    
    show screen examine_clue(ev_butuan_4)
    "Nakahanap kayo ng ebidensya: Lumang manuscript na naglalaman ng sipi mula kila Fr. Francisco Colin at Fr. Francisco Combes."

    show jiperson talking at left, bounce
    jp "Last Evidence muna sa chapter na ito. May mga later historical accounts at traditions na patuloy na nag-uugnay sa First Mass sa Butuan."
    
    hide screen examine_clue
    
    show jiperson normal
    show jipri talking at center, bounce
    jr "Tatlong evidence na yung nakita natin at lahat ay may connection sa Butuan."
    
    show jipri normal
    show judet talking at right, bounce
    jd "Kaya hanggang dito lang tayo, malakas talaga yung Butuan side."
    
    show judet normal
    show jipri thinking at center
    jr "Sa ngayon ang masasabi kong convincing ang theory ng Butuan."
    
    show jipri normal
    show jiperson talking at left, bounce
    jp "Pero hindi pa tayo tapos."
    
    show jiperson normal
    show jipri talking at center, bounce
    jr "Tama ka, baka meron pa tayong makalap na iba pang evidence."
    jr "Kahit na meron na po-provide ang Butuan ay hindi ako pwedeng maniwala agad dahil may alam rin akong impormasyon tungkol sa Limasawa..."
    jr "...ngunit hindi pa ganoong karami ang nalalaman ko tungkol sa Limasawa."

    "END OF CHAPTER 1"
    
    return