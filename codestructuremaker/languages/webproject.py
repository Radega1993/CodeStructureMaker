from decouple import config
import os
import shutil
from pathlib import Path
import common.common as common

class WebProject(object):
    """docstring for WebProject."""

    def __init__(self, name, mylicense):
        super(WebProject, self).__init__()
        self.project_name = name
        self.license = mylicense
        self.myname = cfg.MYNAME
        self.mypath = cfg.MYPATH
        self.access_rights = int(cfg.ACCES_RIGHT,8)
        self.myemail = cfg.MYEMAIL
        self.myurl = cfg.MYURL

        empty = ''
        if self.mypath is not empty:
            if not common.check_if_exist(self.mypath, self.myname):
                create_structure = self.make_structure()
        else:
            print("Define a root path in env file to create a project")


    def make_structure(self):
        try:
            #define working directory from congif var
            os.chdir(self.mypath)
            #create root project directory
            os.mkdir(self.project_name, self.access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % self.project_name)
        else:
            print ("Successfully created the directory %s " % self.project_name)

        # Creating all default structure
        try:
            #working on root directory
            os.chdir(self.project_name)

            os.mkdir('css', self.access_rights)
            Path('css/style.css').touch()
            content = "h1 {text-align: center;}\np {text-align: center;}\n.center {\n  display: block;\n  margin-left: auto;\n  margin-right: auto;\n  width: 30%;\n}"
            f = open("css/style.css","w+")
            f.write(content)
            f.close()
            print("Creating css folder")

            os.mkdir('docs', self.access_rights)
            Path('docs/index.md').touch()
            print("Creating documentation folder")

            os.mkdir('js', self.access_rights)
            Path('js/main.js').touch()
            print("Creating js folder")

            os.mkdir('img', self.access_rights)
            os.mkdir('img/favicon', self.access_rights)
            Path('img/favicon/.gitkeep').touch()
            os.mkdir('img/home', self.access_rights)
            Path('img/home/.gitkeep').touch()
            print("Creating img folder")

            os.mkdir('fonts', self.access_rights)
            Path('fonts/.gitkeep').touch()
            print("Creating fonts folder")

            os.mkdir('scss', self.access_rights)
            Path('scss/main.scss').touch()
            print("Creating scss folder")

            Path('index.html').touch()
            add_index_content = self.index_file()

            if self.license is not None:
                Path('LICENSE').touch()
                get_license = common.generate_license(self.license)

            print("Creating default files")

        except OSError:
            print ("Creation of the structure for project %s failed" % self.project_name)
            os.chdir(self.mypath)
            shutil.rmtree(self.project_name)
        else:
            print ("Successfully created the structure for project %s " % self.project_name)


    def index_file(self):
        import sample_files.html as text
        f = open("index.html","w+")
        f.write(text.html_structure)
        f.close()
