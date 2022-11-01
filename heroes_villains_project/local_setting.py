# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^a2h(7zh4wthil*$%4ze(u0w!)(&k3^$9uzdl96hravq!*yv_y'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password99!'
    }
}