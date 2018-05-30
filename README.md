# spaFlaskApp
Tutorial of Angular/TypeScript Python/Flask app

    https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/
    https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-web-apps-part-2/
    https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-web-apps-part-3/

# Build

Copy ./nginx/defaultByIP to /etc/nginx/sites-enabled
and fix `server_name x.x.x.x` to your host

Change `DATABASES` in ./backend/src/settings.py
Create file ./frontend/src/app/env.ts with:

    export const API_URL = 'http://x.x.x.x/api'; #x.x.x.x is a host to api

If you want to build without docker you can now::

    cd ./backend
    virtualenv env -p python3
    source env/bin/activate
    pip install -r requirements.txt
    python ./src/main.py
    # or use: ./run.sh (file must be executable: chmod +x run.sh)

If you want to use Docker you can now::

    Change `map_db` database host in ./docker-compose.yml

    # build the docker container
    docker-compose build

    # run the docker container
    docker-compose up

    # turn it off
    docker-compose down