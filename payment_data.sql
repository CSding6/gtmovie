-- at lease 5 customer have more than one credit card saved
INSERT INTO Payment_info
(
    card_num,
    name_on_card,
    cvv,
    saved,
    expiration_date,
    username
)
VALUES
(
    1234561,
    'name1',
    121,
    true,
    '2020-01-01',
    'user1'
),
(
    1234511,
    'name1',
    111,
    true,
    '2020-05-01',
    'user1'
),



(
    1234562,
    'name2',
    122,
    true,
    '2020-02-01',
    'user2'
),
(
    1234522,
    'name2',
    131,
    true,
    '2020-05-01',
    'user2'
),



(
    1234563,
    'name3',
    123,
    true,
    '2020-03-01',
    'user3'
),
(
    1234533,
    'name3',
    133,
    true,
    '2020-06-01',
    'user3'
),



(
    1234564,
    'name4',
    124,
    true,
    '2020-04-01',
    'user4'
),
(
    1234544,
    'name4',
    144,
    true,
    '2020-06-01',
    'user4'
),



(
    1234565,
    'name5',
    125,
    true,
    '2020-05-01',
    'user5'
),
(
    1234555,
    'name5',
    155,
    true,
    '2020-03-01',
    'user5'
);