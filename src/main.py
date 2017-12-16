import sys
from PyQt5.Qt import QApplication
import QT_msg
import WhatLog
from frmLog_in import logIn

if __name__=="__main__":
    app = QApplication(sys.argv)
    formMain = logIn()
    formMain.show()
    try:
        app.verbose_crash = True
#TODO: Use the line below only when not debugging
        app.exec_()
    except BaseException as e1:
        QT_msg.error(txt="O erro foi: ", verbTxt=str(e1))
        WhatLog.errorHappen(info=e1)
    sys.exit()
    
    
    
    
