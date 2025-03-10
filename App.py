import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def convert_to(value):
    value = str(value).split('/')
    return value[0]

def main():
    st.title("Zomato Data Analysis")
    
    # Upload dataset
    uploaded_file = st.file_uploader("Upload Zomato Dataset (CSV)", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Data Cleaning
        df['rate'] = df['rate'].apply(convert_to)
        
        st.subheader("Data Overview")
        st.write(df.head())
        
        # Visualization 1: Countplot for Restaurant Type
        st.subheader("Restaurant Type Distribution")
        fig, ax = plt.subplots()
        sb.countplot(x=df['listed_in(type)'], ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
        # Visualization 2: Votes by Restaurant Type
        st.subheader("Votes by Restaurant Type")
        grouped_data = df.groupby('listed_in(type)')['votes'].sum()
        fig, ax = plt.subplots()
        ax.plot(grouped_data, marker='o', color='green')
        plt.xlabel('Type of Restaurant')
        plt.ylabel('Votes')
        st.pyplot(fig)
        
        # Max Votes
        max_votes = df['votes'].max()
        res_with_max_votes = df.loc[df['votes'] == max_votes, 'name'].values[0]
        st.subheader("Restaurant with Maximum Votes")
        st.write(f"{res_with_max_votes} with {max_votes} votes")
        
        # Visualization 3: Online Orders
        st.subheader("Online Order Distribution")
        fig, ax = plt.subplots()
        sb.countplot(x=df['online_order'], ax=ax)
        st.pyplot(fig)
        
        # Visualization 4: Rating Distribution
        st.subheader("Rating Distribution")
        fig, ax = plt.subplots()
        plt.hist(df['rate'], bins=5)
        plt.title('Rating Distributions')
        st.pyplot(fig)
        
        # Visualization 5: Cost for Two People
        st.subheader("Cost for Two People Distribution")
        fig, ax = plt.subplots()
        sb.countplot(x=df['approx_cost(for two people)'], ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
        # Visualization 6: Boxplot of Online Order vs Rating
        st.subheader("Online Order vs Rating")
        fig, ax = plt.subplots()
        sb.boxplot(x='online_order', y='rate', data=df, ax=ax)
        st.pyplot(fig)
        
        # Heatmap
        st.subheader("Heatmap of Online Order vs Restaurant Type")
        pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
        fig, ax = plt.subplots()
        sb.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d', ax=ax)
        st.pyplot(fig)
    else:
        st.write("Please upload a CSV file to continue.")

if __name__ == "__main__":
    main()
