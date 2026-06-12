# streamlit_app/app.py

try:
    import streamlit as st
except ModuleNotFoundError:
    # Provide a minimal fallback so static analysis / editors don't warn and
    # so the file can still be run in non-streamlit environments for basic testing.
    class _Stub:
        def set_page_config(self, *args, **kwargs):
            return None

        def title(self, txt):
            print(txt)

        def metric(self, label, value):
            print(f"{label}: {value}")

    st = _Stub()


st.set_page_config(
    page_title="Healthcare AI Dashboard",
    layout="wide"
)

st.title("🏥 AI Healthcare Analytics")

st.metric("Prediction Accuracy", "96%")
st.metric("Active Patients", "1250")
st.metric("Doctors", "150")
st.metric("Available Beds", "300")