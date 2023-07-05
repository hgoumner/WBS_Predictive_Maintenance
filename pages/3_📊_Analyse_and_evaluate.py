# Import modules
import streamlit as st
import joblib
import pandas as pd

# ----------------------------------------------------------------
# Load model
# ----------------------------------------------------------------
model = joblib.load('./models/DL_balanced_multi.joblib')


def set_failure():
    fs = []
    for ind, val in enumerate(result[0]):
        if (val == 1):
            fs.append(f'<p style="color:red; text-align:center; font-size:15pt;">{failure_types[ind]}</p>')
        else:
            fs.append(f'<p style="color:green; text-align:center; font-size:15pt;">{failure_types[ind]}</p>')

    return fs


st.header(":white[Enter input values]")

# ----------------------------------------------------------------
# Input
# ----------------------------------------------------------------
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# Air temperature
with col1:
    temp_air = st.slider(
        '**Enter air temperature**',
        min_value=295.0,
        max_value=305.0,
        value=300.0,
        format='%.2f',
        on_change=set_failure
    )

# Process temperature
with col2:
    temp_process = st.slider(
        '**Enter process temperature**',
        min_value=305.0,
        max_value=315.0,
        value=310.0,
        format='%.2f',
        on_change=set_failure
    )

# Rotational speed
with col3:
    rot_speed = st.slider(
        '**Enter rotational speed**',
        min_value=1150.0,
        max_value=3000.0,
        value=1538.0,
        format='%.2f',
        on_change=set_failure
    )

# Torque
with col4:
    torque = st.slider(
        '**Enter torque**',
        min_value=0.0,
        max_value=100.0,
        value=40.0,
        format='%.2f',
        on_change=set_failure
    )

# Tool wear [min]
with col5:
    tool_wear = st.slider(
        '**Enter tool wear life**',
        min_value=0.0,
        max_value=400.0,
        value=150.0,
        format='%.2f',
        on_change=set_failure
    )

input_values = pd.DataFrame(
    {
        'Air temperature [K]': [temp_air],
        'Process temperature [K]': [temp_process],
        'Rotational speed [rpm]': [rot_speed],
        'Torque [Nm]': [torque],
        'Tool wear [min]': [tool_wear]
    }
)

result = model.predict(input_values).round()

failure_types = [
    'Tool wear failure',
    'Heat dissipation failure',
    'Power failure',
    'Overstrain failure',
    'Random failure'
]

st.header('Model prediction')

failures = set_failure()

cols = st.columns(5, gap='medium')
for i, c in enumerate(failures):
    cols[i].markdown(c, unsafe_allow_html=True)