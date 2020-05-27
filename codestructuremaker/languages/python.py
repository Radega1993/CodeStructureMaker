from decouple import config
import os
import shutil
from pathlib import Path
import common.common as common

class Python(object):
    """docstring for Python."""

    def __init__(self, name, mylicense):
        super(Python, self).__init__()
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

            os.mkdir('docs', self.access_rights)
            Path('docs/index.md').touch()
            print("Creating documentation folder")

            os.mkdir('test', self.access_rights)
            Path('test/.gitkeep').touch()
            print("Creating test folder")

            projectfolder = self.project_name.lower()
            os.mkdir(projectfolder, self.access_rights)
            Path(projectfolder+'/__init__.py').touch()
            Path(projectfolder+'/app.py').touch()
            print("Creating src folder")

            Path('requirements.txt').touch()
            Path('.gitignore').touch()
            add_gitignore = self.git_ignore()
            Path('setup.py').touch()
            add_setup_content = self.setup_file()

            Path('README.md').touch()

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


    def git_ignore(self):
        import sample_files.gitignore.python as text
        f = open(".gitignore","w+")
        f.write(text.python_gitignore)
        f.close()


    def setup_file(self):
        text = "" \
        "#!/usr/bin/env python\n" \
        "\n" \
        "from distutils.core import setup\n" \
        "\n" \
        "setup(name='Distutils',\n" \
        "      version='1.0',\n" \
        "      description='<description>',\n" \
        "      author=" + "'" + self.myname + "',\n" \
        "      author_email=" + "'" + self.myemail + "',\n" \
        "      url=" + "'" + self.myurl + "',\n" \
        "      packages=['distutils', 'distutils.command'],\n" \
        "     )"

        f = open("setup.py","w+")
        f.write(text)
        f.close()
