
init python:
    POS = {"jiperson": "left", "jipri": "center", "judet": "right"}

    def _at(tag, dimmed):
        p = getattr(renpy.store, POS[tag])
        return [p, renpy.store.dim if dimmed else renpy.store.undim]

    def make_cb(tag, mood="talking"):
        def cb(event, interact=True, **kwargs):
            if not interact:
                return
            showing = renpy.get_showing_tags()
            if event == "begin":
                for t in POS:
                    if t not in showing:
                        continue
                    if t == tag:
                        renpy.show((t, mood), at_list=_at(t, False))
                    else:
                        renpy.show((t,), at_list=_at(t, True))
            elif event == "end":
                for t in POS:
                    if t in showing:
                        renpy.show((t,), at_list=_at(t, False))
        return cb

#change image name if not identical
define judet = Character("Judet", image="judet", callback=make_cb("judet"))
define jipri = Character("Jipri", image="jipri", callback=make_cb("jipri"))
define jiperson = Character("Jiperson", image="jiperson", callback=make_cb("jiperson"))
define judet_ti = Character("Judet", image="judet", callback=make_cb("judet", "thinking"), what_italic=True)
define jipri_ti = Character("Jipri", image="jipri", callback=make_cb("jipri", "thinking"), what_italic=True)
define jiperson_ti = Character("Jiperson", image="jiperson", callback=make_cb("jiperson", "thinking"), what_italic=True)
define judet_ta = Character("Judet", image="judet", callback=make_cb("judet", "talking"), what_italic=True)
define jipri_ta = Character("Jipri", image="jipri", callback=make_cb("jipri", "talking"), what_italic=True)
define jiperson_ta = Character("Jiperson", image="jiperson", callback=make_cb("jiperson", "talking"), what_italic=True)
#change each name asset if not identical
image judet = Transform("judet.png", zoom=0.25)
image judet talking = Transform("judet talking.png", zoom=0.25,)
image judet thinking = Transform("judet thinking.png", zoom=0.25)
image jipri = Transform("jipri.png", zoom=0.25)
image jipri talking = Transform("jipri talking.png", zoom=0.25)
image jipri thinking = Transform("jipri thinking.png", zoom=0.25)
image jiperson = Transform("jiperson.png", zoom=0.25)
image jiperson talking = Transform("jiperson talking.png", zoom=0.25)
image jiperson thinking = Transform("jiperson thinking.png", zoom=0.25)

image evidence_placeholder1 = Fixed(
    Solid("#8a794b", xsize=840, ysize=460),
    Transform("L8.png", size=(300, 300), xpos=60, ypos=70), #change image if not identical
    
    Text("Evidence Obtained: Pigafetta's Account", size=30, color="#060606", xpos=44, ypos=34),

    xsize=840,
    ysize=460
)
image evidence_placeholder2 = Fixed(
    Solid("#8a794b", xsize=840, ysize=460),
    Transform("L8.png", size=(300, 300), xpos=60, ypos=70), #change image if not identical
    
    Text("Evidence Obtained: Mazua Identity", size=30, color="#060606", xpos=44, ypos=34),

    xsize=840,
    ysize=460
)
image evidence_placeholder3 = Fixed(
    Solid("#8a794b", xsize=840, ysize=460),
    Transform("L8.png", size=(300, 300), xpos=60, ypos=70), #change image if not identical
    
    Text("Evidence Obtained: Geographical Description", size=30, color="#060606", xpos=44, ypos=34),

    xsize=840,
    ysize=460
)

image evidence_placeholder4 = Fixed(
    Solid("#8a794b", xsize=840, ysize=460),
    Transform("L8.png", size=(300, 300), xpos=60, ypos=70), #change image if not identical
    
    Text("Evidence Obtained: Two Rulers / Political Context", size=30, color="#060606", xpos=44, ypos=34),

    xsize=840,
    ysize=460
)

image evidence_placeholder5 = Fixed(
    Solid("#8a794b", xsize=840, ysize=460),
    Transform("L8.png", size=(300, 300), xpos=60, ypos=70), #change image if not identical
    
    Text("Evidence Obtained: Primary Sources vs. Later Tradition", size=30, color="#060606", xpos=44, ypos=34),

    xsize=840,
    ysize=460
)
transform dim:
    matrixcolor BrightnessMatrix(-0.3)
transform undim:
    matrixcolor BrightnessMatrix(0.0)


