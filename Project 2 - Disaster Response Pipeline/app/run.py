import json
import plotly
import plotly.express as px
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request

import joblib
from sqlalchemy import create_engine

app = Flask(__name__)


def tokenize(text):
    print('tokenize...')
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('Message', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    graphs = []
    
    # Graph 1) Messages per category
    df_categories = pd.DataFrame(df.iloc[:, 5:].sum())
    df_categories.rename(columns={0:'count'}, inplace=True)
         
    fig = px.bar(df_categories, x=df_categories.index, y='count',
             title="Messages per category",
             labels={'index':'Message Category',
                       'count': 'Number of Messages'},
            color_discrete_sequence=px.colors.qualitative.Bold)
    graphs.append(fig.to_plotly_json())
    
    # Graph 2) Message genres by category
    df_category_genre = df.iloc[:, 4:].groupby(by=['genre']).sum().T
    fig = px.bar(df_category_genre, x=df_category_genre.index, y=['direct', 'news', 'social'],
             title="Message Genres by Category",
            labels={'index':'Category', 'value': 'Number of Messages', 'variable': 'Genre'},
            color_discrete_sequence=px.colors.qualitative.Bold)
    graphs.append(fig.to_plotly_json())
    
    # Graph 3) Proportion of message genres by category
    df_category_genre['overall'] = df_category_genre['direct'] + df_category_genre['news'] + df_category_genre['social']
    df_category_genre_normed = pd.DataFrame()
    df_category_genre_normed['direct'] = df_category_genre['direct'] / df_category_genre['overall'] * 100
    df_category_genre_normed['news'] = df_category_genre['news'] / df_category_genre['overall'] * 100
    df_category_genre_normed['social'] = df_category_genre['social'] / df_category_genre['overall'] * 100
    df_category_genre_normed
    fig = px.bar(df_category_genre_normed, x=df_category_genre_normed.index, y=['direct', 'news', 'social'],
             title="Proportion of Message Genres by Category",
            labels={'index':'Category', 'value': 'Proportion of Messages in %', 'variable': 'Genre'},
             color_discrete_sequence=px.colors.qualitative.Bold)
    graphs.append(fig.to_plotly_json())
    
    # Graph 4) Number of categories per messasge
    df_cat_per_message = pd.DataFrame()
    df_cat_per_message['Number of categories'] = df.iloc[:, 5:].sum(axis=1)
    fig = px.histogram(df_cat_per_message, x='Number of categories', labels={'count':'Number of Messages'},
            color_discrete_sequence=px.colors.qualitative.Bold)
    graphs.append(fig.to_plotly_json())
    
    # Graph 5) Number of messages per genre
    df_genres = df.groupby(by='genre').count()
    fig = px.bar(df_genres, x=df_genres.index, y='index', labels={'x':'Message Genre', 'index': 'Number of Messages'},
            color_discrete_sequence=px.colors.qualitative.Bold,
            width=400, height=400)
    graphs.append(fig.to_plotly_json())
      
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print('graphJSON:')
    print(graphJSON)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
