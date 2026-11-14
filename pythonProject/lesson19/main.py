
import pandas as pd
import streamlit as st



books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Best selling Books")
st.write("this app analyzes the amazon top selling books from 2009 to 2022")

st.sidebar.header("Add new book data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("User Rating",0.0,5.0,0.0,0.1)
    new_reviews = st.number_input("Reviews",min_value=0, step=1)
    new_price = st.number_input("Price",min_value=0,step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2022, step=1)
    new_genre = st.selectbox("Genre", books_df["Genre"].unique())


    submit_button = st.form_submit_button(label="Add Book")

    if submit_button:
        new_data={
            "Name": new_name,
            "Author":new_author,
            "User Rating":new_user_rating,
            "Reviews":new_reviews,
            "Price":new_price,
            "Year":new_year,
            "Genre":new_genre
        }
        books_df = pd.concat([pd.DataFrame(new_data,index=[0]),books_df],ignore_index=True)
        books_df.to_csv("bestsellers_with_categories_2022_03_27.csv",index=False)
        st.sidebar.success("New book added successfully")




st.sidebar.header("Filter Options")
selected_author = st.sidebar.selectbox("Selected Author",["All"] + list(books_df["Author"].unique()))
selected_year = st.sidebar.selectbox("Selected Year",["All"] + list(books_df["Year"].unique()))
selected_genre = st.sidebar.selectbox("Selected Genre",["All"] + list(books_df["Genre"].unique()))


filtred_books_df = books_df.copy()

if selected_author !="All":
    filtred_books_df = filtred_books_df[filtred_books_df["Author"]==selected_author]

if selected_year !="All":
    filtred_books_df = filtred_books_df[filtred_books_df["Year"]==selected_year]

if selected_genre !="All":
    filtred_books_df = filtred_books_df[filtred_books_df["Genre"]==selected_genre]

st.subheader("Summary statistic")

total_books = filtred_books_df.shape[0]
unique_titles = filtred_books_df["Name"].nunique()


col1,col2 = st.columns(2)

col1.metric("Total books",total_books)
col2.metric("Unique titles",unique_titles)


