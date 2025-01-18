# Warehouse

Simple warehouse application, developed in one day to revisit Flask skills.

## Features

This application has:

- simple warehouse with editable entries and auto-created history
- server-side rendering with additional modern JavaScript and CSS
- server-side translations provided by flask-babel
- client-side filtering, searching and printing
- support for user locale and timezone when rendering dates and numbers
- good look and feel without external libraries such as bootstrap
- basic docker compose configuration with gunicorn as a WSGI server
- sqlite for persistence, which should be enough for single user purpose
- well organized code (directories, blueprints, split into multiple files)
