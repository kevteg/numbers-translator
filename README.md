# Number translator

This API can help you translate your numbers to plain english! (Up to a quadrillion, 15 zeros!) 🎊

This API makes use of docker + django rest 🐳 🐍

You can also try the API online here: https://kevteg.pythonanywhere.com/num_to_english

## Setting up the project

### Building the App (This will install requirements + Python image)

```
docker compose build
```

### Running the App

```
docker compose up
```

### Running tests

```
docker compose run api make test
```

## Using the API

The API endpoint is: `/num_to_english`. The only enabled methods are `GET` and `POST`

### GET

Usage example: `/num_to_english?number=12345678`

### POST

Usage example: `/num_to_english`
Body:
```
{
    "number": 123455678
}
```

### Example response:

```
{
    "status": "ok",
    "error_description": "",
    "num_in_english": "twelve million three hundred forty five thousand six hundred seventy eight"
}
```

### Possible errors:

- The number field is required, if it is not send you'll get a 400 error:

```
{
    "status": "error",
    "error_description": "{'number': [ErrorDetail(string='This field is required.', code='required')]}",
    "num_in_english": null
}
```

- Negative numbers or greater than a quadrillion are not allowed:

```
{
    "status": "error",
    "error_description": "{'number': [ErrorDetail(string='Ensure this value is greater than or equal to 1.', code='min_value')]}",
    "num_in_english": null
}
```



