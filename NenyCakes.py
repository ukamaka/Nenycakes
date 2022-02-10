import streamlit as st

from PIL import Image


img = Image.open("Nenycakes.png")
 
st.image(img, width=300)

st.title("Welcome to NenyCakes!")


st.text("Dear Customer kindly look through the menu options and Order:")



Type_of_cake = st.radio("Select: ", ('Birthday Cake', 'Wedding Cake', 'Plain Cakes', 'Pastries'))

if (Type_of_cake == 'Birthday Cake'):
    st.success("Birthday Cake") 
if (Type_of_cake == 'Wedding Cake'):
    st.success("Wedding Cake")   
if (Type_of_cake == 'Plain Cakes'):
    st.success("Plain Cakes") 
if (Type_of_cake == 'Pastries'):
    st.success("Pastries") 

             
if (Type_of_cake == 'Birthday Cake'):
    cake = st.selectbox("Select Option: ",
                     ['8 inches Butter cream cake', '8 inches Whipped cream cake', '8 inches Fondant cake'])
if (Type_of_cake == 'Wedding Cake'):
    cake = st.selectbox("Select Option: ",
                     ['Two tier Princess cake', 'Two tier Castle cake', 'Two tier Flowery cake'])
if (Type_of_cake == 'Plain Cakes'):
    cake = st.selectbox("Select Option: ",
                     ['Fudged Chocolate cake', 'Carrot cake', 'Banana cake', 'Fruit Cake', 'Red velvet cake'])
if (Type_of_cake == 'Pastries'):
    cake = st.selectbox("Select Option: ",
                     ['Meatpie', 'Chicken pie', 'Doughnut', 'Samosa', 'Spring Roll'])
 
st.text("NB: Birthday cake costs $50 each,Wedding cake costs $100 each, plain cakes cost $23 each and pastries cost $4 each")

cake_item = {} 
cake_history = [] 

cake_name = st.text_input("Order Option:\n", cake)

quantity = st.number_input("Quantity needed:\n")

cost = st.number_input("Kindly input the cost of the item:\n")

cake_item = {'name': cake_name, 'number': int(quantity), 'price': float(cost)} 
cake_history.append(cake_item) 

grand_total = 0  

for index, cake in enumerate(cake_history):
    cake_total = cake['number'] * cake['price']
    grand_total = grand_total + cake_total
    ('%d %s @ $%.1f Sub_Total $%.1f' % (cake['number'], cake['name'],  cake['price'], cake_total)) 
    
    
st.text("Please find below the total cost of your  order:")   

st.write('grand total: $%.1f' % grand_total)
         

Payment = st.selectbox("Kindly select a payment method: ",
                     ['Bank Transfer', 'USDT TRC-20'])
if (Payment == 'Bank Transfer'):
    st.text("Kindly make a transfer to 12345678, Golden Bank")
else:
    st.text("Kindly make a transfer to wallet address: TAT18LshdyDhhygTYhgsbUjy9")

Payment_status = st.radio ("Have you made the payment", ('Yes', 'No' ))

if (Payment_status == 'Yes'):
    st.text('Your order will be processed ASAP')
    
           
else:
    st.text('Your order cannot be processed until payment is made')    
    
date = st.date_input("Select Delivery date:")


name = st.text_input("Enter Your name, delivery address and phone number:", "Type Here ...")
 

if(st.button('Submit')):
        result = name.title()
        st.success(result)
st.text("Kindly note that delivery incurs extra cost of $4")

level = st.select_slider('How would you rate our services?', ['Bad', 'Fair', 'Very Satisfied'])
 

st.text('Selected: {}'.format(level))

if (level == 'Bad'):
         Feedback = st.text_input("Kindly tell us what you did not like:", "Type Here ...")

    
st.text("Thank you for choosing NenyCakes, your satisfaction is our priority!")
