
# Workout API

This is an API that allows users to create, read, update, and delete workouts with data like distance, name, and heart rate.

## Tool Choices

### FastAPI

I chose FastAPI for three main reasons:
- Data validation: FastAPI's integration with Pydantic allows for rigorous validation of request data. This type checking is done automatically, increasing readability and maintainability.
- Automatic Documentation: FastAPI uses OpenAPI to generate Swagger UI documentation. This documentation is interactive and makes the API easier to test, understand, and use.
- Efficiency: FastAPI's speed and efficiency would be important if this API were to be used at a larger scale.

### SQLAlchemy

- SQLAlchemy is database agnostic which would make it easy to switch to a more robust database from the lightweight SQLite one used in this project.
- The abstraction SQLAlchemy's ORM maps Python classes to database tables and allows the code to work with Python objects. This keeps the backend simple to understand and work with.

## Design Choices

### Service Layer
The service layer, in the services folder, are functions the API endpoints call to perform CRUD operations on the database. This design keeps the business logic separate from the API routes. This increases codebase organization, testability of the logic, and ease of transition if the application switches to a different API framework.

### API Routing
This API makes use of FastAPI's APIRouter() to group all the workout endpoints under the '/workout' prefix in a separate file. This keeps the endpoints organized and would greatly aid readability if more API routes with different paths were added to the application.

## Getting Started

1. Install packages: `pip install -r requirements.txt`
2. Create tables (and database if not already created): `python -m scripts.reset_database`
3. Start application: `fastapi dev main.py`
4. Go to http://127.0.0.1:8000/docs
5. Expand endpoints and use "Try it out" button to test
## API Endpoints
### Get Workouts - GET /workouts
#### Parameters:
-   workout_type: WorkoutTypeEnum | None - Optional parameter for filtering by type
-   min_distance: float | None - Optional parameter for filtering for workouts with greater than or equal to a distance
-   after_time: datetime | None - Optional parameter for filtering for workouts that started after a datetime
#### Responses
-   200 OK - A list of WorkoutModel instances
-   400 Bad Request - JSON object with string “detail” describing the error
-   422 Validation Error - JSON object with string “detail” describing the error
### Get Workout by ID - GET /workouts/{workout_id}
#### Parameters:
-   workout_id: integer, required - The ID of the workout to be retrieved
#### Responses
-   200 OK - A list of WorkoutModel instances
-   400 Bad Request - JSON object with string “detail” describing the error
-   422 Validation Error - JSON object with string “detail” describing the error
### Get Average Heart Rate - GET /workouts/heartrate/average
#### Parameters:
-   None
#### Responses
-   200 OK - A list of WorkoutModel instances
-   400 Bad Request - JSON object with string “detail” describing the error
### Create Workout - POST /workouts
#### Parameters:
-   workout: WorkoutModel - The workout to be created
#### Responses
-   201 Created - The WorkoutModel instance created
-   400 Bad Request - JSON object with string “detail” describing the error
-   422 Validation Error - JSON object with string “detail” describing the error
### Update Workout by ID - PUT /workouts/{workout_id}
#### Parameters:
-  workout_id: integer, required - The ID of the workout to be updated
-  workout: WorkoutModel - The new information to update the workout with

#### Responses
-   200 Created - The WorkoutModel instance created
-   400 Bad Request - JSON object with string “detail” describing the error
-   404 Not Found - JSON object with string “detail” describing the error
-   422 Validation Error - JSON object with string “detail” describing the error
### Delete Workout by ID - DELETE /workouts/{workout_id}
#### Parameters:
-  workout_id: integer, required - The ID of the workout to be deleted
#### Responses
-   200 Created - The WorkoutModel instance created
-   404 Not Found - JSON object with string “detail” describing the error
-   422 Validation Error - JSON object with string “detail” describing the error