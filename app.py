import streamlit as st
import pyotp
import pyperclip
import time


def generate_totp(secret_key):
    secret_key = secret_key.replace(' ', '')
    try:
        totp = pyotp.TOTP(secret_key)
        return totp.now()
    except Exception as e:
        st.error(f"Error: {e}")
        return None


st.title('TOTP Generator')

secret_key = st.text_input('Input your secret key:')

if secret_key:
    totp_code = generate_totp(secret_key)

    st.code(totp_code)

    if totp_code:
        time_left = 30 - int(time.time()) % 30
        st.write(f'New code in: {time_left} sec')

        while time_left > 0:
            time.sleep(1)
            time_left = 30 - int(time.time()) % 30
            st.rerun()
