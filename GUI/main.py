import sys
from PySide6 import QtCore, QtWidgets, QtGui
from gui import Ui_Form
from initial import Ui_Form as Ui_Form_init
from spmi import tests
import random
import textwrap

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('books.ico'))
Form2 = QtWidgets.QWidget()
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui2 = Ui_Form_init()
ui2.setupUi(Form)
#ui.setupUi(Form)
Form.show()

# app logic
def get_random_question(db, ):
    q = random.choice(db)
    true_answer = None
    true_answer_text = None
    for elem in range(1, len(q)):
        if q[elem][0] == '@':
            true_answer = elem
            true_answer_text = q[elem][1:]
            q[elem] = q[elem][1:]
    return q, true_answer, true_answer_text

q = []

def go_warp(text, symbols):
    return textwrap.fill(text, symbols)

def change_question(database):
    question, true_answer_position, true_answer_text = get_random_question(database)

    ui.textEdit_question.setText(go_warp(question[0], 500))
    

    ui.pushButton_a1.setText(go_warp(question[1], 40))
    ui.pushButton_a2.setText(go_warp(question[2], 40))
    ui.pushButton_a3.setText(go_warp(question[3], 40))
    ui.pushButton_a4.setText(go_warp(question[4], 40))

    q.append([question, true_answer_position, true_answer_text])
    ui.pushButton_5.setText('Пропуск')

    ui.pushButton_a1.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color: rgb(241, 154, 117);\nborder-radius: 25;\npadding: 0px 15px 0px 15px;')
    ui.pushButton_a2.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color: rgb(241, 154, 117);\nborder-radius: 25;\npadding: 0px 15px 0px 15px;')
    ui.pushButton_a3.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color: rgb(241, 154, 117);\nborder-radius: 25;\npadding: 0px 15px 0px 15px;')
    ui.pushButton_a4.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color: rgb(241, 154, 117);\nborder-radius: 25;\npadding: 0px 15px 0px 15px;')
    
    ui.pushButton_a1.setDisabled(False)
    ui.pushButton_a2.setDisabled(False)
    ui.pushButton_a3.setDisabled(False)
    ui.pushButton_a4.setDisabled(False)

    #ui.pushButton_a3.


def checkanswer(q, click_position):
    ui.pushButton_5.setText('Дальше')
    question = q[0]
    true_answer_position = q[1]
    true_answer_text = q[2]
    if click_position == true_answer_position:
        print('correct!')
        ui.label_2.setText(str(int(ui.label_2.text()) + 1))

        ui.__getattribute__(f'pushButton_a{true_answer_position}').setStyleSheet('color: rgb(255, 250, 252); background-color: rgb(182, 234, 114); border-radius: 25;')

    else:
        print('incorrect :0')
        

        ui.__getattribute__(f'pushButton_a{true_answer_position}').setStyleSheet('color: rgb(255, 250, 252); background-color: rgb(182, 234, 114); border-radius: 25;')
        ui.__getattribute__(f'pushButton_a{click_position}').setStyleSheet('background-color: rgb(255, 110, 87);color: rgb(255, 250, 252); border-radius: 25;')
        
    ui.label_4.setText(str(int(ui.label_4.text()) + 1))
    ui.pushButton_a1.setDisabled(True)
    ui.pushButton_a2.setDisabled(True)
    ui.pushButton_a3.setDisabled(True)
    ui.pushButton_a4.setDisabled(True)


# Here starts:
def go_run(filepath):
    database = tests(filepath)
    Form.close()
    ui.setupUi(Form2)
    Form2.show()
    change_question(database)
    ui.pushButton_5.clicked.connect(lambda: change_question(database))

    ui.pushButton_a1.clicked.connect(lambda: checkanswer(q[-1], 1))
    ui.pushButton_a2.clicked.connect(lambda: checkanswer(q[-1], 2))
    ui.pushButton_a3.clicked.connect(lambda: checkanswer(q[-1], 3))
    ui.pushButton_a4.clicked.connect(lambda: checkanswer(q[-1], 4))


def fileinfo():
    qfiledialog = QtWidgets.QFileDialog()
    filepath = qfiledialog.getOpenFileName(ui2.pushButton, 'Open file', '/ home', "Data files (*.txt)")[0]
    if filepath == '':
        pass
    else:
        go_run(filepath)

ui2.pushButton.clicked.connect(fileinfo)



# run app

sys.exit(app.exec())

