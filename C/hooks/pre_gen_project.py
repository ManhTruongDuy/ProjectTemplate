import os
import json
import datetime

username = os.environ.get("USERNAME", "user")
today = datetime.date.today().strftime("%Y%m%d")

data = {
    "project_name": f"{username}_c_project",
    "author": username
}

with open("cookiecutter.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
