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
     where p.username = %s; -- input username


-- search theater by name
select * 
  from Theater as t 
 where t.name = %s; -- input theater name

-- search theater by city
select * 
  from Theater as t 
 where t.city = %s; -- input city

-- search theater by state
 select *
   from Theater as t 
  where t.state = %s; -- input state

-- or use this, I think it will be better
-- search theater by name/city/state
  select *
    from Theater as t
   where t.name = %s 
         t.city = %s
         t.state = %s; 

-- save theather to preferred list
INSERT INTO Prefers 
(
    theater_ID,
    username
)
VALUES
(
    %s,
    %s
);

-- After selecting the theater, the customer 
-- can select the movie time
   select *
     from Theater  as t
left join Plays_at as p
       on t.theater_ID = p.theater_ID
left join Movie    as m
       on m.title = p.title;
    where t.name = %s; -- selected theather name



-- There are three types of tickets: adult, senior and child.
-- Seniors can enjoy 20% off discount and children can enjoy
-- 30% off discount.
    select * 
      from System_info;


