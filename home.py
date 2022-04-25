from utils import *

# ----------------------------------
# css
from master_css import get_css
# ----------------------------------

#local variabel
with open('rose.png', 'rb') as image_file:
        image_as_base64 = base64.b64encode(image_file.read())

#open page home
def load_home(data, penduduk, maps):
    _lock = RendererAgg.lock
    sns.set_style('darkgrid')

    home_space1, home_1, home_space2 = st.columns(
            (.5, 1, .5)
        )

    with home_1, _lock:
        html(rf'''
            <div style='''+get_css('bg_style')+rf'''>
                <img style='''+get_css('img_style')+rf''' src="data:image/png;base64, {image_as_base64.decode('utf-8')}"/>

                <!--upper-->
                <div style='''+get_css('upper_right_wrap_style')+'''>
                    <a style='''+get_css('text_up_right1')+'''>HIV/AIDS</a>
                    <a style='''+get_css('text_up_right2')+rf'''>Provinsi Jawa Barat</a>
                </div>

                <!--bottom-->
                <div style='''+get_css('bottom_left_wrap_style1')+'''>
                    <a style='''+get_css('text_bottom_left1a')+'''>Penderita HIV</a>
                    <a style='''+get_css('text_bottom_left1b')+'''>'''+str(data['HIV'].sum())+'''</a>
                </div>

                <div style='''+get_css('bottom_left_wrap_style2')+'''>
                    <a style='''+get_css('text_bottom_left2a')+'''>Penderita AIDS</a>
                    <a style='''+get_css('text_bottom_left2b')+'''>'''+str(data['AIDS'].sum())+'''</a>
                </div>

                <div style='''+get_css('bottom_left_wrap_style3')+'''>
                    <a style='''+get_css('text_bottom_left3a')+'''>Kasus Kematian</a>
                    <a style='''+get_css('text_bottom_left3b')+'''>'''+str(data['Kematian'].sum())+'''</a>
                </div>

                <div style='''+get_css('bottom_left_wrap_style4')+'''>
                    <a style='''+get_css('text_bottom_left4a')+'''>Jumlah Penduduk</a>
                    <a style='''+get_css('text_bottom_left4b')+'''>
                        '''+'{:.1f}'.format(penduduk['total'].iloc[0]/1000000).
                        replace('.',',')+''' Juta</a>
                </div>


            </div>
            ''')

    #inject css
    st.markdown(get_css('pictframe'), unsafe_allow_html=True)

    home_space1, home_1, home_space2, home_2, home_space3 = st.columns(
            (.4, .4, .2, .5, .2)
        )

    with home_1, _lock:
        filter_total = st.selectbox('Pilih pemetaan kasus HIV/AIDS:', ('HIV','AIDS','Kematian akibat AIDS'))

        dict_filter = {
            'HIV': 'total HIV',
            'AIDS': 'total AIDS',
            'Kematian akibat AIDS': 'total Kematian'
        }
    
    st.write('')

    home_space1, home_1, home_space2 = st.columns(
            (.2, 1, .2)
        )

    with home_1, _lock:
        fullData = maps.merge(total_by_region(data, penduduk), left_on=['ID_KAB'], right_on=['Kode Kabupaten/Kota']).set_index('Kabupaten/Kota')
        
        fig = px.choropleth(fullData,
            geojson=fullData.geometry,
            locations=fullData.index,
            color=dict_filter[filter_total], color_continuous_scale="reds",
            projection="natural earth")

        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(height=100)
        fig.update_traces(
            marker_line_width=.2,
            marker_line_color = 'gray'
        )
        fig.update_coloraxes(
            colorbar_orientation='h',
            colorbar=dict(
            yanchor='bottom', y=0, xanchor='center', x=0.5))
        fig.update_layout(height=700,
            title=dict(text='Persebaran '+str(dict_filter[filter_total]),
            xanchor='center', x=0.5, font=dict(size=36))
            )

        
        # plt.title('Peta Sebaran HIV di Provinsi Jawa Barat 2019', fontsize=13);
        st.plotly_chart(fig, use_container_width=True, config={
            'doubleClick': 'reset'
        })