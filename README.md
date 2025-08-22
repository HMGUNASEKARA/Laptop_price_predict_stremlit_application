
# Laptop Price Prediction in the Sri Lankan Market

## 🚀 Check out the deployed app here:
[Laptop Price Predictor](https://your-app-link.com)

## 1. Machine Learning Concepts Applied
This project framed laptop price prediction as a supervised regression problem, aiming to estimate laptop prices based on specifications. Key concepts applied include:

- **Regression task:** predicting continuous target values (Price in Euros)  
- **Data preprocessing:** handling categorical and numerical variables, managing high-cardinality features  
- **Encoding techniques:** one-hot encoding for categorical data  
- **Feature scaling:** StandardScaler applied to numerical variables  
- **Dimensionality reduction:** Principal Component Analysis (PCA) for feature transformation  
- **Model evaluation:** R², Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and cross-validation  
- **Model comparison:** baseline regression, distance-based, tree-based, and ensemble methods  
- **Hyperparameter tuning:** grid/random search for KNN, SVR, Random Forest, and XGBoost  
- **Overfitting detection:** monitoring train vs test performance  
- **Model persistence:** saving trained model, encoder, and scalers for deployment  

## 2. Data Preparation

### Dataset Overview
- **Source:** Kaggle  
- **Size:** 1,303 records, 12 columns  
- **Target:** Price (Euros)  
- **Features:** company, product name, type, screen size, resolution, CPU, RAM, GPU, OS, weight  

### Key Steps
- Loaded dataset with **Latin1 encoding** to handle accents/non-English characters  
- Checked for missing values → none found  
- **Data type adjustments:**  
  - RAM → removed “GB” and converted to integer  
  - Weight → removed “kg” and converted to float  
- **Correlation check:** Weight and Inches highly correlated → retained Weight, dropped Inches  
- **Categorical simplification:**  
  - Company: minor brands grouped into “Other”  
  - OS: rare systems grouped into “Other”  
  - CPU: reduced 118 types to 5 categories (Intel Core i7, Intel Core i5, Intel Core i3, AMD, Other)  
  - GPU: grouped into Nvidia, Intel, AMD, Other  
- Dropped irrelevant columns: laptop_ID, product name, raw CPU/GPU strings, screen resolution, Inches  
- **Final features:** Company, TypeName, CPU Name, GPU Name, OS, RAM, Weight  
- **Target:** Price in Euros  

## 3. Feature Engineering
- **Independent variables:** Company, TypeName, CPU Name, GPU Name, OS, RAM, Weight  
- **Dependent variable:** Price  
- **Processing steps:**  
  - One-hot encoding for categorical features  
  - Scaling numerical features (RAM, Weight)  
  - Scaling target variable for prediction and inverse transformation  
  - PCA applied to reduce feature dimensions; 2 components improved generalization with XGBoost  

## 4. Model Building
- **Train/Test split:** 80% training, 20% testing  
- **Evaluation metrics:** R², MSE, RMSE  
- **Cross-validation:** 10-fold CV  

### Models Tested
- **Multiple Linear Regression:** R² ≈ 0.70; rejected due to assumption violations  
- **Classical ML:** Decision Tree, KNN, SVR → KNN and SVR initially performed well but overfitted  
- **Ensemble methods:** Random Forest, XGBoost → moderate improvements initially  
- **PCA experiment:** 1 component performed poorly; 2 components + XGBoost gave best performance  

### Final Model
- **XGBoost with 2 PCA features**  
- **Performance:**  
  - Test R² ≈ 0.81  
  - Train R² ≈ 0.90 (low overfitting)  
  - Error metrics significantly reduced  
- **Persistence:** saved model, encoder, feature scaler, and target scaler using pickle

  ## Tools & Environment

- **VS Code:** Used to build and test the web application.  
- **Framework:** Streamlit for creating the GUI.  
- **Environment:** Local virtual environment with required dependencies (scikit-learn, XGBoost, Streamlit).  
- **Integration:** Pickle files (model, encoder, scalers) from Google Colab were transferred and used in the Streamlit app in VS Code.


## 5. Deployment
- **Framework:** Streamlit GUI for interactive web app, developed in VS Code  
- **Workflow:**  
  - User inputs laptop specs via dropdowns/sliders  
  - Inputs are encoded and scaled  
  - Model predicts price, then inverse-transformed to Euros  
  - Result displayed instantly  
- **Features:** instant prediction, simple interface  
- **Future enhancements:** online deployment (Streamlit Cloud/Heroku), feature visualizations, currency conversion to LKR  

## 6. Conclusion
This project demonstrates the complete ML lifecycle:
- Data cleaning and preparation  
- Feature engineering and PCA  
- Model evaluation and hyperparameter tuning  
- Final selection of XGBoost (R² = 0.81)  
- Deployment via Streamlit for interactive use  
