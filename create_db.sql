CREATE TABLE IF NOT EXISTS "context" (
    "name" VARCHAR(32) PRIMARY KEY,
    "description" VARCHAR(512) NOT NULL,
    "folder" VARCHAR(512) NOT NULL,
    "password" VARCHAR(32) NOT NULL
);
