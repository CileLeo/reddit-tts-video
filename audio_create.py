from gtts import gTTS
import json

def generate(accent):
    commentFile = open("temp/comments.json")
    comments = json.load(commentFile)
    language = accent

    text = comments["main_post"][0]["author"] + " says, " + comments["main_post"][0]["title"] + ". " + comments["main_post"][0]["description"]
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save(f"audio/main_post.mp3")

    i = 0
    for comment in comments["comments"]:
        i += 1

        text = comment["author"] + " says.... " + comment["comment"]
        audio = gTTS(text=text, lang=language, slow=False)
        audio.save(f"audio/{i}.mp3")