## Alarme ULA demonstration

```sh
# 1 - Create environment
python -m venv venv

# 2 - install dependencies
pip install -r requirements.txt

# 3 - Config flask app
export FLASK_ENV="development"; export FLASK_APP=main.py; export FLASK_DEBUG=True

# 4 - Run the project
flask run
```