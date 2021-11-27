from PyQt5 import QtCore, QtGui, QtWidgets
import functions

class Ui_func_input(object):
    def setupUi(self, myWindow):
        myWindow.setObjectName("func_input")
        myWindow.resize(631, 481)
        self.centralwidget = QtWidgets.QWidget(myWindow)

        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)

        self.func_input = QtWidgets.QLineEdit(self.centralwidget)
        self.func_input.setGeometry(QtCore.QRect(10, 40, 231, 20))

        self.tolerance_input = QtWidgets.QLineEdit(self.centralwidget)
        self.tolerance_input.setGeometry(QtCore.QRect(410, 410, 113, 20))

        self.iterations_input = QtWidgets.QLineEdit(self.centralwidget)
        self.iterations_input.setGeometry(QtCore.QRect(50, 410, 113, 20))

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(430, 380, 61, 16))
        self.label3.setFont(font)

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 380, 211, 16))
        self.label2.setFont(font)

        self.method_options = QtWidgets.QComboBox(self.centralwidget)
        self.method_options.setGeometry(QtCore.QRect(50, 200, 111, 22))
        self.method_options.addItem("")
        self.method_options.addItem("")
        self.method_options.addItem("")
        self.method_options.addItem("")
        self.method_options.addItem("")

        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(260, 450, 121, 23))

        self.fileName_input = QtWidgets.QLineEdit(self.centralwidget)
        self.fileName_input.setGeometry(QtCore.QRect(380, 40, 201, 20))

        self.method_name_label = QtWidgets.QLabel(self.centralwidget)
        self.method_name_label.setGeometry(QtCore.QRect(340, 160, 180, 20))
        self.method_name_label.setFont(font)
        self.method_name_label.setAlignment(QtCore.Qt.AlignCenter)

        self.range_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.range_input1.setGeometry(QtCore.QRect(270, 220, 113, 20))

        self.range_input2 = QtWidgets.QLineEdit(self.centralwidget)
        self.range_input2.setGeometry(QtCore.QRect(470, 220, 113, 20))

        self.range_label1 = QtWidgets.QLabel(self.centralwidget)
        self.range_label1.setGeometry(QtCore.QRect(260, 200, 131, 20))
        self.range_label1.setFont(font)
        self.range_label1.setAlignment(QtCore.Qt.AlignCenter)

        self.range_label2 = QtWidgets.QLabel(self.centralwidget)
        self.range_label2.setGeometry(QtCore.QRect(510, 200, 31, 16))
        self.range_label2.setFont(font)
        self.range_label2.setAlignment(QtCore.Qt.AlignCenter)

        self.function_rbutton = QtWidgets.QRadioButton(self.centralwidget)
        self.function_rbutton.setGeometry(QtCore.QRect(80, 10, 91, 17))
        self.function_rbutton.setFont(font)
        self.function_rbutton.setChecked(True)

        self.file_rbutton = QtWidgets.QRadioButton(self.centralwidget)
        self.file_rbutton.setGeometry(QtCore.QRect(440, 10, 91, 17))
        self.file_rbutton.setFont(font)
        self.fileName_input.setEnabled(False)

        myWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(myWindow)
        QtCore.QMetaObject.connectSlotsByName(myWindow)

    def retranslateUi(self, myWindow):
        _translate = QtCore.QCoreApplication.translate
        myWindow.setWindowTitle(_translate("myWindow", "MainWindow"))
        self.label3.setText(_translate("myWindow", "Tolerance"))
        self.label2.setText(_translate("myWindow", "Maximum Number of Iterations"))
        self.method_options.setItemText(0, _translate("myWindow", "Bisection"))
        self.method_options.setItemText(1, _translate("myWindow", "False-Position"))
        self.method_options.setItemText(2, _translate("myWindow", "Newton-Raphson"))
        self.method_options.setItemText(3, _translate("myWindow", "Secant"))
        self.method_options.setItemText(4, _translate("myWindow", "Fixed Point"))
        self.method_options.activated.connect(self.activated)


        self.file_rbutton.toggled.connect(self.checked)


        self.calculate_button.setText(_translate("myWindow", "Calculate"))
        self.method_name_label.setText(_translate("myWindow", "Bisection Method"))
        self.range_label1.setText(_translate("myWindow", "Xu"))
        self.range_label2.setText(_translate("myWindow", "Xl"))
        self.function_rbutton.setText(_translate("myWindow", "Function"))
        self.file_rbutton.setText(_translate("myWindow", "File Name"))

        self.calculate_button.clicked.connect(self.clicked)

    def checked(self):
        if self.file_rbutton.isChecked():
            self.func_input.setEnabled(False)
            self.func_input.setText("")
            self.fileName_input.setEnabled(True)
        else:
            self.func_input.setEnabled(True)
            self.fileName_input.setText("")
            self.fileName_input.setEnabled(False)

    def activated(self):
        index = self.method_options.currentIndex()
        self.range_input1.setText("")
        self.range_input2.setText("")
        if index == 0:
            self.range_input2.setEnabled(True)
            self.method_name_label.setText("Bisection Method")
            self.range_label1.setText('Xu')
            self.range_label2.setText('Xl')
        elif index == 1:
            self.range_input2.setEnabled(True)
            self.method_name_label.setText("False Position Method")
            self.range_label1.setText('Xu')
            self.range_label2.setText('Xl')
        elif index == 2:
            self.method_name_label.setText("Newton Raphson Method")
            self.range_label2.setText('')
            self.range_label1.setText('Initial Guess')
            self.range_input2.setEnabled(False)
        elif index == 3:
            self.method_name_label.setText("Secant Method")
            self.range_label1.setText('Initial Guess')
            self.range_label2.setText('')
            self.range_input2.setEnabled(False)
        else:
            self.range_input2.setEnabled(True)
            self.method_name_label.setText("Fixed Point Method")
            self.range_label1.setText('Start')
            self.range_label2.setText('End')

    def clicked(self):
        index = self.method_options.currentIndex()
        maxIterations = self.iterations_input.text()
        tolerance = self.tolerance_input.text()
        function = self.func_input.text()
        function = function.replace('^', '**')
        file_name = self.fileName_input.text()
        if index == 0:
            method = "bisection"
            xu = self.range_input1.text()
            xl = self.range_input2.text()
        elif index == 1:
            method = "false position"
        elif index == 2:
            method = "newton raphson"
        elif index == 3:
            method = "secant"
        else:
            method = "fixed point"

        xl_list = []
        f_xl_list = []
        xu_list = []
        f_xu_list = []
        xr_list = []
        f_xr_list = []
        print(tolerance)
        print(functions.bisection(function, xu, xl, maxIterations, xl_list, xu_list, f_xl_list, f_xu_list, xr_list, f_xr_list, tolerance))