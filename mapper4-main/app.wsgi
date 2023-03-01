import sys
sys.path.insert(0, '/home/student-user/demos/flaskheroku')

activate_this = '/home/student-user/.local/share/virtualenvs/student-user-ylEI8pvg/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file.read(), dict(__file__=activate_this))

from app.main import app as application