label chapter3:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    with fade
    show text "{size=76}CHAPTER 3{/size}" at truecenter
    with dissolve
    pause 3.0
    hide text
    with dissolve
    show text "{size=50}{i}Habang naglalakad papunta sa susunod na lugar...{/size}{i}"
    with dissolve
    pause 3.0
    hide text
    with dissolve
    
    scene street
    with fade
    show jiperson at left
    with dissolve
    jiperson_ta "Grabe, parang ang dami na nating napuntahan. Akala ko ba simpleng investigation at pag-aaral lang to?"
    show judet at right
    with dissolve
    judet_ta "Simple sana kung isang lugar lang ang may claim eh."
    show jipri at center
    with dissolve
    jipri_ta "At kung lahat ng evidence ay nagtuturo sa iisang direksyon at lugar."
    jiperson_ti "Pero hindi naman ganon ang nangyayari."
    jipri_ta "Exactly."
    judet_ti "So, saan na tayo papunta ngayon?"
    jipri_ta "Sa lugar kung saan pwede natin mahanap at mabalikan ang pinakaunang account patungkol sa First Mass."
    scene black
    with fade
    pause 2.0
    scene museum
    with dissolve
    show jiperson at left
    with dissolve
    jiperson_ti "..."
    jiperson_ti "Ano naman ‘tong nahanap natin?"
    show jipri
    show judet at right
    with dissolve
    jipri_ta "Isang account mula kay Antonio Pigafetta."
    judet_ta "Siya yung kasama sa ekspedisyon ni Magellan, diba?"
    jipri_ta "Oo. At dahil kasama siya mismo sa ekspedisyon, importante at mahalaga na malaman natin kung ano ang isinulat niya tungkol sa lugar kung saan ginanap ang First Mass."
    show evidence_placeholder1 at truecenter
    with dissolve
    pause
    jiperson_ti "Wait… Mazua?"
    judet_ti "Huh? Hindi Butuan?"
    hide evidence_placeholder1
    jipri_ta "Sa account ni Pigafetta, ang lugar ay tinawag na Mazua, at doon inilagay ang easter Sunday Mass noong March 31, 1521."
    jiperson_ti "Pero bakit ganon? Yung mga evidence na nakuha natin ay nag l-lead sa Butuan. Paano nangyari iyon?"
    judet_ta "Ayan, kaya hindi tayo matapos-tapos e. Yung mga evidence na nakukuha natin sumasalungat sa isa’t-isa. "
    jipri_ta "Dumagdag pa yang Mazua. Hindi natin alam kung saan at ano ba ang tinutukoy nito. "
    scene black
    with fade
    show text "{size=50}{i}Habang naghahanap ng iba pang mga ebidensya...{/size}{i}"
    with dissolve
    pause 3.0
    hide text
    with dissolve
    scene museum
    with fade
    show jiperson at left
    show jipri at center
    show judet at right
    with dissolve
    judet_ta "Kung Mazua yung pangalan sa original account ni Pigafetta, saan naman natin hahanapin yun?"
    jipri_ta "Yan ang kailangan nating alamin."
    show evidence_placeholder2 at truecenter
    with dissolve
    pause
    hide evidence_placeholder2
    jiperson_ta "So, dalawang possible location ulit?"
    jipri_ta "Sa investigation natin, kailangan ikumpara ang Butuan at Limasawa base sa mga historical clues."
    judet_ta "Hindi pwedeng dahil matagal nang connected ang Butuan sa First Mass, automatic na masasabi nating Mazua na yun."
    jiperson_ta "Tama. Kailangan nating tignan kung aling lugar sa dalawa ang mas tugma sa description ng Mazua. "
    scene black
    with fade
    show text "{size=50}{i}...{/size}{i}"
    with dissolve
    pause 3.0
    hide text
    with dissolve
    scene museum
    with fade
    show jiperson at left
    show jipri at center
    show judet at right
    with dissolve
    show evidence_placeholder3 at truecenter
    with dissolve
    pause
    hide evidence_placeholder3
    jiperson_ta "Ito ba yung geographical evidence?"
    jipri_ta "Oo. Kung may description ng lugar, pwede natin ikumpara iyon sa actual geography."
    judet_ti "So basically, titignan natin alin sa dalawa ang tugma ang geographical features ng Mazua."
    jipri_ta "Exactly. Tama."
    jiperson_ti "Wait, parang nag i-iba na yung approach natin."
    jipri_ta " Akala ko ako lang ang naka pansin."
    jipri_ti "Ngayon, hinahanap na natin kung alin ang mas tugma sa description ng Mazua instead na hanapin natin mismo kung ano ang connection nito sa Butuan."
    return
