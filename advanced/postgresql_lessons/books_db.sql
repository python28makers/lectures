--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

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
-- Name: author; Type: TABLE; Schema: public; Owner: tima
--

CREATE TABLE public.author (
    author_id integer NOT NULL,
    name character varying(100) NOT NULL,
    surname character varying(100),
    birth_date date,
    country character varying(50) NOT NULL
);


ALTER TABLE public.author OWNER TO tima;

--
-- Name: author_author_id_seq; Type: SEQUENCE; Schema: public; Owner: tima
--

CREATE SEQUENCE public.author_author_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.author_author_id_seq OWNER TO tima;

--
-- Name: author_author_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tima
--

ALTER SEQUENCE public.author_author_id_seq OWNED BY public.author.author_id;


--
-- Name: book; Type: TABLE; Schema: public; Owner: tima
--

CREATE TABLE public.book (
    book_id integer NOT NULL,
    title character varying(255),
    price numeric(8,2) DEFAULT 0.00,
    author_id integer,
    quantity integer,
    CONSTRAINT book_quantity_check CHECK ((quantity >= 0))
);


ALTER TABLE public.book OWNER TO tima;

--
-- Name: book_book_id_seq; Type: SEQUENCE; Schema: public; Owner: tima
--

CREATE SEQUENCE public.book_book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.book_book_id_seq OWNER TO tima;

--
-- Name: book_book_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tima
--

ALTER SEQUENCE public.book_book_id_seq OWNED BY public.book.book_id;


--
-- Name: book_genre_mtm; Type: TABLE; Schema: public; Owner: tima
--

CREATE TABLE public.book_genre_mtm (
    book_id integer,
    genre_id integer
);


ALTER TABLE public.book_genre_mtm OWNER TO tima;

--
-- Name: genre; Type: TABLE; Schema: public; Owner: tima
--

CREATE TABLE public.genre (
    genre_id integer NOT NULL,
    title character varying(50)
);


ALTER TABLE public.genre OWNER TO tima;

--
-- Name: genre_genre_id_seq; Type: SEQUENCE; Schema: public; Owner: tima
--

CREATE SEQUENCE public.genre_genre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genre_genre_id_seq OWNER TO tima;

--
-- Name: genre_genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tima
--

ALTER SEQUENCE public.genre_genre_id_seq OWNED BY public.genre.genre_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: tima
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(100) NOT NULL,
    email character varying(255),
    password character varying(100) NOT NULL,
    age smallint,
    CONSTRAINT users_age_check CHECK ((age > 14))
);


ALTER TABLE public.users OWNER TO tima;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: tima
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO tima;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tima
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: author author_id; Type: DEFAULT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.author ALTER COLUMN author_id SET DEFAULT nextval('public.author_author_id_seq'::regclass);


--
-- Name: book book_id; Type: DEFAULT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.book ALTER COLUMN book_id SET DEFAULT nextval('public.book_book_id_seq'::regclass);


