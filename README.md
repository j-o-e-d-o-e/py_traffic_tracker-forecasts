# traffic_tracker_forecasts

Rest service for [traffic-tracker-api](https://github.com/j-o-e-d-o-e/traffic_tracker_api) providing forecasts.

### endpoints
- `http://localhost:8000/planes` fetches forecasts from db
- `http://localhost:8000/planes/predict` predicts, saves and fetches forecasts

### api-calls via httpie-lib
- `http localhost:8000/planes` shows all forecasts
- `http localhost:8000/planes/predict` predicts and shows all forecasts

### general
- `python3 manage.py shell` opens shell
- `python3 manage.py runserver` starts dev-server
- `sqlite3 db.sqlite3` opens db-cli
    - `.tables` shows all tables
    - `select * from planes_day;` shows all daily forecasts
    - `select * from planes_hour;` shows all hourly forecasts

## deployment on heroku
- `heroku apps:create traffic-tracker-forecasts --region eu` prepares Heroku to receive source code
- `git push heroku master` deploys code
- `heroku ps:scale web=1` ensure at least one instance of the app is running (optional...?)


### Materials
- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)
- [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)
