

import FileCtrl
# import TextCtrl as TC

class cls_Common():

    CurrentDir = FileCtrl.GetCurrentDirectory()

    #↓Window情報=======================================
    #[tkinter_, width_, height_, point_x, point_y, value_, write_sts]
    Stage0_x =[10, 35, 335]
    Stage10_x = [10]
    Stage11_x = [10]
    # Stage1_x = []
    Stage_main_y = [10, 40, 235, 260, 465]#Y位置

    StageInf_y = [Stage_main_y[1] + 10, Stage_main_y[1] + 30, Stage_main_y[1] + 60, Stage_main_y[1] + 90, Stage_main_y[1] + 120, Stage_main_y[1] + 140]#Y位置
    StageDebug = 500#デバッグボタンのY位置
    PointLeft = 10#X左側の位置


    def __init__(self):
        # 
        # [サイズX, サイズY, ポジションX, ポジションY, テキスト(タイトル等), 書込み可否]
        
        # self.windowSts = [tkinter_, 600, 530, 100, 100, 'Flash binary read', False] #Debugボタンを有効にするときはこちら
        self.windowSts = [600, 500, 100, 100, 'Flash binary read', False]

        # -----Stage0-----
        self.LBL_File_Sts = [0, 20, self.Stage0_x[0], self.Stage_main_y[0], 'file', False]
        self.TXB_FilePath_Sts = [480 , 20, self.Stage0_x[0] + 30, self.LBL_File_Sts[3], '', True]
        self.Btn_FileRead_Sts = [60, 20, self.Stage0_x[0] + self.TXB_FilePath_Sts[0] + 40, self.LBL_File_Sts[3], 'select', False]

        #-----Stage10-----
        self.Frm_Info_tk = [self.windowSts[0] - 20, 190, 10, self.Stage_main_y[1], '', False]
        # -----Stage11-----
        self.Lbl_Title_tk = [0, 0, self.Frm_Info_tk[2] + 10, self.StageInf_y[0], 'Title', False]
        self.Txb_Title_tk = [self.Frm_Info_tk[0] - 20, 20, self.Lbl_Title_tk[2], self.StageInf_y[1], 'no title', True]
        # -----Stage12-----
        self.Lbl_FileName_tk = [0, 0, self.Frm_Info_tk[2] + 10, self.StageInf_y[2],'File name       : ', False]
        self.Lbl_FileNameValue_tk = [0, 0, self.Lbl_FileName_tk[2] + 80, self.StageInf_y[2],'', False]
        # -----Stage13-----
        self.Lbl_FileSize_tk = [0, 0, self.Frm_Info_tk[2] + 10, self.StageInf_y[3], 'Num address : ', False]
        self.Lbl_FileSizeValue_tk = [0, 0, self.Lbl_FileName_tk[2] + 80, self.StageInf_y[3], '', False]
        # -----Stage14-----
        self.Lbl_Memo_tk = [0, 0, self.Frm_Info_tk[2] + 10, self.StageInf_y[4], 'Memo', False]
        self.Txb_Memo_tk = [self.windowSts[0] - 40,  40, self.Frm_Info_tk[2] + 10, self.StageInf_y[5], '', True]


        self.Btn_BatB_Sts = [self.windowSts[0] - 20, 20, self.PointLeft, self.Stage_main_y[2], 'Check', False]

        self.Txb_Log_Sts = [self.windowSts[0] - 20, 200, self.PointLeft, self.Stage_main_y[3], '', False]

        self.Btn_SaveLog = [100, 20, self.PointLeft, self.Stage_main_y[4], 'Log保存', False]

        self.Btn_Debug_Sts = [50, 20, self.PointLeft, self.StageDebug, 'Debug', False]

    #↑Window情報=======================================

    #↓アドレス情報========================================
    Adr_Start = 0x1000
    Adr_Step = 0x44000
    Adr_End = 0x21FFFFFF
    Adr_Partition = [0x00,
                    0x220000,
                    0xAA0000,
                    0x1BA0000,
                    0x5FA0000,
                    0xE7A0000,
                    0xE9C0000,
                    0xF240000,
                    0xFAC0000,
                    0x10BC0000]
    #↑アドレス情報========================================

    # Partition_adr = [0, 0x220000, 0xAA0000, 0x1BA0000, 0x5FA0000, 0xE7A0000, 0xE9C0000, 0xF240000, 0xFAC0000, 0x10BC0000, 0x50000000]

    #*****************************************************************************
    # 読み込んだ、configデータをディクショナリー化
    # def SetPart(ary_part):
    #     result_dict = {}
    #     data_buf = ary_part.split('\n')
    #     for d in data_buf:
    #         a = d.split(',')
    #         if a[0] == '':
    #             continue
    #         result_dict[a[0]] = TC.TextHex_to_int(a[1])
    #     return result_dict


    #*****************************************************************************
    # アドレス情報を取得
    def GetStartMessage(self):
        result = ''
        result = '-----Address info-----\n'
        result += '■Start : %s\n' % str(hex(self.Adr_Start))
        result += '■Step  : %s\n' % str(hex(self.Adr_Step))
        result += '■End   : %s\n' % str(hex(self.Adr_End))
        result += '\n'
        result += "■ Partition address ■" + "\n"
        for i in range(len(self.Adr_Partition)):
            result += "address %d : %s\n" % (i ,str(hex(self.Adr_Partition[i])))

        return result

    #*****************************************************************************
    # Binaryデータを判定
    def Checkking(self, file_path, adr_start, adr_step, adr_end, bl_data_out = False, bl_all_output = False):
        import BinaryCtrl as BC
        err_cnt = 0
        part_num = 0
        address_ = adr_start
        result_str = ''
        adr_head = adr_start#先頭アドレス(スペアエリアで無い)

        print('Check start')
        result_str += '%s\n%s\n\n' %('◆ : All 0x00（後発）', '★ : 2Bytes 0x00')
        CheckData_All = BC.Get_BinValue_All(file_path)
        result_str += '-----part %s [ %s ]-----\n' % (str(part_num), str(hex(self.Adr_Partition[0])))

        while True:
            CheckData_256Byte = CheckData_All[address_:address_ + 256]
            # print(len(CheckData_256Byte))
            CheckData_2Byte = CheckData_All[address_:address_ + 2]
            #先頭2バイトを判定 0x00, 0x00 でエラー判定
            if address_ == 0x723900:
                result_str += '0x723900\n'
                result_str += '%s : %s\n' % (str(hex(address_)),  str(hex(CheckData_All[address_])))
            # if BC.BinaryCheck(CheckData_2Byte, bytes([0x00, 0x00])):
            #     print('%s, %s' % (str(hex(address_)) , BC.BinaryCheck_CntNum(CheckData_256Byte, 0x00)))
            
            # 後発をチェック　全て0x00であればエラー判定
            if BC.BinaryCheck_CntNum(CheckData_256Byte, 0x00) == 256:
                if bl_data_out:
                    result_str += '◆%s : %s, %s, %s, %s...\n' % (str(hex(address_ - adr_head)), str(hex(CheckData_All[address_])), str(hex(CheckData_All[address_ + 1])), str(hex(CheckData_All[address_ + 2])), str(hex(CheckData_All[address_ + 3])))
                else:
                    result_str += '◆%s\n' % str(hex(address_ - adr_head))
                err_cnt += 1
            # 先頭2Byteをチェック　共に0x00であればエラー判定
            elif BC.BinaryCheck_CntNum(CheckData_2Byte, 0x00) == 2:
                if bl_data_out:
                    result_str += '★%s : %s, %s, %s, %s...\n' % (str(hex(address_ - adr_head)), str(hex(CheckData_All[address_])), str(hex(CheckData_All[address_ + 1])), str(hex(CheckData_All[address_ + 2])), str(hex(CheckData_All[address_ + 3])))
                else:
                    result_str += '★%s\n' % str(hex(address_ - adr_head))
                err_cnt += 1
            elif bl_all_output:
                result_str += '%s : %s, %s, %s, %s...\n' % (str(hex(address_)), str(hex(CheckData_All[address_])), str(hex(CheckData_All[address_ + 1])), str(hex(CheckData_All[address_ + 2])), str(hex(CheckData_All[address_ + 3])))

            address_ = address_ + adr_step

            if address_ > adr_end:
                result_str += 'err = %s\n' % str(err_cnt)
                break;
            if len(self.Adr_Partition) > part_num + 1 and self.Adr_Partition[part_num + 1] < address_:
                result_str += 'err = %s\n' % str(err_cnt)
                err_cnt = 0
                part_num += 1
                result_str += '-----part %s [ %s ]-----\n' % (str(part_num), str(hex(self.Adr_Partition[part_num])))
        print('Check done')
        return result_str
