# ITSPL Task
You have to test Contact List App (https://thinking-tester-contact-list.herokuapp.com/).\
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
    - Loggging in (receiving token)
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