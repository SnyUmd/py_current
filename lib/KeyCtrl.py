from turtle import screensize
from pynput import keyboard
import keyboard

# # *****************************************************************
# def on_press(key):
#     try:
#         print('Alphanumeric key pressed: {0} '.format(
#             key.char))
#     except AttributeError:
#         print('special key pressed: {0}'.format(
#             key))
        
#     return key.char

# # *****************************************************************
# def on_release(key):
#     print('Key released: {0}'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False



# *****************************************************************
def CheckPress_CS(key_):
    # keys = ["shift", "ctrl", key_]
    keys = ["win", "ctrl", key_]
    return True if keyboard.is_pressed(keys[2]) and keyboard.is_pressed(keys[0]) and keyboard.is_pressed(keys[1]) else False


# *****************************************************************
def Loop_CheckPress_CS(key_, time_out_sec = 0):
    import SysCtrl as sCtrl

    sts_cnt = [0, 0, 0]
    time_start = 0
    time_current = 0
    time_now = 0
    LoopCnt = 0

    keys = ["win", "ctrl", key_]

    time_start = sCtrl.GetPrcsTime()
    time_current = sCtrl.GetPrcsTime()
    time_now = sCtrl.GetPrcsTime()
    
    while True:
        if keyboard.is_pressed(keys[2]):
            sts_cnt[2] += 1

            if keyboard.is_pressed(keys[0]):
                sts_cnt[0] += 1
            if keyboard.is_pressed(keys[1]):
                sts_cnt[1] += 1
        
        if time_now - time_current > 0.1:
            # print("%d, %d, %d" % (sts_cnt[0], sts_cnt[1], sts_cnt[2]))
            # print(time_now - time_current)
            if not sts_cnt[0] == 0 and not sts_cnt[1] == 0 and not sts_cnt[2] == 0:
                return True
            time_current = sCtrl.GetPrcsTime()
            time_now = sCtrl.GetPrcsTime()
            sts_cnt = [0, 0, 0]
        LoopCnt += 1
        time_now = sCtrl.GetPrcsTime()

        if time_now - time_start > time_out_sec and not time_out_sec == 0:
            return False
