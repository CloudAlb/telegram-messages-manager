# Initial Setup

## Install Python

- (With Python available on system with Mise) `pip install --user pipx`

## Install Poetry

- https://python-poetry.org/
- `pipx install poetry`

## Install dependencies

- `https://python-poetry.org/docs/basic-usage/#installing-dependencies-only`

## Run the Editor

- `./runEditor.sh`

## Setup .env file

- Example:

```
api_id=1234
api_hash="foo"
bot_token="bar"
```

## Run the program

- `./runDev.sh`

## Build the Docker image for the project

- `./buildDockerImage.sh`
