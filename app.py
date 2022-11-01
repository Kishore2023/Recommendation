import streamlit as st
import pickle
import pandas as pd

st.title('Food Recommendation')

#breakfast = pd.read_excel("C:\\Users\\gan8k\\OneDrive - Contoso\\Documents\\Kishore - Personal\\Data Science\\Recommendation Engine Project\\Github1- Streamlit\\Dataset\\BreakfastVeg.xlsx")
#pickle.dump(breakfast, open('BreakfastVeg.pkl','wb'))
breakfast_list = pickle.load(open('BreakfastVeg.pkl','rb'))
Orderbreakfast = pd.DataFrame(breakfast_list)


#lunch = pd.read_excel("C:\\Users\\gan8k\\OneDrive - Contoso\\Documents\\Kishore - Personal\\Data Science\\Recommendation Engine Project\\Github1- Streamlit\\Dataset\\LunchVeg.xlsx")
#pickle.dump(lunch, open('LunchVeg.pkl','wb'))
lunch_list = pickle.load(open('LunchVeg.pkl','rb'))
Orderlunch = pd.DataFrame(lunch_list)

#dinner = pd.read_excel("C:\\Users\\gan8k\\OneDrive - Contoso\\Documents\\Kishore - Personal\\Data Science\\Recommendation Engine Project\\Github1- Streamlit\\Dataset\\DinnerVeg.xlsx")
#pickle.dump(dinner, open('DinnerVeg.pkl','wb'))
dinner_list = pickle.load(open('DinnerVeg.pkl','rb'))
Orderdinner = pd.DataFrame(dinner_list)

#-------------------------------

#breakfastNV = pd.read_excel("C:\\Users\\gan8k\\OneDrive - Contoso\\Documents\\Kishore - Personal\\Data Science\\Recommendation Engine Project\\Github1- Streamlit\\Dataset\\BreakfastNV.xlsx")
#pickle.dump(breakfastNV, open('BreakfastNV.pkl','wb'))
breakfastNV_list = pickle.load(open('BreakfastNV.pkl','rb'))
OrderbreakfastNV = pd.DataFrame(breakfastNV_list)

#lunchNV = pd.read_excel("C:\\Users\\gan8k\\OneDrive - Contoso\\Documents\\Kishore - Personal\\Data Science\\Recommendation Engine Project\\Github1- Streamlit\\Dataset\\LunchNV.xlsx")
#pickle.dump(lunchNV, open('LunchNV.pkl','wb'))
lunchNV_list = pickle.load(open('LunchNV.pkl','rb'))
OrderlunchNV = pd.DataFrame(lunchNV_list)

#dinnerNV = pd.read_excel("C:\\Users\\gan8k\\OneDrive - Contoso\\Documents\\Kishore - Personal\\Data Science\\Recommendation Engine Project\\Github1- Streamlit\\Dataset\\DinnerNV.xlsx")
#pickle.dump(dinnerNV, open('DinnerNV.pkl','wb'))
dinnerNV_list = pickle.load(open('DinnerNV.pkl','rb'))
OrderdinnerNV = pd.DataFrame(dinnerNV_list)

#------------------------------------------------------------------------

#breakfastBoth = pd.read_excel("C:\\Users\\gan8k\\OneDrive - Contoso\\Documents\\Kishore - Personal\\Data Science\\Recommendation Engine Project\\Github1- Streamlit\\Dataset\\BreakfastBoth.xlsx")
#pickle.dump(breakfastBoth, open('BreakfastBoth.pkl','wb'))
breakfastBoth_list = pickle.load(open('BreakfastBoth.pkl','rb'))
OrderbreakfastBoth = pd.DataFrame(breakfastBoth_list)

#lunchBoth = pd.read_excel("C:\\Users\\gan8k\\OneDrive - Contoso\\Documents\\Kishore - Personal\\Data Science\\Recommendation Engine Project\\Github1- Streamlit\\Dataset\\LunchBoth.xlsx")
#pickle.dump(lunchBoth, open('LunchBoth.pkl','wb'))
lunchBoth_list = pickle.load(open('LunchBoth.pkl','rb'))
OrderlunchBoth = pd.DataFrame(lunchBoth_list)

#dinnerBoth = pd.read_excel("C:\\Users\\gan8k\\OneDrive - Contoso\\Documents\\Kishore - Personal\\Data Science\\Recommendation Engine Project\\Github1- Streamlit\\Dataset\\DinnerBoth.xlsx")
#pickle.dump(dinnerBoth, open('DinnerBoth.pkl','wb'))
dinnerBoth_list = pickle.load(open('DinnerBoth.pkl','rb'))
OrderdinnerBoth = pd.DataFrame(dinnerBoth_list)

#--------------------------------------------------------------
food_list = pickle.load(open('Order1.pkl','rb'))
#food_list = food_list['Order1'].values
data = pd.DataFrame(food_list)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(food):
    food_index = data[data["Order1"] == food].index[13]
    distances = similarity[food_index]
    food_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:11] 

    recommended_foods= []
    for i in food_list:
        recommended_foods.append(data.iloc[i[13]].Order1)
    return recommended_foods
    

meal_type = st.selectbox('Select Meal Type',('Select Meal Type','Breakfast','Lunch','Dinner'))
Variety = st.selectbox('Choose Veg or Non-Veg or Both', ('Select','Vegetarian','NonVegetarian', 'Both'))

if meal_type is ('Breakfast') and Variety is('Vegetarian'):
    food_break = Orderbreakfast.Order1
    for i in food_break:
        st.write(i)

if meal_type is ('Lunch') and Variety is('Vegetarian'):
    food_break1 = Orderlunch.Order1
    for i in food_break1:
        st.write(i)
        
if meal_type is ('Dinner') and Variety is('Vegetarian'):
    food_break2 = Orderdinner.Order1
    for i in food_break2:
        st.write(i)        
        
if meal_type is ('Breakfast') and Variety is('NonVegetarian'):
    food_break3 = OrderbreakfastNV.Order1
    for i in food_break3:
        st.write(i)

if meal_type is ('Lunch') and Variety is('NonVegetarian'):
    food_break4 = OrderlunchNV.Order1
    for i in food_break4:
        st.write(i)
        
if meal_type is ('Dinner') and Variety is('NonVegetarian'):
    food_break5 = OrderdinnerNV.Order1
    for i in food_break5:
        st.write(i)         

if meal_type is ('Breakfast') and Variety is('Both'):
    food_break6 = OrderbreakfastBoth.Order1
    for i in food_break6:
        st.write(i)

if meal_type is ('Lunch') and Variety is('Both'):
    food_break7 = OrderlunchBoth.Order1
    for i in food_break7:
        st.write(i)
        
if meal_type is ('Dinner') and Variety is('Both'):
    food_break8 = OrderdinnerBoth.Order1
    for i in food_break8:
        st.write(i)        


selected_food = st.selectbox('What would you like to Order?', food_list)
if st.button('Recommend'):
    recommendations = recommend(selected_food)
    st.subheader("Also try this")
    for i in recommendations:
        st.write(i)
