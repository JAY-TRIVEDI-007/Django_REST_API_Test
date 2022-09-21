# REST API Test Project

## Models

### User model
    User model is used for users information.

### Car model
    Car model is used for user's car details.

### Ad model
    Ad model is used for user's advertisment on cars.


## Database Schema

### Table-1 Users
```sql
CREATE TABLE Users (userID int AUTO_INCREMENT, f_name varchar(255) NOT NULL, l_name varchar(255) NOT NULL, age int NOT NULL,
house_no varchar(255) NOT NULL, street varchar(255) NOT NULL, city varchar(255) NOT NULL, country varchar(255) NOT NULL,
PRIMARY KEY (userID));
```

### Table-2 Cars
```sql
CREATE TABLE Cars (carID int AUTO_INCREMENT, brand varchar(255) NOT NULL , model varchar(255) NOT NULL,
number_plate varchar(255) NOT NULL, PRIMARY KEY (carID));
```

### Table-3 Ads
```sql
CREATE TABLE Ads (adID int AUTO_INCREMENT, title varchar(255) NOT NULL , description varchar(255) NOT NULL,
price_per_km int NOT NULL, PRIMARY KEY (adID));
```

### Table-4 Posts
```sql
CREATE TABLE Posts (postID int AUTO_INCREMENT, userID int, adID int, PRIMARY KEY (postID),
FOREIGN KEY (userID) REFERENCES Users(userID), FOREIGN KEY (adID) REFERENCES Ads(adID));
```

### Table-5 Owner
```sql
CREATE TABLE Owner (ownerID int AUTO_INCREMENT, userID int, carID int, PRIMARY KEY (ownerID),
FOREIGN KEY (userID) REFERENCES Users(userID), FOREIGN KEY (carID) REFERENCES Cars(carID));
```


# REFERENCES
1. [Django REST Framework Docs](https://www.django-rest-framework.org/)
2. [Django Docs](https://docs.djangoproject.com/en/4.1/)
3. [Django REST Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
