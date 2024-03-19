import json
from csv import DictReader

with open("users.json", "r") as f:
    users = json.loads(f.read())

users_pars = []
for i in users:
    user_dict = {}
    user_dict["name"], user_dict["gender"], user_dict["address"], user_dict["age"], user_dict["books"] = i["name"], i["gender"], i["address"], i["age"], []
    users_pars.append(user_dict)

with open("books.csv", newline='') as f:
    reader = DictReader(f)
    g = 0
    for row in reader:
        books_dict = {}
        books_dict["title"], books_dict["author"], books_dict["pages"], books_dict["genre"] = row["Title"], row["Author"], row["Pages"], row["Genre"]
        users_pars[g]["books"].append(books_dict)
        g+=1
        if g == len(users_pars):
            g = 0

with open("result.json", "x") as f:
    s = json.dumps(users_pars, indent=4)
    f.write(s)