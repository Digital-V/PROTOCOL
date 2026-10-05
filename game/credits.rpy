transform credit_scroll(t):
    ypos 1.0
    linear t ypos -3.5

screen credits():
    modal True
    
    add "#000000"
    
    # Automatically exits the screen when the 48-second scroll finishes
    timer 48.0 action Return()

    frame:
        background None
        xalign 0.5
        xysize (1200, 900)
        
        vbox:
            xalign 0.5
            spacing 30
            
            text "{size=80}Mazaua: The Lost Shore{/size}" xalign 0.5 color "#ffcc00"
            text "{size=34}A Visual Novel on the First Mass Controversy{/size}" xalign 0.5 color "#f5eedc"
            
            null height 60
            
            text "{size=52}CHARACTER CAST{/size}" xalign 0.5 color "#ffcc00"
            text "Jiperson" xalign 0.5 color "#ffffff" size 38
            text "Jipri" xalign 0.5 color "#ffffff" size 38
            text "Judet" xalign 0.5 color "#ffffff" size 38
            
            null height 50
            
            text "{size=52}DEVELOPMENT{/size}" xalign 0.5 color "#ffcc00"
            
            text "Lead Visual Artist" xalign 0.5 color "#aaaaaa" size 28
            text "Louise Castañares" xalign 0.5 color "#ffffff" size 38
            
            null height 15
            text "Lead Writer" xalign 0.5 color "#aaaaaa" size 28
            text "Zeto Cabahug" xalign 0.5 color "#ffffff" size 38
            
            null height 15
            text "Assistant Lead" xalign 0.5 color "#aaaaaa" size 28
            text "Ashley Nicole Quiambao" xalign 0.5 color "#ffffff" size 38
            
            null height 15
            text "Writer" xalign 0.5 color "#aaaaaa" size 28
            text "Sam Gabriel Mendoza" xalign 0.5 color "#ffffff" size 38
            
            null height 15
            text "Lead Developer" xalign 0.5 color "#aaaaaa" size 28
            text "Caleb Vargas" xalign 0.5 color "#ffffff" size 38
            
            null height 25
            text "Developers" xalign 0.5 color "#aaaaaa" size 28
            text "Janzen Joshua Martinez" xalign 0.5 color "#ffffff" size 32
            text "Vaughn Christian Tolentino" xalign 0.5 color "#ffffff" size 32
            text "Louiegie Lariosa" xalign 0.5 color "#ffffff" size 32
            text "Ruperth Jay Vesina" xalign 0.5 color "#ffffff" size 32
            
            null height 50
            
            text "{size=52}MADE IN{/size}" xalign 0.5 color "#ffcc00"
            text "Ren'Py" xalign 0.5 color "#ffffff" size 38
            
            null height 50
            
            text "{size=52}ACKNOWLEDGEMENTS & DISCLAIMER{/size}" xalign 0.5 color "#ffcc00"
            text "All information and historical details within this game were gathered from various credible resources. As this game was developed in just one week, minor mistakes and errors may exist. Events and details have been thoroughly researched, but please keep in mind this is an educational visual novel and some dramatization applies." xalign 0.5 color "#f5eedc" size 26 text_align 0.5 xmaximum 1000 line_spacing 8
            
            null height 40
            
            text "{size=52}AUDIO DISCLAIMER{/size}" xalign 0.5 color "#ffcc00"
            text "All background music and sound effects used in this game are not the property of the developers. All rights and ownership belong entirely to their respective copyright holders." xalign 0.5 color "#f5eedc" size 26 text_align 0.5 xmaximum 1000 line_spacing 8
            
            null height 70
            
            text "{size=36}GROUP PROTOCOL | BSCS 2 - 4{/size}" xalign 0.5 color "#ffcc00"
            
            at credit_scroll(48.0)

    textbutton "Skip" action Return() xalign 0.95 yalign 0.95 text_color "#f5eedc" text_hover_color "#ffcc00" text_size 30

label show_credits:
    scene black with fade
    hide screen chapter_info_hud
    play music "audio/bg_music_credits.mp3" fadein 0.5 volume 1.0 loop
    call screen credits
    stop music fadeout 1.0
    $ MainMenu(confirm=False)()
    return