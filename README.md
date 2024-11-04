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
You can download and read detailed reports in `reports` folder.

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

### User API
Notes:
 - [Found: manually tested in Postman] When you log in multiple times then each token is valid.
 - [Found: test_log_out_user has error] When you log out every token is invalidated - not only the one used to log out. A real use scenario is when you are logged in from your phone and PC and when you log out on your phone you can't continue the session on your PC.
 - [Found: manually in Postman] Can create user with my _id.
 - [Found: manually in Postman] When trying to patch user and set own _id in response body there is url to AWS MongoDB database. I can ping it externally from my computer.
 - [Found: manually in Postman] When registering a user with no fields in response, it says that only firstName, userName, and password are required. When trying to register a user without email it says that "Email address is already in use" and it is misleading.
 - Limits:
   - user required fields - all
   - password len: 7 <= len <= 100
   - email doesn't allow invalid domain, spaces, missed @, missed user part, missed domain part
   - _id len is 24

Bugs:
 - [Found: automation tests] Special charactes possible in email like jo#n.green@mail.com

### Contact API
Notes:
 - [Found: manually inspected in Postman] Contact List DELETE endpoint is not working if followed by API docs (Error 503) 
 - [Found: manually inspected in Firefox with DevTools] API docs doesn't have information on how to delete one contact. Endpoint to get/put/delete contact needs auth and looks like `url/contacts/{{contactId}}`
 - [Found: manually guessed in Postman] API endpoint to patch contact is `url/contacts/{{contactId}}`
 - [Found: manually in Postman] If try to create Contact and then the same one but give it _id of the first in response is shown MongoError
 - [Found: manually in Postman] Created contact with all fields. Updated with only firstName and lastName. After trying to get thet contact each field exists but with null value. Don't know whether to consider it good or bad sign and which outcome tests should have.
 - Limits:
   - contact required fields: firstName, lastName
   - firstName, lastName: empty not allowed, max len 20
   - birthdate YYYY-mm-dd: empty not allowed, year any 4 numbers, month only 2 numbers and [01; 12], day only 2 numbers and [01;31]
   - email: empty not allowed, same as in user tests
   - phone: empty not allowed, strange validation - can't test it thoroughly
   - stree1, street2, city: empty is allowed, max len 40
   - stateProvince: empty is allowed, max len 20
   - postalCode: empty not allowed, only numbers, len is [3; 7]
   - country: empty is allowed, max len 40

### UI
Notes:
 - [Found: manually inspected in Firefox with DevTools] tbody is empty, each row is under table tag. Each table row should be under tbody. Nevethless, I'll write ui test to this part.
 - [Found: manually inspected in Firefox with DevTools] id of each contact is sent to client, it's just set to be invisible
