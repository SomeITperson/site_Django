# """
# WSGI config for shop project.
#
# It exposes the WSGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
# """
#
# import os, sys
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
#
# #путь к проекту
# sys.path.append('/home/u/username/public_html')
# #путь к фреймворку
# sys.path.append('/home/u/username/')
# #путь к виртуальному окружению
# sys.path.append('/home/u/username/.djangovenv/lib/python3.8/site-packages/')
# #исключить системную директорию
# sys.path.remove('/usr/lib/python3.8/site-packages')
# os.environ["DJANGO_SETTINGS_MODULE"] = "SWeb_DjangoSite.settings"
#
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()