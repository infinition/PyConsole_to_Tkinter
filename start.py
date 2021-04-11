from gui import *
from program import *

if __name__ == '__main__':
    program = Program()
    gui_thread = Gui(program)
    gui_thread.run()
