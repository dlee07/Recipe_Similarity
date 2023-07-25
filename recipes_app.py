import streamlit as st
import streamlit.web.cli as stcli
import pandas as pd
import numpy as np

def display_recipe_table(df):
    st.write("## Recipe Similarity Table")
    st.dataframe(df, width=5600)

def main():
    # Replace 'your_recipe_data.xlsx' with the actual path to your Excel file
    recipe_df = pd.read_excel('/Users/chaniel/Desktop/data_recipes_similarity.xlsx', index_col=0)
    pd.set_option('display.max_colwidth', None)
    recipe_df.columns = np.array(['Recipe 1', 'Recipe 2', 'Recipe 3', 'Recipe 4', 'Recipe 5'])
    selected_recipes = st.multiselect("Select up to 3 recipes:", recipe_df.index, default=[])
    filtered_df = recipe_df.loc[selected_recipes]

    display_recipe_table(filtered_df.T)

if __name__ == "__main__":
    main()
