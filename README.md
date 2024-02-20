# LAB - Class 31

## Project: Django REST Framework & Docker

### Project Description



### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Beginners Guide to Docker](https://wsvincent.com/beginners-guide-to-docker/)

### Setup

#### To run in Docker

- Install Docker Desktop and verify installation
  - Run `docker --version` and `docker-compose --version` to ensure both are correctly installed.

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- `PORT` - 8000

#### How to initialize/run your application (where applicable)

- Clone repo
- Install dependencies (see above)
- See the page in browser by running `docker-compose up`
- Open the page in the localhost specified in the terminal to view GET request and add `/api/v1/brews` to end of url

#### How to use your library (where applicable)

Use Thunder Bird or other application of your choice to complete PUT, POST, DELETE Requests

##### GET Requests (Read)

- `http://0.0.0.0:8000/api/v1/brews`

##### PUT Requests (Update)

- `http://0.0.0.0:8000/api/v1/brews/7/{id}`

##### POST Requests (Add)

- `http://0.0.0.0:8000/api/v1/brews`

#### Tests

- `python manage.py test`
