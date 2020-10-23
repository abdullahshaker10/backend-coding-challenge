# backend-coding-challenge
In this progect we want to fetch trending programmig languages used in repositories using Github API

# Motivations
it is a python task for performing filtering on repos and getting the trending programmig languages :

- Django.
- Django Rest Framework.

## Getting Started
### Pre-requisites and Local Development

Developers using this project should already have Python3 and pip3 installed in their local machines.

#### PIP Dependencies

Ensure you are working using your created virtual environment.

To install all dependencies execute this command in the root folder:
```bash
pip3 install -r requirements.txt
```

To run the server, execute this command in the root folder:

```bash
python3 manage.py runserver
```


## API Reference

### Endpoints

#### GET 'api/languages/{date}'

   - GET all languages as objects.  
   - Request Arguments: date.
   - Return languages objects with the repos used this language and number of them.
  ```
{
   "JavaScript": {
        "repos": [
            {
                "id": 252144263,
                :
                :
                :
            },
            {
              
                "id": 123548579,
                :
                :
                :
            }
         ],
        "num_repos": 2
 }
 ```
