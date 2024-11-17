#  AirBnB Clone : HolbertonBnB
<p align="center">
<img src="https://github.com/Michaelndula/AirBnB_clone/blob/master/65f4a1dd9c51265f49d0.png?raw=true" alt="HolbertonBnB logo" width="300" height="auto">
</p>

## Description 🏠
HolbertonBnB is a comprehensive full-stack web application mimicking the core functionality of [AirBnB](https://airbnb.com).

Upon completion, the application will consist:

- [x] A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- [ ] A website (the front-end) that shows the final product to everybody: static and dynamic
- [ ] A database or files that store data (data = objects)
- [ ] An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

Currently, the project focuses on the backend console for managing application data and logic.

## Key Components 🛠️
HolbertonBnB features the following core classes:

|    Model    |                                Description                                      |           Attributes and Methods                   |
|-------------|---------------------------------------------------------------------------------|----------------------------------------------------|
| BaseModel   | Base class for all models, providing universal attributes and methods.          | `id`, `created_at`, `updated_at`                   |
| User        | Handles user-specific data such as email, password, and name.                   | `email`, `password`, `first_name`, `last_name`     |
| State       | Stores information about states.                                                | `name`                                             |
| City        | Contains details for cities, linked to a State.                                 | `state_id`, `name`                                 |
| Amenity     | Represents amenities available in a place.                                      |  `name`          |
| Place       | Captures data about rental properties like rooms, price, and location.          | `city_id`, `user_id`, `name`, `description`, `price_by_night`, |
| Review      | Stores user reviews for a place, linked to a User and Place.                    | `place_id`, `user_id`, `text`                      |


## Storage System 🛄
Currently the application uses a JSON-based file storage system, managed through the FileStorage class:

### File: 
`file.json` stores all data persistently.
Storage Object: An instance of FileStorage (storage) handles loading, saving, and updating class instances.

## The Console 💻
The console serves as a command-line interface (CLI) for managing HolbertonBnB's backend. It supports interactive and non-interactive modes.

Usage
Start the console by executing console.py:

```
$ ./console.py
```
Commands are entered at the (hbnb) prompt.

Quit with:
`quit`/
`EOF signal (Ctrl+D)`

Commands Overview

| Command         | Description                                                                                   | Usage Example                |
|------------------|-----------------------------------------------------------------------------------------------|-------------------------------|
| `create`        | Creates a new instance of a class and saves it to the JSON file.                              | `create User`                |
| `show`          | Displays the string representation of an instance by its class name and ID.                   | `show User 1234-5678-9101`   |
| `destroy`       | Deletes an instance by its class name and ID, removing it from the JSON file.                 | `destroy Place 9876-5432-101`|
| `all`           | Displays all instances, or all instances of a specific class if a class name is provided.     | `all` or `all User`          |
| `update`        | Updates an instance based on its class name and ID, adding or changing an attribute.          | `update User 1234 name "John"`|
| `count`         | Counts the number of instances of a specific class.                                           | `count User`                 |
| `quit` or `EOF` | Exits the console.                                                                            | `quit` or `Ctrl+D`           |
| `help`          | Displays a list of available commands or usage instructions for a specific command.           | `help` or `help create`      |

## Example Usage:

### Create a New Instance
```
$ ./console.py
(hbnb) create User
3c8e7696-98c8-45e1-bce1-5539e6b44cf2
```

### Show Instance Details
```
$ ./console.py
(hbnb) show User 3c8e7696-98c8-45e1-bce1-5539e6b44cf2
[User] (3c8e7696-98c8-45e1-bce1-5539e6b44cf2) {'id': '3c8e7696...', 'email': ...}
```
### Delete an Instance
```
$ ./console.py
(hbnb) destroy User 3c8e7696-98c8-45e1-bce1-5539e6b44cf2
```
### Update e-mail
```
(hbnb)update User e0a1d892-db08-41d3-9ed1-a9d8b448eef2 e-mail someone@example.com
(hbnb)show User e0a1d892-db08-41d3-9ed1-a9d8b448eef2
[User] (e0a1d892-db08-41d3-9ed1-a9d8b448eef2) {'id': 'e0a1d892-db08-41d3-9ed1-a9d8b448eef2', ... 'e-mail': 'someone@example.com'}
```
## Project Roadmap 🛣️
### Future enhancements:
1. Add database storage.
2. Build a RESTful API.
3. Develop a user-friendly front-end interface.
   
<p align="center">
<img src="https://github.com/HeimerR/AirBnB_clone/raw/master/images/pipeline.png" alt="HolbertonBnB logo" width="600" height="auto">
</p>
