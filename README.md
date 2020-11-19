## Creating the virtual environment (Windows10 + VS code )
- allow execution of scripts:

    `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
- create a virtual environment, e.g. "tachy_gui":

    `py -3 -m venv .tachy_gui`
- activate the created virtual environment "tachy_gui":

    `.\.tachy_gui\Scripts\activate`
- update "tachy_gui":

    `python -m pip install -r .\requirements.txt`
## Minimal HowTo about creating an executable with a GUI using Python under Windows10
- PySimpleGui Cookbook

    https://pysimplegui.readthedocs.io/en/latest/cookbook/

- Example used to create a GUI that lets the user browse to a file:

    https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-get-filename-with-no-input-display-returns-when-file-selected

- Example how to create an .exe from a python script

    https://realpython.com/pysimplegui-python/#packaging-your-pysimplegui-application-for-windows

    Command used to create "tachymeter_filter.exe": 
    
    `pyinstaller --onefile .\main.py --name tachymeter_filter --noconsole`

    When the previous command is executed several new folders will be created in its process. One of them is "dist" in which the "tachymeter_filter.exe"-file can be found.

## TODOs
- Keep application window open, add Quit-Button.
- Print/Show path to newly created file in application window. At the moment the path is shown in the terminal when "main.py" script is executed via python.