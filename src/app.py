# Include standard modules
import argparse

# Initiate the parser
parser = argparse.ArgumentParser(description="Create default code project structure automaticaly")
valid_licenses = [None, "mit"]
valid_languages = ["python", "webproject", "cpp", "c", "nodejs"]


# Add long and short argument
parser.add_argument("--language", "-l", choices=valid_languages, help="Set the language of the project")
parser.add_argument("--name", "-n", help="Set the name of the project")
parser.add_argument("--license", "-li", default=None, choices=valid_licenses, help="Set the license of the project")
#parser.add_argument("--path", "-p", help="Set the path of the project")

# Read arguments from the command line
args = parser.parse_args()

# Check for --width
if (args.language and args.name):
    if args.language == "python":
        from languages.python import Python
        Python(args.name, args.license)
    if args.language == "webproject":
        from languages.webproject import WebProject
        WebProject(args.name, args.license)
    if args.language == "cpp":
        from languages.cpp import CPP
        CPP(args.name, args.license)
    if args.language == "c":
        from languages.c import C
        C(args.name, args.license)
    if args.language == "nodejs":
        from languages.nodejs import Nodejs
        Nodejs(args.name, args.license)
else:
    print("Language and project name are compulsary")
