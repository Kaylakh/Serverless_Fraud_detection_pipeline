import streamlit as st
import requests, json
from PIL import Image
import io
import pandas as pd


st.markdown('<style>  body {background-color: black; color: black}</style>', unsafe_allow_html=True)

st.markdown('<style>body{background-color: cornsilk;}</style>',unsafe_allow_html=True)
html_temp = """
<div style="background-color:black;padding:10px">
<h1 style="color:red;text-align:center;">E-Commerce </h1>
</div> """
st.markdown(html_temp,unsafe_allow_html=True)



menu = ["Home","Login","Sign Up"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.write('')
    image=Image.open('commerce.png')
    st.image(image, caption='E-commerce',use_column_width=True)

    


if choice == "Login":
    
    username = st.sidebar.text_input("Enter Username")
    password = st.sidebar.text_input("Enter Password", type='password')

#    st.subheader("Login Section ")
#
#     username = st.text_input("User Name")
#     password = st.text_input("Password", type='password')
#     if st.button("SignIn"):
    if st.sidebar.checkbox("Login"):

        st.success("Logged in as {}".format(username))
        gateway_url0 = 'https://sjys10yiqj.execute-api.us-east-1.amazonaws.com/dev/signin'
        # convert into json format
        json_payload0 = json.dumps({"username": username, "password": password})
        response0 = requests.post(gateway_url0, data=json_payload0)
        st.write("Token generated is:")
        data0 = response0.json()
        display_data0 = st.text(data0)


        # st.success("Logged in as {}".format(username))
        gateway_url0 = 'https://sjys10yiqj.execute-api.us-east-1.amazonaws.com/dev/signin'
        # convert into json format
        json_payload0 = json.dumps({"username": username, "password": password})
        response0 = requests.post(gateway_url0, data=json_payload0)

        # st.success("Logged In as {}".format(username))
        # st.subheader("INFO")

        id_29_choice= ["Found","Not Found"]
        id_29 = st.selectbox("id_29",id_29_choice)

        id_31_choice = ["android","android browswer 4.0","android webview 4.0","samsung browser 6.2", "mobile safari 11.0", "chrome 62.0", "edge 15.0", "chrome 62.0 for android", "mobile safari generic",
                    "chrome 49.0","chrome 61.0","edge 16.0","safari generic"]
        id_31 = st.selectbox("id_31", id_31_choice)

        device_type_choice = ["Mobile", "Desktop"]
        device_type = st.selectbox("Device Type", device_type_choice)

        device_info_choice = ['Samsung','ios','macos','windows','redmi']
        device_info = st.selectbox("Device Information", device_info_choice)

        transaction_dt = st.text_input("Enter Transaction DT")

        transaction_amt = st.text_input("Enter Transaction Amount")

        product_cd_choice = ["C", "H", "R", "S"]
        product_cd = st.selectbox("Device ProductCD", product_cd_choice)

        card1 = st.text_input("Enter card1 Input")

        card4_choice = ["Master", "Visa"]
        card4 = st.selectbox("Device Card4", card4_choice)

        card6_choice = ["Credit", "Debit"]
        card6 = st.selectbox("Device Card6", card6_choice)

        addr1 = st.text_input("Enter addr1 Input")

        addr2 = st.text_input("Enter addr2 Input")

        emaildomain = st.text_input("Enter email ")

        if st.button("Submit"):
            url = "https://al1279jin8.execute-api.us-east-1.amazonaws.com/dev/transaction"

            json_payload5 = json.dumps({"id_29":id_29, "id_31":id_31, "DeviceType":device_type, "DeviceInfo": device_info,
                    "TransactionDT":transaction_dt, "TransactionAmt":transaction_amt, "ProductCD":product_cd, "card1":card1,
                    "card4":card4, "card6":card6, "addr1":addr1, "addr2":addr2, "email":emaildomain})

            response = requests.post(url, data=json_payload5)

            # data5 = response5.json()
            # display_data5 = st.text(data5)
            # response = requests.post(url, info)
            #st.write(response.json())
            response.json()
            st.write("Thank you for ordering")
            st.write("Please check you email for your order confirmation")


if choice == "Sign Up":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    username1 = new_user
    password1 =new_password

    if st.button("SignUp"):
        gateway_url5 = 'https://sjys10yiqj.execute-api.us-east-1.amazonaws.com/dev/signup'
        # convert into json format
        json_payload5 = json.dumps({"username": username1, "password": password1})
        response5 = requests.post(gateway_url5, data=json_payload5)

        data5 = response5.json()
        display_data5 = st.text(data5)

        st.success("You have successfully created a valid account")
        st.info("Go to Login Menu to Login")




