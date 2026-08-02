import numpy as np  #linear Algebra operations
import pandas as pd  #For Data Preparation
import plotly.express as px  #used for data visualization
from textblob import TextBlob  #used for sentiment analysis
import plotly.io as pio

pio.renderers.default = "browser"

df = pd.read_csv('netflix_titles.csv.zip')


# ### Checking number of rows and columns in data

# In[2]:

def dataset_shape():
    print(df.shape)


# ### Checking content available in Dataset

# In[3]:

def dataset_head():
    print(df.head())


# ### Checking columns name of Dataset

# In[4]:

def dataset_columns():
    print(df.columns)


# ### Taking the count of ratings available

# In[5]:

def show_content_rating_pie():
    x = df.groupby(['rating']).size().reset_index(name = 'counts')
    print(x)


    # ### Creating piechart based on content rating

    # In[6]:


    pieChart = px.pie(x, values='counts', names='rating', title='Distribution of content ratings on Netflix')
    pieChart.show()


# # Analyzing the top 5 directors on Netflix

# In[9]:

def clean_data():
    global df
    df['director'] = df['director'].fillna('Director not specified')
    df['cast'] = df['cast'].fillna('Cast not specified')
    df['country'] = df['country'].fillna('Country not specified')
    print(df.head())


# In[10]:

def show_top5_directors():
    directors_list = pd.DataFrame()
    print(directors_list)


# In[11]:


    directors_list = df['director'].str.split(',', expand=True).stack()
    print(directors_list)


# In[12]:


    directors_list = directors_list.to_frame()
    print(directors_list)


# In[13]:


    directors_list.columns = ['Director']
    print(directors_list)


# In[20]:


    directors = directors_list.groupby(['Director']).size().reset_index(name='Total Count')
    print(directors)


# In[22]:


    directors = directors[directors.Director != 'Director not specified']
    print(directors)


# In[23]:


    directors = directors.sort_values(by=['Total Count'],ascending=False)
    print(directors)


# In[24]:


    top5_directors = directors.head()
    print(top5_directors)


# In[26]:


    top5_directors = top5_directors.sort_values(by=['Total Count'])
    barChart = px.bar(top5_directors, x='Total Count', y='Director', title='Top 5 Directors on Netflix')
    barChart.show()


# # Analyzing the Top 5 actors on Netflix

# In[5]:

def show_top5_actors():
    cast_df = pd.DataFrame()
    cast_df = df['cast'].str.split(',',expand=True).stack()
    cast_df = cast_df.to_frame()
    cast_df.columns = ['Actor']
    actors = cast_df.groupby(['Actor']).size().reset_index(name = 'Total Count')
    actors = actors[actors.Actor != 'Cast not specified']
    actors = actors.sort_values(by=['Total Count'],ascending=False)
    top5_actors = actors.head()
    top5_actors = top5_actors.sort_values(by=['Total Count'])
    barChart2 = px.bar(top5_actors, x='Total Count', y='Actor', title='Top 5 actors on Netflix')
    barChart2.show()


# # Analyzing the content produced on Netflix based on years

# In[7]:

def show_content_trend():
    df1 = df[['type', 'release_year']]
    df1 = df1.rename(columns = {"release_year":"Release Year", "type":"Type"})
    df2 = df1.groupby(['Release Year','Type']).size().reset_index(name = "Total Count")


# In[8]:


    print(df2)


# In[10]:


    df2 = df2[df2['Release Year']>=2000]
    graph = px.line(df2, x = "Release Year", y = "Total Count", color = "Type",
                title = "Trend of content produced on Netflix every year")
    graph.show()


# # Sentiment Analysis of Netflix Content

# In[15]:

def show_sentiment_analysis():
    df3 = df[['release_year', 'description']]
    df3 = df3.rename(columns = {'release_year':'Release Year', 'description':'Description'})
    for index,row in df3.iterrows():
        d = row['Description']
        testimonial = TextBlob(d)
        p = testimonial.sentiment.polarity
        if p==0:
            sent = 'Neutral'
        elif p>0:
            sent = 'Positive'
        else:
            sent = 'Negative'
        df3.loc[index, 'Sentiment'] = sent
    df3 = df3.groupby(['Release Year','Sentiment']).size().reset_index(name = 'Total Count')

    df3 = df3[df3['Release Year']>2005]
    barGraph = px.bar(df3, x="Release Year", y="Total Count", color="Sentiment", title="Sentiment Analysis of Content on Netflix")
    barGraph.show()

# ==========================================================
# Top 5 Countries Analysis
# ==========================================================

def show_top5_countries():

    # Split countries separated by commas
    country_df = pd.DataFrame()

    country_df = df['country'].str.split(',', expand=True).stack()

    country_df = country_df.to_frame()

    country_df.columns = ['Country']

    # Remove extra spaces
    country_df['Country'] = country_df['Country'].str.strip()

    # Count occurrences
    countries = country_df.groupby(['Country']).size().reset_index(name='Total Count')

    # Remove missing values
    countries = countries[countries.Country != 'Country not specified']

    # Sort in descending order
    countries = countries.sort_values(by='Total Count', ascending=False)

    # Select top 5
    top5_countries = countries.head()

    # Sort for better horizontal bar chart
    top5_countries = top5_countries.sort_values(by='Total Count')

    # Plot graph
    barChart = px.bar(
        top5_countries,
        x='Total Count',
        y='Country',
        title='Top 5 Countries Producing Netflix Content'
    )

    barChart.show()


def main():

    clean_data()

    dataset_shape()

    dataset_head()

    dataset_columns()

    # Uncomment any graph if you want to test it

    # show_content_rating_pie()
    # show_top5_directors()
    # show_top5_actors()
    # show_top5_countries()
    # show_content_trend()
    # show_sentiment_analysis()
if __name__ == "__main__":
    main()