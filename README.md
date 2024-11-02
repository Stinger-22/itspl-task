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

## Usage

## TODO Checklist
- [x] Handle token with fixture
- [ ] Use requests to write API tests
- [ ] Write POM
- [ ] Write UI tests
- [ ] Write logging
- [ ] Write Usage and Description in README.md

### User API
Notes:
 - [Found: manually tested in Postman] When you log in multiple times then each token is valid.
 - [Found: test_log_out_user has error] When you log out every token is invalidated - not only the one used to log out. A real use scenario is when you are logged in from your phone and PC and when you log out on your phone you can't continue the session on your PC.
 - [Found: manually in Postman] Can create user with my _id
 - [Found: manually in Postman] When trying to patch user and set own _id in response body there is url to AWS MongoDB database. I can ping it externally from my computer.
 - Limits:
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
