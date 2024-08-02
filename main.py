import os
for file in os.listdir("."):
    if file.endswith(".exe") and file.startswith("setup"):
        print(os.path.join(".", file))
        os.system("start "+os.path.join(".", file)+" /SILENT")
