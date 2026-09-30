define jiperson = Character("Jiperson", image="jiperson")
define jipri = Character("Jipri", image="jipri")
define judet = Character("Judet", image="judet")

#Place holdes satrt can be deleted later when assets are ready.
init python:
    def expression_placeholder(base_image, mood, accent):
        return Transform(
            Fixed(
                base_image,
                Solid(accent, xsize=184, ysize=44, xpos=200, ypos=26),
                Text(mood, size=18, color="#fff4dd", xpos=212, ypos=36),
                xsize=400,
                ysize=620
            ),
            zoom=1.1
        )

image bg placeholder_coastal_area = Fixed(
    Solid("#18343a", xsize=1920, ysize=1080),
    Solid("#315c58", xsize=1920, ysize=250, ypos=830),
    Solid("#c18a55", xsize=1920, ysize=8, ypos=828),
    Solid("#0006", xsize=1920, ysize=1080),
    Text("COASTAL EXPEDITION ROUTE", size=54, color="#f3e6c8", xalign=0.5, ypos=100),
    Text("BUTUAN  /  RECORDED ROUTE  /  LIMASAWA", size=30, color="#d9d1b7", xalign=0.5, ypos=180),
    xsize=1920,
    ysize=1080
)

image bg placeholder_limasawa_island = Fixed(
    Solid("#234951", xsize=1920, ysize=1080),
    Solid("#38727a", xsize=1920, ysize=260, ypos=820),
    Solid("#9b9b70", xsize=520, ysize=115, xalign=0.5, ypos=705),
    Solid("#0006", xsize=1920, ysize=1080),
    Text("LIMASAWA ISLAND", size=56, color="#f3e6c8", xalign=0.5, ypos=100),
    Text("ISLAND DESCRIPTION", size=30, color="#d9d1b7", xalign=0.5, ypos=180),
    xsize=1920,
    ysize=1080
)

image bg placeholder_limasawa_shrine = Fixed(
    Solid("#253c35", xsize=1920, ysize=1080),
    Solid("#526a4e", xsize=1920, ysize=250, ypos=830),
    Solid("#b98b58", xsize=1920, ysize=8, ypos=828),
    Solid("#0006", xsize=1920, ysize=1080),
    Text("LIMASAWA SHRINE", size=56, color="#f3e6c8", xalign=0.5, ypos=100),
    Text("HISTORICAL INVESTIGATION SITE", size=30, color="#d9d1b7", xalign=0.5, ypos=180),
    xsize=1920,
    ysize=1080
)

image jiperson placeholder = Fixed(
    Solid("#386f75", xsize=400, ysize=620),
    Solid("#e3a35c", xsize=400, ysize=14),
    Text("JP", size=112, color="#fff4dd", xalign=0.5, yalign=0.38),
    Text("JI PERSON\nPLACEHOLDER", size=29, color="#fff4dd", xalign=0.5, yalign=0.82),
    xsize=400,
    ysize=620
)

image jipri placeholder = Fixed(
    Solid("#59634d", xsize=400, ysize=620),
    Solid("#d5b96d", xsize=400, ysize=14),
    Text("JR", size=112, color="#fff4dd", xalign=0.5, yalign=0.38),
    Text("JIPRI\nPLACEHOLDER", size=29, color="#fff4dd", xalign=0.5, yalign=0.82),
    xsize=400,
    ysize=620
)

image judet placeholder = Fixed(
    Solid("#76534a", xsize=400, ysize=620),
    Solid("#d5b96d", xsize=400, ysize=14),
    Text("JD", size=112, color="#fff4dd", xalign=0.5, yalign=0.38),
    Text("JUDET\nPLACEHOLDER", size=29, color="#fff4dd", xalign=0.5, yalign=0.82),
    xsize=400,
    ysize=620
)

image jiperson placeholder speaking = expression_placeholder("jiperson placeholder", "SPEAKING", "#dfad58")
image jiperson placeholder thinking = expression_placeholder("jiperson placeholder", "THINKING", "#5297a0")

image jipri placeholder speaking = expression_placeholder("jipri placeholder", "SPEAKING", "#dfad58")
image jipri placeholder thinking = expression_placeholder("jipri placeholder", "THINKING", "#5297a0")

image judet placeholder speaking = expression_placeholder("judet placeholder", "SPEAKING", "#dfad58")
image judet placeholder thinking = expression_placeholder("judet placeholder", "THINKING", "#5297a0")

