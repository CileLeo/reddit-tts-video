import tkinter as tk
import praw
import audio_create, comment_get, image_create, video_create

# MAKING A UI. WIP.


reddit = praw.Reddit(
    user_agent="",
    client_id="",
    client_secret="",
)

window = tk.Tk()

button = tk.Button(window, text ="Render Video")
button.pack()

window.mainloop()
#comment_get.generate("rmdwsr", 3, reddit)
#image_create.generate()
#audio_create.generate("en")
#video_create.generate(10)