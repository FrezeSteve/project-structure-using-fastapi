-- upgrade --
CREATE TABLE IF NOT EXISTS "names" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "text" VARCHAR(255) NOT NULL,
    "completed" BOOL NOT NULL  DEFAULT False
);
-- downgrade --
DROP TABLE IF EXISTS "names";
