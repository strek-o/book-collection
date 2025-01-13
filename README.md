# Book Collection

### Overview

This project is a simple CRUD application that uses `sqlite3` module to manage and interact with a SQLite database. It features a modular structure and a console-driven interface to perform **CRUD** operations on a database storing a collection of books.

### Features

- **SQLite Integration** - Leverages seamless execution of `SQL` queries directly from Python scripts.

- **Persistent Data Storage** - Stores data in a `.db` file, ensuring information is retained between sessions.

- **Console Interface** - Provides an intuitive main menu and detailed submenus to guide users through various operations.

- **Modular Design** - Organized into distinct modules for database management, user interface, data models, and utility functions.

### File Structure

```
|   .gitignore
|   LICENSE.md
|   main.py
|   README.md
|
\---book_collection
   +---data
   |       .gitkeep
   |       collection.db
   |
   +---database
   |       db.py
   |       __init__.py
   |
   +---interface
   |       create_menu.py
   |       delete_menu.py
   |       main_menu.py
   |       read_menu.py
   |       update_menu.py
   |       __init__.py
   |
   +---models
   |       Author.py
   |       Book.py
   |       Genre.py
   |       __init__.py
   |
   +---schemas
   |       Authors.py
   |       Books.py
   |       Genres.py
   |       __init__.py
   |
   +---service
   |       delete.py
   |       get.py
   |       post.py
   |       put.py
   |       __init__.py
   |
   \---utils
           input.py
           __init__.py
```

### Key Components

- `data/` - Contains the SQLite database file.

- `interface/` - Handles user interactions through console menus for main operations.

- `models/` - Defines Python classes (_Author_, _Book_, _Genre_) representing the database entities.

- `schemas/` - Defines schema structures used to standardize database operations.

- `service` - Implements business logic for CRUD operations with scripts like **get.py**, **post.py**, **put.py**, and **delete.py**.

# Setup

1. Clone the repository

```
git clone https://github.com/strek-o/book-collection.git
```

2. Navigate to the project directory

```
cd book-collection
```

3. Run the main script

```
python main.py
```

### License

This project is licensed under the MIT License. See the `LICENSE.md` file for more details.
