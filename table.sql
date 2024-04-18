create table author(
	id int primary key,
	name varchar(50)
);

create table books(
	id int,
	book varchar(50),
	author_id int,
	foreign key(author_id) references author(id)
);

insert into author(id,name)
values (1,'ram');

insert into books (id,book,author_id)
values (1,'ABC',1);

select books.id, books.book as book_name, author.name as author_name
from books inner join author 
on books.author_id = author.id;

