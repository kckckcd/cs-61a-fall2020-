.read data.sql


CREATE TABLE bluedog AS
  select color as color, pet as pet from students where color="blue" and pet="dog";

CREATE TABLE bluedog_songs AS
  SELECT color as color, pet as pet, song as song from students where color="blue" and pet="dog";


CREATE TABLE smallest_int AS
  SELECT time as time, smallest as smallest from students where smallest > 2 order by smallest limit 20;


CREATE TABLE matchmaker AS
  select a.pet as pet, a.song as song, a.color as color, b.color as color1 from students as a, students as b where a.time < b.time and a.pet = b.pet and a.song = b.song;
 

CREATE TABLE sevens AS
  SELECT a.seven from students as a, numbers as b where a.number = 7 and a.time = b.time and b.'7' = 'True';

