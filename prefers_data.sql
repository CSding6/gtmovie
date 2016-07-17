-- at least 5 customers have more than one theater saved in the prefered list
INSERT INTO Prefers
(
    theater_ID,
    username
)
VALUES
    (1, 'user1'),
    (2, 'user1'),
    
    (2, 'user2'),
    (3, 'user2'),

    (3, 'user3'),
    (4, 'user3'),

    (4, 'user4'),
    (5, 'user4'),

    (5, 'user5'),
    (6, 'user5'),

    (6, 'user6'),
    (7, 'user6');