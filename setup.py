import os
key = "'" + str(os.urandom(24)) + "'"
config = open("config.cfg", "w")

standard = """DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'"""

keyVar = 'SECRET_KEY = ' + key

print keyVar

config.write(standard + '\n' + keyVar)
config.close()