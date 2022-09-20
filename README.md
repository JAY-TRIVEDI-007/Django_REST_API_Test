# REST API Test Project

## Database Schema

### Table-1 Users
```sql
CREATE TABLE Users (uid int, f_name varchar(255), l_name varchar(255), age int, house_no varchar(255), street varchar(255), city varchar(255), country varchar(255));
```

### Dummy Data

### Table-2 Cars
```sql
CREATE TABLE Cars (cid int, brand varchar(255), model varchar(255), number_plate varchar(255));
```

### Table-3 Ads
```sql
CREATE TABLE Ads (aid int, title varchar(255), description varchar(255), price_per_km int);
```

### Table-4 Posts
```sql
CREATE TABLE Posts (uid int, ad_id int);
```

### Table-5 Owner
```sql
CREATE TABLE Owner (uid int, car_id int);
```


# REFERENCES
1. [Django REST Framework Docs](https://www.django-rest-framework.org/)
2. [Django Docs](https://docs.djangoproject.com/en/4.1/)
3. [Django REST Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
