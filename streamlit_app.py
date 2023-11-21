import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#set page/use all #df is your dataframe
st.set_page_config(layout="wide", page_title="Ecotiva Carbon Calculator", initial_sidebar_state="expanded")

st.subheader("Leading Tomorrow's Climate Action Today")

EMISSION_FACTORS = {
    "India": {
        "Transport": 0.14,  # kgCO2/km
        "Electricity": 0.02,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5 kgCO2/kg
        "Waste": 0.1  # kgCO2/meal
    },
    "UK": {
        "Transport": 0.12,  # kgCO2/km
        "Electricity": 0.03,  # kgCO2/kWh
        "Diet": 1.15,  # kgCO2/meal, 2.3 kgCO2/kg
        "Waste": 0.09  # kgCO2/meal
    },
    "Germany": {
        "Transport": 0.13,  # kgCO2/km
        "Electricity": 0.02,  # kgCO2/kWh
        "Diet": 1.20,  # kgCO2/meal, 2.4 kgCO2/kg
        "Waste": 0.1  # kgCO2/meal
    },
    "USA": {
        "Transport": 0.15,  # kgCO2/km
        "Electricity": 0.025,  # kgCO2/kWh
        "Diet": 1.35,  # kgCO2/meal, 2.7 kgCO2/kg
        "Waste": 0.12  # kgCO2/meal
    },
    "West_Africa": {
        "Transport": 0.18,  # kgCO2/km
        "Electricity": 0.04,  # kgCO2/kWh
        "Diet": 1.40,  # kgCO2/meal, 2.8 kgCO2/kg
        "Waste": 0.15  # kgCO2/meal
    },
    "East_Africa": {
        "Transport": 0.17,  # kgCO2/km
        "Electricity": 0.035,  # kgCO2/kWh
        "Diet": 1.38,  # kgCO2/meal, 2.76 kgCO2/kg
        "Waste": 0.14  # kgCO2/meal
    },
    "Central_Africa": {
        "Transport": 0.19,  # kgCO2/km
        "Electricity": 0.038,  # kgCO2/kWh
        "Diet": 1.45,  # kgCO2/meal, 2.9 kgCO2/kg
        "Waste": 0.16  # kgCO2/meal
    },
    "South_Africa": {
        "Transport": 0.16,  # kgCO2/km
        "Electricity": 0.03,  # kgCO2/kWh
        "Diet": 1.30,  # kgCO2/meal, 2.6 kgCO2/kg
        "Waste": 0.11  # kgCO2/meal
    },
    "North_Africa": {
        "Transport": 0.2,  # kgCO2/km
        "Electricity": 0.036,  # kgCO2/kWh
        "Diet": 1.48,  # kgCO2/meal, 2.96 kgCO2/kg
        "Waste": 0.17  # kgCO2/meal
    }
}

st.sidebar.header("Your Carbbon Footprint")


#Adding option menu in sidebar
with st.sidebar:
     selected = option_menu(
        menu_title=None, #main menu
        options=["Home", "About US", "Products", "Solutions", "Company", "Emissions", "Scope 1-3" ],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"pardding": "0!important", "background-color": ""},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link":{
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "green"},
        }
         
        
    )
     
# ... (existing code)



# ... (remaining code)

## change menu to home page horizontal
# selected = option_menu(
#         menu_title=None, #"main menu"
#         options=["Home", "Projects", "Contact"],
#         icons=["house", "book", "envelope"],
#         menu_icon="cast",
#         default_index=0,
#         orientation="horizontal",
#         styles={
#             "container": {"pardding": "0!important", "background-color": "white"},
#             "icon": {"color": "orange", "font-size": "25px"},
#             "nav-link":{
#                 "font-size": "25px",
#                 "text-align": "left",
#                 "margin": "0px",
#                 "--hover-color": "#eee",
#             },
#             "nav-link-selected": {"background-color": "green"},
#         }
        
#     )



#if option select menu
if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")

# Check the selected menu option
# if selected == "Home":
#     st.title("Home Page")
#     # Display content for the Home page
    
# elif selected == "About US":
#     st.title("About Us")
#     # Display content for the About Us page
    
# elif selected == "Products":
#     st.title("Products")
#     # Display content for the Products page
    
# elif selected == "Solutions":
#     st.title("Solutions")
#     # Display content for the Solutions page
    
# elif selected == "Company":
#     st.title("Company")
#     # Display content for the Company page
    
# elif selected == "Emissions":
#     st.title("Emissions")
#     # Display content for the Emissions page
    
# elif selected == "Scope 1-3":
#     st.title("Scope 1-3")
#     # Display content for the Scope 1-3 page

# ... (existing code)

# Check the selected menu option
if selected == "Home":
    st.title("Home Page")
    # Display content for the Home page

elif selected == "About US":
    st.title("About Us")
    
    if st.button("Read About US"):
        # Displaying an image
        image = Image.open('econ.png')
        st.image(image, caption='Ecotiva')
        st.title("About Ecotiva")
        st.write("Ecotiva is a leading company is carbon Financing committed to provide organisations, individuals and governments agencies to undertand and to offer the best software to offset their carbon emissions in African and across the globe")
    # Display content for the About Us page

elif selected == "Products":
    st.title("Products")
    # Display content for the Products page

# Add a new conditional block for Company's Mission page
elif selected == "Company":
    st.title("Company")
    # Display content for the Company page
    # For instance, a button to navigate to the Company's Mission page
    if st.button("View Company's Mission"):
        st.title("Company's Mission")
        # Here, display detailed information about the company's mission, values, etc.

elif selected == "Solutions":
    st.title("Solutions")
    # Display content for the Solutions page

elif selected == "Emissions":
    st.title("Emissions")
    # Display content for the Emissions page

elif selected == "Scope 1-3":
    st.title("Scope 1-3")
    # Display content for the Scope 1-3 page

# ... (remaining code)



st.title ("Ecotiva Carbon Accounting Software")

#user input
st.subheader("Your Country")
country = st.selectbox("Select", ['India','UK', 'USA', 'West_Africa', 'East_Africa', 'Central_Africa', 'South_Africa', 'North_Africa' ])
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
    st.subheader("Waste Generated per Week (per Ton)")
    waste = st.slider("Waste", 0, key="waste_input")
    #distance = st.number_input("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("Number of Meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")


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

    
    
    # with col3:
    #     st.subheader('Carbon Emission by Categories')
    #     st.info(f" Transportation: (transportation_emission) tonnes C02 per year")
    #     st.info(f" Electricity: (electricity_emissions) tonnes C02 per year")
    #     st.info(f" Diet: (diet_emissions) tonnes C02 per year")
    #     st.info(f" Waste: (waste_emissions) tonnes C02 per year")
        
    # with col4:
    #     st.subheader("Total Carbon Footprint")
    #     st.info(f" Your total carbon footprint is: (total_emissions) tonnes C02 per year")
    #     st.warning("In 2021, C02 emissions per capital for Ghana was 1.9 tones. Between 2000 and 2021, total emission per capital of Ghana grew substantially from 0.08 to 1.9 rising at an increasing annual rate that reached a maximum of 9.41% in 2021")
     

    