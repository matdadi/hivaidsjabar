from utils import *

# ----------------------------------
# css
from master_css import get_css
# ----------------------------------

def load_pagedata(data, penduduk, region=''):
    _lock = RendererAgg.lock
    sns.set_style('darkgrid')

    tbl_space1, tbl_col1, tbl_space2, tbl_col2, tbl_space3, tbl_col3, tbl_space4 = st.columns(
                (.1, 1, .1, 1, .1, 1, .1)
            )

    with tbl_col1, _lock:
        if region=='':
            filter_region = st.multiselect('Kabupaten/Kota', tuple(np.unique(data['Kabupaten/Kota'])))
        else: filter_region = st.multiselect('Kabupaten/Kota', tuple(np.unique(data['Kabupaten/Kota'])), [region])

    with tbl_col2, _lock:
        filter_gender = st.selectbox('Jenis Kelamin', tuple(np.insert(np.unique(data['Jenis Kelamin']), 0, '-Pilih-', axis=0)))
    with tbl_col3, _lock:
        filter_age = st.selectbox('Kelompok umur', tuple(np.insert(np.unique(data['Umur']), 0, '-Pilih-', axis=0)))

    tbl_space1, tbl_col1, tbl_space2 = st.columns(
        (.1, 1, .1)
    )

    filtered = []

    with tbl_col1, _lock:
        if any(filter_region):
            filtered = data['Kabupaten/Kota'].isin(filter_region)
            filtered = data[filtered]
        else: filtered = data.copy(deep=True)

        if filter_gender!='-Pilih-': filtered = filtered[filtered['Jenis Kelamin']==filter_gender]
        if filter_age!='-Pilih-': filtered = filtered[filtered['Umur']==filter_age]
        
        st.dataframe(filtered)


