# Hygge Homes

This repository contains a full-stack web application to search and book vacation homes created with Python 3.6+, HTML and CSS.

What is Hygge? Hygge is a Danish and Norwegian word for a mood of coziness and comfortable conviviality with feelings of wellness and contentment.
This inspiration for this project is to create a site where users can search and find the perfect spot for their vacation home, much like Airbnb.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Features](#features)
- [Views](#views)
- [Models](#models)
- [Status](#status)
- [Authors](#authors)

## Tech Stack
- Frontend libraries:
  - Bootstrap
  - Jquery
  - FontAwesome
  - Datepicker
- Backend framework
  - Django 3.0 and Jinja2
- Databases
  - SQLite (development)
  - PostgreSQL (production)
- Deployment
  - Amazon Web Services EC2 (Ubuntu 18.04)
  - Amazon Web Services Elastic IP

This is a portfolio project made by 2 computer science students who want to showcase our web development skills.

Ryuichi Miyazaki: [LinkedIn](https://www.linkedin.com/in/rmiyazaki/)

Tu Vo: [LinkedIn](https://www.linkedin.com/in/tu-vo/)

Check out our other projects at: [Akatsuki Co](https://github.com/akatsuki-co)


## Features

Users can:

- register
- login
- view featured stays
- browse top cities
- search stays by city and/or location
- book stays

### API Integrations

#### Stripe

We accept and process credit card payments for bookings using Stripe's API.

#### Unsplash

Images for all of the stays are completely random and are rendered dynamically using Unsplash's API.

#### Mapbox

Maps of cities are rendered using Mapbox's API.

## Views

### Landing

![Landing](./static_files/img/homepage.png)

### Explore

![Explore](./static_files/img/explore.png)

### City

![City](./static_files/img/city.png)

### Detail

![Detail](./static_files/img/detail.png)

### My Trips

![My Trips](./static_files/img/my_trips.png)

## Models

Our data has 5 schemas:

- Amenity
- Booking
- Review
- Stay
- User

![Database Schema](./static_files/img/database_schema.png)

### Relationships

A user has a one-to-many relationship to review, booking and stay.
A stay has a many-to-many relationship to amenity, review, and booking.

## Status

Project is complete and deployed!
Check it out here: https://hyggehomes.dev

## Authors

Created by:

- [Ryuichi Miyazaki](https://github.com/rmiyazaki6499)
- [Tu Vo](https://github.com/tuvo1106)
