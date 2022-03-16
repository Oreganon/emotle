import os, sys

lines = []

with open("ffz", "r") as f:
    lines = f.readlines()


for line in lines:
    [url, emote] = line.replace("\n","").split(" ")

    try:
        os.mkdir("../emotes/" + emote)
    except:
        pass

    os.system("wget " + url + " -O ../emotes/" + emote + "/orig.png")

