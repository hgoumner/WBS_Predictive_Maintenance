# Import modules
import streamlit as st
import streamlit.components.v1 as components
import joblib
import pandas as pd

# Load model
# model = joblib.load('/home/hristo/Documents/WBS_Data_Science/WBS_Predictive_Maintenance/models/ML_balanced_multi.joblib')
model = joblib.load('/home/hristo/Documents/WBS_Data_Science/WBS_Predictive_Maintenance/models/DL_balanced_multi.joblib')


def ChangeButtonColour(widget_label, background_color='transparent'):
    print(result[0])
    print(widget_label, background_color)
    htmlstr = f"""
        <script language="javascript">
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{
                if (elements[i].innerText == '{widget_label}') {{
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)


def set_color():
    for ind, val in enumerate(result[0]):
        if (val == 1):
            ChangeButtonColour(failure_types[ind], 'red')
        elif (val == 0):
            ChangeButtonColour(failure_types[ind], 'green')


def set_failure():
    fs = []
    for ind, val in enumerate(result[0]):
        if (val == 1):
            fs.append(f"<font color=red>{failure_types[ind]}</font>")
        else:
            fs.append(f"<font color=green>{failure_types[ind]}</font>")

    return fs


st.header('Enter input values')

# Air temperature
temp_air = st.slider(
    'Enter air temperature',
    min_value=295.0,
    max_value=305.0,
    value=300.0,
    format='%.2f',
    on_change=set_failure
)

st.divider()

# Process temperature
temp_process = st.slider(
    'Enter process temperature',
    min_value=305.0,
    max_value=315.0,
    value=310.0,
    format='%.2f',
    on_change=set_failure
)

st.divider()

# Rotational speed
rot_speed = st.slider(
    'Enter rotational speed',
    min_value=1150.0,
    max_value=3000.0,
    value=1538.0,
    format='%.2f',
    on_change=set_failure
)

st.divider()

# Torque
torque = st.slider(
    'Enter torque',
    min_value=0.0,
    max_value=100.0,
    value=40.0,
    format='%.2f',
    on_change=set_failure
)
st.divider()

# Tool wear [min]
tool_wear = st.slider(
    'Enter tool wear life',
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

# result = [[0, 0, 1, 0, 0]]

failure_types = [
    'Tool wear failure',
    'Heat dissipation failure',
    'Power failure',
    'Overstrain failure',
    'Random failure'
]

st.header('Model prediction')

# buttons = []
# cols = st.columns(len(failure_types), gap='small')
# for i, col in enumerate(cols):
#     col.button(
#         label=failure_types[i],
#     )

# st.write(result[0])

# st.markdown(
#     """
#     <style>
#     div.stButton > button:first-child {
#         background-color: green;
#         height: 150px;
#         width: 150px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.write(result[0])
st.write('Failure:')
failures = set_failure()
for f in failures:
    st.markdown(f, unsafe_allow_html=True)

# 0 0 1 1 0 - torque 69, twl 276