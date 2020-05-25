from decouple import config
import os
import shutil
from pathlib import Path
import common.common as common

class Nodejs(object):
    """docstring for Nodejs."""

    def __init__(self, name, mylicense):
        super(Nodejs, self).__init__()
        self.project_name = name
        self.license = mylicense
        self.myname = config('MYNAME', default="DefaultName")
        self.mypath = config('MYPATH')
        self.access_rights = int(config('ACCES_RIGHT', default=0o755),8)
        self.myemail = config('MYEMAIL', default="default@defaultmail.com")
        self.myurl = config('MYURL', default="www.sampleurl.com")

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

            os.mkdir('src', self.access_rights)
            Path('src/app.js').touch()
            print("Creating src folder")

            Path('package.json').touch()
            add_package_json_content = self.package_json_file()
            Path('.gitignore').touch()
            add_gitignore = self.git_ignore()

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
        import sample_files.gitignore.node as text
        f = open(".gitignore","w+")
        f.write(text.node_gitignore)
        f.close()


    def package_json_file(self):
        text = "" \
        "{\n" \
        "  \"name\": \"" +self.project_name +"\",\n" \
        "  \"version\": \"1.0.0\",\n" \
        "  \"description\": \"\",\n" \
        "  \"main\": \"src/app.js\",\n" \
        "  \"scripts\": {\n" \
        "      \"test\": \"echo \\\"Error: no test specified\\\" && exit 1\"\n" \
        "  },\n" \
        "  \"author\": \"" + self.myname + "\",\n" \
        "  \"license\": \"ISC\"\n" \
        "}\n"

        f = open("package.json","w+")
        f.write(text)
        f.close()
