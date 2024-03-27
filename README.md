## Alarme ALU - Arithmetic Logic Unit demonstration


```sh
# 1 - Create environment
python -m venv venv

# 2 - install dependencies
pip install -r requirements.txt

# 3 - Config environment variable flask app (Linux | Mac)
export FLASK_ENV="development"; export FLASK_APP=main.py; export FLASK_DEBUG=True

# 3.1 - Config environment variable flask app (Windows)
$Env:FLASK_ENV="development"; $Env:FLASK_APP=main.py; $Env:FLASK_DEBUG=True

# 4 - Run the project
flask run

# Or

python main.py
```