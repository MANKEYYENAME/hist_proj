from os import listdir
from os.path import isfile, join

img_path = "images/"

onlyfiles = [f for f in listdir(img_path) if isfile(join(img_path, f))]

onlyfiles = sorted(onlyfiles)

print(onlyfiles)

f = open("text.txt", "r", encoding="utf-8")

names = []
for l in list(f.readlines()):
    l = l.split(":")[1].strip()
    names += [l]

header = """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="style.css">
</head>
<body>
"""

end = """
</body>
</html> 
"""

doc = ""

for i in range(0, len(onlyfiles)):
    line = f"""
        <div class="container">
            <img src="images/{onlyfiles[i]}" alt="image"> 
            <div class="textd">
                {names[i]} 
            </div>
        </div>
    """
    doc += line

doc = header + doc + end

open("index.html", "w", encoding="utf-8").write(doc)