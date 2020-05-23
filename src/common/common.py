import os
from pathlib import Path

def generate_license(mylicense):
    import sample_files.license as get_license
    f = open("LICENSE","w+")
    if mylicense == "mit":
        f.write(get_license.mit())
        f.close()


def check_if_exist(path, name):
    full_path = path + name
    exist = os.path.exists(full_path)
    if exist:
        print("The directory %s already exist" % config('MYNAME', default="DefaultName"))
        return exist
    return exist
