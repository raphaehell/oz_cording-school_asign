use yes24

-- SELECT title, author FROM Books;

-- SELECT title, rating FROM Books WHERE rating >= 4;

-- SELECT title, review FROM Books WHERE review >= 100;

-- SELECT title, price FROM Books WHERE price < 20000;

-- SELECT title, ranking_weeks FROM Books WHERE ranking_weeks >= 4;

-- SELECT title FROM Books WHERE author = '유시민';

-- SELECT title FROM Books WHERE publisher = '우리학교';

-- SELECT author, COUNT(*) FROM Books GROUP BY author;

-- SELECT publisher, COUNT(*) AS num_books FROM Books GROUP BY publisher ORDER BY num_books DESC LIMIT 1;

-- SELECT author, AVG(rating) AS avg_rating FROM Books GROUP BY author ORDER BY avg_rating DESC LIMIT 1;

-- SELECT title, author FROM Books WHERE ranking = 1;

-- SELECT title, sales, review FROM Books ORDER BY sales DESC, review DESC LIMIT 10;

-- SELECT title, publishing FROM Books ORDER BY publishing DESC LIMIT 5;

-- SELECT author, AVG(rating) FROM Books GROUP BY author;

-- SELECT publishing, COUNT(*) FROM Books GROUP BY publishing;

-- SELECT title, AVG(price) FROM Books GROUP BY title;

-- SELECT title, review FROM Books ORDER BY review DESC LIMIT 5;

-- SELECT ranking, AVG(review) FROM Books GROUP BY ranking;

-- SELECT title, rating FROM Books WHERE rating > (SELECT AVG(rating) FROM Books);

-- SELECT title, price FROM Books WHERE price > (SELECT AVG(price) FROM Books);

-- SELECT title, review FROM Books WHERE review > (SELECT MAX(review) FROM Books);

-- SELECT title, sales FROM Books WHERE sales < (SELECT AVG(sales) FROM Books);

-- SELECT title, publishing FROM Books WHERE author = (SELECT author FROM Books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1) ORDER BY publishing DESC LIMIT 1;

-- UPDATE Books SET price = 30000 WHERE title = '자존감 수업';

-- UPDATE Books SET title = '츠츠츠츠' WHERE author = '사계절';

-- DELETE FROM Books WHERE sales = (SELECT MIN(sales) FROM Books);

-- UPDATE Books SET rating = rating + 1 WHERE publisher = '서삼독';

-- SELECT author, AVG(rating) as avg_rating, AVG(sales) as avg_sales FROM Books GROUP BY author;

-- SELECT publishing, AVG(price) as avg_price FROM Books GROUP BY publishing;

-- SELECT publisher, COUNT(*) as num_books, AVG(review) as avg_review FROM Books GROUP BY publisher;

-- SELECT ranking, AVG(sales) as avg_sales FROM Books GROUP BY ranking;

SELECT price, AVG(review) as avg_review, AVG(rating) as avg_rating FROM Books GROUP BY price;