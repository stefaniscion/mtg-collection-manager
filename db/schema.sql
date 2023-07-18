--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Debian 15.3-1.pgdg120+1)
-- Dumped by pg_dump version 15.3 (Debian 15.3-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: card; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.card (
    id integer NOT NULL,
    skryfall_id character varying,
    quantity integer,
    altered boolean,
    foil boolean,
    condition integer
);


ALTER TABLE public.card OWNER TO "user";

--
-- Name: cards_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.cards_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_id_seq OWNER TO "user";

--
-- Name: cards_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.cards_id_seq OWNED BY public.card.id;


--
-- Name: card_cache; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.card_cache (
    id integer DEFAULT nextval('public.cards_id_seq'::regclass) NOT NULL,
    skryfall_id character varying NOT NULL,
    skryfall_data character varying NOT NULL,
    expire timestamp without time zone
);


ALTER TABLE public.card_cache OWNER TO "user";

--
-- Name: card id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.card ALTER COLUMN id SET DEFAULT nextval('public.cards_id_seq'::regclass);


--
-- Name: card_cache card_cache_pk; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.card_cache
    ADD CONSTRAINT card_cache_pk PRIMARY KEY (id);


--
-- Name: card cards_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.card
    ADD CONSTRAINT cards_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

