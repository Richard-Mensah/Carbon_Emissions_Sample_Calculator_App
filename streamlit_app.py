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
     



# #if option select menu
# if selected == "Home":
#     st.title(f"You have selected {selected}")
# if selected == "Projects":
#     st.title(f"You have selected {selected}")
# if selected == "Contact":
#     st.title(f"You have selected {selected}")

# Check the selected menu option
# CREATE PAGES 
if selected == "Home":
    st.title("Home Page")
    # Display content for the Home page

elif selected == "About US":
    st.title("About Us") 
    
    if st.button("Read About US"):
        # Displaying an image
        image = Image.open('econ.png')
        st.image(image, caption='Ecotiva')
        st.title("Ecotiva Excecutiva Summary")
        st.write("Ecotiva addresses the pressing problem of limited accessibility to a comprehensive platform for individuals and businesses to calculate, track, and offset their carbon footprints. With a user-centric approach, Ecotiva empowers individuals and businesses to easily participate in sustainable emissions reductions. Through a diverse portfolio of verified projects, transparent impact tracking, and personalized recommendations, we bridge the gap between climate-conscious individuals and impactful carbon offset projects. At Ecotiva, we recognize the growing need for convenient carbon offsetting in both the African and German markets. Our approach hinges on transparency and engagement. By offering a diverse array of meticulously verified projects, coupled with real-time impact tracking, we empower users with a tangible sense of their contributions to a greener future. Personalized recommendations further enhance the user experience, making sustainability a personalized journey. Our business model incorporates revenue from individual and corporate subscriptions, project verification fees, and potential strategic partnerships. The scalability and potential for expansion into other sustainability areas contribute to a promising revenue trajectory. Our dedicated team comprises tech and environmental experts, committed to making a positive environmental impact. The African market offers immense potential for carbon offset projects, driven by increasing climate awareness. While some existing platforms lack user-friendliness and transparency, we differentiate through our intuitive interface, robust verification processes, and personalized project suggestions. We aim to disrupt the market with a sustainable business model that involves project developers, corporations, and individual users. By connecting buyers with verified projects, we create a win-win scenario for offset providers and carbon-conscious consumers. Our value proposition lies in offering convenience, transparency, and impactful engagement in the carbon offset ecosystem. In the competitive landscape, our platform stands out with its user-centric design, comprehensive project information, and data-driven insights. We're poised to capture a significant share of the growing carbon offset market in Africa and Germany, driven by our commitment to transparency, innovation, and environmental impact. In summary, our platform bridges the gap in the African and German carbon offset markets, offering a comprehensive solution that empowers users, fosters sustainability, and contributes to the global fight against climate change.")
        st.title("Business Idea")
        #founding history
        st.subheader("Founding history")
        st.write("The carbon offset platform idea originates from a collaboration between environmentalists and tech enthusiasts with a shared vision for sustainable emissions reductions. The idea's originator, Emmanuel Danso, has a background in sustainability and has previously worked on climate projects. The concept was further developed through a synergy of entrepreneurial spirit and technical expertise. The business idea has been nurtured through extensive research and analysis, drawing from Emmanuel's background in sustainability. Property rights will be ensured, and intellectual property related to the platform's unique features and functionality secured from relevant stakeholders.")
        #kw
        st.subheader("Know-how Carrier")
        st.write("The foundation of our platform is rooted in a visionary founding team, committed to driving positive environmental impact while embracing gender diversity and innovative company structure. Our journey is anchored by each member's unique expertise, contributions, and shared passion for creating a more sustainable future.")
        st.markdown("Planned Founding Team and Task Distribution")
        st.markdown("""
        - Emmanuel Danso - With a background in sustainability and ESG, Emmanuel brings extensive experience in developing user-centric technological solutions that bridge people and sustainability. His innovative thinking and problem-solving skills have been instrumental in shaping the platform's features and functionality.
        - Victor Githinji - A seasoned full-stack developer, Victor Githinji contributes deep industry knowledge and strategic insight in developing customer-centric software applications. His experience in software development adds a valuable dimension to our team's capabilities.
        - Richard Mensah - As an Artificial Intelligence and Data Lead. With over 6 years of experience in building AI tools to solve issues in the African health space. 
        """)
        st.write("Each team member brings a unique set of skills, allowing us to tackle challenges from multiple angles. Task distribution is carefully planned to optimize individual strengths:")
        st.markdown("""
        - Victor Githinji focuses on platform development, user experience, and technical innovation.
        - Emmanuel Danso spearheads business development, market analysis, and strategic partnerships
        - Richard Mensah led the development of the AI and Machine learning and Data Analysis component of our software platform.
        """)
        #mark
        st.subheader("Contributions to Gender Diversity")
        st.write("We are committed to championing gender diversity within our team, strongly aligned with the BMWK's objective of enhancing women's presence in start-ups. Our team's foundation is built upon a robust gender balance, as we aim to have 80% of our workforce comprise women. This commitment is a testament to our dedication to fostering an inclusive and innovative environment that not only empowers women but also values diverse perspectives. By leveraging a diverse talent pool, we believe we can drive more comprehensive solutions and contribute significantly to our carbon offset platform's success.")
        #plan
        st.title("Planned Company Structure and Share Distribution")
        st.write("Our company structure is thoughtfully designed to foster seamless collaboration and informed decision-making. Each team member brings a unique set of skills and expertise, contributing to the holistic success of our carbon offset platform.")
        #emmanuel
        st.markdown("""
        - Emmanuel Danso - CEO        
        """)
        st.write("Emmanuel Danso will lead our team as the Chief Executive Officer. With a background in sustainability and business management, Emmanuel's role encompasses providing strategic direction, overseeing overall operations, and leveraging his technical expertise to ensure the platform's success. Emmanuel's dedication to environmental sustainability drives our vision forward.")
        #Githinji
        st.markdown("""
        - Victor Githinji - CTO 
        """)
        st.write("Taking the position of Chief Technical Officer, Victor Githinji will drive our platform's development, user experience enhancements, and technical innovation. Victor's profound understanding of software and product development positions him to lead the technical aspects of our platform, ensuring its functionality and user-friendliness.")
        #Richard
        st.markdown("""
        - Richard Mensah - Head of Data Analytics, AI, Machine Learning Lead        
        """)
        st.write("Richard Mensah is responsible for crucial aspects of data analytics, project verification, and quality assurance, spearheading the development of the AI and Machine Learning components of our software platform. Mustapha's proficiency in Data analysis, Artificial Intelligence equips us to harness advanced technologies that enhance user experience and recommendations.")
        
        
        
        
        
    # Display content for the About Us page

