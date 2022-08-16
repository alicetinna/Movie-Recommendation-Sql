use `Project 1`;
#select Mov_name , Avg_Rating from movies
#where Avg_rating = (select max(Avg_rating) from movies) ;

#select count(user_id) as No_of_users , user_type as User_Type from user
#group by user_type;

#select concat(u.First_name ,' ' , u.Last_name) as Full_Name from user u ,viewing_history v
#where u.user_id=v.user_id
#order by u.First_name 

select * from movies;
#SELECT Mov_name , Releasing_year FROM movies WHERE
#Releasing_year between 1991 AND 2002
#order by Releasing_year;

select Mov_name from `project 1`.movies
where Avg_rating between 7 and 9
And Genre = "Thriller" ;




