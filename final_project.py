import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def get_out_sql(sql):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  auth_plugin='mysql_native_password',
                                  )
    cursor = cnx.cursor()
    # query1 = "SELECT * FROM `project 1`.rating"

    sql_output = pd.read_sql(sql, cnx)
    cnx.close()
    return sql_output


# # QUERIES:
#
# # 1. write a query to find the movies with highest avg rating
# query1 = get_out_sql(
#     "select Mov_name , Avg_Rating  from `project 1`.movies where Avg_rating = (select max(Avg_rating) from `project 1`.movies)")
# print(query1)
#
# # 2. Write a query to find no of users in each catergory
#
# query2 = get_out_sql(
#     "select count(user_id) as No_of_users , user_type as User_Type from `project 1`.user group by user_type;")
# print(query2)
#
# #3. Write a query to print full name of the user which have saved their viewing history
#
# query3 = get_out_sql(
#     "select concat(u.First_name ,' ' , u.Last_name) as Full_Name , Date from `project 1`.user u ,`project 1`.viewing_history v where u.user_id=v.user_id order by u.First_name ")
# print(query3)
#
# #4 Write a query to print the movies which were released between 1991 to 2002
# query4 = get_out_sql(
#     "SELECT Mov_name , Releasing_year FROM `project 1`.movies WHERE Releasing_year between 1991 AND 2002 order by Releasing_year;")
# print(query4)
#
# #5 Write a Query to print the name of movies which have avg rating more than 7 and genre is thriller
# query5 = get_out_sql(
#     "select Mov_name from `project 1`.movies where Avg_rating > 7 And Genre = 'Thriller' ;")
# print(query5)


#VISUALIZATION

#1. Visualizing Rating to see the frequency
ratings=get_out_sql("SELECT * FROM `project 1`.rating")
# plot graph of 'ratings' column
plt.figure(figsize=(10, 4))
plt.xlabel("Rating")
plt.ylabel("Frequency")
ratings['Rating'].hist(bins=20)
plt.show()

#2. Making Word cloud of Genre
movie_genre = get_out_sql("SELECT Genre from `project 1`.movies")
print(movie_genre.head(20))

comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
for val in movie_genre.Genre:

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split()

    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(6, 8), facecolor=None)
plt.imshow(wordcloud , interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
# plt.show()

#3 Visualizing through histogram to total number of users in each category
user_type1 = get_out_sql("SELECT User_type from `project 1`.user")
print(user_type1.head(20))
plt.figure(figsize=(10, 4))
plt.xlabel("User_Type")
plt.ylabel("Frequency")
user_type1['User_type'].hist(bins=20)
plt.show()

#4. word cloud of name of movies
movies=get_out_sql("SELECT Mov_name from `project 1`.movies")
print(movies.head())

comment_words = ''
stopwords = set(STOPWORDS)

#iterate through the csv file
for val in movies.Mov_name:

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split()

    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(6, 8), facecolor=None)
plt.imshow(wordcloud , interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

