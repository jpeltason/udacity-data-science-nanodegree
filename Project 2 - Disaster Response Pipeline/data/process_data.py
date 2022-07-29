import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    # Load data and merge into one df
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    return messages.merge(categories, on='id')
    
def clean_data(df):
    # Handle column names
    # Split categories into separate columns, value of the columns will be e.g. 'related-1'
    categories_df = pd.DataFrame(df['categories'].str.split(';', expand=True))
    # Select first row and extract a list of new column names for categories by stripping the '-1' or '-0'
    row = categories_df.iloc[0]
    category_colnames = row.apply(lambda x: x[:len(x)-2]).values
    # rename the columns of `categories`
    categories_df.columns = category_colnames
 
    # Handle column values, convert e.g. 'related-1' to '1'
    for column in categories_df:
        # set each value to be the last character of the string
        col_str = categories_df[column].str.split("-").str.get(1)
    
        # convert column from string to numeric
        categories_df[column] = pd.to_numeric(col_str)

    # Drop original 'categories' column, replace with new 'categories_df'
    df = df.drop(columns='categories')
    df = df.join(categories_df, on='id')
    
    # For category 'related' the original dataset contained some entries with value 'related-2'
    # This value is invalid, replace by 1 
    df['related'].replace(2, 1, inplace=True) 
    
    # Drop duplicates
    return df.drop_duplicates(subset='message')


def save_data(df, database_filename):
    engine = create_engine('sqlite:///' + database_filename + '.db')
    df.to_sql(database_filename, engine, index=False)  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()