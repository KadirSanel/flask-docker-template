# Flask & Postgresql Docker Template

Docker template for flask api projects and postgresql

## Installation
You have to edit your configurations first. After that, you can run the docker images by typing the codes below into the terminal.
```bash
sudo chmod +x ./service.sh
sudo ./service.sh install
```

## Configurations
Add the python libraries you want to add to the requirements.txt file.
```requirements.txt
requirements.txt 

click==8.0.3
colorama==0.4.4
Flask==2.0.2
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
Werkzeug==2.0.2
gunicorn==20.1.0
```

Write your own migrations to the database migration file.
```sql
0001_inital.sql

CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    user_name varchar(255),
    user_phone varchar(255),
    user_mail varchar(255),
    user_mail varchar(255),
    user_register_date timestamp,
)
```

Edit config.ini for database configuration.
```ini
config.ini

[DATABASE]
host=
port=
user=
pass=
db_name=
```

To change the default password in Postgresql, put your own password in the service.sh file where it says 'api_db' in the code POSTGRES_PASSWORD=api_db in the section below.
```bash
service.sh

...
if [ "$1" == "createdb" ]
then
    systemctl stop postgresql
    docker run --name api_db -e POSTGRES_PASSWORD=api_db -d -p 5432:5432 -v /volumes/api_db/data:/var/lib/postgresql/data  postgres
fi
...
```

## Starting Server
To start the server, first configure it. Then you can start the services by entering the following codes into the terminal.
```bash
sudo ./service.sh createdb
sudo ./service.sh rundb
sudo ./service.sh build
sudo ./service.sh migrate
sudo ./service.sh runserver
```

## Stoping Servis/Servises
To terminate all services:
```bash
sudo ./service.sh stopall
```
To terminate postgresql containers:
```bash
sudo ./service.sh stopdb
```
To remove postgresql containers:
```bash
sudo ./service.sh removedb
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
