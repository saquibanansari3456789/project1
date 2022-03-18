import streamlit as st
import pickle

model = pickle.load(open('RF_Price_Predection_model.pkl', 'rb'))


def main():
    string = "Car Price Predector"
    st.title("Car Price Predector 🚗")
    # st.set_page_config(page_title=string)
    st.markdown(
        "#### Are you plaining to sell your car !?\n #### Try to evaluate the price")
    st.image(
        "https://imgd.aeplcdn.com/0x0/n/cw/ec/27032/s60-exterior-right-front-three-quarter-3.jpeg",
        width=400,  # Manually Adjust the width of the image as per requirement
    )

    st.write('')
    st.write('')

    # Get input years
    years = st.number_input(
        "In which year car was purchased ?", 1990, 2021, step=1, key='year')
    Years_old = 2021 - years

    # Get pressent price
    Present_Price = st.number_input(
        "current ex-showroom price of the car ?  (In ₹lakhs)", 0.00, 50.00, step=0.05, key='Preseny_Price')

    # KMS car driven
    KMS_Driven = st.number_input(
        'How much ccar driven in kelometers', key='KMS_Driven')

    # Getting no of owners
    Owner = st.radio(
        'The number of owners the car had previously ?', (1, 2, 3), key='Owner')

    # Get Fuel type
    Fuel_Type = st.selectbox(
        'What is the fuel type of the car ?', ('Petrol', 'Diesel', 'CNG'), key='fuel')

    # Checking fuel type
    if(Fuel_Type == 'Petrol'):
        Fuel_Type_Petrol = 1
        Fuel_Type_Diesel = 0
    elif(Fuel_Type == 'Diseal'):
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 1
    else:
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 0

    # Get seller type
    Seller_Type = st.selectbox(
        'Are you a de aler or an individual ?', ('Dealer', 'Individual'), key='dealer')
    # Checking seller type
    if(Seller_Type == 'Individual'):
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0

    # Transmition type
    Transmission_Mannual = st.selectbox(
        'What is the Transmission Type ?', ('Manual', 'Automatic'), key='manual')
    # Checking transmition type
    if(Transmission_Mannual == 'Mannual'):
        Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0

    if st.button('Estimate Price', key='Predict'):
        try:
            Model = model
            # Providing data to our model
            prediction = Model.predict([[Present_Price, KMS_Driven, Owner, Years_old, Fuel_Type_Diesel,
                                       Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            # Final output of our model
            output = round(prediction[0], 2)
            if output < 0:
                st.warning("This car can't be sell !!")
            else:
                st.success(
                    'You can sell this car for {} Lakhs  🙌' . format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")


if __name__ == '__main__':
    main()
