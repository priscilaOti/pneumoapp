# TGI - Pneumonia  

# Preparing the environment
```sh
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export DATABASE_URL='postgresql://user:password@localhost:5432/pneumoapp'
```

# Run Application
```sh
flask run
```


# List routes
```sh
flask routes
# Endpoint                 Methods  Rule
# -----------------------  -------  -------------------------
# classifiers.get_results  POST     /api/classifiers/predict/
```
    