from datetime import datetime #???
laiks=str(datetime.now().time())
print(laiks)
if "6"<laiks<"12":
    print("Labrīt!")
elif "12"<laiks<"17":
    print("Labdien!")
else:
    print("Labvakar!")