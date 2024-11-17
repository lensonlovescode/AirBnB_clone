HolbertonBnB: AirBnB Clone
Description 🏠

HolbertonBnB is a comprehensive web application mimicking the core functionality of AirBnB. It combines:
Database storage
Backend API
Frontend interface

Currently, the project focuses on the backend console for managing application data.

Key Components 🛠️
HolbertonBnB features the following core classes:

BaseModel - Base class for all models, providing universal attributes and methods.
User - Handles user-specific data such as email, password, and name.
State - Stores information about states.
City - Contains details for cities, linked to a State.
Amenity - Represents amenities available in a place.
Place - Captures data about rental properties like rooms, price, and location.
Review - Stores user reviews for a place, linked to a User and Place.

Attributes and Methods
Each class inherits from BaseModel and includes unique attributes:

BaseModel : id, created_at, updated_at	None
User : Inherits BaseModel attributes	email, password, first_name, last_name
State : Inherits BaseModel attributes	name
City : Inherits BaseModel attributes	state_id, name
Amenity : Inherits BaseModel attributes	name
Place : Inherits BaseModel attributes	city_id, user_id, name, description, price_by_night, etc.
Review : Inherits BaseModel attributes	place_id, user_id, text

Storage System 🛄
HolbertonBnB uses a JSON-based file storage system, managed through the FileStorage class:

File: file.json stores all data persistently.
Storage Object: An instance of FileStorage (storage) handles loading, saving, and updating class instances.

The Console 💻
The console serves as a command-line interface (CLI) for managing HolbertonBnB's backend. It supports interactive and non-interactive modes.

Usage
Start the console by executing console.py:

bash
./console.py
(hbnb)

Commands are entered at the (hbnb) prompt. Quit with:

quit
EOF signal (Ctrl+D)

Commands Overview

create - create <class>	: Creates a new instance of the specified class.
show - show <class> <id>	: Displays the string representation of a class instance.
destroy - destroy <class> <id>	: Deletes a class instance. Updates storage.
all - all or all <class>	: Prints all instances of a class or all instances if no class is specified.
count - count <class>	: Returns the number of instances of a specific class.

Example Usage
Create a New Instance
bash
Copy code
$ ./console.py
(hbnb) create User
3c8e7696-98c8-45e1-bce1-5539e6b44cf2
Show Instance Details
bash
Copy code
$ ./console.py
(hbnb) show User 3c8e7696-98c8-45e1-bce1-5539e6b44cf2
[User] (3c8e7696-98c8-45e1-bce1-5539e6b44cf2) {'id': '3c8e7696...', 'email': ...}
Delete an Instance
bash
Copy code
$ ./console.py
(hbnb) destroy User 3c8e7696-98c8-45e1-bce1-5539e6b44cf2

Project Roadmap 🛣️
Future enhancements:

Add database storage via SQLAlchemy.
Build a RESTful API.
Develop a user-friendly front-end interface.