image investigation_board_placeholder = Fixed(
    Solid("#e4d8b8", xsize=840, ysize=460),
    Solid("#a94f3d", xsize=840, ysize=12),
    Text("INVESTIGATION BOARD", size=42, color="#20343a", xpos=44, ypos=34),
    xsize=840,
    ysize=460
)
#Place holder end can be deleted later when assets are ready.


#Just make things and assets centered on the screeen.
transform stage_left:
    xalign 0.15
    yalign 1.0

transform stage_center:
    xalign 0.5
    yalign 1.0

transform stage_right:
    xalign 0.85
    yalign 1.0

transform investigation_board_center:
    xalign 0.5
    yalign 0.42

label chapter4:

    scene black
    with fade

    show text "{size=76}CHAPTER 4{/size}" at truecenter
    with dissolve
    pause 2.0
    hide text
    with dissolve

    scene bg placeholder_coastal_area
    with fade

    # EVIDENCE 1: EXPEDITION ROUTE
    show jiperson placeholder at stage_center
    show jipri placeholder at stage_left
    show judet placeholder at stage_right

    jiperson @ speaking "So ito na ba yung route ng expedition?"
    jipri @ speaking "Oo. Kailangan nating ikumpara ang recorded route sa lugar na pinagpipilian natin. Sa Butuan o Limasawa."
    judet @ thinking "So paano kung hindi tugma yung location sa route, ibig sabihin ba questionable na yung claim?"
    jipri @ speaking "Tama."

    hide jiperson
    hide jipri
    hide judet

    # EVIDENCE 2: DISTANCE AND DIRECTION
    show jiperson placeholder at stage_center
    show jipri placeholder at stage_left
    show judet placeholder at stage_right

    judet @ speaking "May compass at distance markers dito."
    jipri @ speaking "Gagamitin natin yung recorded directions at distances bilang clues."
    jiperson @ thinking "So hindi lang kung saan sila pumunta, pati na rin kung gaano kalayo at anong direksyon."
    judet @ thinking "Hmmm... and kapag pinagsama natin yung route, distance, at direction..."
    jipri @ speaking "...mas makikita natin kung alin ang mas consistent."

    hide jiperson
    hide jipri
    hide judet

    # EVIDENCE 3: ISLAND DESCRIPTION
    scene bg placeholder_limasawa_island
    with dissolve

    show jiperson placeholder at stage_center
    show jipri placeholder at stage_left
    show judet placeholder at stage_right

    jiperson @ speaking "Wait, nasa Limasawa tayo?"
    jipri @ speaking "Oo."
    judet @ speaking "Ibig sabihin pwede natin ma-check dito yung ibang descriptions ng Mazaua?"
    jipri @ speaking "Sa account ni Pigafetta, ang Mazaua ay inilarawan bilang isang isla."
    jiperson @ speaking "And Limasawa is an island."
    judet @ thinking "Pero sabi mo kanina, hindi sapat ang isang evidence."
    jiperson @ speaking "Correct. Kaya kailangan pa rin natin i-connect sa route, distance, direction, at sa original account."

    hide jiperson
    hide jipri
    hide judet


    # EVIDENCE 4: HISTORICAL INVESTIGATION
    scene bg placeholder_limasawa_shrine
    with dissolve

    show jiperson placeholder at stage_center
    show jipri placeholder at stage_left
    show judet placeholder at stage_right

    judet @ speaking "Ito na ba yung shrine?"

    jipri @ speaking "Oo. At dito natin pagsasama-samahin ang lahat."

    # Investigation board placeholder
    show investigation_board_placeholder at investigation_board_center
    with dissolve

    # Optional pause for the player to examine the board
    pause

    jiperson @ thinking "Kapag pinag-connect natin lahat..."
    judet @ speaking "Mas nag-lead sa Limasawa."
    jipri @ speaking "Hmm... Pero kailangan nating tandaan na hindi lamang isang evidence ang nagbigay sa atin ng conclusion."
    jipri @ speaking "So, after reviewing all the evidence, which side are you guys?"

    # PLAYER CHOICE
    menu:
        "BUTUAN":
            $ historical_choice = "Butuan"
            jump chapter4_choice_result
        "LIMASAWA":
            $ historical_choice = "Limasawa"
            jump chapter4_choice_result

label chapter4_choice_result:
    # REGARDLESS OF CHOICE
    jipri @ speaking "Interesting. Pero hindi pa tapos ang investigation."
    judet @ speaking "Bakit? May kulang pa ba na evidence?"
    jipri @ speaking "Meron."
    jipri @ speaking "At dito natin malalaman kung ano ang naging conclusion kung Butuan ba o Limasawa."

    scene black
    with fade
    centered "{size=50}END OF CHAPTER 4!!{/size}"
    pause 2.0

    return