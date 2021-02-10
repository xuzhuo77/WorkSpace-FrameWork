import os
import sys
from PyQt5.QtWidgets import *

<<<<<<< .mine

||||||| .r96
=======
from examples.example_calculator.Test_CalculatorWindow import Test_CalculatorWindow

>>>>>>> .r107
sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from examples.example_calculator.test_calc_window import Test_CalculatorWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # print(QStyleFactory.keys())
    app.setStyle('Fusion')

    wnd = Test_CalculatorWindow()
    wnd.show()
    wnd.onFileNew()
    wnd.addTestNodes()

    sys.exit(app.exec_())
