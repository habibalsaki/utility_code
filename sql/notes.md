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