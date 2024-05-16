--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)

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
-- Name: softcartDimCategory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."softcartDimCategory" (
    categoryid integer NOT NULL,
    category character varying(100)
);


ALTER TABLE public."softcartDimCategory" OWNER TO postgres;

--
-- Name: softcartDimCountry; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."softcartDimCountry" (
    countryid integer NOT NULL,
    country character varying(10)
);


ALTER TABLE public."softcartDimCountry" OWNER TO postgres;

--
-- Name: softcartDimDate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."softcartDimDate" (
    dateid integer NOT NULL,
    month integer,
    monthname character varying(15),
    day integer,
    weekday integer,
    weekdayname character varying(20),
    quarter integer,
    quartername character varying(2),
    year integer
);


ALTER TABLE public."softcartDimDate" OWNER TO postgres;

--
-- Name: softcartDimItem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."softcartDimItem" (
    itemid integer NOT NULL,
    item character varying(100)
);


ALTER TABLE public."softcartDimItem" OWNER TO postgres;

--
-- Name: softcartFactSales; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."softcartFactSales" (
    salesid "char" NOT NULL,
    price double precision,
    itemid integer,
    countryid integer,
    dateid integer,
    categoryid integer
);


ALTER TABLE public."softcartFactSales" OWNER TO postgres;

--
-- Data for Name: softcartDimCategory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."softcartDimCategory" (categoryid, category) FROM stdin;
\.


--
-- Data for Name: softcartDimCountry; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."softcartDimCountry" (countryid, country) FROM stdin;
\.


--
-- Data for Name: softcartDimDate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."softcartDimDate" (dateid, month, monthname, day, weekday, weekdayname, quarter, quartername, year) FROM stdin;
\.


--
-- Data for Name: softcartDimItem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."softcartDimItem" (itemid, item) FROM stdin;
\.


--
-- Data for Name: softcartFactSales; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."softcartFactSales" (salesid, price, itemid, countryid, dateid, categoryid) FROM stdin;
\.


--
-- Name: softcartDimCategory softcartDimCategory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."softcartDimCategory"
    ADD CONSTRAINT "softcartDimCategory_pkey" PRIMARY KEY (categoryid);


--
-- Name: softcartDimCountry softcartDimCountry_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."softcartDimCountry"
    ADD CONSTRAINT "softcartDimCountry_pkey" PRIMARY KEY (countryid);


--
-- Name: softcartDimDate softcartDimDate_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."softcartDimDate"
    ADD CONSTRAINT "softcartDimDate_pkey" PRIMARY KEY (dateid);


--
-- Name: softcartDimItem softcartDimItem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."softcartDimItem"
    ADD CONSTRAINT "softcartDimItem_pkey" PRIMARY KEY (itemid);


--
-- Name: softcartFactSales softcartFactSales_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."softcartFactSales"
    ADD CONSTRAINT "softcartFactSales_pkey" PRIMARY KEY (salesid);


--
-- Name: softcartFactSales softcartFactSales_categoryid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."softcartFactSales"
    ADD CONSTRAINT "softcartFactSales_categoryid_fkey" FOREIGN KEY (categoryid) REFERENCES public."softcartDimCategory"(categoryid) NOT VALID;


--
-- Name: softcartFactSales softcartFactSales_countryid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."softcartFactSales"
    ADD CONSTRAINT "softcartFactSales_countryid_fkey" FOREIGN KEY (countryid) REFERENCES public."softcartDimCountry"(countryid) NOT VALID;


--
-- Name: softcartFactSales softcartFactSales_dateid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."softcartFactSales"
    ADD CONSTRAINT "softcartFactSales_dateid_fkey" FOREIGN KEY (dateid) REFERENCES public."softcartDimDate"(dateid) NOT VALID;


--
-- Name: softcartFactSales softcartFactSales_itemid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."softcartFactSales"
    ADD CONSTRAINT "softcartFactSales_itemid_fkey" FOREIGN KEY (itemid) REFERENCES public."softcartDimItem"(itemid) NOT VALID;


--
-- PostgreSQL database dump complete
--

