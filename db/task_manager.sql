DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;



CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR,
  last_name  VARCHAR


)


CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255),
  -- assignee VARCHAR(255),
  duration INT,
  completed BOOLEAN DEFAULT FALSE
  user_id IN REFERENCES users(id)
  
);


