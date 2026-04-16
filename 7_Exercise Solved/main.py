import os

files = os.listdir("seriesfolder")
i = 1
for file in files:
    if file.endswith('.png'):
      print(file)


    os.rename(f"seriesfolder/{file}", f"seriesfolder/{i}.png")
    i = i + 1