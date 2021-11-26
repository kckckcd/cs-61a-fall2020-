.read data.sql


CREATE TABLE average_prices AS
  SELECT category as category, avg(MSRP) as average_price from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store as store, item as item, price as price from inventory group by item having min(price);

create table shopping_list_helper as
  select category as category, name as name, MSRP/rating as point from products group by category having min(point);

CREATE TABLE shopping_list AS
  SELECT a.name as name, b.store as store from shopping_list_helper as a, lowest_prices as b where a.name = b.item;

create table bandwidth_helper as
  select a.name as name, a.store as store, b.Mbs as Mbs from shopping_list as a, stores as b where a.store = b.store;

CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs) from bandwidth_helper;

