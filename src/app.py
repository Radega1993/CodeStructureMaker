# Include standard modules
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--language", "-l", help="Set the language of the project")
parser.add_argument("--name", "-n", help="Set the name of the project")
#parser.add_argument("--path", "-p", help="Set the path of the project")

# Read arguments from the command line
args = parser.parse_args()

# Check for --width
if (args.language and args.name):
    from languages.python import Python
    Python(args.name)
else:
    print("Language and project name are compulsary")
