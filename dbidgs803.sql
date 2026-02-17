use bdidgs803;

insert into alumnos(nombre, apaterno, email) values 
("jonathan", "Gomez", "1234@gmail", now()),
("jonathan", "Gomez", "4321@gmail", now()),
("jonathan", "Gomez", "5463@gmail", now());

drop table alumnos; 
select * from alumnos;