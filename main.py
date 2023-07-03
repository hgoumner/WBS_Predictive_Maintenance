import pandas as pd
import pandas_profiling
import streamlit as st
st.set_page_config(layout='wide')

from streamlit_pandas_profiling import st_profile_report

# with open(r'/home/hristo/Documents/WBS_Data_Science/WBS_Predictive_Maintenance/data/report.html', 'r') as f:
#     html = f.read()

with open(r'/home/hristo/Documents/WBS_Data_Science/WBS_Predictive_Maintenance/doc/index.html', 'r') as f:
    html2 = f.read()

tab0, tab1, tab2, tab3 = st.tabs(['Introduction', 'EDA', 'Modeling', 'Result'])

with tab0:

    st.components.v1.html(html=html2, height=500, scrolling=True)

with tab1:

    # online
    df = pd.read_csv(r"/home/hristo/Documents/WBS_Data_Science/WBS_Predictive_Maintenance/data/ai4i2020.csv")
    pr = df.profile_report()

    st_profile_report(pr)

    # offline
    # st.components.v1.html(html=html, height=500, scrolling=True)