'''
Created on 09/02/2018

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import  Qt, QStyledItemDelegate

class CustomItemDelegate(QStyledItemDelegate):
    def __init__(self):
        super().__init__()
        
    def paint(self, painter, option, index ):
        text = index.data(Qt.DisplayRole)
        align = Qt.AlignCenter
        if isinstance(text,bool):
            column = index.column()
            row = index.row()
            value = index.model().record(row).value(column)
            if value == True: 
                painter.drawText(option.rect, align, 'Sim')
            else:
                painter.drawText(option.rect, align, 'Não')
        
        elif isinstance(text,str):
            painter.drawText(option.rect, align, text)
        else:
            text = str(text)
            painter.drawText(option.rect, align, text)
        


        
        
            
            