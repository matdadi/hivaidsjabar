from utils import *

# ----------------------------------
#css menu
menu_style = '''
        "font-style: normal;
        font-weight: 700;
        font-size: 24px;
        line-height: 29px;
        color: #000;
        text-decoration: none;
        text-weight: normal;
        "
    '''

menu_select_style = '''
    "font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 29px;
    text-decoration-line: underline;
    color: #6B6B6B;"
'''

#css home
pictframe = '''
    <style>
        [title^='st.iframe'] {
            height: 800px;
            width:600px;
            margin-left: auto;
            margin-right: auto;
            display: block;
            }
    </style>
'''

chartframe = '''
    <style>
        [title^='st.iframe'] {
            height: 400px;
            width:600px;
            margin-left: auto;
            margin-right: auto;
            display: block;
            }
    </style>
'''

bg_style = '''
    "position: relative;
    width: 600px;
    height: 800px;
    background: #FFFFFF;"
'''

img_style = '''
    "position: absolute;
    width: 400px;
    height: 400px;
    left: 100px;
    top: 158px;
    border-radius: 400px;"
'''

upper_right_wrap_style = '''
    "position: absolute;
    width: 240px;
    height: 151px;
    left: 320px;
    top: 92px;
    background: #FFFFFF;
    border: 1px solid #C3C3C3;
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 8px;
    display: block;"
'''

text_up_right1 = '''
    "position: absolute;
    width: 145px;
    height: 39px;
    left: 30px;
    top: 37px;
    font-style: normal;
    font-weight: 700;
    font-size: 32px;
    line-height: 39px;
    color: #5C8D6F;"
'''

text_up_right2 = '''
    "position: absolute;
    width: 147px;
    height: 19px;
    left: 30px;
    top: 92px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 300;
    font-size: 16px;
    line-height: 19px;
    color: #000000;"
'''

bottom_left_wrap_style1 = '''
    "position: absolute;
    width: 140px;
    height: 120px;
    left: 10px;
    top: 457px;
    background: #FFFFFF;
    border: 1px solid #C3C3C3;
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 8px;"
'''

bottom_left_wrap_style2 = '''
    "position: absolute;
    width: 140px;
    height: 120px;
    left: 160px;
    top: 457px;
    background: #FFFFFF;
    border: 1px solid #C3C3C3;
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 8px;"
'''

bottom_left_wrap_style3 = '''
    "position: absolute;
    width: 140px;
    height: 120px;
    left: 10px;
    top: 607px;
    background: #FFFFFF;
    border: 1px solid #C3C3C3;
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 8px;"
'''

bottom_left_wrap_style4 = '''
    "position: absolute;
    width: 140px;
    height: 120px;
    left: 160px;
    top: 607px;
    background: #FFFFFF;
    border: 1px solid #C3C3C3;
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 8px;"
'''

text_bottom_left1a = '''
    "position: absolute;
    width: 103px;
    height: 19px;
    left: 12px;
    top: 18px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 300;
    font-size: 16px;
    line-height: 19px;
    color: #000000;"
'''

text_bottom_left1b = '''
    "position: absolute;
    width: 101px;
    height: 29px;
    left: 12px;
    top: 60px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 24px;
    line-height: 29px;
    color: #599580;"
'''

text_bottom_left2a = '''
    "position: absolute;
    width: 113px;
    height: 19px;
    left: 12px;
    top: 18px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 300;
    font-size: 16px;
    line-height: 19px;
    color: #000000;"
'''

text_bottom_left2b = '''
    "position: absolute;
    width: 101px;
    height: 29px;
    left: 12px;
    top: 60px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 24px;
    line-height: 29px;
    color: #599580;"
'''

text_bottom_left3a = '''
    "position: absolute;
    width: 119px;
    height: 19px;
    left: 12px;
    top: 18px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 300;
    font-size: 16px;
    line-height: 19px;
    color: #000000;"
'''

text_bottom_left3b = '''
    "position: absolute;
    width: 101px;
    height: 29px;
    left: 12px;
    top: 60px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 24px;
    line-height: 29px;
    color: #599580;"
'''

text_bottom_left4a = '''
    "position: absolute;
    width: 75px;
    height: 19px;
    left: 12px;
    top: 18px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 300;
    font-size: 16px;
    line-height: 19px;
    color: #000000;"
'''

text_bottom_left4b = '''
    "position: absolute;
    width: 101px;
    height: 29px;
    left: 12px;
    top: 60px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 24px;
    line-height: 29px;
    color: #599580;"
'''

text_chart_1 = '''
    "position: absolute;
    font-style: normal;
    font-weight: 400;
    font-size: 36px;
    line-height: 44px;
    color: #C3C3C3;"
'''

text_chart_2 = '''
    "position: absolute;
    font-style: normal;
    font-weight: 400;
    font-size: 36px;
    line-height: 44px;
    color: #C3C3C3;"
'''

text_chart_3 = '''
    "position: absolute;
    width: 220px;
    height: 264px;
    left: 20px;
    top: 0px;
    font-style: normal;
    font-weight: 400;
    font-size: 36px;
    line-height: 44px;
    color: #C3C3C3;"
'''

text_chart_4 = '''
    "position: absolute;
    width: 220px;
    height: 264px;
    left: 20px;
    top: 0px;
    font-style: normal;
    font-weight: 400;
    font-size: 36px;
    line-height: 44px;
    color: #C3C3C3;"
'''


# ----------------------------------

dict_css = {
    # css menu
    'menu_style' : menu_style,
    'menu_select_style' : menu_select_style,
    # css home
    'pictframe' : pictframe,
    'chartframe' : chartframe,
    'bg_style' : bg_style,
    'img_style' : img_style,

    'upper_right_wrap_style' : upper_right_wrap_style,

    'text_up_right1' : text_up_right1,
    'text_up_right2' : text_up_right2,

    'bottom_left_wrap_style1' : bottom_left_wrap_style1,
    'bottom_left_wrap_style2' : bottom_left_wrap_style2,
    'bottom_left_wrap_style3' : bottom_left_wrap_style3,
    'bottom_left_wrap_style4' : bottom_left_wrap_style4,

    'text_bottom_left1a' : text_bottom_left1a,
    'text_bottom_left1b' : text_bottom_left1b,
    'text_bottom_left2a' : text_bottom_left2a,
    'text_bottom_left2b' : text_bottom_left2b,
    'text_bottom_left3a' : text_bottom_left3a,
    'text_bottom_left3b' : text_bottom_left3b,
    'text_bottom_left4a' : text_bottom_left4a,
    'text_bottom_left4b' : text_bottom_left4b,

    'text_chart1' : text_chart_1,
    'text_chart2' : text_chart_2,
    'text_chart3' : text_chart_3,
    'text_chart4' : text_chart_4
}

def get_css(key):
    return dict_css[key]
