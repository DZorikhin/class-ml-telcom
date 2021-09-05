import streamlit as st
import pickle
import numpy as np


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🔮",
    initial_sidebar_state="expanded",
    )


def map_inputs(*parameters):
    gender_ = 0 if parameters[0] == 'Female' else 1
    senior_citizen_ = 0 if parameters[1] == 'No' else 1
    partner_ = 0 if parameters[2] == 'No' else 1
    dependents_ = 0 if parameters[3] == 'No' else 1
    
    if parameters[4] <= 9.0:
        tenure_ = 0
    elif parameters[4] > 9.0 and parameters[4] <= 29.0:
        tenure_ = 1
    elif parameters[4] > 29.0 and parameters[4] <= 56.0:
        tenure_ = 2
    else:
        tenure_ = 3

    phone_service_ = 0 if parameters[5] == 'No' else 1

    if parameters[6] == 'No phone service':
        multiple_lines_ = 0 
    elif parameters[6] == 'No':
        multiple_lines_ = 1
    else:
        multiple_lines_ = 2
    
    if parameters[7] == 'No':
        internet_service_ = 0 
    elif parameters[7] == 'DSL':
        internet_service_ = 1
    else:
        internet_service_ = 2
    
    if parameters[8] == 'No':
        online_security_ = 0 
    elif parameters[8] == 'Yes':
        online_security_ = 1
    else:
        online_security_ = 2
    
    if parameters[9] == 'No':
        online_backup_ = 0 
    elif parameters[9] == 'Yes':
        online_backup_ = 1
    else:
        online_backup_ = 2

    if parameters[10] == 'No':
        device_protection_ = 0 
    elif parameters[10] == 'Yes':
        device_protection_ = 1
    else:
        device_protection_ = 2

    if parameters[11] == 'No':
        tech_support_ = 0 
    elif parameters[11] == 'Yes':
        tech_support_ = 1
    else:
        tech_support_ = 2

    if parameters[12] == 'No':
        streaming_tv_ = 0 
    elif parameters[12] == 'Yes':
        streaming_tv_ = 1
    else:
        streaming_tv_ = 2

    if parameters[13] == 'No':
        streaming_movies_ = 0 
    elif parameters[13] == 'Yes':
        streaming_movies_ = 1
    else:
        streaming_movies_ = 2

    if parameters[14] == 'Month-to-month':
        contract_ = 0 
    elif parameters[14] == 'One year':
        contract_ = 1
    else:
        contract_ = 2

    paperless_billing_ = 0 if parameters[15] == 'No' else 1

    if parameters[16] == 'Electronic check':
        payment_ = 0 
    elif parameters[16] == 'Mailed check':
        payment_ = 1
    elif parameters[16] == 'Bank transfer (automatic)':
        payment_ = 2
    else:
        payment_ = 3

    if parameters[17] <= 35.65:
        monthly_charges_ = 0
    elif parameters[17] > 35.65 and parameters[17] <= 70.4:
        monthly_charges_ = 1
    elif parameters[17] > 70.4 and parameters[17] <= 89.9:
        monthly_charges_ = 2
    else:
        monthly_charges_ = 3
    
    if parameters[18] <= 404.3:
        total_charges_ = 0
    elif parameters[18] > 404.3 and parameters[18] <= 1412.0:
        total_charges_ = 1
    elif parameters[18] > 1412.0 and parameters[18] <= 3847.0:
        total_charges_ = 2
    else:
        total_charges_ = 3

    features = np.array([[gender_, senior_citizen_, partner_, dependents_, tenure_, 
                        phone_service_, multiple_lines_, internet_service_, online_security_, 
                        online_backup_, device_protection_, tech_support_, streaming_tv_, 
                        streaming_movies_, contract_, paperless_billing_, payment_, monthly_charges_, 
                        total_charges_]])
    return features


