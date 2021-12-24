import json
from PIL import Image, ImageDraw, ImageFont
import textwrap

def wrapDrawText(draw, text, font, y):
    lines = textwrap.wrap(text=text, width=40)
    text = y

    for line in lines:
        width, height = font.getsize(line)
        draw.text(((1920 - width) / 2, text), line, (0, 0, 0), font=font)
        text += height

def drawMainPost(font):
    commentFile = open("temp/comments.json")
    comments = json.load(commentFile)
    image = Image.new('RGB', (1920, 1080), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    wrapDrawText(draw, comments["main_post"][0]["author"], font, 150)
    wrapDrawText(draw, comments["main_post"][0]["title"], font, 200)
    wrapDrawText(draw, comments["main_post"][0]["description"], font, 400)
    image.save(f"images/main_post.png", "PNG")


def generate():
    commentFile = open("temp/comments.json")
    comments = json.load(commentFile)
    font = ImageFont.truetype("temp/arial.ttf", 40)

    drawMainPost(font)

    i = 0
    for comment in comments["comments"]:
        i += 1
        image = Image.new('RGB', (1920, 1080), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        wrapDrawText(draw, comment["author"] + ": " + comment["comment"], font, 400)

        image.save(f"images/{i}.png", "PNG")