from flask import Flask

app = Flask(__name__)

# from project.db_management import add_student_if_not_exists, check_if_student_exist
from server import routes, forms, config, models, utils