def handle_output(prediction):
    if prediction == 0:
        return 'Customer with selected features is NOT likely to churn'
    else:
        return 'Customer with selected features is likely to churn'


def main():
    st.title("Telco Customer Churn")
    html_temp = """
    <div style="background-color:#117A65; padding:9px">
    <h2 style="color:white;text-align:center;">Behavior to Retain Customers</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write(f'Github repository with project description, EDA and model training could be accessed here: https://github.com/DZorikhin/class-ml-telcom')
    activities = ['Random Forest', 'Logistic Regression', 'SVM', 'Gradient Boosting', 'AdaBoost', 'XGBoost']
    model_option = st.selectbox('Which model would you like to use?', activities)
    st.subheader(f'Select features and predict with {model_option} model')

    gender = st.radio("Gender", ("Female", "Male"))
    senior_citizen = st.radio("Senior Citizen", ("Yes", "No"))
    partner = st.radio("Partner", ("Yes", "No"))
    dependents = st.radio("Dependents", ("Yes", "No"))
    tenure = st.number_input("How long does client use company\'s service (months)?", value=12, step=1, min_value=0, max_value=75)
    phone_service = st.radio("Does customer have phone service?", ("Yes", "No"))
    multiple_lines = st.selectbox("Does customer have multiple lines?", ("Yes", "No", "No phone service"))
    internet_service = st.selectbox("What internet service does customer have?", ("DSL", "Fibre optic", "No internet service"))
    online_security = st.radio("Does customer have online security service?", ("Yes", "No", "No internet service"))
    online_backup = st.radio("Does customer have online backup service?", ("Yes", "No", "No internet service"))
    device_protection = st.radio("Does customer have device protection service?", ("Yes", "No", "No internet service"))
    tech_support = st.radio("Does customer have tech support option?", ("Yes", "No", "No internet service"))
    contract = st.selectbox("What kind of contract does customer have?", ("Month-to-month", "One year", "Two year"))
    streaming_tv = st.radio("Does customer have Streaming TV?", ("Yes", "No", "No internet service"))
    streaming_movies = st.radio("Does customer have Streaming movies option?", ("Yes", "No", "No internet service"))
    paperless_billing = st.radio("Does customer prefer paperless billing?", ("Yes", "No"))
    payment = st.selectbox("What payment method does customer prefer?", ("Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"))
    monthly_charges = st.slider("What is the amount charged to the customer monthly?", value=60.0, step=0.5, min_value=15.0, max_value=120.0)
    total_charges = st.slider("What is the total amount charged to the customer?", value=4000.0, step=0.5, min_value=15.0, max_value=9000.0)

    X = map_inputs(gender, senior_citizen, partner, dependents, tenure, phone_service, multiple_lines, internet_service, 
                    online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movies, contract, 
                    paperless_billing, payment, monthly_charges, total_charges)
    
    if st.button('Predict Churn'):
        if model_option == 'Random Forest':
            random_forest = pickle.load(open('random-forest.pkl','rb'))            
            st.success(handle_output(random_forest.predict(X)[0]))
        elif model_option == 'Logistic Regression':
            log_reg = pickle.load(open('logistic-regression.pkl','rb'))
            st.success(handle_output(log_reg.predict(X)[0]))
        elif model_option == 'SVM':
            svm = pickle.load(open('SVM.pkl','rb'))
            st.success(handle_output(svm.predict(X)[0]))
        elif model_option == 'Gradient Boosting':
            grad_boost = pickle.load(open('gradient-boosting.pkl','rb'))
            st.success(handle_output(grad_boost.predict(X)[0]))
        elif model_option == 'AdaBoost':
            ada_boost = pickle.load(open('ada-boost.pkl','rb'))
            st.success(handle_output(ada_boost.predict(X)[0]))
        elif model_option == 'XGBoost':
            xg_boost = pickle.load(open('XGBoost.pkl','rb'))
            st.success(handle_output(xg_boost.predict(X)[0]))


if __name__=='__main__':
    main()