# Student CRUD API

This project is a simple RESTful API for managing student records, allowing basic CRUD operations: Create, Read, Update, and Delete. The API is built 
using Python's Flask framework and is designed to be lightweight and easy to set up.

API Endpoints:

The application exposes several RESTful endpoints to perform CRUD operations on student records:
GET /students: Retrieve a list of all students.
GET /students/{id}: Retrieve details of a specific student by their ID.
POST /students: Create a new student record.
PUT /students/{id}: Update an existing student record by their ID.
DELETE /students/{id}: Delete a student record by their ID.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your machine. Check with:
  ```bash
  python --version

The application uses an in-memory list (students) to store student records.

A test.http file is included in the project for testing the API endpoints, and it allows you to send HTTP requests directly.

Structure of the directory:

student-crud-api/
├── app.py             # Main application file containing API endpoints and logic
├── api_test.http      # HTTP file for testing API endpoints
└── README.md          # Project documentation and setup instructions


The Environment Configuration:

1. Check if Python is installed by running: python --version
2. Clone the repository: git clone https://github.com/NikkiShaker/students-api.git
3. Change into the project directory: cd students-api
4. Install dependencies:
    * pip install flask
    * pip install -r requirements.txt
6. Run the application:
     * python simple_api.py (for Windows)
     * python3 simple_api.py (for Ubuntu)


Run the service:

1. To run the service: python simple_api.py
2. To test the API, open test.http and click on 'send requests'

![image](https://github.com/user-attachments/assets/aa9bd143-0165-450f-b089-418a0b8b22f9)
