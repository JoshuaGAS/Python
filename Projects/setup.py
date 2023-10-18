from setuptools import setup

APP = ['ClipBoardManager.py']  # Replace with the name of your Python script
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'pyperclip'],  # Correct package names
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
