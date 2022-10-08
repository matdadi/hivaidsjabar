# used library
from matplotlib.backends.backend_agg import RendererAgg
import streamlit as st
import pandas as pd
import urllib.request
import seaborn as sns
import matplotlib
from streamlit_lottie import st_lottie
import requests
import json
import geopandas as gpd
import altair as alt
import numpy as np
from streamlit_option_menu import option_menu
from functools import reduce
from streamlit.components.v1 import html
import base64
import plotly.graph_objects as go
import plotly.express as px

#variabel master
dict_master = {
        'menu': ['Home', 'Detail', 'Data']
    }

#url
dict_url = {
    'hiv': 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17570_jumlah_kasus_hiv_berdasarkan_kelompok_umur?limit=1000',
    'aids': 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17572_jumlah_kasus_aids_berdasarkan_kelompok_umur?limit=1000',
    'mortality': 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17575_jumlah_kematian_akibat_aids_berdasarkan_kelompok_umur?limit=1000',
    'animasi': 'https://assets2.lottiefiles.com/packages/lf20_t2bpn6yt.json'
}

#csv file
dict_csv = {
    'penduduk': 'bps_penduduk_jabar_2019.csv'
}

def load_json(key):
    '''
    key: pilih data yang akan diambil seperti hiv, aids, mortality, atau animasi.
    '''
    url = dict_url[key]
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def load_csv(key):
    '''
    key: pilih data csv yang akan diambil seperti penduduk.
    '''
    filepath = dict_csv[key]
    r = pd.read_csv(filepath, sep=';')
    return(r)

def load_geodata():
    data = gpd.read_file('Jabar_By_Kab.geojson')
    return data

def json2df(json_data):
    '''
    read json to dataframe
    '''
    contents = json_data
    data = contents['data']
    df = pd.DataFrame(data)
    return df

def preprocess_data(raw):
    res = raw.copy(deep=True)
    res['kelompok_umur'] = res['kelompok_umur'].str.replace(r'≥50','More than 50', regex=True)
    res['kelompok_umur'] = res['kelompok_umur'].str.replace(r'5-14','05-14', regex=True)
    res['kelompok_umur'] = res['kelompok_umur'].str.replace(r'TIDAK DIKETAHUI','Unknown', regex=True)
    res['nama_kabupaten_kota'] = res['nama_kabupaten_kota'].str.replace(r'KABUPATEN','KAB.', regex=True)
    return res

def preprocess_csv(df):
    df['wilayah'] = df['wilayah'].str.replace(r'KABUPATEN','KAB.', regex=True)
    return df

def preprocess_map():
    geoData = load_geodata()
    geoData['OBJECTID'] = geoData['OBJECTID'].astype(str).astype(int)
    geoData['ID_KAB'] = geoData['ID_KAB'].astype(float).astype(int)
    return geoData

def merge_data(df_aids, df_hiv, df_mortal):
    join = [df_aids, df_hiv, df_mortal]
    join = reduce(lambda left,right: pd.merge(left,right,on=['kode_provinsi', 'nama_provinsi', 'nama_kabupaten_kota','kode_kabupaten_kota',
                'kelompok_umur','jenis_kelamin', 'satuan', 'tahun'], how='left'), join).fillna(0)
    join = join.drop(columns=['id', 'id_x', 'id_y', 'kode_provinsi', 'nama_provinsi', 'tahun', 'satuan'])
    join['jumlah_kasus_y'] = join['jumlah_kasus_y'].astype(int)
    join['jumlah_kasus_x'] = join['jumlah_kasus_x'].astype(int)
    join['jumlah_kasus'] = join['jumlah_kasus'].astype(int)
    join = join.rename(columns={'kode_kabupaten_kota': 'Kode Kabupaten/Kota',
                            'nama_kabupaten_kota': 'Kabupaten/Kota',
                            'kelompok_umur': 'Umur',
                            'jenis_kelamin': 'Jenis Kelamin',
                            'jumlah_kasus': 'Kematian',
                            'jumlah_kasus_x': 'AIDS',
                            'jumlah_kasus_y': 'HIV',
                        })
    return join

def load_master(key):
    '''
    key: pilih data master yang ingin digunakan
    '''
    return dict_master[key]

def navigation():
        if st.experimental_get_query_params()['p'][0]=='':
                st.experimental_set_query_params(p=load_master('menu')[0])
        return st.experimental_get_query_params()['p'][0]
                
#     try:
#         path = st.experimental_get_query_params()['p'][0]
#     except Exception as e:
#         st.experimental_set_query_params(p=load_master('menu')[0])
#         return st.experimental_get_query_params()['p'][0]
#     return path

def grup_by_gender(data, key):
    grup = data.copy(deep=True)
    grup['Total'] = grup.groupby(['Kabupaten/Kota', 'Jenis Kelamin'], as_index=False)[key].transform('sum')
    grup = grup.groupby(['Kabupaten/Kota', 'Jenis Kelamin'], as_index=False).head(1).reset_index(drop=True)
    return grup

def grup_by_age(data, key):
    grup = data.copy(deep=True)
    grup['Total'] = grup.groupby(['Kabupaten/Kota', 'Umur'], as_index=False)[key].transform('sum')
    grup = grup.groupby(['Kabupaten/Kota', 'Umur'], as_index=False).head(1).reset_index(drop=True)
    return grup

def grup_by_region(data, key):
    grup = data.copy(deep=True)
    grup['Total'] = grup.groupby(['Kabupaten/Kota'], as_index=False)[key].transform('sum')
    grup = grup.groupby(['Kabupaten/Kota'], as_index=False).head(1).reset_index(drop=True)
    return grup

def total_by_region(data, penduduk):
    tot = data.copy(deep=True)
    tot['total HIV'] = tot.groupby(['Kabupaten/Kota'], as_index=False)['HIV'].transform('sum')
    tot['total Kematian'] = tot.groupby(['Kabupaten/Kota'], as_index=False)['Kematian'].transform('sum')
    tot['total AIDS'] = tot.groupby(['Kabupaten/Kota'], as_index=False)['AIDS'].transform('sum')
    tot = tot.drop(['HIV', 'Kematian','AIDS','Umur','Jenis Kelamin'], axis=1)
    tot = tot.merge(penduduk, how='left', left_on='Kabupaten/Kota', right_on='wilayah').fillna(0)
    tot = tot.drop(['wilayah', 'tahun'], axis=1)
    tot['laki-laki'] = tot['laki-laki'].astype(int)
    tot['perempuan'] = tot['perempuan'].astype(int)
    tot['total'] = tot['total'].astype(int)
    tot = tot.groupby(['Kabupaten/Kota', 'total HIV', 'total Kematian', 'total AIDS', 'laki-laki', 'perempuan', 'total'], as_index=False).head(1).reset_index(drop=True)
    tot['tanpa HIV'] = tot['total']-tot['total HIV']
    tot['tanpa Kematian'] = tot['total AIDS']-tot['total Kematian']
    tot['tanpa AIDS'] = tot['total']-tot['total AIDS']
    return tot
