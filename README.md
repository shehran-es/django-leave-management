# Leave Management (Django REST Framework)

This project is a simple REST API implementation for learning Django REST Framework. Here is the API list with sample payloads:
```
01. POST:   /login - Loging a user and return a JWT token
02. GET:    /users - List all users in an array
03. POST:   /users - Add a new user
04. PUT:    /users/:userId - Update a user
05. DELETE: /users/:userId - Delete a user
06. GET:    /users/:userId - Get a user
07. GET:    /leaves List - all leaves
08. POST:   /leaves - Add a leave
09. PUT:    /leaves/:leaveId - Update the leave
10. DELETE: /leaves/:leaveId - Delete the leave
11. GET:    /leaves/:leaveId - Get the leave

Payload:

Login:
-----
{
	"userId": 346,
	"password": "abdur12345"
}


User:
-----
{
	"userId": 346,
	"firstName": "Abdur",
	"lastName": "Rahman",
	"email": "abdur.not.real.email@enosisbd.com",
	"designation": "Software Engineer",
	"dateOfBirth": "1996-11-15",
	"supervisor": "Linus Torvalds",
	"password": "abdur12345"
}

Leave:
-----
{
	"leaveId": 1,
	"from": "2018-09-15",
	"to": "2018-09-20",
	"type": "sick",
	"reason": "personal",
	"emergencyContact": "+8801625012345",
	"userId": 347
}
```


## Setting up the Project

1. Set up env: From the .env.example, we initialize the values to a .env file in the project root. 
2. Create database: Create a new database named "leave_db" with user "postgres". This default can be changed from the env file.
3. Create and activate virtual environment:

    ```bash
    # Create a virtual environment named 'leave_env'
    python -m venv leave_env

    # Activate the virtual environment (Linux/macOS):
    source leave_env/bin/activate

    # or on Windows:
    leave_env\Scripts\activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
5. Run migrations: 
    ```bash
    python manage.py migrate
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```
