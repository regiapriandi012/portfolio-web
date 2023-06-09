# Django Portfolio App

![django-nginx (3)](https://user-images.githubusercontent.com/69528812/224524889-8b40a446-487c-4e78-ba01-1e8cf2aa5b66.jpg)

#

## Deployments
> #### [Deploy Local Machine](#deploy-local-machine-1)
> #### [Deploy Docker (Docker Compose)](#deploy-docker-docker-compose-1)
> #### [Deploy Kubernetes](#deploy-kubernetes-1)

#

# Deploy Local Machine

### Configure virtualenv

```
$ python3 -m venv webfortoenv
$ source webfortoenv/bin/activate
$ pip install -r requirements.txt
```

### Configure static root in django

```
sudo nano webforto/settings.py
```

```
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

### Collect static files

```
python manage.py collectstatic
```

### Testing gunicorn

```
gunicorn --bind 0.0.0.0:8000 webforto.wsgi
```

### Creating systemd Socket and Service Files for Gunicorn

```
sudo nano /etc/systemd/system/gunicorn.socket
```

```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=regiapriandi
Group=www-data
WorkingDirectory=/home/regiapriandi/PythonProjects/Bismillahirrahmanirrahim/BismillahProject/web-porto/webforto
ExecStart=/home/regiapriandi/PythonProjects/Bismillahirrahmanirrahim/BismillahProject/web-porto/webforto/webfortoenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          webforto.wsgi:application

[Install]
WantedBy=multi-user.target
```

### Apply the systemd unit file and gunicorn socket

```
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

### Check the succesfully config of the gunicorn.socket

```
curl --unix-socket /run/gunicorn.sock localhost
```

## Configure nginx

### Create a new server block file

```
sudo nano /etc/nginx/sites-available/webforto
```

```
server {
    listen 80;
    server_name 172.18.37.21;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/regiapriandi/PythonProjects/Bismillahirrahmanirrahim/BismillahProject/web-porto/webforto;
    }

    location /media/ {
        root /home/regiapriandi/PythonProjects/Bismillahirrahmanirrahim/BismillahProject/web-porto/webforto;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

### Enable the server block

```
sudo ln -s /etc/nginx/sites-available/webforto /etc/nginx/sites-enabled
```

### Test the Nginx configuration

```
sudo nginx -t
```

#

# Deploy Docker (Docker Compose)

### Configure docker compose

![container docker compose](https://user-images.githubusercontent.com/69528812/224495726-e9421919-fdf0-4ab2-b887-746d26a4bcc8.jpg)

### Apply Configuration

```
$ docker-compose up --build -d
[+] Running 3/0
 ⠿ Container webforto-db-1     Running                                                                                                0.0s
 ⠿ Container webforto-web-1    Running                                                                                                0.0s
 ⠿ Container webforto-nginx-1  Running                                                                                                0.0s
```

### Check Deployment
![image](https://user-images.githubusercontent.com/69528812/224495967-1dba4920-ad0b-467f-8474-ba90c29989b8.png)

#

# Deploy Kubernetes

## (Soon)
