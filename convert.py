import os, json

dirs = os.listdir("emotes")

print(dirs)
with open("emotes.json", "w") as f:
    f.write(json.dumps(dirs))

for emote in dirs:
    orig = "emotes/"+emote+"/orig.png"

    for size in range(0,12):
        out = "emotes/"+emote+"/"+str(size)+".png"

        os.system("convert " + orig + " -resize " + str(size+1) + " " + out)

    print(emote)

