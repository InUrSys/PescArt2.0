from PyQt5.Qt import QAbstractItemModel, QModelIndex, Qt, QApplication,\
    QTreeView, QSqlQuery, QSqlDatabase, QHeaderView
import sys
from pprint import pprint
class Node(object): #Estrutura de dados Hirarica
    def __init__(self, name, parent=None):
        
        self._name = name #Name of the Node to ahve sothing to display in the treeView
        self._children = [] #Children of the Node
        self._parent = parent #Parent of the Node
        
        if parent is not None:
            parent.addChild(self)
    
    def typeInfo(self):
        '''
        Informacao Do tipo de Nodo
        Ex: Nodo Provincia
        '''
        return "Nodo"
            
            
    def addChild(self, child):
        self._children.append(child)#Add the given child to the Chidren list
        
    def name(self):
        return self._name
    
    def child(self, row):
        return self._children[row]

    def childCount(self):
        return len(self._children)
    
    def parent(self):
        return self._parent
    
    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)
        
    def setName(self, name):
        self._name = name
        
    def log(self, tablevel=-1):
        output = ""
        tablevel +=1
        
        for i in range(tablevel):
            output += "\t"
            
        output += "|-----"+self._name+"\n"
        
        for child in self._children:
            output += child.log(tablevel)
        
        tablevel -= 1
        output += "\n"
        
        return output
 
 
    
    
class TreeModel(QAbstractItemModel):
    #Input: Node, Qubject
    def __init__(self, root, parent=None):
        super(TreeModel, self).__init__(parent)
        self._rootNode = root

    #input QmodelIndex
    #Output int
    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self._rootNode
        else:
            parentNode = parent.internalPointer()
        return parentNode.childCount()
    
    
    #input QmodelIndex
    #Output int
    def columnCount(self, parent):
        return 2
    
    #input QmodelIndex, int
    #Output QVariant, string are cast to QString which is a QVariant
    def data(self, index, role):
        if not index.isValid():
            return None
        
        node = index.internalPointer()
        
        if role == Qt.DisplayRole or role ==Qt.EditRole:
            if index.column() == 0:#column corresponds to the header section
                return node.name()
            else:
                return node.typeInfo()
        
        
    #Input int, Qt:: Orientation, int
    #Output QVariant, string are cast to QString which is a QVariant
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if section ==0:
                return "Nome"
            else:
                return "Descrição"
    
    
    #Input ModelIndex
    #Int(flag)
    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
    
    #QModelIndex
    #QModelIndex
    #Should return the paren of the node with the given QModelIndex
    def parent(self, index):
        node = index.internalPointer()
        parentNode = node.parent()

        if parentNode == self._rootNode:
            return QModelIndex()
        
        return self.createIndex(parentNode.row(), 0, parentNode)
        
        
    #int, int, QModelIndex
    #QModelIndex
    #should return the a QModelIndex that corresponds to the given Row, column and parent Node
    def index(self, row, column, parent):
        if not parent.isValid():
            parentNode = self._rootNode
        else:
            parentNode = parent.internalPointer()
        childItem = parentNode.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

class Pais_Nodo(Node):
    """
    Sub-Class do Nodo princinpal 
    """
    def __init__(self, name, parent=None):
        super().__init__(name, parent)#Super class constructor
        
    def typeInfo(self):
        return "Pais"



class Provincia_Nodo(Node):
    """
    Sub-Class do Nodo princinpal 
    """
    def __init__(self, name, parent=None):
        super().__init__(name, parent)#Super class constructor
        
    def typeInfo(self):
        return "Provincia"



class Distrito_Nodo(Node):
    """
    Sub-Class do Nodo princinpal 
    """
    def __init__(self, name, parent=None):
        super().__init__(name, parent)#Super class constructor
        
    def typeInfo(self):
        return "Distrito"
    
    
    
class Posto_Nodo(Node):
    """
    Sub-Class do Nodo princinpal 
    """
    def __init__(self, name, parent=None):
        super().__init__(name, parent)#Super class constructor
        
    def typeInfo(self):
        return "Posto Administrativo"
    
    
    
class Centro_Nodo(Node):
    """
    Sub-Class do Nodo princinpal 
    """
    def __init__(self, name, parent=None):
        super().__init__(name, parent)#Super class constructor
        
    def typeInfo(self):
        return "Centro de Pesca"
    
    