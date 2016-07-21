-- get avg rating
select avg(rating) from Review; 

-- give new review
INSERT INTO Review 
(
    title,
    comment,
    rating,
    username
)
VALUES
(

);

-- view review
select review_ID, title, comment, rating, username from Review;

-- check movie status if the user already watched the movie
   select status
     from Order_info as o
left join Movie      as m
       on o.title = m.title;
    where o.username = %s; -- input username


-- serach all theater
select * from Theater;

-- serach theater from Preferred list
    select * 
      from Prefers as p
 left join Theater as t
        on p.theater_ID = t.theater_ID
     where p.username = %s -- input username