# REST API Test Project

## Database Schema

### Table-1 Users
```sql
CREATE TABLE Users (uid, f_name,, l_name, age, house_no, street, city, country);
```

### Table-2 Cars
```sql
CREATE TABLE Cars (cid, brand, model, number_plate);
```

### Table-3 Ads
```sql
CREATE TABLE Ads (aid, title, description, price_per_km);
```

### Table-4 Posts
```sql
CREATE TABLE Posts (uid, ad_id);
```

### Table-5 Owner
```sql
CREATE TABLE Owner (uid, car_id);
```


# REFERENCES
1. [Django REST Framework Docs](https://www.django-rest-framework.org/)
2. [Django Docs](https://docs.djangoproject.com/en/4.1/)
3. [Django REST Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
