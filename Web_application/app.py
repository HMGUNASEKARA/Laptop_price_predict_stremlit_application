import streamlit as st 
import pickle 
import pandas as pd 

def main():
    with st.form("Form1"):
        st.header("Laptop Price Prediction App")
        col1,col2 = st.columns(2)

        ram = col1.number_input("RAM(GB)",min_value=2, max_value=64)
        weight = col2.number_input("Weight(KG)")

        brand = st.selectbox("Brand",["Lenovo","Dell","HP","Asus","Acer","Others","MSI","Toshiba"])
        Type  = st.selectbox("Type",["Notebook","Gaming","Ultrabook","2 in 1 Convertible ","Workstation","Netbook"])
        oparation_system = st.selectbox("Operating System",["Windows","Other","Linux"])
        CPU = st.selectbox("CPU",["Intel Core i7","Intel Core i5","Other","Intel Core i3","AMD"])
        GPU = st.selectbox("GPU",["Intel","Nvidia","AMD"])
        

        
        
        
        submitted = st.form_submit_button("Submit")

    st.header("Laptop Price Prediction App")

    if submitted:
        data = pd.DataFrame({
            "Brand": [brand],
            "Type": [Type],
            "RAM": [ram],
            "Weight": [weight],
            "Operating System": [oparation_system],
            "CPU": [CPU],
            "GPU": [GPU]
                   })

        st.write(data)


if __name__ == '__main__':
    main()



    