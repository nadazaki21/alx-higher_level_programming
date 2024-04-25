--  script that lists all cities contained in the database hbtn_0d_usa.
SELECT id, name, (SELECT name FROM states WHERE state_id= id) FROM cities ORDER BY id;