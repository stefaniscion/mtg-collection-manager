# mtg-collection-manager
mtg-collection manager is a fast and lightweight web application to manage your Magic: The Gathering card collection.

It Uses FastApi and PostgeSQL to be the fastest possible, then all data are fetched from Skryfall API and cached in the database.
## Features
I've used those technologies to build this project:
- [FastAPI](https://fastapi.tiangolo.com/) - Backend Framework
- [Svelte](https://svelte.dev/) - Frontend Framework
- [Tailwind](https://tailwindcss.com/) - CSS Framework
- [PostgreSQL](https://www.postgresql.org/) - Database
## Installation through Docker
### Backend preparation
You need to create a ```.env``` file in the ```app/``` directory.
You can find an example of the ```.env``` file, named ```.env.example``` in the ```backend/``` directory.
### Frontend preparation
You must install all needed packages, cd into the ```frontend/``` directory and run the following command:
```sh 
npm install
```
### Run the containers
To run the container stack simply run the following command in the root directory:
```sh
docker-compose up --build
```
## Installation without Docker
You need to do the following steps to initialize the project the first time.
### DB
First of all you need to create a PostgreSQL database, you can find a dump of the database in the ```db/``` directory.
### Backend
You need to create a ```.env``` file in the ```app/``` directory.
You can find an example of the ```.env``` file in the ```app/``` directory.
It is named ```.env.example```.

Then install the needed dipendencies with the following command in the ```app/``` directory:

```sh
pip install -r requirements.txt
```
I haven't tested pip packages corrispondence with this project, so, i suggest you to use conda or mamba.

if you are using conda use the following command:
```sh
conda install --file requirements.txt
```
If you are using mamba use the following command:
```sh
mamba install --file requirements.txt
```
## Usage
### Run the Backend
To run the Backend do the following command in the ```app/``` directory:

```uvicorn main:app --reload --host 0.0.0.0 --port 8000```
### Run the Frontend
To start the frontend, while in the ```public/``` directory, simply run with

```npm run dev```
## Other usefull resources
- [CSS Foil Card Effect](https://deck-24abcd.netlify.app/)