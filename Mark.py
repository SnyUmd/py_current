#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PySide2 import QtWidgets
from PySide2 import QtCore
import time


# In[3]:


class Window(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Sample")
        self.setStyleSheet("background-color:white;")
        self.setFixedSize(480, 320)

        
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setStyleSheet("background-color: rgba(255, 0, 0, 127);")
        
#         self.setWindowOpacity(0.5)

        hbox = QtWidgets.QHBoxLayout()
        vbox = QtWidgets.QVBoxLayout()
        hbox.addLayout(vbox)

        self.setLayout(hbox)
    
    def setSize(self, w, h):
        self.setFixedSize(w, h)
        
    def setTransparent(self, val):
        self.setWindowOpacity(val)
    
    #rgba_str = "rgba(255,255,255,127)" ←白
    #           "rgba(255,0,0,127)" ←赤
    def setColor(self, rgba_str):
        setStr = "background-color: " + rgba_str + ";"
        self.setStyleSheet(setStr)


# In[4]:


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.setSize(100, 100)
    window.setTransparent(0.5)
    window.setColor("rgba(255, 255, 0, 127)")
    window.show()
    exit(app.exec_())
#     window.collect()


# In[ ]:




