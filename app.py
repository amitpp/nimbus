import datetime
from flask import Flask, Response, jsonify
from github import Github

client = Github()
app = Flask(__name__)


@app.route("/")
def welcome():
    message = "Please Provide a Github user's username"
    return jsonify({"Message": message})


@app.route("/<username>")
def get_github_user_details(username):
    try:
        user = client.get_user(username)
    except Exception as e:
        message = "No Such GitHub user exists"
        return jsonify({"Message": message})
    basic_profile_info = {
            "id": user.id,
            "name": user.name,
            "company": user.company,
            "location": user.location,
            "public_repos": user.public_repos,
            "last_modified": user.last_modified
            }
    languages = {}
    commit_counter = 0
    for repo in user.get_repos():
        if repo.parent is None:
            if repo.language not in languages:
                languages[repo.language] = 1
            else:
                languages[repo.language] += 1
        if repo.get_stats_commit_activity():
            for commit in repo.get_stats_commit_activity():
                if commit.last_modified is not None:
                    last_modified_date = datetime.datetime.strptime(
                            commit.last_modified[5: 16], "%d %b %Y")
                    three_months_ago = datetime.datetime.now() - datetime.\
                        timedelta(days=90)
                    if last_modified_date > three_months_ago:
                        commit_counter += 1
    if None in languages:
        del languages[None]
    languages_decreasing = sorted([key for(key, value) in languages.items()],
                                  reverse=True)
    top_languages = languages_decreasing[:3]
    return jsonify({"Basic Profile Information": basic_profile_info,
                    "Top Languages": top_languages,
                    "Number Of Contributions In Last Three Months":
                    commit_counter})


if __name__ == "__main__":
    app.run(debug=True)
