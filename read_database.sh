#! /usr/bin/expect

spawn python manage.py shell

expect ">>>"
send "from Article.models import Article\n"

expect ">>>"
send "from security import backends\n"

expect ">>>"
send "backends.read_database(Article, 'title', 'title')\n"

interact

