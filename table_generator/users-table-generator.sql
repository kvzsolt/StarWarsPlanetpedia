CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE IF NOT EXISTS public.users (
    id serial PRIMARY KEY,
    username varchar(20) NOT NULL,
    password varchar(255) NOT NULL
);
