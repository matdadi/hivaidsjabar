from utils import *

# ----------------------------------
# css
from master_css import get_css
# ----------------------------------

#open page home
def load_detail(data, penduduk, region=''):
    _lock = RendererAgg.lock

    det_space1, det_col1, det_space2, det_col2, det_space3, det_col3, det_space4 = st.columns(
                (.1, 1, .1, 1, .1, 1, .1)
            )

    with det_col1, _lock:
        if region=='':
            filter_region = st.multiselect('Kabupaten/Kota', tuple(np.unique(data['Kabupaten/Kota'])))
        else: filter_region = st.multiselect('Kabupaten/Kota', tuple(np.unique(data['Kabupaten/Kota'])), [region])

    if any(filter_region):
        temp = data[data['Kabupaten/Kota'].isin(filter_region)]
    else:
        temp = data.copy(deep=True)


    det_space1, det_1, det_space2, det_2, det_space3 = st.columns(
            (.2, 1, .1, .5, .2)
        )

    with det_1, _lock:
        gender = grup_by_gender(temp, 'HIV')

        color_scale = alt.Scale(domain=['LAKI-LAKI', 'PEREMPUAN'],
                            range=['#4287f5', '#e377c2'])

        left = alt.Chart(gender).transform_filter(
            alt.datum['Jenis Kelamin']=='PEREMPUAN'
        ).mark_bar().encode(
            x=alt.X('Total:Q', sort=alt.SortOrder('descending'), scale=alt.Scale(domain=[0, np.max(gender['Total'])])),
            y=alt.Y('Kabupaten/Kota:O', axis=None),
            color=alt.Color('Jenis Kelamin:N', scale=color_scale, legend=None)
        ).mark_bar().properties(title='PEREMPUAN', width=250)
        text_left = alt.Chart(gender[gender['Jenis Kelamin']=='PEREMPUAN']).mark_text(dx=-15, color="black").encode(
            x=alt.X("Total:Q"),
            y=alt.Y("Kabupaten/Kota:N"),
            text=alt.Text("Total:Q"))

        middle = alt.Chart(gender).encode(
            y=alt.Y('Kabupaten/Kota:O', axis=None),
            text=alt.Text('Kabupaten/Kota:O'),
        ).mark_text().properties(width=130)

        right = alt.Chart(gender).transform_filter(
            alt.datum['Jenis Kelamin']=='LAKI-LAKI'
        ).mark_bar().encode(
            x=alt.X('Total:Q', scale=alt.Scale(domain=[0, np.max(gender['Total'])])),
            y=alt.Y('Kabupaten/Kota:O', axis=None),
            color=alt.Color('Jenis Kelamin:N', scale=color_scale, legend=None)
        ).mark_bar().properties(title='LAKI-LAKI', width=250)
        text_right = alt.Chart(gender[gender['Jenis Kelamin']=='LAKI-LAKI']).mark_text(dx=15, color="black").encode(
            x=alt.X("Total:Q"),
            y=alt.Y("Kabupaten/Kota:N"),
            text=alt.Text("Total:Q"))
        fig1 = alt.concat(left+text_left, middle, right+text_right, spacing=3)
        st.altair_chart(fig1, use_container_width=True)

    with det_2, _lock:
        st.markdown('''
        <p style='''+get_css('text_chart1')+'''>Pembagian</br>Jumlah</br>Pengidap</br>HIV</br>Sesuai</br>Jenis</br>Kelamin</p>
        ''', unsafe_allow_html=True)

    det_space1, det_1, det_space2, det_2, det_space3 = st.columns(
            (.2, 1, .1, .5, .2)
        )

    with det_1, _lock:
        gender = grup_by_gender(temp, 'AIDS')

        color_scale = alt.Scale(domain=['LAKI-LAKI', 'PEREMPUAN'],
                            range=['#4287f5', '#e377c2'])

        left = alt.Chart(gender).transform_filter(
            alt.datum['Jenis Kelamin']=='PEREMPUAN'
        ).mark_bar().encode(
            x=alt.X('Total:Q', sort=alt.SortOrder('descending'), scale=alt.Scale(domain=[0, np.max(gender['Total'])])),
            y=alt.Y('Kabupaten/Kota:O', axis=None),
            color=alt.Color('Jenis Kelamin:N', scale=color_scale, legend=None)
        ).mark_bar().properties(title='PEREMPUAN', width=250)
        text_left = alt.Chart(gender[gender['Jenis Kelamin']=='PEREMPUAN']).mark_text(dx=-15, color="black").encode(
            x=alt.X("Total:Q"),
            y=alt.Y("Kabupaten/Kota:N"),
            text=alt.Text("Total:Q"))

        middle = alt.Chart(gender).encode(
            y=alt.Y('Kabupaten/Kota:O', axis=None),
            text=alt.Text('Kabupaten/Kota:O'),
        ).mark_text().properties(width=130)

        right = alt.Chart(gender).transform_filter(
            alt.datum['Jenis Kelamin']=='LAKI-LAKI'
        ).mark_bar().encode(
            x=alt.X('Total:Q', scale=alt.Scale(domain=[0, np.max(gender['Total'])])),
            y=alt.Y('Kabupaten/Kota:O', axis=None),
            color=alt.Color('Jenis Kelamin:N', scale=color_scale, legend=None)
        ).mark_bar().properties(title='LAKI-LAKI', width=250)
        text_right = alt.Chart(gender[gender['Jenis Kelamin']=='LAKI-LAKI']).mark_text(dx=15, color="black").encode(
            x=alt.X("Total:Q"),
            y=alt.Y("Kabupaten/Kota:N"),
            text=alt.Text("Total:Q"))
        fig1 = alt.concat(left+text_left, middle, right+text_right, spacing=3)
        st.altair_chart(fig1, use_container_width=True)
    
    with det_2, _lock:
        st.markdown('''
        <p style='''+get_css('text_chart2')+'''>Pembagian</br>Jumlah</br>Penderita</br>AIDS</br>Sesuai</br>Jenis</br>Kelamin</p>
        ''', unsafe_allow_html=True)

    # --------------------------------------------

    det_space1, det_1, det_space2, det_2, det_space3 = st.columns(
            (.2, 1, .1, .5, .2)
        )

    with det_1, _lock:
        age = grup_by_age(temp, 'HIV')
        region = grup_by_region(temp, 'HIV')

        bars = alt.Chart(age).mark_bar().encode(
            x=alt.X('Total:Q', stack='zero'),
            y=alt.Y('Kabupaten/Kota:N', axis=alt.Axis(format='', title='Kabupaten/Kota')),
            color=alt.Color('Umur', legend=alt.Legend(orient='bottom'))
        ).mark_bar().properties(width=720)

        text = alt.Chart(region).mark_text(dx=10, color="black").encode(
            x=alt.X("Total:Q"),
            y=alt.Y("Kabupaten/Kota:N"),
            text=alt.Text("Total:Q"))

        fig = bars+text
        st.altair_chart(fig, use_container_width=True)

    with det_2, _lock:
        st.markdown('''
        <p style='''+get_css('text_chart3')+'''>Pembagian</br>Jumlah</br>Pengidap</br>HIV</br>Sesuai</br>Kelompok</br>Umur</p>
        ''', unsafe_allow_html=True)

    det_space1, det_1, det_space2, det_2, det_space3 = st.columns(
            (.2, 1, .1, .5, .2)
        )

    with det_1, _lock:
        age = grup_by_age(temp, 'AIDS')
        region = grup_by_region(temp, 'AIDS')

        bars = alt.Chart(age).mark_bar().encode(
            x=alt.X('Total:Q', stack='zero'),
            y=alt.Y('Kabupaten/Kota:N', axis=alt.Axis(format='', title='Kabupaten/Kota')),
            color=alt.Color('Umur', legend=alt.Legend(orient='bottom'))
        ).mark_bar().properties(width=720)

        text = alt.Chart(region).mark_text(dx=10, color="black").encode(
            x=alt.X("Total:Q"),
            y=alt.Y("Kabupaten/Kota:N"),
            text=alt.Text("Total:Q"))

        fig = bars+text
        st.altair_chart(fig, use_container_width=True)

    with det_2, _lock:
        st.markdown('''
        <p style='''+get_css('text_chart4')+'''>Pembagian</br>Jumlah</br>Penderita</br>AIDS</br>Sesuai</br>Kelompok</br>Umur</p>
        ''', unsafe_allow_html=True)

    #css
    minheight = '''
        <style>
            .css-12w0qpk {min-height: 350px}
        </style>
    '''

    #inject css
    st.markdown(minheight, unsafe_allow_html=True)

    det_space1, det_col1, det_space2, det_col2, det_space3, det_col3, det_space4 = st.columns(
                (.1, 1, .1, 1, .1, 1, .1)
            )

    with det_col1, _lock:
        if len(filter_region)==1:
            total = total_by_region(data, penduduk)
            total = total[total['Kabupaten/Kota']==filter_region[0]]
            per = [['Bebas HIV', total['tanpa HIV'].iloc[0]*100/total['total'].iloc[0]], ['Pengidap HIV', total['total HIV'].iloc[0]*100/total['total'].iloc[0]]]
            df_per = pd.DataFrame(per, columns=['Status', 'Jumlah'])

            # pull is given as a fraction of the pie radius
            fig = go.Figure(data=[go.Pie(labels=df_per['Status'], values=df_per['Jumlah'], pull=[0, 0.2], texttemplate="%{value:.2f}%")])
            fig.update_layout(legend=dict(
                yanchor="bottom",
                xanchor="center",
                y=-0.1,
                x=0.5
            ))
            st.plotly_chart(fig, use_container_width=True)

            st.subheader('Prevalensi dalam 100 ribu populasi')
            prev = [['Bebas HIV', total['tanpa HIV'].iloc[0]/(total['total'].iloc[0]/100000)], ['Penderita HIV', total['total HIV'].iloc[0]/(total['total'].iloc[0]/100000)]]
            df_prev = pd.DataFrame(prev, columns=['Status', 'Jumlah'])
            df_prev['Jumlah'] = df_prev['Jumlah'].astype('int')
            st.dataframe(df_prev)

    with det_col2, _lock:
        if len(filter_region)==1:
            total = total_by_region(data, penduduk)
            total = total[total['Kabupaten/Kota']==filter_region[0]]
            per = [['Bebas AIDS', total['tanpa AIDS'].iloc[0]*100/total['total'].iloc[0]], ['Pasien AIDS', total['total AIDS'].iloc[0]*100/total['total'].iloc[0]]]
            df_per = pd.DataFrame(per, columns=['Status', 'Jumlah'])

            # pull is given as a fraction of the pie radius
            fig = go.Figure(data=[go.Pie(labels=df_per['Status'], values=df_per['Jumlah'], pull=[0, 0.2], texttemplate="%{value:.2f}%")])
            fig.update_layout(legend=dict(
                yanchor="bottom",
                xanchor="center",
                y=-0.1,
                x=0.5
            ))
            st.plotly_chart(fig, use_container_width=True)

            st.subheader('Prevalensi dalam 100 ribu populasi')
            prev = [['Bebas AIDS', total['tanpa AIDS'].iloc[0]/(total['total'].iloc[0]/100000)], ['Penderita AIDS', total['total AIDS'].iloc[0]/(total['total'].iloc[0]/100000)]]
            df_prev = pd.DataFrame(prev, columns=['Status', 'Jumlah'])
            df_prev['Jumlah'] = df_prev['Jumlah'].astype('int')
            st.dataframe(df_prev)

    with det_col3, _lock:
        if len(filter_region)==1:
            total = total_by_region(data, penduduk)
            total = total[total['Kabupaten/Kota']==filter_region[0]]
            per = [['Pasien AIDS', total['tanpa Kematian'].iloc[0]*100/total['total AIDS'].iloc[0]], ['Pasien Meninggal', total['total Kematian'].iloc[0]*100/total['total AIDS'].iloc[0]]]
            df_per = pd.DataFrame(per, columns=['Status', 'Jumlah'])

            if df_per['Jumlah'].sum()>0:
                # pull is given as a fraction of the pie radius
                fig = go.Figure(data=[go.Pie(labels=df_per['Status'], values=df_per['Jumlah'], pull=[0, 0.2], texttemplate="%{value:.2f}%")])
                fig.update_layout(legend=dict(
                    yanchor="bottom",
                    xanchor="center",
                    y=-0.2,
                    x=0.5
                ))
                st.plotly_chart(fig, use_container_width=True)

                st.subheader('Prevalensi dalam 100 populasi')
                prev = [['Pasien AIDS', total['tanpa Kematian'].iloc[0]/(total['total AIDS'].iloc[0]/100)], ['Pasien Meninggal', total['total Kematian'].iloc[0]/(total['total AIDS'].iloc[0]/100)]]
                df_prev = pd.DataFrame(prev, columns=['Status', 'Jumlah'])
                df_prev['Jumlah'] = df_prev['Jumlah'].astype('int')
                st.dataframe(df_prev)
            else:
                st.markdown('<div style="height:220px;"></div>', unsafe_allow_html=True)
                st.success(filter_region[0]+' bebas dari AIDS')
        

    