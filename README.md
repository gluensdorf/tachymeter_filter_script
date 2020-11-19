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