import os.path

import requests
from flask import Flask, request, render_template, url_for, redirect

from FinancePlanning.Logic.UserService import UserService
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.TableRepository import TableRepository
from FinancePlanning.UOF.TableUnitOfWork import TableUnitOfWork

xml_repo_path = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning\\xml"
json_repo_path = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning\\JSON"

app = Flask(__name__)


@app.route("/user/<int:user_id>")
def get_user(user_id):
    uof = TableUnitOfWork(User)

    with uof:
        user = uof.batches.GetById(user_id)

        if user is None:
            return dict(), 404

        return user.object_to_dict()


@app.route("/user/add", methods=["POST"])
def add_user():

    uof = TableUnitOfWork(User)
    uservice = UserService(uof)

    data = request.json
    user = uservice.add_user(data["name"], data["surname"])

    return {"user": user}


@app.route("/user/form", methods=["GET", "POST"])
def user_form():
    if request.method == "POST":
        path = "http://localhost:5000" + url_for("add_user")
        response = requests.post(path, json=request.form)
        return render_template("input.html", response=response)
    else:
        return render_template("input.html")


# @app.route("/user/add")
# def get_user(userData):
#     # uof = TableUnitOfWork(User)
#     # userService = UserService(uof)
#     #
#     # userService.add_user(userData["name"], userData["surname"])
#
#     return url_for('user_form')


if __name__ == '__main__':
    app.run()
