import streamlit as st

Emission_Factors = {
    "India" :{
        "Transportation" : 0.142, #kgCO2/-km
        "Electricity" : 0.82, #kgCO2/kWh
        "Diet": 1.25, #kgCO2/meal
        "Waste": 0.5, #kgCO2/kg
        
    }
}

st.set_page_config(page_title="Carbon Calculator", page_icon=":earth_asia:", layout="wide")
st.title("Carbon Calculator")

#inputs
st.subheader("Your Country")

country = st.selectbox("Select your country", ["India"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗Daily Compute Distance")
    distance = st.slider("Enter the distance you travel daily", 0.0, 100.0, key = "distance_input")
    
    st.subheader("⚡Monthly Electricity Consumption (kWh)")
    electricity = st.slider("Electricity imput", 0.0, 2000.0, key = "electricity_input")

with col2:
    st.subheader("🗑️Waste generated/week (kg)")
    waste = st.slider("Enter the Waste", 0.0, 100.0, key = "waste_input")
    
    st.subheader("🍲Meals per day")
    meals = st.number_input("Meals/day", 0, key = "meals_input")
    
    
if distance>0:
    distance = distance*365 #convert distance to km/year
    
if electricity>0:
    electricity = electricity*12 #convert electricity to kWh/year
    
if waste>0:
    waste= waste * 52 #convert distance to km/year
    
if meals>0:
    meals = meals * 365 #convert distance to km/year
    
#calculations

transport_emission = distance * Emission_Factors[country]["Transportation"]
electricity_emission = electricity * Emission_Factors[country]["Electricity"]  
meals_emission = meals * Emission_Factors[country]["Diet"]
waste_emission = waste * Emission_Factors[country]["Waste"]

transport_emission = round(transport_emission /1000, 2)
electricity_emission = round(electricity_emission /1000, 2)
meals_emission = round(meals_emission /1000, 2)
waste_emission = round(waste_emission /1000, 2)



    
total_emission = round (
    transport_emission + electricity_emission + meals_emission + waste_emission
    )

if st.button("Calculate Emission"):
    st.subheader("Your Carbon Footprint is")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Emission By categories")
        st.info(f"🚗Transportation: {transport_emission} tones co2/year")
        st.info(f"⚡Electricity: {electricity_emission} tones co2/year")
        st.info(f"🍲Meals: {meals_emission} tones co2/year")
        st.info(f"🗑️Waste: {waste_emission} tones co2/year")
        
    with col4:
        st.subheader("Total Emission")
        st.info(f" Your Total Emission is : {total_emission} tones co2/year")
        st.warning("Co2 Emission per capita in india is 1.9 tones/year, the increasing rate of emission is alarming its about 9.41%")
    

