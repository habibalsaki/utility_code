## SQL Notes

#### Select All recrods from table

```sql
SELECT * FROM employees;
```
#### Select specific fields from table
```sql
SELECT categoryname, description FROM categories;
```

#### Select distinct fields from table
```sql
SELECT distinct region from suppliers;
```

#### Count records
```sql
SELECT count(distinct productid) from order_details;
```

#### Grouping sets
```sql
SELECT companyname,categoryname,SUM(od.unitprice*quantity)
FROM customers AS c
NATURAL JOIN orders
NATURAL JOIN order_details AS od
JOIN products USING (productid)
JOIN categories  AS s USING (categoryid)
GROUP BY GROUPING SETS ((companyname),(companyname,categoryname))
ORDER BY companyname,categoryname NULLS FIRST;
```

#### Rollup and Cube
```
Cube (c1,c2,c3):
(c1, c2, c3)
(c1, c2)
(c2, c3)
(c1,c3)
(c1)
(c2)
(c3)
()

Rollup (c1,c2,c3):
(c1, c2, c3)
(c1, c2)
(c1)
()
```

#### Union
```sql
select country from customers
union
select country from suppliers
order by country;
```

> Union removes duplicates, Union All doesn't

#### Intersect, Intersect All, Except, Except all are similar to Union and Union All

#### Where exists
```sql
SELECT companyname
FROM suppliers
WHERE EXISTS (SELECT productid FROM products
             	WHERE products.supplierid=suppliers.supplierid AND
               	unitprice > 200);
```

#### In 
```sql
select companyname from customers
where country in (select country from suppliers)
```

- Though In and =Any is equivalent, Not in and <>Any is not similar

#### Insert into
```sql
INSERT INTO orders
(orderid,customerid, employeeid, orderdate, requireddate, shipvia,
 freight, shipname, shipaddress, shipcity, shippostalcode,shipcountry)
VALUES (11078, 'VINET', 4, '2017-09-16','2017-09-30',3,
        42.5, 'Vins et alcools Chevalier',"59 rue de l'Abbaye" 'Reims','51100', 'France');
```

#### Update
```sql
Update [tablename]
set col1 = value1, col2 = value2
Where condition
```

#### Delete
```sql
Delete from [tablename]
where condition
```

#### Select into
```sql
select * into
newtable
from oldtable
where condition
```

#### Insert into select
```sql
INSERT into newtable
Select * from oldtable
where condition
```

#### Return data while inserting, updating and deleting
- After the query, add returning [columnnames]

#### Create index
```sql
create unique index idx_employees_employee_id
on employees (employeeid);
```
- Unique index ensures no duplicate in that column
- we can use only index
- index can be created for multiple columns


#### Drop index
```sql
DROP INDEX INDEX_NAME
```

#### Stop running queries
```sql
--See what is running
SELECT * FROM pg_stat_activity WHERE state = 'active';

--polite way to stop
SELECT pg_cancel_backend(PID);

--stop at all costs - can lead to full database restart
SELECT pg_terminate_backend(PID);
```

- Using 'Explain' before queries shows you the query execution process 

#### Calculating Query Planning Cost
```sql
SET max_parallel_workers_per_gather = 0;
EXPLAIN SELECT * FROM performance_test
WHERE location like 'ab%';

-- size of table
SELECT pg_relation_size('performance_test'),
  pg_size_pretty(pg_relation_size('performance_test'));


-- number of relation pages
SELECT relpages
FROM pg_class
WHERE relname='performance_test';

--
SELECT relpages, pg_relation_size('performance_test') / 8192
FROM pg_class
WHERE relname='performance_test';

-- I/O cost per relationship page read
SHOW seq_page_cost;

-- total I/O cost
SELECT relpages * current_setting('seq_page_cost')::numeric
FROM pg_class
WHERE relname='performance_test';

-- number of rows
SELECT reltuples
FROM pg_class
WHERE relname='performance_test';

--CPU cost per row processed
SHOW cpu_tuple_cost;
SHOW cpu_operator_cost;

-- Total CPU Costs
SELECT reltuples * current_setting('cpu_tuple_cost')::numeric +
reltuples * current_setting('cpu_operator_cost')::numeric
FROM pg_class
WHERE relname='performance_test';

-- Total Costs for a table scan
SELECT relpages * current_setting('seq_page_cost')::numeric +
reltuples * current_setting('cpu_tuple_cost')::numeric +
reltuples * current_setting('cpu_operator_cost')::numeric
FROM pg_class
WHERE relname='performance_test';

SHOW parallel_setup_cost;
SHOW parallel_tuple_cost;

SET max_parallel_workers_per_gather = 4;
EXPLAIN (ANALYZE, VERBOSE) SELECT * FROM performance_test
WHERE location like 'ab%';
```

