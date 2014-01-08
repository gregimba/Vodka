from fabric.api import run, local

def setup():
    local("chmod 700 app.py")

def server():
    local("python app.py")