CREATE DATABASE CARS24;

USE cars24;

-- Users Table
CREATE TABLE Users (userID int AUTO_INCREMENT, f_name varchar(255) NOT NULL, l_name varchar(255) NOT NULL, age int NOT NULL,
house_no varchar(255) NOT NULL, street varchar(255) NOT NULL, city varchar(255) NOT NULL, country varchar(255) NOT NULL,
PRIMARY KEY (userID));

-- Cars Table
CREATE TABLE Cars (carID int AUTO_INCREMENT, brand varchar(255) NOT NULL , model varchar(255) NOT NULL,
number_plate varchar(255) NOT NULL, PRIMARY KEY (carID));

-- Ads Table
CREATE TABLE Ads (adID int AUTO_INCREMENT, title varchar(255) NOT NULL , description varchar(255) NOT NULL,
price_per_km int NOT NULL, PRIMARY KEY (adID));

-- Posts Table
CREATE TABLE Posts (postID int AUTO_INCREMENT, userID int, adID int, PRIMARY KEY (postID),
FOREIGN KEY (userID) REFERENCES Users(userID), FOREIGN KEY (adID) REFERENCES Ads(adID));

-- Owner Table
CREATE TABLE Owner (ownerID int AUTO_INCREMENT, userID int, carID int, PRIMARY KEY (ownerID),
FOREIGN KEY (userID) REFERENCES Users(userID), FOREIGN KEY (carID) REFERENCES Cars(carID));
