# Countdown Timer CLI with SQLAlchemy

## Introduction

This CLI application is a dynamic countdown timer with SQLAlchemy integration. It allows users to set a specific time duration, counts down second by second, and records timer sessions in a SQLite database. Users can also associate timer sessions with projects for better organization.

## Author
This CLI application was created by:
Kelvin Moti Shombe
email: kmotties@gmail.com
tel: +254708054757

## Features

- Set a timer for a specific duration in seconds.
- Record timer sessions with start and end times.
- Associate timer sessions with projects.
- Display timer sessions in a tabular format.
- Database integration with SQLAlchemy.
- User authentication and registration.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Pipenv (for managing dependencies)

## Installation

1. Clone this repository:

   
   git clone https://github.com/motikev/Phase-3-Python-Project-SQL-SQLAlchemy.git

#### Create a virtual environment and install dependencies:
pipenv install
### Activate the virtual environment:
pipenv shell

## To initialize the SQLite database, run:
python3 init_db.py

# Usage
To run the countdown timer CLI, use the following command:

python3 CountDown_Timer.py

Follow the on-screen instructions to set the timer, register or log in, and associate timer sessions with projects.


## Acknowledgements
. SQLQlchemy: => For the database ORM{Object Relational Mapping}
. Pipenv: => For managing project dependencies. 
. Tabulate: => For displaying data in a tabular format.