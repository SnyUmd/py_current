from enum import Enum, auto
import FileCtrl as FC
import TextCtrl as TC

class enmInf(Enum):
    enmSizeX = 0
    enmSizeY = auto()
    enmPointX = auto()
    enmPointY = auto()
    enmValue = auto()


    
class AreaInfCol():
    TxbFolder = 10
    BtnFolder = TxbFolder

class AreaInfRow():
    FolderSelect = 10

class ClsCommon():
    # ------------------------------------------
    P_Left = 10
    P_Top = 10
    
    # ------------------------------------------
    WinInf = []
    LblFolderInf = []
    TxbFolderInf = []
    BtnFolderInf = []
    
    BtnDebugInf = []
    
    # ------------------------------------------
    RunDir = ''
    sizeX = enmInf.enmSizeX.value
    sizeY = enmInf.enmSizeY.value
    pointX = enmInf.enmPointX.value
    pointY = enmInf.enmPointY.value
    content_ = enmInf.enmValue.value

    # ------------------------------------------

    # def __init__(self):
    Win_Size = [600, 530]
    
    def __init__(self):
        self.WinInf = [self.Win_Size[0], 
                       self.Win_Size[1], 
                       10, 
                       10, 
                       'Win']
        
        self.LblFolderInf = [0, 0, self.P_Left, self.P_Top, 'フォルダ ：']
        
        self.TxbFolderInf = [450, 
                             20, 
                             self.LblFolderInf[self.pointX] + 60, 
                             self.LblFolderInf[self.pointY], 
                             ""]
        
        self.BtnFolderInf = [60, 
                             20, 
                             self.TxbFolderInf[self.pointX] + self.TxbFolderInf[self.sizeX] + 10, 
                             self.TxbFolderInf[self.pointY],
                             "Dir select"]
        
        
        
        self.BtnDebugInf = [50, 20, self.P_Left, 500, 'Debug']
    # def init_(self):
        
    # if __name__ == "__main__":
        
    