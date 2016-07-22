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


-- for payment
-- use a saved card
    select *
      from Payment_info as p 
     where p.username = %s; -- input username


-- save a new card
-- need to check data
INSERT INTO Payment_info
(
    card_num,
    name_on_card,
    cvv,
    saved,
    expiration_date
    username
)
VALUES 
(
    -- expiration_date needs to be checked
);


-- generated a new order
INSERT INTO Order_info
(
    status,
    time,
    date,
    num_of_child_ticket,
    num_of_adult_ticket,
    num_of_senior_ticket,   
    num_of_total_ticket,
    username
    card_num
    theater_ID
)
VALUES
(

);

-- get order history
-- order_id, movie, stauts, total
with tt_sys as (
    select child_discount,
           senior_discount
      from System_info
)
   select order_id,
          title,
          status,
          (num_of_child_ticket * % * tt_sys.child_discount 
            + num_of_senior_ticket * % * tt_sys.senior_discount
            + num_of_adult_ticket * %) as total
     from Order_info
 order by order_id;

 -- get order history detail

   select s.show_time
     from Order_info as o 
left join Theater    as t
       on o.theater_ID = o.theater_ID
left join Movie      as m
       on m.title = o.title
left join Show_time  as s
       on s.theater_ID = o.theater_ID
      and m.title = o.title
    where o.order_id = %s;


   select name,
          state,
          city,
          street,
          zip,
          num_of_adult_ticket,
          num_of_senior_ticket,
          num_of_child_ticket,
     from Order_info as o 
left join Theater    as t
       on o.theater_ID = o.theater_ID
left join Movie      as m
       on m.title = o.title
left join Show_time  as s
       on s.theater_ID = o.theater_ID
      and m.title = o.title
    where o.order_id = %s;


-- cancall order
UPDATE Order_info
   SET status = 'cancalled'
 where order_id = %s;


-- movie report
  select month(date) as month,
         title,
         count(order_id) as orders
    from Order_info as o
   where o.status != 'cancalled'
group by month, title
order by orders desc, month desc;
