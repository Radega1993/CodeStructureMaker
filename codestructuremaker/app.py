# Include standard modules
import argparse
import sys
import logging


def codestructuremaker_main():
    # loggin system
    logging.basicConfig(filename='log', level=logging.DEBUG)

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

    if len(sys.argv) == 1:
        from pyfiglet import Figlet
        f = Figlet(font='slant')
        print(f.renderText('CSM'))
        print("Language list")
        for language in valid_languages:
            print("- "+ language)
        while True:
            args.language = input("Please chose language: ")
            if args.language not in valid_languages:
                print("Not supported language")
            else:
                break
        args.name = input("Please chose projectName: ")


        args.license = input("Please chose license: (defaul: None) ")
        if args.license not in valid_licenses:
            print("Not supported license, we use default")
            args.license = None

    # Check args
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

    return 0

if __name__ == '__main__':
    codestructuremaker_main()
