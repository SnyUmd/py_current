#!/usr/bin/env python
# coding: utf-8


'''
a_data = bytes('あ', 'UTF-8')
print(a_data)

b_data = bytearray('あ', 'shift-jis')
print(b_data)

print('---------------')

b_data = bytes(b'abc')
print(b_data[0])

check = bytes([ord('a'), 99, 100])

if b_data == check:
    print('true')
print(ord('a'))
'''

Partition_adr = [0, 0x220000, 0xAA0000, 0x1BA0000, 0x5FA0000,
              0xE7A0000, 0xE9C0000, 0xF240000, 0xFAC0000, 0x10BC0000, 0x50000000]
#*****************************************************************************
def Get_BinValue_All(file_path):
    bin_file = open(file_path, 'rb')
    result = bin_file.read()
    bin_file.close()
    return result

#*****************************************************************************
def BinaryCheck(bin_target, bin_check_word):
    for i in range(len(bin_target)):
        if bin_target[i] != bin_check_word[i]:
            #print(i)
            return False
    return True

#*****************************************************************************
def BinaryCheck_CntNum(bin_target, bin_check_word = 0x00):
    return bin_target.count(bin_check_word)

#*****************************************************************************
def GetAddressNum(file_path):
    bin_file = open(file_path, 'rb')
    buf = bin_file.read()
    result = len(buf)
    bin_file.close()
    return result

#*****************************************************************************
# def BinaryCheck1(bin_target, bin_check_word):
#     result = list(range(0))

#     for i in range(len(bin_target)):
#         if bin_target[i] != bin_check_word[i]:
#             result.append([i, bin_target[i]])#要素追加
#     return result


#*****************************************************************************
#ファイル分割
def divide_file(filePath, chunkSize):
    import os
    readedDataSize = 0
    i = 0
    fileList = []

    # 対象ファイルを開く
    f = open(filePath, "rb")

    # ファイルを読み終わるまで繰り返す
    contentLength = os.path.getsize(filePath)
    while readedDataSize < contentLength:

        # 読み取り位置をシーク
        f.seek(readedDataSize)

        # 指定されたデータサイズだけ読み込む
        data = f.read(chunkSize)

        # 分割ファイルを保存
        saveFilePath = filePath + "." + str(i)
        with open(saveFilePath, 'wb') as saveFile:
            saveFile.write(data)

        # 読み込んだデータサイズの更新
        readedDataSize = readedDataSize + len(data)
        i = i + 1
        fileList.append(saveFilePath)

    return fileList


#*****************************************************************************
def main0():
    # test = Get_BinValue_All('C:\\Users\\E324595\\Documents\\_umd\\soft\\Flash_エラー箇所読込み\\Flashデータ\\PSN7_No18443_BETA_COPY_PAT000.BIN')
    test = Get_BinValue_All('C:\\Users\\E324595\\Documents\\_umd\\soft\\Flash_エラー箇所読込み\\Flashデータ\\PSN7_No18448_BETA_COPY_PAT001.BIN')
    #print('size = ' + str(hex(len(test))))
    adress = 0x1000
    adress_add = 0x44000
    max_adress = 0x21FFFFFF
    # max_adless = 0x21FBC000
    #max_adless = 0x20021000
    #max_adless = 0x1FFDD000
    # max_adless = 0x10BC0000

    err_cnt = 0


    part_num = 0

    print('-----part ' + str(part_num) + ' [ ' + str(hex(Partition_adr[0])) + ' ]'  +'-----')

    while True:
        out_txt = ''
        #print(hex(adless) + ' : ' + str(hex(test[adless])) + ', ' + str(hex(test[adless + 1])))
        #2バイト格納
        a_ = [test[adress], test[adress + 1]]
        #先頭2バイトを判定 0x00, 0x00 でエラー判定
        if adress == 0x723900:
            print('0x723900')
            print(hex(adress) + ' : ' + str(hex(test[adress])))
        if BinaryCheck(a_, bytes([0x00, 0x00])):
            out_txt ='★' + hex(adress) + ' : ' + str(hex(test[adress])) + ', ' + str(hex(test[adress + 1])) + ', ' + str(hex(test[adress + 2])) + ', ' + str(hex(test[adress + 3]) + '...')
            err_cnt += 1
            print(out_txt)
        else:
            out_txt = hex(adress) + ' : ' + str(hex(test[adress])) + ', ' + str(hex(test[adress + 1])) + ', ' + str(hex(test[adress + 2])) + ', ' + str(hex(test[adress + 3])  + '...')
            #print(out_txt)

        adress = adress + adress_add

        if adress > max_adress:
            print('err = ' + str(err_cnt))
            break;

        if Partition_adr[part_num + 1] < adress:
            print('err = ' + str(err_cnt))
            err_cnt = 0
            part_num += 1
            print('-----part ' + str(part_num) + ' [ ' + str(hex(Partition_adr[part_num])) + ' ]'   + '-----')


#*****************************************************************************
def main1():
    import os
    file_path = 'C:\\Users\\E324595\\Documents\\_umd\\soft\\Flash_エラー箇所読込み\\scr\\PAT000_af - コピー.BIN'
    print(os.path.getsize(file_path)/32)
    print(type(os.path.getsize(file_path)/32))
    file_list = divide_file(file_path, os.path.getsize(file_path)/32)
    #print(file_list)


#*****************************************************************************
#*****************************************************************************
#*****************************************************************************
#*****************************************************************************
if __name__ == "__main__":
    print(BinaryCheck_Advance([0x00, 0x00], 0x00))
