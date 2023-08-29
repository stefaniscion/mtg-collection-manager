# mtg-collection-manager
mtg-collection manager is a fast and lightweight web application to manage your Magic: The Gathering card collection.

It Uses FastApi and PostgeSQL to be the fastest possible, then all data are fetched from Skryfall API and cached in the database.
## State of completion
WIP
## Features
I've used those technologies to build this project:
- [FastAPI](https://fastapi.tiangolo.com/) - Backend Framework
- [SvelteKit](https://svelte.dev/) - Frontend Framework
- [Tailwind](https://tailwindcss.com/) - CSS Framework
- [PostgreSQL](https://www.postgresql.org/) - Database
## Installation through Docker
I suggest you to use Docker to run this project, it's the easiest way to run it.
I have prepared a docker-compose file to run the project with all needed containers.

First you have to prepare install the frontend manualy, because of some issues with bindings.

Cd into the ```frontend/``` directory and run the following command:
```sh
npm install
```
So return to the root directory and run the following command:
```sh
docker-compose up --build
```
And you are ready to go!
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

In my installation i used mamba so i done
```sh
mamba install --file requirements.txt
```
#### Unsupported methods
You can try as well with pip:
```sh
pip install -r requirements.txt
```
Or with conda:
```sh
conda install --file requirements.txt
```
But i didn't assure that it will work. Probably you will need to edit the requirements.txt file to make it work.
### Frontend
You must install all needed packages, cd into the ```frontend/``` directory and run the following command:
```sh
npm install
```
## Usage
### Run the Backend
To run the Backend do the following command in the ```app/``` directory:
```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
### Run the Frontend
To start the frontend, while in the ```public/``` directory, simply run with
```sh
npm run dev
```
## Other usefull resources
- [PowerTables](https://github.com/muonw/muonw-powertable) - DataTable component for SvelteKit
- [CSS Foil Card Effect](https://github.com/simeydotme/pokemon-cards-css) - Cool TCG Card inspect with foil effects (Missing source code :C)