#!/usr/bin/env python
import os

DB_PORT = int(os.environ["OPENSHIFT_MYSQL_DB_PORT"])
DB_HOST = os.environ["OPENSHIFT_MYSQL_DB_HOST"]
DB_PASSWD = os.environ["OPENSHIFT_MYSQL_DB_PASSWORD"]
DB_USER = os.environ["OPENSHIFT_MYSQL_DB_USERNAME"]
DB_ENGINE = "peewee.MySQLDatabase"
DB_NAME = "class6"
