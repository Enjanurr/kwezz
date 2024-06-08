SHOW databases;

-- @block
CREATE TABLE Users(
    id integer primary key auto_increment,
    student_name text not null
);

-- @block
CREATE TABLE Questions(
    id integer primary key auto_increment,
    Questions text not null unique,
    anwers text not null unique
);
-- @block

INSERT into Questions values("What is the capital city of France?", "Paris");
INSERT into Questions values("Who wrote the play 'Romeo and Juliet'?", " William Shakespeare");
INSERT into Questions values(" What is the chemical symbol for water?", " H2O");
INSERT into Questions values("Who was the first President of the United States?", " George Washington");
INSERT into Questions values(" What is the largest planet in our solar system?", "Jupiter");
-- @block
CREATE TABLE Scores(
    id integer primary key auto_increment,
    scores integer not null 
);

--@block
SELECT * from Users;