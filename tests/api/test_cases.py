USER = {
    "firstName": "John",
    "lastName": "Green",
    "email": "john.green@mail.com",
    "password": "1234567",
}

USER_UPDATED = {
    "firstName": "John_updated",
    "lastName": "Green_updated",
    "email": "john.green_updated@mail.com",
    "password": "1234567_updated",
}

USERS_INVALID = [
    (
        {
            "firstName": "",
            "lastName": "Green",
            "email": "john.green@mail.com",
            "password": "1234567",
        },
        "Empty firstName",
    ),
    (
        {
            "firstName": "John",
            "lastName": "",
            "email": "john.green@mail.com",
            "password": "1234567",
        },
        "Empty lastName",
    ),
    (
        {
            "firstName": "John",
            "lastName": "Green",
            "email": "",
            "password": "1234567",
        },
        "Empty email",
    ),
    (
        {
            "firstName": "John",
            "lastName": "Green",
            "email": "john.green@mail.com",
            "password": "",
        },
        "Empty password",
    ),
    (
        {
            "firstName": "",
            "lastName": "",
            "email": "",
            "password": "",
        },
        "Empty each field",
    ),
    (
        {
            "lastName": "Green",
            "email": "john.green@mail.com",
            "password": "1234567",
        },
        "Missing field firstName",
    ),
    (
        {
            "firstName": "John",
            "email": "john.green@mail.com",
            "password": "1234567",
        },
        "Missing field lastName",
    ),
    (
        {
            "firstName": "John",
            "lastName": "Green",
            "password": "1234567",
        },
        "Missing field email",
    ),
    (
        {
            "firstName": "John",
            "lastName": "Green",
            "email": "john.green@mail.com",
        },
        "Missing field password",
    ),
    (
        {

        },
        "No fields",
    ),
]
