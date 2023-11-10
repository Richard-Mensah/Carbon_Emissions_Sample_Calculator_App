import streamlit as st
#from streamlit_option_menu import option_menu

#set page/use all #df is your dataframe
st.set_page_config(layout="wide", page_title="Ecotiva Carbon Footprint")


EMISSION_FACTORS = {
    "India":{
        "Transport": 0.14, #kgc02/km
        "Electricity": 0.02, #kgc02/kwl
        "Diet": 1.25, #kgc02/meal, 2.5 kgc02/kg
        "Waste": 0.1 #kgc02/meal 
    }
}

  

st.title ("Ecotiva Carbon Calculator")

#user input
st.subheader("Your Country")
country = st.selectbox("Select", ['India','Ghana', 'Nigeria'])
#country = st.selectbox("Select", ['India', 'Ghana', 'Nigeria'])

#devide into columns 
#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns(2)

with col1:
    st.header('Scope 1')
    st.subheader('Daily commute distance(in km)')
    distance = st.number_input("Distance", 0, key="distance_input")
    #distance = st.slider("Distance", 0, key="distance_input")
    
    st.subheader("Monthly Electricity Consumption")
    electricity = st.number_input("Electricity", 0, key='electricity_input')
    
    
with col2:
    st.header('Scope 2')
    st.subheader("Waste Generated per Week (in kg)")
    waste = st.slider("Waste", 0, key="waste_input")
    #distance = st.number_input("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("Number of Meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

# with col3:
#     st.header('Downloa Databse here')
#     upload_folder = st.file_uploader("download data")
     
    
    # take_pic = st.camera_input("Take a photo")
    # st.success("Your photo uploaded successfuly")
    #normalise inputs
    if distance > 0:
        distance = distance * 365
    
    #12months=1year
    if electricity > 0:
       electricity = electricity * 12  
        
    if meals > 0:
        meal = meals * 365
    
    #52week=1year
    if waste > 0:
        waste = waste * 52  
        
#Calculate Carbon Emission
#Defind the variables
transportation_emissions = EMISSION_FACTORS[country]['Transport'] * distance
electricity_emissions = EMISSION_FACTORS[country]['Electricity'] * electricity
diet_emissions = EMISSION_FACTORS[country]['Diet'] * meals
waste_emissions = EMISSION_FACTORS[country]['Waste'] * waste

#Round off here
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)


#Convert to tonnes and round off to 2 decimal places
total_emissions = round(
   transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

if st.button("Calculate Emissions"):
 
    #Display Result
    st.header("Results")
    
    col3, col4 = st.columns(2)
    
    
    with col3:
        st.subheader('Carbon Emission by Categories')
        st.info(f" Transportation: {transportation_emissions} tonnes C02 per year")
        st.info(f" Electricity: {electricity_emissions} tonnes C02 per year")
        st.info(f" Diet: {diet_emissions} tonnes C02 per year")
        st.info(f" Waste: {waste_emissions} tonnes C02 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.info(f" Your total carbon footprint is: {total_emissions} tonnes C02 per year")
        st.warning("In 2021, C02 emissions per capita for Ghana was 1.9 tonnes. Between 2000 and 2021, total emission per capita of Ghana grew substantially from 0.08 to 1.9 rising at an increasing annual rate that reached a maximum of 9.41% in 2021")

    
    
   

    
