from utils import *
from master_css import get_css

def load_menu():
    menu_space1, menu_1, menu_space2, menu_2, menu_space3, menu_3, menu_space4 = st.columns(
        (2, .5, .1, .5, .1, .5, 2)
    )
    _lock = RendererAgg.lock
    sns.set_style('darkgrid')

    selected_style = [
        get_css('menu_style'),
        get_css('menu_style'),
        get_css('menu_style')
    ]

    if navigation()==load_master('menu')[0]:
        selected_style[0]=get_css('menu_select_style')
    elif navigation()==load_master('menu')[1]:
        selected_style[1]=get_css('menu_select_style')
    elif navigation()==load_master('menu')[2]:
        selected_style[2]=get_css('menu_select_style')
    else: None

    with menu_1, _lock:
        st.markdown('''<div style="text-align: center; margin-bottom: 100px;"><a target="_self"
            href=http://localhost:8501/?p='''+load_master('menu')[0]+
            ''' style='''+selected_style[0]+'''>'''+load_master('menu')[0]+'''</a></div>
        ''', unsafe_allow_html=True)

    with menu_2, _lock:
        st.markdown('''<div style="text-align: center; margin-bottom: 100px;"><a target="_self"
            href=http://localhost:8501/?p='''+load_master('menu')[1]+
            ''' style='''+selected_style[1]+'''>'''+load_master('menu')[1]+'''</a></div>
        ''', unsafe_allow_html=True)

    with menu_3, _lock:
        st.markdown('''<div style="text-align: center; margin-bottom: 100px;"><a target="_self"
            href=http://localhost:8501/?p='''+load_master('menu')[2]+
            ''' style='''+selected_style[2]+'''>'''+load_master('menu')[2]+'''</a></div>
        ''', unsafe_allow_html=True)