# mtg-collection-manager
mtg-collection manager is a fast and lightweight web application to manage your Magic: The Gathering card collection.

It Uses FastApi and PostgeSQL to be the fastest possible, then all data are fetched from Skryfall API and cached in the database.
## Features
I've used those technologies to build this project:
- [FastAPI](https://fastapi.tiangolo.com/) - Backend Framework
- [Svelte](https://svelte.dev/) - Frontend Framework
- [Tailwind](https://tailwindcss.com/) - CSS Framework
- [PostgreSQL](https://www.postgresql.org/) - Database

## Installation
You need to do the following steps to initialize the project the first time.
### DB
First of all you need to create a PostgreSQL database, you can find a dump of the database in the ```db/``` directory.
### Env
You need to create a ```.env``` file in the ```app/``` directory.
You can find an example of the ```.env``` file in the ```app/``` directory.
It is named ```.env.example```.
### Backend
Install the needed dipendencies with the following command in the ```app/``` directory:

```pip install -r requirements.txt```

if you are using conda use the following command:

```conda install --file requirements.txt```

If you are using mamba use the following command:

```mamba install --file requirements.txt```
## Usage
### Run the Backend
To run the Backend do the following command in the ```app/``` directory:

```uvicorn main:app --reload```
### Run the Frontend
To start the frontend, while in the ```public/``` directory, simply run

```npm run dev```
## Other usefull resources
- [CSS Foil Card Effect](https://deck-24abcd.netlify.app/)