elif selected == "Products":
    st.title("Products")
    
    if st.button("Read Our Products"):
        st.title("Our Prouducts")
        st.write("Our products includes all green house gases and its equivalents, thus CO2e related emissions")
    # Display content for the Products page

# Add a new conditional block for Company's Mission page
elif selected == "Company":
    st.title("Company")
    # Display content for the Company page
    # For instance, a button to navigate to the Company's Mission page
    if st.button("View Company's Market Strategy"):
        st.title("Company's Strategy")
        st.write("Our mission is to provide high qualitty and best carbon emission software to organisations, individuals and the state to calculate their emission and offset them")
        # Here, display detailed information about the company's mission, values, etc.
        st.subheader("Market Entry and Expansion")
        st.write("The culmination of our developmental journey leads us to the market entry stage. Armed with a refined prototype, fortified user engagement, and a comprehensive marketing strategy, we officially introduce our carbon offset platform to the world. This phase not only marks our formal market entry but also signals the beginning of our impact amplification.")
        st.markdown("""
        - Refined Prototype: Introducing our platform armed with a meticulously refined prototype, blending AI, ML, user interfaces, and educational resources.
        - Fortified User Engagement: A vibrant community nurtured through insightful content, interactive workshops, and strategic engagement initiatives.
        - Marketing Symphony: A comprehensive marketing strategy leveraging digital platforms, social media engagement, and strategic partnerships to generate buzz.
        - Impact Amplification: Each carbon offset transaction contributes to a collective effort, showcasing the platform's efficacy and role in shaping a sustainable future.
        - Inception of Growth: Market entry paves the way for expansion in user base and geographical reach, fueling innovations and features in alignment with user needs.
        - Resonating Transformation: Phase 4 crystallizes aspirations into reality, marking the prelude to a symphony of impact that will reverberate for generations.
        """)
        #
        st.title("Towards Subsequent Funding Phases: Envisioning Growth")
        st.subheader("Growth and Scaling")
        st.write("Post-market entry, our trajectory evolves into the growth and scaling phase. Bolstered by user adoption, strategic partnerships, and data-driven insights, we endeavor to expand our reach, broaden our user base, and intensify our environmental impact. This phase necessitates a nimble approach, where scalability, sustainability, and innovation stand as the guiding beacons.")
        st.markdown("""
        - R&D Advancements: Subsequent funding phases empower us to delve into research and development. The infusion of resources enables us to explore technological advancements and innovative features, propelling our offering to new horizons
        - Scaling Operations: With growth, our operational capacity expands. Recruitment, training, and resource augmentation align with the surge in demand and user base.
        - Global Expansion: The journey doesn't halt at local impact. Subsequent funding phases enable us to venture into international markets, amplifying our environmental impact and global footprint.
        """)
        #
        st.subheader("Sustainability")
        st.write("In our pursuit of a greener and more sustainable future, our carbon offset platform stands as an embodiment of commitment to both qualitative and quantitative contributions to the sustainability goals set forth by the federal government. Our strategic alignment with these goals transcends mere compliance, representing a profound dedication to fostering a positive environmental impact.")
        #
        st.subheader("Quantitative Impact: Carbon Mitigation and Reduction")
        st.write("At the heart of our venture lies the quantifiable reduction of carbon footprints. Through our innovative platform, we empower individuals and businesses alike to meticulously measure, understand, and mitigate their carbon emissions. By facilitating tangible reductions in carbon footprints, we align with federal sustainability objectives, specifically those targeting greenhouse gas emission reduction.")
        st.write("Our data-driven insights, fortified by AI and ML algorithms, propel users towards adopting carbon-neutral practices. This confluence of technology and environmental consciousness translates to a measurable decrease in carbon emissions, contributing to the nation's overarching goal of achieving a sustainable carbon footprint reduction.")
        st.write("Our educational resources arm users with knowledge about environmental impact, offering a qualitative avenue to empower individuals. Through this, we're contributing to an informed society that comprehends the implications of carbon emissions on ecosystems, biodiversity, and overall planetary health.")
        st.write("Furthermore, our data analytics empower enterprises to make informed decisions regarding their environmental impact, thereby enhancing energy efficiency, resource allocation, and sustainable practices. These measurable contributions, consolidated across our user base, translate into significant reductions in carbon emissions, aligning impeccably with the government's sustainability benchmarks.")
        #
        st.subheader("Qualitative Contributions: Fostering Environmental Literacy")
        st.write("Beyond mere metrics, our contribution extends to qualitative dimensions that align with the government's holistic sustainability agenda. We recognize that sustainable transformation encompasses informed choices and conscious decisions. Our platform fosters heightened environmental awareness, steering individuals and businesses towards conscious choices. Our comprehensive educational resources empower users with the knowledge to grasp the intricacies of carbon accounting, emission impacts, and eco-friendly practices.")
        st.write("By fostering a culture of environmental literacy, we align with federal objectives to cultivate sustainable behaviors and responsible citizenship. Our qualitative contribution lies in shaping a conscious generation that understands the nuances of environmental responsibility, ultimately leading to a more ecologically aware and environmentally resilient society.")
        #
        st.subheader("Addressing Multidimensional Goals: ESG and Beyond")
        st.write("Our sustainability commitment transcends carbon emissions reduction, extending into the realm of Environmental, Social, and Governance (ESG) practices. By enabling organizations to incorporate ESG considerations into their strategies, we contribute to fostering ethical business practices, social inclusivity, and responsible governance – elements pivotal for holistic sustainability.")
        st.write("Our qualitative and quantitative contributions serve as a testament to our alignment with the federal government's sustainability goals. The combination of informed decision-making, behavioral shifts, and impactful actions underscores our dedication to creating a sustainable future. Through our platform, we not only address environmental concerns but also create a paradigm of collaboration, education, and action that reverberates across society, making the government's sustainability vision a tangible reality.")
        #
        st.subheader("Market/Competition")
        st.markdown("Market situation")
        st.write("The global carbon market has undergone a profound transformation, marked by an extraordinary surge in value. In the year 2022, the market's worth soared by an astounding 13.5 percent, reaching an unprecedented pinnacle of 865 billion euros. This meteoric rise underscores a paradigm shift in environmental consciousness and a resolute commitment towards carbon mitigation on a global scale.")
        #
        st.subheader("Market Volume:")
        st.write("The market's robust valuation of $2 billion attests to its substantial volume and economic significance. It encapsulates diverse entities, spanning from individual consumers aiming to curtail their carbon footprint to corporations striving for sustainable operations. The surge in demand for carbon credits translates into a bustling market segment that spans industries, bridging the gap between environmental consciousness and financial action.")
        #
        st.subheader("Global Carbon Market:")
        st.write("The global carbon market's ascent has been nothing short of remarkable. In 2022 alone, its value surged by an impressive 13.5 percent, catapulting to an unprecedented high of 865 billion euros. This phenomenal growth echoes the increasing recognition of carbon neutrality's imperative and the collective commitment to combatting climate change. Within this expansive market, a multitude of segments coexist, ranging from voluntary carbon offsetting to regulatory compliance mechanisms. These segments mirror the diverse avenues through which individuals and businesses are engaging with carbon reduction efforts.")
        #
        st.subheader("ESG Market on the Rise:")
        st.write("The global ESG (Environmental, Social, and Governance) market follows a similar trajectory of ascendancy. Poised to reach a valuation of 36.4 billion euros in 2023, this market is emblematic of a broader paradigm shift towards conscious and ethical investing. ESG principles are no longer ancillary; they're integral to investment decisions, emphasizing sustainability, social responsibility, and ethical governance.")
        #
        st.subheader("Anticipating Future Growth:")
        st.write("Market growth projections stand as a beacon of opportunity for our platform. The estimated Compound Annual Growth Rate (CAGR) of 6.3% signifies a steady climb, culminating in a projected valuation of US$ 67 billion by the close of 2033. This growth trajectory is not just indicative of increased market demand but also reflects a transformation in societal attitudes towards sustainable practices.")
        
        
        
    

