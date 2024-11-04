# ITSPL Task
You have to test Contact List App (https://thinking-tester-contact-list.herokuapp.com/).  
Write automation tests using *pytest* to validate different operations with the app. You should use fixtures for data preparation. Automation tests must validate UI and API.

## Minimum Requirements
- Implemented positive and negative test cases;
- Tests use logging for actions;
- Report in the form of a HTML file must be generated after executing automation tests;
- Tested different HTTP request methods: GET, POST, PUT, DELETE;
- If you have the option to use a token in API tests then you should use it;
- Token obtaining must be implemented in a fixture;
- Browser creation must be implemented in a fixture;

### Examples of API tests:
1. Positive test cases:
    - Logging in (receiving token)
	- Receiving contact
2. Negative test cases:
    - Deleting non-existent contact
	- ...

### Examples of UI tests:
1. Positive test cases:
    - Existing user can authenticate in the system
	- User can create a new entry in the contact list
2. Negative test cases:
    - Non-existing user can't authenticate in the system
	- ...

Upload your project on GitHub or another repository.\
Write in the README.md instructions for the execution of the automated tests.

## Description
Performed Exploratory, API, and UI testing of Contact List App (https://thinking-tester-contact-list.herokuapp.com/).  
Used libs: pytest, pytest-html, requests, selenium.  
You can read detailed reports in `reports` folder. Also, you can import Postman collection. Requests with buggy responses are saved and named after the charter and note/bug number (see exploratory_test_charter file for the details).

## Usage
1. Download this repository: `git clone https://github.com/Stinger-22/itspl-task.git`.
2. Create python virtual environment and activate it.
3. Install all dependencies: `pip install -r 'requirements.txt'`.
4. Run tests: `pytest`.  
To change logging level use `--log-cli-level=LEVEL`.  
To set log file use `--log-file=FILE`.  
To generate html report use `--html=FILE`.  
For more info about CLI parameters read docs.

## Project structure
```
.
├── ITSPL-Task.postman_collection.json
├── pyproject.toml
├── README.md
├── reports
├── requirements.txt
├── src
│   ├── __init__.py
│   └── util
│       ├── admin
│       │   ├── admin_api.py
│       │   ├── bearer_auth.py
│       │   ├── __init__.py
│       └── __init__.py
└── tests
    ├── api
    │   ├── conftest.py
    │   ├── contact
    │   │   ├── conftest.py
    │   │   ├── __init__.py
    │   │   ├── test_api_contact.py
    │   │   └── test_cases_contact.py
    │   ├── __init__.py
    │   ├── test_cases_user.py
    │   └── user
    │       ├── conftest.py
    │       ├── __init__.py
    │       └── test_api_user.py
    ├── conftest.py
    ├── __init__.py
    ├── ui
    │   ├── conftest.py
    │   ├── __init__.py
    │   ├── pages.py
    │   ├── test_contact.py
    │   ├── test_log_in.py
    │   └── test_sign_up.py
    └── util
        ├── __init__.py
        └── test_case_parse.py
```
