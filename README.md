<!-- start project-info -->
<!--
project_title: CodeStructureMaker
github_project: https://github.com/Radega1993/CodeStructureMaker
license: MIT
icon: img/logo.svg
homepage: https://www.radega.com
license-badge: True
lastcommit-badge: True
codefactor-badge: True
--->

<!-- end project-info -->

<!-- start badges -->

![License MIT](https://img.shields.io/badge/MIT-license-green)
![Last commit](https://img.shields.io/github/last-commit/Radega1993/CodeStructureMaker)
[![CodeFactor](https://www.codefactor.io/repository/github/radega1993/codestructuremaker/badge)](https://www.codefactor.io/repository/github/radega1993/codestructuremaker)
<!-- end badges -->

<!-- start description -->
<h1 align="center">This is <span id="project_title">CodeStructureMaker</span> 👋</h1>
<p>
<a href="https://www.radega.com" id="homepage" rel="nofollow">
<img align="right" height="128" id="icon" src="img/logo.svg" width="128"/>
</a>
</p>
<h2>CodeStructureMaker</h2>
<p><span id="project_title">CodeStructureMaker</span> is a command line application to create folders structure and no waste time to start coding.

<!-- end description -->

<!-- start prerequisites -->
## Prerequisites

Any prerequisites for this project

<!-- end prerequisites -->

<!-- start using -->
## Using <span id="project_title">CodeStructureMaker</span>

### Dev enviroment

- First copy `.env_example` to `.env` to define enviroment variables
```
cp .env_example .env
```

- Modify the file with your data:
```
MYPATH=path
ACCES_RIGHT=0o755
MYNAME=myname
MYURL=url
MYEMAIL=email
LICENSENAME=namesurname
```

- Create a virtual enviroment:
```
python3 -m venv venv
```

- Activate virtual enviroment:
```
source myenv/bin/activate
```

- Install required package:
```
pip install -Ur requirements.txt
```

Example of usage:
```
python src/app.py -l python -n testproject
```

Structure generated:

- Project_name
  - docs
    - ***index.md***
  - src
    - ***\_\_init\_\_.py***
    - ***app.py***
  - test
    - ***.gitkeep***
  - ***README.md***
  - ***requirements.txt***
  - ***setup.py***
  - ***.gitignore***

To start **<span id="project_title">CodeStructureMaker</span>** just open a command line/terminal (`Ctrl+Alt+T`),

Right now, python is the only language avaliable but i'm working in other languages.

### Valid options

| long | short | Description |
| ---: | :---: | :---------- |
| --help | -h | Show options table and exit |
| --language | -l | Set the language of the project |
| --name | -n | Set the name of the project |
| --license | -li | [optional] Set the license of the project |

### Valid languages

- python
- webproject (html/css/js)
- c
- cpp

### Valid licenses

- None
- MIT

<!-- end using -->


## Structures generated

### Python
![python](img/python_structure.png)

### Web Projet
![webproject](img/webproject_structure.png)

<!-- start contributing -->
## Contributing to <span id="project_title">CodeStructureMaker</span>

To contribute to **<span id="project_title">CodeStructureMaker</span>**, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <branch_name>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

<!-- end contributing -->
