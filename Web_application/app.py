import streamlit as st 
import pickle 
import pandas as pd 

from xgboost import XGBRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the model,encoder,scaler and PCA2
import os
import pickle

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the pickle file
model_path = os.path.join(BASE_DIR, "final_model.pkl")

# Load the model
with open(model_path, "rb") as f:
    model = pickle.load(f)




# Get the directory of the current script
BASE_DIR2 = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the pickle file
encoder_path = os.path.join(BASE_DIR2, "encoder.pkl")

# Load the model
with open(encoder_path, "rb") as f:
    encoder = pickle.load(f)




# Get the directory of the current script
BASE_DIR3 = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the pickle file
pca_path = os.path.join(BASE_DIR3, "PCA.pkl")

# Load the model
with open(pca_path, "rb") as f:
    pca = pickle.load(f)



# Get the directory of the current script
BASE_DIR4 = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the pickle file
scaler_x_path = os.path.join(BASE_DIR4, "scaler_x.pkl")

# Load the model
with open(scaler_x_path, "rb") as f:
    scaler_x = pickle.load(f)



# Get the directory of the current script
BASE_DIR5 = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the pickle file
scaler_y_path = os.path.join(BASE_DIR5, "scaler_y.pkl")

# Load the model
with open(scaler_y_path, "rb") as f:
    scaler_y = pickle.load(f)

#with open("encoder.pkl", "rb") as f:
    #encoder = pickle.load(f)

#with open("final_model.pkl", "rb") as f:
   # model = pickle.load(f)

#with open("pca.pkl", "rb") as f:
   # pca = pickle.load(f)

#with open("scaler_x.pkl", "rb") as f:
#    scaler_x = pickle.load(f)


#with open("scaler_y.pkl", "rb") as f:
#    scaler_y = pickle.load(f)


def main():

    with st.form("Form1"):
        st.header("Laptop Price Prediction App")
        col1,col2 = st.columns(2)

        ram = col1.number_input("RAM(GB)",min_value=2, max_value=64)
        weight = col2.number_input("Weight(KG)")

        brand = st.selectbox("Brand",["Lenovo","Dell","HP","Asus","Acer","Others","MSI","Toshiba","Apple"])
        Type  = st.selectbox("Type",["Notebook","Gaming","Ultrabook","2 in 1 Convertible","Workstation","Netbook"])
        oparation_system = st.selectbox("Operating System",["Windows","Other","Linux","Mac"])
        CPU = st.selectbox("CPU",["Intel Core i7","Intel Core i5","Other","Intel Core i3","AMD"])
        GPU = st.selectbox("GPU",["Intel","Nvidia","AMD"])
        submitted =st.form_submit_button("Predict Price")

        

    if submitted:
        data = pd.DataFrame({
            "Company": [brand],
            "TypeName": [Type],
            "Ram": [ram],
            "Weight": [weight],
            "OpSys": [oparation_system],
            "CPU_name": [CPU],
            "GPU_Name": [GPU]
                   })

        #st.write(data)
        # Define the catergarical and numarical features 
        data_catergarical = data[["Company","TypeName","OpSys","CPU_name","GPU_Name"]]
        data_numerical = data[["Ram","Weight"]]

        # Use the encoder for catergarical features, after encoding that givs the array then make data frame
        data_catergarical = encoder.transform(data_catergarical) 
        data_catergarical = pd.DataFrame(data_catergarical, columns=encoder.get_feature_names_out())
        
        # Use the standard scaler for numarical features
        data_numerical = scaler_x.transform(data_numerical)
        data_numerical = pd.DataFrame(data_numerical,columns=["Ram", "Weight"]   )
        
        # Apply PCA to numarical features
        data_numerical = pca.transform(data_numerical)
        data_numerical = pd.DataFrame(data_numerical,columns=[f"PCA_{i}" for i in range(data_numerical.shape[1])])

        # Add all the varibles together and make x varibles for prediction.
        data= pd.concat([data_catergarical,data_numerical], axis=1)
        #Print(data)

        # Predict the price using the model
        price = model.predict(data)
        real_price = (scaler_y.inverse_transform(price.reshape(-1,1)))*295-50000
        #Print(real_price)
        #st.write(f"The predicted price of the laptop is: LKR{real_price[0][0]:.2f}")
        st.markdown(f"## The predicted price of the laptop is: LKR {real_price[0][0]:.2f}")

if __name__ == '__main__':
    main()



    