elif selected == "Solutions":
    st.title("Solutions")
    if st.button("Ecotiva's Smart Carbon Solution"):
        st.title(" Ecotiva's Solution")
        st.subheader("Innovation")
        st.write("In the dynamic landscape of carbon offsetting and environmental stewardship, our venture emerges as a beacon of innovation, redefining the contours of sustainable practices. Our innovation narrative is an intricate tapestry woven with threads of technological advancement, knowledge infusion, and strategic implementation.")
        #
        st.subheader("Technology-Driven Transformation")
        st.write("At the heart of our innovation lies a cutting-edge technological ecosystem that redefines the very essence of carbon offset platforms. Our platform leverages state-of-the-art artificial intelligence (AI) and machine learning (ML) algorithms to analyze diverse data streams. This fusion of data-driven intelligence and automation elevates the efficiency and precision of carbon footprint calculations. Furthermore, our AI-driven insights propel users towards personalized offset strategies, enhancing their contributions to environmental preservation.")
        #
        st.subheader("The Power of Knowledge-Based Service")
        st.write("Beyond technological sophistication, our innovation extends to the realm of knowledge-based services. Our platform offers comprehensive educational resources that empower users to comprehend the intricacies of carbon accounting and environmental impact. This knowledge empowers users to make informed choices, fostering a culture of conscious carbon offsetting.")
        #
        st.subheader("Inception to Implementation: An Evolutionary Journey")
        st.write("Our innovation story initiated with meticulous research, intertwined with the wisdom of our dynamic team and insights from revered advisors. This foundation paved the way for a comprehensive blueprint that orchestrates the amalgamation of AI, ML, and data analytics. Presently, our development journey unfolds through a methodical series of iterations, rooted in rigorous testing and refinement. This approach ensures that our platform's functionality aligns seamlessly with our visionary blueprint. As of now, we've transitioned from theoretical frameworks to tangible implementation, yielding functional samples that showcase the potential of our technological paradigm")
        #
        st.subheader("Innovation Unveiled: The Road Ahead")
        st.write("Our innovation narrative is poised for a dynamic future. Scaling our functional samples into a comprehensive prototype is our next stride. We envision a phase of seamless integration, marrying user feedback with AI-driven insights to craft an unparalleled user experience. This blueprint guides us towards a full-scale launch, where our innovation will unfold in all its splendor, fostering a new era of conscious carbon offsetting.")
        #
        st.subheader("Transformation with Purpose: Beyond Carbon Offsetting")
        st.write("Our innovation echoes beyond the contours of carbon offset platforms, epitomizing a seismic shift in environmental awareness. It is the embodiment of technological prowess harmonized with service ethos, converging towards a shared objective – nurturing a sustainable planet. As the chapters of our innovation narrative unfold, it crystallizes the latent potential of technology and knowledge, redefining individual and corporate engagement with their carbon footprint. With each calculated step forward, we catalyze transformation that resonates, uniting technology, knowledge, and service in a harmonious symphony of change.")
        #
        st.subheader("Project planning")
        st.write("In the intricate web of our carbon offset platform's realization, a meticulous project plan serves as our guiding compass. This strategic roadmap encapsulates the trajectory of our venture from its current juncture through the funding period, culminating in market entry or subsequent funding phases. The project plan is a dynamic articulation of our actions, milestones, and aspirations, offering a comprehensive view of our journey toward sustainable impact.")
        #
        st.subheader("Foundation and Ideation")
        st.write("During the early stages, our focus revolves around ideation and conceptualization. This phase encompasses the refinement of our platform's blueprint, drawing from the collective wisdom of our team, advisory network, and university affiliations. Extensive market research and feasibility studies underpin this phase, enabling us to sculpt a robust foundation for our venture.")
        #
        st.subheader("Development and Prototype Creation")
        st.write("As our blueprint takes shape, development comes to the forefront. We channel our innovative ethos into the creation of a functional prototype. This prototype fuses our technological innovation with user-centric design, resulting in a platform that marries cutting-edge AI and ML algorithms with seamless user experience. Rigorous testing and iterations form the crux of this phase, ensuring that our prototype attains the highest standards of quality and usability. Our work plan during this phase is multifaceted, addressing key pillars that underpin our journey.")
        st.markdown("""
        - Developmental Refinement: The funding period sees the transformation of functional samples into a refined prototype. Iterative enhancements are conducted to ensure seamless functionality, user-centric design, and technical precision
        - User Engagement and Feedback Integration: Our engagement with users is instrumental. User feedback is not only solicited but is meticulously integrated into the platform's enhancement. This iterative cycle strengthens our offering's relevance and usability.
        - AI and ML Enhancement: Our platform's AI and ML algorithms are fine-tuned during this phase. The focus lies on enhancing accuracy, predictive capabilities, and personalization, ensuring that users receive insights that are both insightful and actionable.
        - Educational Resource Augmentation: The educational arm of our platform undergoes enrichment. Comprehensive resources are curated to empower users with an in-depth understanding of carbon accounting, environmental impact, and sustainable living.
        - 
        """)
        #
        st.subheader("User Engagement and Iterative Refinement")
        st.write("Upon unveiling our prototype, we enter the realm of user engagement. Feedback loops are established, inviting users to interact with our platform and provide insights. This iterative process, driven by user input, is pivotal in enhancing user experience, streamlining functionality, and fortifying the accuracy of our AI-driven insights. This phase solidifies our commitment to user-centricity and adaptability.")
        st.markdown("""
        - Comprehensive User Testing: Rigorous testing is conducted to validate the platform's readiness for market entry. User scenarios, stress tests, and real-world simulations ensure that every aspect is primed for a flawless user experience.
        - Strategic Alliances and Partnerships: This phase witnesses the cultivation of strategic alliances that bolster our market presence. Partnerships with enterprises, institutions, and environmental organizations amplify our reach and impact.
        - Marketing and Outreach: A comprehensive marketing strategy is deployed to communicate our platform's value proposition. Engaging content, targeted campaigns, and social media initiatives serve as conduits to reach our target audience.
        """)
    
    # Display content for the Solutions page

elif selected == "Emissions":
    st.title("Emissions")
    
    if st.button("Understand Emissions"):
        st.title("Types of Emissions")
        st.write("Emissions are ............................................")
        #adding extra button
        if st.button("type1 emission"):
            st.title("what is type 1 emission")
            st.write("type 1 emissions include the emissions......")
    # Display content for the Emissions page

elif selected == "Scope 1-3":
    st.title("Scope 1-3")
    st.write("Emissions are ............................................")
        #adding extra button
    if st.button("Scope 1"):
        st.title("Scope 1 Emissions")
        st.write("scope emissions include the emissions......")
       
        if st.button("Scope 2"):
            st.title("Scope 2 Emissions")
            st.write("scope emissions include the emissions......")
           
            if st.button("Scope 3"):
                st.title("Scope 3 Emissions")
                st.write("scope emissions include the emissions......")
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
     

    