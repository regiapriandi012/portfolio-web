# Django Portfolio App

![django-nginx (2)](https://user-images.githubusercontent.com/69528812/224481785-a624287d-463b-4b64-8efb-01b06a988ab8.jpg)

#

## Deployments
> #### [Deploy Local Machine](#deploy-local-machine-1)
> #### [Deploy Docker (Docker Compose)](#deploy-docker-docker-compose-1_
> #### [Deploy Kubernetes](#deploy-kubernetes-1)

#

# Deploy Local Machine
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
