import praw
import json

def generate(url_id, comment_amount, reddit):
    reddit = reddit

    submission = reddit.submission(id=url_id)

    data = {}
    data["comments"] = []
    data["main_post"] = []

    data["main_post"].append({
        "description": submission.selftext,
        "title": submission.title,
        "author": submission.author.name,
    })

    i = 0
    for comment in submission.comments:
        if (i >= comment_amount): break
        i += 1

        data["comments"].append({
            "comment": comment.body,
            "author": comment.author.name,
        })

    with open("temp/comments.json", 'w') as f:
        json.dump(data, f)