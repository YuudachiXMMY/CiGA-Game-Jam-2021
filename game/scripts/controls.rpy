
init offset = -2

default curr_mouse_xpos = 0
default curr_player_xpos = 0
default tar_player_xpos = curr_mouse_xpos
default global_xoffset = 0
default player_xoffset = global_xoffset
default bar_xoffset = global_xoffset

default TwalkSpeed = 0.2
default diff = (tar_player_xpos - player_xoffset) - curr_player_xpos

screen mouseControl():

    zorder 300

    modal True

    text "Waling...":
        xpos 100 ypos 0

    if firstShowed:
        on 'show' action SetVariable('firstShowed', False)

        on 'show' action [  Hide('mainChacter'),
                            Show('mainChacter')
                            ]
    else:
        on 'show' action [  Hide('mainChacter'),
                            Show('mainChacter'),
                            SetVariable('player_xoffset', global_xoffset),
                            SetVariable('curr_mouse_xpos', renpy.get_mouse_pos()[0]),
                            SetVariable('tar_player_xpos', renpy.get_mouse_pos()[0])
                            ]

    $ diff = (tar_player_xpos - player_xoffset) - curr_player_xpos

    timer 0.0001 action SetVariable('walkSpeed', (0.31-0.026) / (1+(abs(diff)/500) ** 2) + 0.026 )
    $ TwalkSpeed = (0.31-0.026) / (1+(abs(diff)/500) ** 2) + 0.026

    timer (8-0.4) / (1+(TwalkSpeed/0.06) ** 2.4) + 0.4  action Hide('mouseControl')


screen bgControl(width):

    zorder 111

    fixed:
        if renpy.get_screen('train1') or renpy.get_screen('train2') or renpy.get_screen('train3'):
            imagebutton:
                keysym 'mousedown_4'
                ypos -50 xpos -50
                idle "bgControl_slider_btn_idle"
                if global_xoffset <= -(width - 1280 - 75):
                    action NullAction()
                else:
                    if renpy.get_screen('train1'):
                        action [SetVariable('global_xoffset', global_xoffset-75),
                                Hide('train1_bg_front'), Show('train1_bg_front')
                                ]
                    if renpy.get_screen('train2'):
                        action [SetVariable('global_xoffset', global_xoffset-75),
                                Hide('train2_bg_front'), Show('train2_bg_front')
                                ]
                    if renpy.get_screen('train3'):
                        action [SetVariable('global_xoffset', global_xoffset-75),
                                Hide('train3_bg_front'), Show('train3_bg_front')
                                ]
                    else:
                        action [SetVariable('global_xoffset', global_xoffset-75),
                                ]
            imagebutton:
                keysym 'mousedown_5'
                ypos -50 xpos -50
                idle "bgControl_slider_btn_idle"
                if global_xoffset >= 0 - 75:
                    action NullAction()
                else:
                    if renpy.get_screen('train1'):
                        action [SetVariable('global_xoffset', global_xoffset+50),
                                Hide('train1_bg_front'), Show('train1_bg_front')
                                ]
                    if renpy.get_screen('train2'):
                        action [SetVariable('global_xoffset', global_xoffset+50),
                                Hide('train2_bg_front'), Show('train2_bg_front')
                                ]
                    if renpy.get_screen('train3'):
                        action [SetVariable('global_xoffset', global_xoffset+50),
                                Hide('train3_bg_front'), Show('train3_bg_front')
                                ]
                    else:
                        action [SetVariable('global_xoffset', global_xoffset+50),
                                ]

        if width - 1280 > 0:
            style_prefix 'bgControl'
            xpos 493
            if renpy.get_screen('train1'):
                bar value VariableValue('bar_xoffset', width-1280, action=[
                    SetVariable('global_xoffset', -bar_xoffset),
                    Hide('train1_bg_front'), Show('train1_bg_front')
                ])
            elif renpy.get_screen('train2'):
                bar value VariableValue('bar_xoffset', width-1280, action=[
                    SetVariable('global_xoffset', -bar_xoffset),
                    Hide('train2_bg_front'), Show('train2_bg_front')
                ])
            elif renpy.get_screen('train3'):
                bar value VariableValue('bar_xoffset', width-1280, action=[
                    SetVariable('global_xoffset', -bar_xoffset),
                    Hide('train3_bg_front'), Show('train3_bg_front')
                ])
            else:
                bar value VariableValue('bar_xoffset', width-1280, action=[
                    SetVariable('global_xoffset', -bar_xoffset)
                ])

style bgControl_bar:
    xysize(1280, 45)
    xpos-490 ypos 720 - 45
    base_bar "bgControl_slider_idle"
    thumb "bgControl_slider_btn_idle"

screen mainChacter():

    zorder 100

    on 'show' action Play('sound', 'music/walk.mp3')
    timer (8-0.4) / (1+(TwalkSpeed/0.06) ** 2.4) action Stop('sound')

    $ diff = (tar_player_xpos - player_xoffset) - curr_player_xpos

    $ TwalkSpeed = (0.31-0.026) / (1+(abs(diff)/500) ** 2) + 0.026

    # Stable
    if diff == 0:
        add 'main_character_front':
            xoffset global_xoffset
            xpos tar_player_xpos - player_xoffset
    # Move Right
    if diff > 0:
        add 'main_cahracter_walk_right':
            xoffset global_xoffset
            at transform:
                xpos curr_player_xpos
                linear (8-0.4) / (1+(TwalkSpeed/0.06) ** 2.4) + 0.4 xpos tar_player_xpos - global_xoffset
    # Move Left
    elif diff < 0:
        add 'main_cahracter_walk_left':
            xoffset global_xoffset
            at transform:
                xpos curr_player_xpos
                linear (8-0.4) / (1+(TwalkSpeed/0.06) ** 2.4) + 0.4 xpos tar_player_xpos - global_xoffset

    timer 0.01 action SetVariable('curr_player_xpos', tar_player_xpos - player_xoffset)

screen item(name, log):
    zorder 200

    modal True

    imagebutton:
        idle 'null_bg'
        action Hide('item')


    add 'item_bg' align(0.5, 0.5)

    add name align(0.5, 0.5)
    text _(str(log)) align(0.5,0.6)





## Test Map Demo
screen test():

    tag test

    zorder 100

    add "test_bg" xpos 0 xoffset global_xoffset

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl', width=3840)

    imagebutton:
        idle "gui/null_mouseControll.png"
        action Show('mouseControl')


    # dev
    fixed:
        if dev:

            text _('curr_mouse_xpos '+str(curr_mouse_xpos)) xpos 500 ypos 100 xoffset global_xoffset
            text _('curr_player_xpos '+str(curr_player_xpos)) xpos 500 ypos 200 xoffset global_xoffset

            text _('tar_player_xpos '+str(tar_player_xpos)) xpos 900 ypos 100 xoffset global_xoffset
            text _('global_xoffset '+str(global_xoffset)) xpos 900 ypos 200  xoffset global_xoffset
            text _('player_xoffset '+str(player_xoffset)) xpos 900 ypos 300  xoffset global_xoffset
