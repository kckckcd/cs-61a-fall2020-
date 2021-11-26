CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name as name, b.size as size from dogs as a, sizes as b where a.height > b.min and a.height <= b.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.name as name from dogs as a, parents as b, dogs as c where a.name = b.child and b.parent = c.name order by c.height desc; 


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.name as sib_1, b.name as sib_2 from dogs as a, dogs as b, parents as c, parents as d where a.name = c.child and b.name = d.child and c.parent = d.parent and a.name < b.name order by a.name desc;

create table sib_size as 
  select a.sib_1 as sib_1, b.size as sib_1_size, a.sib_2 as sib_2, c.size as sib_2_size from siblings as a, size_of_dogs as b, size_of_dogs as c where b.name = a.sib_1 and c.name = a.sib_2;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || sib_1 || " plus " || sib_2 || " have the same size: " || sib_1_size as output from sib_size where sib_1_size = sib_2_size;

