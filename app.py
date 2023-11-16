import streamlit as st
import pandas as pd
import pymongo

uri = "mongodb+srv://tutorial-1:Tsh7212012@cluster0.oomvsot.mongodb.net/?retryWrites=true&w=majority"
client =pymongo.MongoClient(uri)
db = client["todo"]
collection =db["task"]

############################## App Setting ##############################
categories = ['home', 'work', 'school']

############################## UI ##############################
st.title('TODO APP')
st.write('this is a todo list,which allows you to read,insert,edit,delete')
# st.text_input('Enter your task here')
# st.selectbox('category',categories)
# # Add a selectbox to select actions:

# st.slider('importance',0,10,1)
# st.table([{'name':'peter','age':'25'},{'name':'mary','age':'29'}])

# # Add a selectbox to select actions:
# page = st.sidebar.selectbox('Menu',['home','insert','edit','delete'])
 


# if page == 'insert':
#   st.header('insert task')
# task = st.text_input('task')
# category = st.selectbox('category',['work','personal'])
# st.button('insert')
# if st.button('insert'):
#    collection.insert_one({'task':task,'category':category})
#      st.success('successfully inserted')
# else page == 'edit'
#     st.header('edit task')
# elif page == 'delete'
#     st.header('delete task')
# elif page == 'home'
#     st.header('home')
#     tasks = collection.find({},{'_id':0}) #不看id
#     st.table(tasks)
page = st.sidebar.selectbox('menu',['home','insert','delete','edit'])
if page == 'insert':
    st.header('insert task')
    task = st.text_input('Task')
    category =st.selectbox('category',['work','personal'])
    if st.button('insert'):
      collection.insert_one({'task':task,'category':category})
      st.success('successfully inserted')
elif page =='home':
    st.header('home') 
    tasks = collection.find({},{'_id':0})
    st.table(tasks)
elif page =='delete':
    st.header('delete task')
elif page =='edit':
    st.header('edit task')
