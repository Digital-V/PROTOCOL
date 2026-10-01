# Characters
init python:
    TAGS = ["jiperson", "jipri", "judet"]

    def make_cb(tag, mood="talking"):
        def cb(event, interact=True, **kwargs):
            if not interact:
                return
            showing = renpy.get_showing_tags()
            if event == "begin":
                for t in TAGS:
                    if t not in showing:
                        continue
                    if t == tag:
                        at = [renpy.store.undim]
                        if mood == "talking":
                            at.append(renpy.store.shake)
                        renpy.show((t, mood), at_list=at)
                    else:
                        renpy.show((t, "normal"), at_list=[renpy.store.dim])
            elif event == "end":
                for t in TAGS:
                    if t in showing:
                        renpy.show((t, "normal"), at_list=[renpy.store.undim])
        return cb

# Base Character Definitions (Fixes "Sayer is not defined" error)
define jiperson = Character("Jiperson", color="#ffcc00")
define jipri = Character("Jipri", color="#00ffcc")
define judet = Character("Judet", color="#ff66b2")

# Short aliases if used elsewhere
define jp = Character("Jiperson", color="#ffcc00")
define jr = Character("Jipri", color="#00ffcc")
define jd = Character("Judet", color="#ff66b2")

# Callback-based character variants for talking/thinking animations
define jiperson_ta = Character("Jiperson", color="#ffcc00", callback=make_cb("jiperson", "talking"))
define jiperson_ti = Character("Jiperson", color="#ffcc00", callback=make_cb("jiperson", "thinking"), what_italic=True)
define jipri_ta = Character("Jipri", color="#00ffcc", callback=make_cb("jipri", "talking"))
define jipri_ti = Character("Jipri", color="#00ffcc", callback=make_cb("jipri", "thinking"), what_italic=True)
define judet_ta = Character("Judet", color="#ff66b2", callback=make_cb("judet", "talking"))
define judet_ti = Character("Judet", color="#ff66b2", callback=make_cb("judet", "thinking"), what_italic=True)

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

transform dim:
    yoffset 0
    matrixcolor BrightnessMatrix(-0.3)

transform undim:
    yoffset 0
    matrixcolor BrightnessMatrix(0.0)

