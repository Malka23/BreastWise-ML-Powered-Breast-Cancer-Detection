import streamlit as st

def collect_user_input(feature_names, means):
    user_input = []
    for i, feature in enumerate(feature_names):
        val = st.number_input(
            label=f"{feature}",
            min_value=0.0,
            value=float(round(means[i], 3)),
            format="%.3f"
        )
        user_input.append(val)
    return user_input
