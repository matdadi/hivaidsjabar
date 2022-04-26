from utils import *
import menu, home, detail, pagedata

# ------------------------------------------

#page config
st.set_page_config(
    page_title="HIV AIDS Jawa Barat",
    layout="wide"
)

matplotlib.use('agg')
sns.set_style('darkgrid')

# ------------------------------------------

#css
hide_df_row_index = '''
    <style>
        .row_heading.level0 {display: none}
        .blank {display: none}
        div.st-cv st-c8 st-bf st-cw st-cx {visibility: hidden;}
        div.st-cv st-c8 st-bf st-cw st-cx:before {content: "-Pilih-"; visibility: visible;}
    </style>
'''

#inject css
st.markdown(hide_df_row_index, unsafe_allow_html=True)

# ------------------------------------------

#local variabel
@st.cache(allow_output_mutation=True)
def get_data():
    data = merge_data(
        preprocess_data(json2df(load_json('aids'))),
        preprocess_data(json2df(load_json('hiv'))),
        preprocess_data(json2df(load_json('mortality')))
        )
    return data

@st.cache(allow_output_mutation=True)
def get_penduduk():
    return preprocess_csv(load_csv('penduduk'))

@st.cache(allow_output_mutation=True)
def get_maps():
    return preprocess_map()


#animasi
get_animate = load_json('animasi')

# ------------------------------------------

st_lottie(get_animate, speed=1, height=100, key='initial')

# ------------------------------------------

#container menu
menu.load_menu()

if navigation()==load_master('menu')[0]:
    home.load_home(get_data(), get_penduduk(), get_maps())

if navigation()==load_master('menu')[1]:
    detail.load_detail(get_data(), get_penduduk())

if navigation()==load_master('menu')[2]:
    pagedata.load_pagedata(get_data(), get_penduduk())
