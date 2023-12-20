# shopping cart program


## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Setup Virtual Environment

Create and activate a virtual environment for the project:

```bash
python3 -m venv venv          # Create virtual environment
source venv/bin/activate      # Activate virtual environment (Linux or macOS)
# or
.\venv\Scripts\activate       # Activate virtual environment (Windows)
```


### Install Dependencies

Install project dependencies using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

### Create Database

Make sure you have a database set up and update the database configuration in your project as needed. For example, you may need to run database migrations:

```bash
python init_db.py
```

### Start the Application

Run the main application:

```bash
uvicorn main:app --reload
```

The application will be available at http://localhost:8000.

### Explore Swagger UI

Visit Swagger UI to explore and test the API using the interactive documentation.

Credentials:
user1/password1

### Run Unit Tests

Run unit tests using your preferred test runner. For example, using pytest:

```bash
pytest
```

### Self Assessment

#### Self-assessment of the solution

##### What is done:
+ APIs to authorize user with JWT token and asynchroniz task to make reservation.
+ Unit test of database interactions and routes

##### What is not touched:
+ Deployment: Should have time to write dockfile to build a image. Even more, should think about how to scale up in a distributed environment.

#### Major tooling/framework/library decisions:

+ API Framework:
FastAPI is known for its performance and modern features.

+ Database Interaction:
SQLAlchemy is used for working with databases. It provides a powerful and flexible Object-Relational Mapping (ORM) system.

+ Testing: 
Pytest is a popular testing framework for Python. It simplifies the process of writing and executing tests.