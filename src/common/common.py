import os
from pathlib import Path

def generate_license(mylicense):
    import sample_files.licenses.license as mylicense
    print(license)
    f = open("LICENSE","w+")
    if license == "mit":
        print("in: "+ license)
        f.write(mylicense.mit())
        f.close()


def check_if_exist(path, name):
    full_path = path + name
    exist = os.path.exists(full_path)
    if exist:
        print("The directory %s already exist" % config('MYNAME', default="DefaultName"))
        return exist
    return exist
