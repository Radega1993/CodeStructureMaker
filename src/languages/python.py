import config.config as cfg
import os
import shutil
from pathlib import Path

class Python(object):
    """docstring for Python."""

    def __init__(self, name):
        super(Python, self).__init__()
        self.name = name

        if not self.check_if_exist():
            create_structure = self.make_structure()


    def check_if_exist(self):
        full_path = cfg.path + self.name
        exist = os.path.exists(full_path)
        if exist:
            print("The directory %s already exist" % self.name)
            return exist
        else:
            return exist


    def make_structure(self):
        try:
            #define working directory from congif var
            os.chdir(cfg.path)
            #create root project directory
            os.mkdir(self.name, cfg.access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % self.name)
        else:
            print ("Successfully created the directory %s " % self.name)

        # Creating all default structure
        try:
            #working on root directory
            os.chdir(self.name)

            os.mkdir('docs', cfg.access_rights)
            Path('docs/index.md').touch()
            print("Creating documentation folder")

            os.mkdir('test', cfg.access_rights)
            Path('test/.gitkeep').touch()
            print("Creating test folder")

            os.mkdir('src', cfg.access_rights)
            Path('src/__init__.py').touch()
            Path('src/app.py').touch()
            print("Creating src folder")

            Path('requirements.txt').touch()
            Path('.gitignore').touch()
            add_gitignore = self.git_ignore()
            Path('setup.py').touch()
            add_setup_content = self.setup_file()

            Path('README.md').touch()
            print("Creating default files")
        except OSError:
            print ("Creation of the structure for project %s failed" % self.name)
            os.chdir(cfg.path)
            shutil.rmtree(self.name)
        else:
            print ("Successfully created the structure for project %s " % self.name)


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
        "      author=" + "'" + cfg.my_name + "',\n" \
        "      author_email=" + "'" + cfg.my_email + "',\n" \
        "      url=" + "'" + cfg.my_url + "',\n" \
        "      packages=['distutils', 'distutils.command'],\n" \
        "     )"

        f = open("setup.py","w+")
        f.write(text)
        f.close()
