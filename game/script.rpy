# Characters
define jp = Character("Jiperson", color="#ffcc00")
define jr = Character("Jipri", color="#00ffcc")
define jd = Character("Judet", color="#ff66b2")

image jiperson normal:
    "characters/jiperson normal.png"
    zoom 0.2
image jiperson talking:
    "characters/jiperson talking.png"
    zoom 0.2
image jiperson thinking:
    "characters/jiperson thinking.png"
    zoom 0.2

image jipri normal:
    "characters/jipri normal.png"
    zoom 0.2
image jipri talking:
    "characters/jipri talking.png"
    zoom 0.2
image jipri thinking:
    "characters/jipri thinking.png"
    zoom 0.2

image judet normal:
    "characters/judet normal.png"
    zoom 0.2
image judet talking:
    "characters/judet talking.png"
    zoom 0.2
image judet thinking:
    "characters/judet thinking.png"
    zoom 0.2

# Animations
transform shake(repeat=2):
    yoffset 0
    easein 0.1 yoffset 20
    easeout 0.1 yoffset 0
    repeat repeat

transform walk(position=0.0, time=0.75):
    parallel:
        ease time xalign position

    parallel:
        shake(repeat=int(time * 3))

# Evidence
init python:
    class Clue:
        def __init__(self, name, visual, details):
            self.name = name
            self.visual = visual
            self.details = details

    ev_c1_b1 = Clue(
        "Historical Connection to Butuan",
        "evidences/butuan_1.png",
        "Historical traditions and records have long connected Butuan with Magellan's expedition and First Mass."
    )
    
    ev_c1_b2 = Clue(
        "The Ruler of Butuan",
        "evidences/butuan_3a.png",
        "A ruler associated with Butuan was involved in events surrounding Magellan's expedition."
    )
    
    ev_c1_b3 = Clue(
        "Historical Tradition",
        "evidences/butuan_4.png",
        "Later historical accounts and traditions continued to associate the First Mass with Butuan.\n\nFrom JJ: leb, ang alam ko sakin tong evidence img hahaha, tig-3 evidences lang tayo per chapters."
    )
    
    ev_c2_b1 = Clue(
        "First Mass Monument",
        "evidences/butuan_5.png",
        "Noong 1872, nagtayo ang pamahalaang Kastila at mga prayleng Rekolekto ng isang obelisko malapit sa bunganga ng Agusan River sa Magallanes, Agusan del Norte (dating bahagi ng lumang Butuan)."
    )
    
    ev_c2_b2 = Clue(
        "Historical Accounts",
        "evidences/butuan_4.png",
        "Isinulat ng Heswitang si Padre Colín na itinayo ni Magellan ang krus at idinaos ang Unang Misa sa Butuan bago naglayag patungong Cebu. Samantala, inilarawan naman ni Padre Combés na dumaong si Magellan sa Limasawa, nagtungo sa Butuan upang magtayo ng krus, at muling bumalik sa Limasawa."
    )
    
    ev_c2_b3 = Clue(
        "Magellan's Expedition",
        "evidences/butuan_6.png",
        "Matapos ang pagkamatay ni Magellan sa Mactan, naglayag ang mga natitirang barko sa baybayin ng hilaga at kanlurang Mindanao bago tuluyang tumuloy sa Moluccas."
    )

default inventory = []

# UI screens
default show_chapter_info = False
default current_evidence_page = 0

screen chapter_info_hud():
    zorder 100 
    
    imagebutton:
        xalign 0.98 yalign 0.02 
        idle Transform("ui/star_button_normal.png", zoom=3.0) 
        hover Transform("ui/star_button_pressed.png", zoom=3.0) 
        action Show("evidence_menu")

screen evidence_menu():
    modal True
    
    button:
        background "#000000cc"
        xfill True
        yfill True
        action [SetVariable("current_evidence_page", 0), Hide("evidence_menu")]

    frame:
        background Transform("ui/wooden_board.png", size=(1200, 800)) 
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
        background Transform("ui/wooden_board.png", size=(1200, 800)) 
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

screen search_item(evidence, x, y, idle_size, hover_size, hover_img=None):
    if hover_img is None:
        $ hover_img = evidence.visual

    if evidence not in inventory:
        imagebutton:
            xpos x ypos y
            idle Transform(evidence.visual, zoom=idle_size)
            hover Transform(hover_img, zoom=hover_size)
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
