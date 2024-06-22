-- 4. ID can't be null
CREATE TABLE IF NO EXISTS  id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);