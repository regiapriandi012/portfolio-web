# menggunakan image python versi 3.9 sebagai base image
FROM python:3.9-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# buat direktori app dan set sebagai working directory
WORKDIR /app

# install dependensi
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# copy file requirements.txt ke dalam container
COPY requirements.txt .

# install dependensi yang diperlukan
RUN pip install -r requirements.txt

# copy seluruh source code ke dalam container
COPY . .

# jalankan perintah untuk mengumpulkan static files
RUN python manage.py collectstatic --noinput

# jalankan perintah untuk mengubah ownership dan permission
RUN chown -R www-data:www-data /app
RUN chmod -R 755 /app

# expose port 8000
EXPOSE 8000

# jalankan gunicorn sebagai server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "webforto.wsgi:application"]