#### Speeding up text matching
```sql
CREATE EXTENSION pg_trgm;

CREATE INDEX trgm_idx_performance_test_location
ON performance_test USING gin (location gin_trgm_ops);

CREATE INDEX idx_performance_test_name
ON performance_test (name);


-- terrible performance
EXPLAIN ANALYZE SELECT location
FROM  performance_test
WHERE name LIKE '%dfe%';

--only situation where pattern matching works
EXPLAIN ANALYZE SELECT location
FROM  performance_test
WHERE name LIKE 'dfe%';


-- much better performance
EXPLAIN ANALYZE SELECT location
FROM  performance_test
WHERE location LIKE '%dfe%';

EXPLAIN ANALYZE SELECT location
FROM  performance_test
WHERE location LIKE 'dfe%';
```

#### Creating table
```sql
CREATE TABLE subscribers (
	firstname varchar(200),
	lastname varchar(200),
	email varchar(250),
	signup timestamp,
	frequency integer,
	iscustomer boolean
);
```

#### Alter Table
```sql
-- renaming columns
ALTER TABLE subscribers
RENAME firstname TO first_name;

ALTER TABLE returns
RENAME returndate TO return_date;

-- renaming table names
ALTER TABLE subscribers
RENAME TO email_subscribers;

ALTER TABLE returns
RENAME TO bad_orders;

-- adding columns
ALTER TABLE email_subscribers
ADD COLUMN last_visit_date timestamp;

ALTER TABLE bad_orders
ADD COLUMN reason text;

-- dropping columns
ALTER TABLE email_subscribers
DROP COLUMN last_visit_date;

ALTER TABLE bad_orders
DROP COLUMN reason;

-- Changing column type
ALTER TABLE email_subscribers
ALTER COLUMN email SET DATA TYPE varchar(225);

ALTER TABLE bad_orders
ALTER COLUMN quantity SET DATA TYPE int;
```


#### Table Constraints
- Setting not null in already available table column
```sql
ALTER TABLE TABLE_NAME
ALTER COL_NAME SET NOT NULL
```

- Setting unique constraint in already available table column
```sql
ALTER TABLE TABLE_NAME
ADD CONSTRAINT new_name UNIQUE (COL_NAME)
```

- Dropping primary key
```sql
ALTER TABLE TABLE_NAME
DROP CONSTRAINT column_pkey -- CONSTRAINT NAME CAN BE SEEN AT pgadmin
```

- Adding primary key
```sql
ALTER TABLE TABLE_NAME
ADD PRIMARY KEY (col_name)
```


- Adding check constraint
```sql
CREATE TABLE practices (
	practiceid integer PRIMARY KEY,
	practicefield varchar(50) NOT NULL,
	employeeid integer NOT NULL,
	cost integer CONSTRAINT practices_cost CHECK (cost >= 0 AND cost <= 1000),
	FOREIGN KEY (employeeid) REFERENCES employees(employeeid)
);

ALTER TABLE orders
ADD CONSTRAINT orders_freight CHECK (freight > 0);
```

- Adding default constraint
```sql
CREATE TABLE practices (
	practiceid integer PRIMARY KEY,
	practicefield varchar(50) NOT NULL,
	employeeid integer NOT NULL,
	cost integer DEFAULT 50 CONSTRAINT practices_cost CHECK (cost >= 0 AND cost <= 1000),
	FOREIGN KEY (employeeid) REFERENCES employees(employeeid)
);

ALTER TABLE orders
ALTER COLUMN shipvia SET DEFAULT 1;


ALTER TABLE orders
ALTER COLUMN shipvia DROP DEFAULT;
```

- Sequence 
```sql
CREATE SEQUENCE test_sequence;

SELECT nextval('test_sequence');
SELECT nextval('test_sequence');

SELECT currval('test_sequence');

SELECT lastval();

-- set value but next value will increment
SELECT setval('test_sequence',14);
SELECT nextval('test_sequence');

-- set value and next value will be what you set
SELECT setval('test_sequence',25,false);
SELECT nextval('test_sequence');

CREATE SEQUENCE IF NOT EXISTS test_sequence2 INCREMENT 5;

CREATE SEQUENCE IF NOT EXISTS test_sequence_3
INCREMENT 50 MINVALUE 350 MAXVALUE 5000 START WITH 550;


CREATE SEQUENCE IF NOT EXISTS employees_employeeid_seq
START WITH 10 OWNED BY employees.employeeid;
```

- Alter and drop sequence
```sql
ALTER SEQUENCE employees_employee_seq RESTART WITH 1000
SELECT nextval('employees_employee_seq')

ALTER SEQUENCE orders_orderid_seq RESTART WITH 200000
SELECT nextval('orders_orderid_seq')

ALTER SEQUENCE test_sequence RENAME TO test_sequence_1

ALTER SEQUENCE test_sequence_4  RENAME TO test_sequence_four

DROP SEQUENCE test_sequence_1

DROP SEQUENCE test_sequence_four
```