--
-- Name: genre genre_id; Type: DEFAULT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.genre ALTER COLUMN genre_id SET DEFAULT nextval('public.genre_genre_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: author; Type: TABLE DATA; Schema: public; Owner: tima
--

COPY public.author (author_id, name, surname, birth_date, country) FROM stdin;
1	Calv	Perschke	1983-06-23	Afghanistan
3	Adrea	Gooderridge	1999-04-18	Colombia
4	Bordy	Claridge	1957-06-25	China
5	Lucilia	Slimon	1981-02-23	Colombia
6	Klement	Brumby	1998-04-17	China
7	Caryl	Sherlaw	1986-11-26	China
8	Madelena	Delf	1976-09-17	Ecuador
9	Letizia	Machel	1986-08-04	Malaysia
10	Marcello	Ottiwill	1956-05-28	China
11	Sharline	Alred	1987-11-30	China
12	Conchita	Paris	1978-05-13	Indonesia
13	Daryl	Locket	1975-07-04	Japan
14	Abbott	Dimitriev	2003-02-21	Panama
15	Lucita	Oswald	1988-06-24	China
16	Jessy	Blatherwick	1989-02-14	Iran
17	Letizia	Bolzen	1967-02-06	China
18	Sam	Ben	1973-05-17	China
19	Nessy	Willshere	1993-10-20	Russia
20	Tiff	Heales	1989-03-23	Russia
\.


--
-- Data for Name: book; Type: TABLE DATA; Schema: public; Owner: tima
--

COPY public.book (book_id, title, price, author_id, quantity) FROM stdin;
1	Wait Until Dark	2517.29	3	33
2	Praying with Lior	889.10	12	13
5	Cry, The (Grido, Il)	8362.14	7	38
6	Problem Child 2	4603.42	12	46
7	Anita	374.88	15	47
8	Mirror, The (Ayneh)	1573.61	4	41
9	Direct Action	1025.88	17	23
10	Shaolin Kung Fu Mystagogue (Da mo mi zong)	8038.47	20	7
11	Sisters of the Gion (Gion no shimai)	4099.08	9	6
12	Little Caesar	5623.63	12	81
13	Dark Knight, The	192.46	3	53
14	Sin City: A Dame to Kill For	4938.99	19	44
15	Magic Sword, The	1281.03	6	82
19	Key, The	4736.64	7	94
20	Stargate	9900.37	5	36
25	Adam Had Four Sons	1124.28	17	54
26	Yuva	9943.28	14	93
28	Side Street	7664.99	18	67
29	Chump at Oxford, A	1435.47	11	67
30	Justice League: The New Frontier 	1420.65	20	13
32	Geography Club	7168.15	5	72
33	Wild Bill	8515.85	6	66
34	Brotherhood of the Wolf (Pacte des loups, Le)	4039.43	16	67
35	Children of the Corn: Genesis	9174.27	17	32
36	All-Star Superman	1661.09	17	51
37	Isolation	8574.86	14	68
38	Private Parts	7528.45	12	70
39	Days Of Darkness	7139.84	16	56
3	Shooting Gallery	0.00	8	2
4	McConkey	0.00	3	12
16	12th & Delaware	0.00	12	90
18	Palindromes	0.00	11	55
21	Resan Till Melonia	0.00	8	33
22	Thunderbolt (Pik lik feng)	0.00	12	79
31	In July (Im Juli)	0.00	4	49
44	Zatoichi's Revenge (Zatôichi nidan-kiri) (Zatôichi 10)	2320.67	7	13
45	Lizard, The (Marmoulak)	1473.98	14	90
48	Red Riding Hood	7598.34	17	13
43	Lacombe Lucien	0.00	14	15
46	Housesitter	0.00	8	66
47	When Evening Falls on Bucharest or Metabolism	0.00	19	91
49	I Thank a Fool	0.00	9	72
50	Artist and the Model, The (El artista y la modelo)	0.00	4	47
\.


--
-- Data for Name: book_genre_mtm; Type: TABLE DATA; Schema: public; Owner: tima
--

COPY public.book_genre_mtm (book_id, genre_id) FROM stdin;
1	1
1	3
6	4
6	2
7	3
7	2
\.


--
-- Data for Name: genre; Type: TABLE DATA; Schema: public; Owner: tima
--

COPY public.genre (genre_id, title) FROM stdin;
1	Horror
2	Detective
3	Drama
4	History
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: tima
--

COPY public.users (id, username, email, password, age) FROM stdin;
1	book-worm2001	chitatel@mail.com	superpassword	15
2	aibek	aibek@gmail.com	mypasssss	23
3	chuvak69	chuvak.69@inbox.ru	skjasdasdf	34
\.


--
-- Name: author_author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tima
--

SELECT pg_catalog.setval('public.author_author_id_seq', 20, true);


--
-- Name: book_book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tima
--

SELECT pg_catalog.setval('public.book_book_id_seq', 50, true);


--
-- Name: genre_genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tima
--

SELECT pg_catalog.setval('public.genre_genre_id_seq', 4, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tima
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- Name: author author_pkey; Type: CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (author_id);


--
-- Name: book book_pkey; Type: CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (book_id);


--
-- Name: genre genre_pkey; Type: CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_pkey PRIMARY KEY (genre_id);


--
-- Name: genre genre_title_key; Type: CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_title_key UNIQUE (title);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: book book_author_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.author(author_id);


--
-- Name: book_genre_mtm book_genre_mtm_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.book_genre_mtm
    ADD CONSTRAINT book_genre_mtm_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.book(book_id) ON DELETE CASCADE;


--
-- Name: book_genre_mtm book_genre_mtm_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tima
--

ALTER TABLE ONLY public.book_genre_mtm
    ADD CONSTRAINT book_genre_mtm_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public.genre(genre_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

