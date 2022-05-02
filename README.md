Squirrel bot
------------

A just-for-fun Discord bot that replies with a 🐿️  emoji to each message sent in the server.

It was made out of boredom a bloomy sunday afternoon, so no special quality requirements were set


The structure of the project is as follows:

* All the logic is in the `main.py` file.
* The `Procfile` is needed by Heroku to start the web process
* `requirements.txt` and `runtime.txt` are also needed by Heroku for the Python buildpack
* The `pyproject.toml` and `poetry.lock` are a result of `Poetry` being used for virtual environment and dependencies management