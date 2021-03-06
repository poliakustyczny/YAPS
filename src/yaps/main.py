import sys
from tkinter import Tk

from logger import Logger
from yaps import Yaps
from gui import Gui

def runGui(app):
    root = Tk()
    root.title('YAPS - Yet Another Picture Sorter')
    root.configure(bg=Gui.MAIN_BACKGROUND)
    gui = Gui(root, app)
    root.mainloop()

def runCli(app):
    app.setDirectory(sys.argv[2])
    if(len(sys.argv) > 3):
        app.setOutputDirectory(sys.argv[3])
    if sys.argv[1] == 'copy':
        app.iterateFiles()
    elif sys.argv[1] == 'check':
        app.checkDuplicates()
    else:
        app.help()

    print(app.logger.getLog())
    app.logger.clearLog()

logger = Logger()
app = Yaps(logger)

if(len(sys.argv) > 1):
    if sys.argv[1] == '--gui' or sys.argv[1] == '-g':
        runGui(app)
    else:
        runCli(app)
else:
    raise Exception('Not enough parameters')




