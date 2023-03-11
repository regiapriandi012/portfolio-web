# Django App
## Configure with nginx and gunicorn

# 

### Configure static root in django

```
$ sudo nano webforto/settings.py
```

```
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

### Collect static files

```
$ python manage.py collectstatic
```

### Testing gunicorn

```
$ gunicorn --bind 0.0.0.0:8000 webforto.wsgi
```


### Creating systemd Socket and Service Files for Gunicorn

```
$ sudo nano /etc/systemd/system/gunicorn.socket
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
$ sudo systemctl start gunicorn.socket
$ sudo systemctl enable gunicorn.socket
```

### Check the succesfully config of the gunicorn.socket

```
$ curl --unix-socket /run/gunicorn.sock localhost
```

## Configure nginx

