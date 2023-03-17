import streamlit 

streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast favorites')
streamlit.text('🥣 Omega 3 and Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('🥣 Omega 3 and Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-RanBreakfast favoritesge Egg')
streamlit.text('🥑🍞 Avocado Toast')


# -----------------------------------------------------------------------------------------------------------
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# -----------------------------------------------------------------------------------------------------------
# Nous souhaitons réaliser un filtre sur la liste des fruits et ne proposer que les fruits le splus populaires 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])


# -----------------------------------------------------------------------------------------------------------
# Nous allons rendre le tableau plus intélligent 
# de façon à ce qu'il ne filtre que sur les fruits qui sont de;qnés (selectionnés)
# pour se faire : We'll ask our app to put the list of selected fruits into a variable called fruits_selected. 
# Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set 
# (and assign that data to a variable called fruits_to_show).
# Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page. 






