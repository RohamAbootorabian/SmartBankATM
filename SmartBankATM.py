from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel, QPushButton, QMenu, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QGridLayout, QRadioButton, QCheckBox, QMessageBox
import sys
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PyQt6.QtCore import QSize, Qt, QRegularExpression


bank_account = {"6037991716688456" : ["2944", 10000000], "6037998179789531" : ["7989", 5000000]}


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Roham ATM")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.button1 = QPushButton("English", self)
        self.button1.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button1.clicked.connect(self.button_event1)

        self.button2 = QPushButton("فارسی", self)
        self.button2.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button2.clicked.connect(self.button_event2)

        self.label = QLabel("choose language:", self)
        self.label.setGeometry(300, 110, 100, 50)
        self.label.setFont(QFont("Georgia", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def button_event1(self):
        self.window = PasswordWindowEnglish()
        self.window.show()
        self.close()


    def button_event2(self):
        self.window = PasswordWindowPersion()
        self.window.show()
        self.close()

class PasswordWindowEnglish(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("password page")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.label1 = QLabel("enter your card number:", self)
        self.label1.setFont(QFont("Georgia", 20))
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_text1 = QLineEdit(self)
        self.input_text1.setPlaceholderText("card number")
        self.input_text1.setFont(QFont("Georgia", 10))
        self.input_text1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label2 = QLabel("enter your password:", self)
        self.label2.setFont(QFont("Georgia", 20))
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_text2 = QLineEdit(self)
        self.input_text2.setPlaceholderText("password")
        self.input_text2.setFont(QFont("Georgia", 10))
        self.input_text2.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_text2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("submit", self)
        self.button.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button.clicked.connect(self.button_event)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.input_text1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.input_text2)
        vbox.addWidget(self.button)
        self.setLayout(vbox)

    def button_event(self):
        card_number = self.input_text1.text()
        password = self.input_text2.text()

        if card_number in bank_account and bank_account[card_number][0] == password:
            self.window = MainWindowEnglish()
            self.window.show()
            self.close()
        else:
            self.show_error_message()

    def show_error_message(self):
        error_msg = QMessageBox(self)
        error_msg.setWindowTitle("Error")
        error_msg.setIcon(QMessageBox.Icon.Warning)
        error_msg.setText("Invalid card number or password!")
        error_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        error_msg.exec()


class PasswordWindowPersion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("صفحه پسورد")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.label1 = QLabel("شماره کارت خود را وارد کنید", self)
        self.label1.setFont(QFont("Georgia", 20))
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_text1 = QLineEdit(self)
        self.input_text1.setPlaceholderText("شماره کارت")
        self.input_text1.setFont(QFont("Georgia", 10))
        self.input_text1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label2 = QLabel("رمز خود را وارد کنید", self)
        self.label2.setFont(QFont("Georgia", 20))
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_text2 = QLineEdit(self)
        self.input_text2.setPlaceholderText("رمز عبور")
        self.input_text2.setFont(QFont("Georgia", 10))
        self.input_text2.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_text2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("ثبت", self)
        self.button.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button.clicked.connect(self.button_event)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.input_text1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.input_text2)
        vbox.addWidget(self.button)
        self.setLayout(vbox)

    def button_event(self):
        card_number = self.input_text1.text()
        password = self.input_text2.text()

        if card_number in bank_account and bank_account[card_number][0] == password:
            self.window = MainWindowPersion()
            self.window.show()
            self.close()
        else:
            self.show_error_message()

    def show_error_message(self):
        error_msg = QMessageBox(self)
        error_msg.setWindowTitle("خطا")
        error_msg.setIcon(QMessageBox.Icon.Warning)
        error_msg.setText("شماره کارت یا رمز عبور اشتباه اس!")
        error_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        error_msg.exec()




class MainWindowEnglish(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main window")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.button1 = QPushButton("Get Cash", self)
        self.button1.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button1.clicked.connect(self.button_event1)

        self.button2 = QPushButton("Change Password", self)
        self.button2.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button2.clicked.connect(self.button_event2)

        self.button3 = QPushButton("Money Transfer", self)
        self.button3.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button3.clicked.connect(self.button_event3)

        self.button4 = QPushButton("Account Balance", self)
        self.button4.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button4.clicked.connect(self.button_event4)

        grid = QGridLayout()
        grid.addWidget(self.button1, 0, 0)
        grid.addWidget(self.button2, 0, 1)
        grid.addWidget(self.button3, 1, 0)
        grid.addWidget(self.button4, 1, 1)
        self.setLayout(grid)

    def button_event1(self):
        self.window = GetCashWindowEnglish()
        self.window.show()
        self.close()

    def button_event2(self):
        self.window = ChangePasswordWindowEnglish()
        self.window.show()
        self.close()

    def button_event3(self):
        self.window = MoneyTransferWindowEnglish()
        self.window.show()
        self.close()

    def button_event4(self):
        self.window = ShowBalanceWindowEnglish()
        self.window.show()
        self.close()




class MainWindowPersion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main window")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.button1 = QPushButton("برداشت وجه", self)
        self.button1.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button1.clicked.connect(self.button_event1)

        self.button2 = QPushButton("تغییر رمز", self)
        self.button2.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button2.clicked.connect(self.button_event2)

        self.button3 = QPushButton("کارت به کارت", self)
        self.button3.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button3.clicked.connect(self.button_event3)

        self.button4 = QPushButton("اعلام موجودی", self)
        self.button4.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button4.clicked.connect(self.button_event4)

        grid = QGridLayout()
        grid.addWidget(self.button1, 0, 0)
        grid.addWidget(self.button2, 0, 1)
        grid.addWidget(self.button3, 1, 0)
        grid.addWidget(self.button4, 1, 1)
        self.setLayout(grid)

    def button_event1(self):
        self.window = GetCashWindowPersion()
        self.window.show()
        self.close()

    def button_event2(self):
        self.window = ChangePasswordWindowPersion()
        self.window.show()
        self.close()

    def button_event3(self):
        self.window = MoneyTransferWindowPersion()
        self.window.show()
        self.close()

    def button_event4(self):
        self.window = ShowBalanceWindowPersion()
        self.window.show()
        self.close()


class GetCashWindowEnglish(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main window")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.button1 = QPushButton("500/000", self)
        self.button1.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button1.clicked.connect(self.button_event)

        self.button2 = QPushButton("1/500/000", self)
        self.button2.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button2.clicked.connect(self.button_event)

        self.button3 = QPushButton("1/000/000", self)
        self.button3.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button3.clicked.connect(self.button_event)

        self.button4 = QPushButton("2/000/000", self)
        self.button4.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button4.clicked.connect(self.button_event)

        grid = QGridLayout()
        grid.addWidget(self.button1, 0, 0)
        grid.addWidget(self.button2, 0, 1)
        grid.addWidget(self.button3, 1, 0)
        grid.addWidget(self.button4, 1, 1)
        self.setLayout(grid)

    def button_event(self):
        self.window = LastWindowEnglish()
        self.window.show()
        self.close()




class GetCashWindowPersion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("صفحه اصلی")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.button1 = QPushButton("۵۰۰/۰۰۰", self)
        self.button1.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button1.clicked.connect(self.button_event)

        self.button2 = QPushButton("۱/۵۰۰/۰۰۰", self)
        self.button2.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button2.clicked.connect(self.button_event)

        self.button3 = QPushButton("۱/۰۰۰/۰۰۰", self)
        self.button3.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button3.clicked.connect(self.button_event)

        self.button4 = QPushButton("۲/۰۰۰/۰۰۰", self)
        self.button4.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button4.clicked.connect(self.button_event)

        grid = QGridLayout()
        grid.addWidget(self.button1, 0, 0)
        grid.addWidget(self.button2, 0, 1)
        grid.addWidget(self.button3, 1, 0)
        grid.addWidget(self.button4, 1, 1)
        self.setLayout(grid)

    def button_event(self):
        self.window = LastWindowPersion()
        self.window.show()
        self.close()


class LastWindowEnglish(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Last Page")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.label = QLabel("Mission Accomplished Successfully", self)
        self.label.setGeometry(300, 110, 100, 50)
        self.label.setFont(QFont("Georgia", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button1 = QPushButton("Good Bye", self)
        self.button1.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button1.clicked.connect(self.button_event1)

        self.button2 = QPushButton("New Mission", self)
        self.button2.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button2.clicked.connect(self.button_event2)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def button_event1(self):
        app.closingDown()
        self.close()

    def button_event2(self):
        self.window = MainWindowEnglish()
        self.window.show()
        self.close()


class LastWindowPersion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("صفحه پایانی")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.label = QLabel("عملیات با موفقیت به انجام شد", self)
        self.label.setGeometry(300, 110, 100, 50)
        self.label.setFont(QFont("Georgia", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button1 = QPushButton("خدانگهدار", self)
        self.button1.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button1.clicked.connect(self.button_event1)

        self.button2 = QPushButton("عملیات جدید", self)
        self.button2.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button2.clicked.connect(self.button_event2)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def button_event1(self):
        app.closingDown()
        self.close()

    def button_event2(self):
        self.window = MainWindowPersion()
        self.window.show()
        self.close()

class ChangePasswordWindowEnglish(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change Password Window")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.label1 = QLabel("Enter your new password:", self)
        self.label1.setFont(QFont("Georgia", 20))
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_new_password = QLineEdit(self)
        self.input_new_password.setPlaceholderText("New Password")
        self.input_new_password.setFont(QFont("Georgia", 10))
        self.input_new_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_new_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label2 = QLabel("Confirm your new password:", self)
        self.label2.setFont(QFont("Georgia", 20))
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_confirm_password = QLineEdit(self)
        self.input_confirm_password.setPlaceholderText("Confirm Password")
        self.input_confirm_password.setFont(QFont("Georgia", 10))
        self.input_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_confirm_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_confirm = QPushButton("Confirm", self)
        self.button_confirm.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button_confirm.clicked.connect(self.update_password)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.input_new_password)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.input_confirm_password)
        vbox.addWidget(self.button_confirm)
        self.setLayout(vbox)

    def update_password(self):
        card_number = window1.window.input_text1.text() #---------------------------------------------------------------------------------------------------------------------
        print(card_number)
        new_password = self.input_new_password.text()
        confirm_password = self.input_confirm_password.text()

        if not new_password or not confirm_password:
            self.show_error_message("New password fields cannot be empty.")
            return
        if new_password != confirm_password:
            self.show_error_message("New passwords do not match.")
            return

        bank_account[card_number][0] = new_password
        self.window = LastWindowEnglish()
        self.window.show()
        self.close()

    def show_error_message(self, message):
        error_msg = QMessageBox(self)
        error_msg.setWindowTitle("Error")
        error_msg.setIcon(QMessageBox.Icon.Warning)
        error_msg.setText(message)
        error_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        error_msg.exec()

    def show_success_message(self, message):
        success_msg = QMessageBox(self)
        success_msg.setWindowTitle("Success")
        success_msg.setIcon(QMessageBox.Icon.Information)
        success_msg.setText(message)
        success_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        success_msg.exec()
        self.close()



class ChangePasswordWindowPersion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("صفحه تغییر پسورد")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.label1 = QLabel("رمز جدید را وارد کنید", self)
        self.label1.setFont(QFont("Georgia", 20))
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_new_password = QLineEdit(self)
        self.input_new_password.setPlaceholderText("رمز جدید")
        self.input_new_password.setFont(QFont("Georgia", 10))
        self.input_new_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_new_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label2 = QLabel("تایید رمز را وارد کنید", self)
        self.label2.setFont(QFont("Georgia", 20))
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_confirm_password = QLineEdit(self)
        self.input_confirm_password.setPlaceholderText("تایید رمز")
        self.input_confirm_password.setFont(QFont("Georgia", 10))
        self.input_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_confirm_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_confirm = QPushButton("تایید", self)
        self.button_confirm.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button_confirm.clicked.connect(self.update_password)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.input_new_password)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.input_confirm_password)
        vbox.addWidget(self.button_confirm)
        self.setLayout(vbox)

    def update_password(self):
        card_number = window1.window.input_text1.text()  # ---------------------------------------------------------------------------------------------------------------------
        print(card_number)
        new_password = self.input_new_password.text()
        confirm_password = self.input_confirm_password.text()

        if not new_password or not confirm_password:
            self.show_error_message("رمز را وارد کنید")
            return
        if new_password != confirm_password:
            self.show_error_message("رمز ها هماهنگ نیست")
            return

        bank_account[card_number][0] = new_password
        self.window = LastWindowPersion()
        self.window.show()
        self.close()

    def show_error_message(self, message):
        error_msg = QMessageBox(self)
        error_msg.setWindowTitle("ارور")
        error_msg.setIcon(QMessageBox.Icon.Warning)
        error_msg.setText(message)
        error_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        error_msg.exec()

    def show_success_message(self, message):
        success_msg = QMessageBox(self)
        success_msg.setWindowTitle("موفقیت")
        success_msg.setIcon(QMessageBox.Icon.Information)
        success_msg.setText(message)
        success_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        success_msg.exec()
        self.close()


class MoneyTransferWindowEnglish(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Money Transfer")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.label1 = QLabel("Destination Card Number:", self)
        self.label1.setFont(QFont("Georgia", 20))
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_destination_card = QLineEdit(self)
        self.input_destination_card.setPlaceholderText("Enter destination card number")
        self.input_destination_card.setFont(QFont("Georgia", 10))
        self.input_destination_card.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label2 = QLabel("Transfer Amount:", self)
        self.label2.setFont(QFont("Georgia", 20))
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_amount = QLineEdit(self)
        self.input_amount.setPlaceholderText("Enter amount")
        self.input_amount.setFont(QFont("Georgia", 10))
        self.input_amount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_amount.setValidator(QIntValidator(1, 1000000000, self))  # Only allow positive integers

        self.button_confirm = QPushButton("Confirm", self)
        self.button_confirm.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button_confirm.clicked.connect(self.transfer_money)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.input_destination_card)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.input_amount)
        vbox.addWidget(self.button_confirm)
        self.setLayout(vbox)

    def transfer_money(self):
        source_card = window1.window.input_text1.text()
        destination_card = self.input_destination_card.text()
        amount = self.input_amount.text()

        if not source_card or not destination_card or not amount:
            self.show_message("Error", "All fields are required!", QMessageBox.Icon.Warning)
            return

        if source_card not in bank_account or destination_card not in bank_account:
            self.show_message("Error", "Invalid card number(s)!", QMessageBox.Icon.Warning)
            return

        amount = int(amount)
        if bank_account[source_card][1] < amount:
            self.show_message("Error", "Insufficient balance!", QMessageBox.Icon.Warning)
            return

        bank_account[source_card][1] -= amount
        bank_account[destination_card][1] += amount
        self.window = LastWindowEnglish()
        self.window.show()
        self.close()

    def show_message(self, title, message, icon):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()


class MoneyTransferWindowPersion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("کارت به کارت")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.label1 = QLabel("شماره کارت مقصد", self)
        self.label1.setFont(QFont("Georgia", 20))
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_destination_card = QLineEdit(self)
        self.input_destination_card.setPlaceholderText("شماره کارت مقصد")
        self.input_destination_card.setFont(QFont("Georgia", 10))
        self.input_destination_card.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label2 = QLabel("مبلغ واریزی", self)
        self.label2.setFont(QFont("Georgia", 20))
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_amount = QLineEdit(self)
        self.input_amount.setPlaceholderText("مبلغ")
        self.input_amount.setFont(QFont("Georgia", 10))
        self.input_amount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_amount.setValidator(QIntValidator(1, 1000000000, self))  # Only allow positive integers

        self.button_confirm = QPushButton("تایید", self)
        self.button_confirm.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button_confirm.clicked.connect(self.transfer_money)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.input_destination_card)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.input_amount)
        vbox.addWidget(self.button_confirm)
        self.setLayout(vbox)

    def transfer_money(self):
        source_card = window1.window.input_text1.text()
        destination_card = self.input_destination_card.text()
        amount = self.input_amount.text()

        if not source_card or not destination_card or not amount:
            self.show_message("ارور", "لطفا کادر های مربوطه را پر کنید", QMessageBox.Icon.Warning)
            return

        if source_card not in bank_account or destination_card not in bank_account:
            self.show_message("ارور", "شماره کارت مقصد معتبر نیست", QMessageBox.Icon.Warning)
            return

        amount = int(amount)
        if bank_account[source_card][1] < amount:
            self.show_message("ارور", "موجودی کافی نیست", QMessageBox.Icon.Warning)
            return

        bank_account[source_card][1] -= amount
        bank_account[destination_card][1] += amount
        self.window = LastWindowPersion()
        self.window.show()
        self.close()

    def show_message(self, title, message, icon):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

class ShowBalanceWindowEnglish(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Show Balance")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        current_number = window1.window.input_text1.text()

        self.label = QLabel(f"your bank account balance {str(bank_account[current_number][1])}", self)
        self.label.setFont(QFont("Georgia", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Confirm", self)
        self.button.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button.clicked.connect(self.button_event)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)
        self.setLayout(vbox)

    def button_event(self):
        self.window = LastWindowEnglish()
        self.window.show()
        self.close()


class ShowBalanceWindowPersion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("اعلام موجودی")
        self.setMaximumSize(500, 500)
        self.setMinimumSize(100, 100)
        self.setFixedSize(700, 700)
        self.setWindowOpacity(0.98)

        self.label = QLabel(f"موجودی حساب شما", self)
        self.label.setFont(QFont("Georgia", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("تایید", self)
        self.button.setFont(QFont("Georgia", 10, QFont.Weight.ExtraBold))
        self.button.clicked.connect(self.button_event)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)
        self.setLayout(vbox)

    def button_event(self):
        self.window = LastWindowPersion()
        self.window.show()
        self.close()





app = QApplication(sys.argv)
window1 = LoginWindow()
window1.show()
app.exec()