# Evidence
init python:
    class Clue:
        def __init__(self, name, visual, details):
            self.name = name
            self.visual = visual
            self.details = details

    # Chapter 1 Evidences
    ev_c1_b1 = Clue(
        "Historical Connection to Butuan",
        "evidences/butuan_1.png",
        "Historical traditions and records have long connected Butuan with Magellan's expedition and First Mass."
    )
    
    ev_c1_b2 = Clue(
        "The Ruler of Butuan",
        "evidences/butuan_3b.png",
        "A ruler associated with Butuan was involved in events surrounding Magellan's expedition."
    )
    
    ev_c1_b3 = Clue(
        "Butuan's Importance",
        "evidences/butuan_2.png",
        "Ang Butuan ay isang kilala at mayamang pamayanan sa Mindanao na tanyag sa paggawa ng ginto, paggawa ng malalaking sasakyang-pandagat (balangay), at pakikipagkalakalan sa mga karatig-bansa sa Asya. Ipinapakita nito na may makatwirang dahilan ang mga Kastila na puntahan at hanapin ang Butuan para kumuha ng suplay at makipagkalakalan."
    )
    
    # Chapter 2 Evidences
    ev_c2_b1 = Clue(
        "First Mass Monument",
        "evidences/butuan_5.png",
        "Noong 1872, nagtayo ang pamahalaang Kastila at mga prayleng Rekolekto ng isang obelisko malapit sa bunganga ng Agusan River sa Magallanes, Agusan del Norte (dating bahagi ng lumang Butuan)."
    )
    
    ev_c2_b2 = Clue(
        "Historical Accounts",
        "evidences/butuan_4.png",
        "Isinulat ng Heswitang si Padre Colín na itinayo ni Magellan ang krus at idinaos ang Unang Misa sa Butuan bago naglayag patungong Cebu."
    )
    
    ev_c2_b3 = Clue(
        "Magellan's Expedition",
        "evidences/butuan_6.png",
        "Matapos ang pagkamatay ni Magellan sa Mactan, naglayag ang mga natitirang barko sa baybayin ng hilaga at kanlurang Mindanao bago tuluyang tumuloy sa Moluccas."
    )

    # Chapter 3 & 4 Evidences
    ev_c3_b1 = Clue(
        "Pigafetta’s Account",
        "evidences/limasawa_1.png",
        "Ang account ni Antonio Pigafetta ay mahalagang primary source dahil kasama siya sa expedition ni Magellan at isinulat niya ang mga pangyayari sa kanilang paglalakbay. Sa kanyang account, binanggit niya ang lugar na tinawag na Mazaua, kung saan ginanap ang Easter Sunday Mass noong March 31, 1521."
    )
    
    ev_c3_b2 = Clue(
        "Mazua Identity",
        "evidences/limasawa_2.png",
        "Ang pangunahing layunin ng investigation ay malaman kung anong aktwal na lokasyon ang tinutukoy ng pangalang Mazua sa account ni Pigafetta."
    )
    
    ev_c3_b3 = Clue(
        "Geography",
        "evidences/limasawa_3.png",
        "Sinusuri ang mga geographical description na makikita sa mga primary account at ikinukumpara ang mga ito sa pisikal na katangian ng mga posibleng lokasyon."
    )
    
    ev_c3_b4 = Clue(
        "Expedition Route",
        "evidences/limasawa_4.png",
        "Ikinukumpara ang recorded route ng expedition ni Magellan sa lokasyon ng Butuan at Limasawa upang malaman kung alin ang mas tugma sa kanilang paglalakbay."
    )
    
    ev_c3_b5 = Clue(
        "Distance and Direction",
        "evidences/limasawa_5.png",
        "Ginagamit ang mga recorded distance at direction mula sa historical accounts bilang mga clue upang matukoy kung aling lokasyon ang mas tugma sa paglalakbay ng expedition."
    )
    
    ev_c3_b6 = Clue(
        "Island Description",
        "evidences/limasawa_6.png",
        "Sa account ni Pigafetta, ang Mazua ay inilarawan bilang isang isla. Kaya importante na ikumpara ang paglalarawan na ito sa lugar na inaakalang Mazua. Ang pagtutugma ng pagkakalarawan ay naging mahalagang bahagi ng argumentong nag-uugnay na sa Limasawa."
    )
    
    ev_c3_b7 = Clue(
        "Dalawang Pinuno / Political Context",
        "evidences/limasawa_7.png",
        "Magkaiba ang pinanggalingan ng isang pinuno at ang lokasyon kung saan ginanap ang First Mass. May mga pinunong nauugnay sa Limasawa at Butuan na naging bahagi ng pangyayari. Kaya ang pagkakaroon ng pinuno na galing sa Butuan ay hindi sapat upang patunayan na sa Butuan mismo naganap ang First Mass."
    )
    
    ev_c3_b8 = Clue(
        "Primary Sources vs. Later Tradition",
        "evidences/limasawa_8.png",
        "Sinusuri kung gaano na katagal ang bawat source at kung ano mismo ang nakapaloob sa source na iyon. Ang original account ni Pigafetta ay gumagamit ng pangalang Mazua, habang ang ilang sumunod na interpretations ay naugnay sa Butuan."
    )
    
    ev_c3_b9 = Clue(
        "Historical Investigation",
        "evidences/limasawa_9.png",
        "Pinagsama-samang iba’t-ibang impormasyon mula sa historical accounts, geography, route, distances, directions, at description para malaman kung anong lugar ang pinakanaayon sa Mazua."
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
                text "[len(inventory)] Collected" size 24 color "#3b2313" xalign 0.5
            
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

screen search_item(evidence, x, y, idle_size, hover_size, idle_img=None, hover_img=None):

    if evidence not in inventory:
        if idle_img != None:
            imagebutton:
                xpos x ypos y
                idle Transform(idle_img, zoom=idle_size)
                hover Transform(hover_img, zoom=hover_size)
                focus_mask True
                action Return("found_clue")
                
        else:
            imagebutton:
                xpos x ypos y
                idle Transform(evidence.visual, zoom=idle_size)
                hover Transform(evidence.visual, zoom=hover_size)
                focus_mask True
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