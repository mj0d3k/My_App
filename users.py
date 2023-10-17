import argparse

from psycopg2 import connect, OperationalError
from psycopg2.errors import UniqueViolation

from clcrypto import hash_password
from models import User

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-n", "--new_pass", help="new password (min 8 characters)")
parser.add_argument("-l", "--list", help="list of users", action="store_true")
parser.add_argument("-d", "--delete", help="delete an user", action="store_true")
parser.add_argument("-e", "--edit", help="edit an user", action="store_true")

args = parser.parse_args()

def edit_user():
    pass

def create_user():
    if args.username

def edit_password():
    pass

def delete_user():
    pass

def list_of_users():
    pass

def print_help():
    pass

print(args.username)