
CREATE TABLE IF NOT EXISTS post(
    id serial,
    title VARCHAR(255) NOT NULL,
    body text
);

INSERT INTO post(title, body) VALUES('Первый пост', 'Это первый пост');
