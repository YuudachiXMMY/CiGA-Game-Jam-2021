init offset = -2

define x_obj = 75

## Gui
image null_bg:
    "gui/null_mouseControll.png"

image item_bg:
    "gui/map/item_bg.png"

image start_btn_idle:
    alpha 0.5
    "gui/start.png"
    linear 1.5 alpha 0.85
    pause 0.5
    linear 1.5 alpha 0.5
    pause 0.1
    repeat

image start_btn_hover:
    alpha 1.0
    "gui/start.png"

## Test
image test_bg:
    "bg/test/bg1.png"
    linear 0.3
    "bg/test/bg2.png"
    linear 0.3
    "bg/test/bg3.png"
    linear 0.3
    repeat

## Intro
image intro_bg:
    "bg/intro/intro.jpg"

image intro_train1_btn:
    "bg/intro/train1_btn_idle.png"

image intro_train1_btn_idle:
    alpha 0.6
    "bg/intro/train1_btn_hover.png"
    linear 1.5 alpha 0.9
    pause 0.1
    linear 1.5 alpha 0.6
    pause 0.5
    repeat

image intro_train1_btn_hover:
    alpha 1.0
    "bg/intro/train1_btn_hover.png"


## Train 1
image train1_bg:
    'bg/train1/bg.jpg'

image train1_bg_ani:
    alpha 0.5
    'bg/train1/bg_ani.jpg'
    linear 1.5 alpha 1.0
    pause 0.1
    linear 1.5 alpha 0.5
    pause 0.5
    repeat

image train1_bg_front:
    'bg/train1/bg_front.png'

image train1_train2_btn:
    "bg/train1/train2_btn_idle.png"

image train1_train2_btn_idle:
    alpha 0.6
    "bg/train1/train2_btn_hover.png"
    linear 1.5 alpha 0.9
    pause 0.1
    linear 1.5 alpha 0.6
    pause 0.5
    repeat

image train1_train2_btn_hover:
    alpha 1.0
    "bg/train1/train2_btn_hover.png"

image train1_candle_btn_idle:
    "bg/train1/candle_hover.png"
    linear 0.7
    "bg/train1/candle_idle.png"
    linear 0.7
    repeat

image train1_candle_btn_hover:
    "bg/train1/candle_idle.png"

image train1_string_btn_idle:
    "bg/train1/string_idle.png"

image train1_string_btn_hover:
    "bg/train1/string_hover.png"


# Train2
image train2_bg:
    'bg/train2/bg.jpg'

image train2_bg_ani:
    alpha 0.5
    'bg/train2/bg_ani.jpg'
    linear 1.5 alpha 1.0
    pause 0.1
    linear 1.5 alpha 0.5
    pause 0.5
    repeat

image train2_bg_front:
    'bg/train2/bg_front.png'

image train2_bg_front_ani:
    alpha 0.2
    'bg/train2/bg_front_ani.png'
    linear 1.5 alpha 0.9
    pause 0.1
    linear 1.5 alpha 0.2
    pause 0.5
    repeat

image train2_train3_btn:
    "bg/train2/train3_btn_idle.png"

image train2_train3_btn_idle:
    alpha 0.6
    "bg/train2/train3_btn_hover.png"
    linear 1.5 alpha 0.9
    pause 0.1
    linear 1.5 alpha 0.6
    pause 0.5
    repeat

image train2_train3_btn_hover:
    alpha 1.0
    "bg/train2/train3_btn_hover.png"

image train2_train2_btn:
    "bg/train2/train2_btn_idle.png"

image train2_train2_btn_idle:
    alpha 0.6
    "bg/train2/train2_btn_hover.png"
    linear 1.5 alpha 0.9
    pause 0.1
    linear 1.5 alpha 0.6
    pause 0.5
    repeat

image train2_train2_btn_hover:
    alpha 1.0
    "bg/train2/train2_btn_hover.png"

image train2_string_btn_idle:
    "bg/train2/string_idle.png"

image train2_string_btn_hover:
    "bg/train2/string_hover.png"

image train2_ske_btn_idle:
    "bg/train2/ske_idle.png"

image train2_ske_btn_hover:
    "bg/train2/ske_hover.png"




# train3
image train3_bg:
    'bg/train3/bg.jpg'

image train3_bg_ani:
    alpha 0.5
    'bg/train3/bg_ani.jpg'
    linear 1.5 alpha 1.0
    pause 0.1
    linear 1.5 alpha 0.5
    pause 0.5
    repeat

image train3_bg_front:
    'bg/train3/bg_front.png'

image train3_bg_front_ani:
    alpha 0.2
    'bg/train3/bg_front_ani.png'
    linear 1.5 alpha 0.9
    pause 0.1
    linear 1.5 alpha 0.2
    pause 0.5
    repeat

image train3_train2_btn:
    "bg/train3/train2_btn_idle.png"

image train3_train2_btn_idle:
    alpha 0.6
    "bg/train3/train2_btn_hover.png"
    linear 1.5 alpha 0.9
    pause 0.1
    linear 1.5 alpha 0.6
    pause 0.5
    repeat

image train3_train2_btn_hover:
    alpha 1.0
    "bg/train3/train2_btn_hover.png"

image train3_post_btn_idle:
    "bg/train3/post_idle.png"

image train3_post_btn_hover:
    "bg/train3/post_hover.png"

image train3_door3_btn_idle:
    "bg/train3/door3_idle.png"

image train3_door3_btn_hover:
    'train3_door3_btn_idle'
    # "bg/train3/door3_hover.png"

image train3_fire_ani:
    "bg/train3/fire.png"

# End 1
image end1_1:
    "bg/end/1/1.jpg"
image end1_2:
    "bg/end/1/2.jpg"
image end1_3:
    "bg/end/1/3.jpg"
image end1_4:
    "bg/end/1/4.jpg"

# End 2
image end2_1:
    xpos 1500
    "bg/end/2/1.jpg"
image end2_2:
    xpos 1500
    "bg/end/2/2.jpg"
image end2_3:
    xpos 1500
    "bg/end/2/3.jpg"
image end2_4:
    xpos 1500
    "bg/end/2/4.jpg"
image end2_5:
    xpos 1500
    "bg/end/2/5.jpg"
image end2_6:
    xpos 1500
    "bg/end/2/6.jpg"




## Map 1
image map1_bg:
    'bg/map1/bg.png'

image map1_bg_front:
    'bg/map1/bg_front.png'