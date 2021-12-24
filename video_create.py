import json
from moviepy.editor import *

def createClip(audio, image, videoFileName, fps):
    audio = AudioFileClip(audio)
    clip = ImageClip(image).set_duration(audio.duration + 1)
    clip = clip.set_audio(audio)
    clip.write_videofile(videoFileName, fps=fps)
    return clip

def generate(fps):
    commentFile = open("temp/comments.json")
    comments = json.load(commentFile)

    clips = []

    clips.append(createClip(f"audio/main_post.mp3", f"images/main_post.png", f"videos/main_post.mp4", fps))

    i = 0
    for comment in comments["comments"]:
        i += 1
        clips.append(createClip(f"audio/{i}.mp3", f"images/{i}.png", f"videos/{i}.mp4", fps))

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("product/final.mp4", fps=fps)