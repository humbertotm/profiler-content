-- EDGAR database Financial Statements Data Sets tables as defined in
-- https://www.sec.gov/dera/data/financial-statement-data-sets.html
-- https://www.sec.gov/files/aqfs.pdf

-- Create tables in the order in which they appear.

CREATE TABLE tickers (
       ticker varchar(20) PRIMARY KEY,
       cik varchar(10) NOT NULL
);

-- Each record represents an XBRL submission
-- ** DROPPED NOT NULL CONSTRAINT ON SOME COLUMNS
CREATE TABLE submissions (
       adsh varchar(20) PRIMARY KEY,
       cik  varchar(10) NOT NULL,
       name varchar(150),
       sic varchar(4),
       countryba varchar(2),
       stprba varchar(2),
       cityba varchar(30),
       zipba varchar(10),
       bas1 varchar(40),
       bas2 varchar(40),
       baph varchar(20),
       countryma varchar(2),
       stprma varchar(2),
       cityma varchar(30),
       zipma varchar(10),
       mas1 varchar(40),
       mas2 varchar(40),
       countryinc varchar(3),
       stprinc varchar(2),
       ein varchar(10),
       former varchar(150),
       changed date,		-- Date format not specified, assuming it is a std one
       afs varchar(5),
       wksi boolean,
       fye varchar(4),	-- mmdd date => Will have to store as varchar
       form varchar(10) NOT NULL,
       period date,	-- yymmdd => Tested
       fy varchar(4) NOT NULL,	-- yyyy => Will have to store as varchar
       fp varchar(2) NOT NULL,
       filed date,	-- yymmdd => Tested
       accepted timestamp, -- yyyy-mm-dd hh:mm:ss => Tested
       prevrpt boolean,
       detail boolean,
       instance varchar(32),
       nciks varchar(4),
       aciks varchar(120)
);

-- Based on predicted use case
CREATE UNIQUE INDEX submissions_cik_adsh
ON submissions (cik, adsh);

-- Index created for common use case
CREATE INDEX submissions_cik_form_fy
ON submissions (cik, form, fy);

-- Each record represents the description of any of the tags employed in line items
-- of submitted statements.
CREATE TABLE tags (
       tag varchar(256),
       version varchar(20),
       custom boolean,
       abstract boolean,
       datatype varchar(20),
       iord varchar(1),
       crdr varchar(1),
       tlabel varchar(512),
       doc text,
       PRIMARY KEY(tag, version)
);

-- Each record represents a line item for each of the statements of each submission.
-- This stable stores the values for each item in each submitted report.
CREATE TABLE numbers (
       adsh varchar(20),
       tag varchar(256),
       version varchar(20),
       coreg varchar(256),
       ddate date,	-- yyyymmdd => Tested
       qtrs integer,
       uom varchar(20),
       value numeric(32, 4),
       footnote text,
       UNIQUE(adsh, tag, version, ddate, coreg, qtrs, uom)
);


-- TEMPORARY TABLES FOR DATA UPLOAD

CREATE TABLE submissions_tmp (
       adsh varchar(20),
       cik  varchar(10),
       name varchar(150),
       sic varchar(4),
       countryba varchar(2),
       stprba varchar(2),
       cityba varchar(30),
       zipba varchar(10),
       bas1 varchar(40),
       bas2 varchar(40),
       baph varchar(20),
       countryma varchar(2),
       stprma varchar(2),
       cityma varchar(30),
       zipma varchar(10),
       mas1 varchar(40),
       mas2 varchar(40),
       countryinc varchar(3),
       stprinc varchar(2),
       ein varchar(10),
       former varchar(150),
       changed date,		-- Date format not specified, assuming it is a std one
       afs varchar(5),
       wksi boolean,
       fye varchar(4),	-- mmdd date => Will have to store as varchar
       form varchar(10),
       period date,	-- yymmdd => Tested
       fy varchar(4),	-- yyyy => Will have to store as varchar
       fp varchar(2),
       filed date,	-- yymmdd => Tested
       accepted timestamp, -- yyyy-mm-dd hh:mm:ss => Tested
       prevrpt boolean,
       detail boolean,
       instance varchar(32),
       nciks varchar(4),
       aciks varchar(120)
);

CREATE TABLE tags_tmp (
       tag varchar(256),
       version varchar(20),
       custom boolean,
       abstract boolean,
       datatype varchar(20),
       iord varchar(1),
       crdr varchar(1),
       tlabel varchar(512),
       doc text
);

CREATE TABLE numbers_tmp (
       adsh varchar(20),
       tag varchar(256),
       version varchar(20),
       coreg varchar(256),
       ddate date,	-- yyyymmdd => Tested
       qtrs integer,
       uom varchar(20),
       value numeric(32, 4),
       footnote text
);
