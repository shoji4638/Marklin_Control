#event_140.py からコピー
#01:

#from getch import getch, pause
import readchar
import sys
import can
import PySimpleGUI as sg
import time
import requests
import random
import pickle#JSONでデータ(辞書型など)保存用
import re
import os
import glob
import pprint

from marklin_can import *
from Event_Data130 import *
from init_gui_07 import gui_init
from init_gui_07 import make_lok_data
from init_gui_07 import init_lok_data

#print=sg.Print

#print(os.path.dirname(__file__))
#print(f'__file__: {__file__}')
#path_icon = 'lok/lok_s/'
path_icon = 'icon/'

can_interface = 'can0'
pi88_mode = [False,0x00]
pibo_mode = [False,0x00]
send = 0
time_mode2 = 0
init_sw_sk = [True,False]     #[スキャン処理、送信完了受信待ち]
load_lok_status = True
#init_sw_sk = [False,False]
debug_l = 0
debug_print = 0

#Pi88_UID = 0x53383BF7
Pi88_UID = bytes([0x53,0x38,0x3B,0x88])

Pi88_HASH = 0x4730
#Link88
Lk88_HASH = 0x474C

#暫定（CS3）
Pi88_ID = Pi88_UID[3]
Pi88_SW = {}

#Pibo_UID = bytes([0x42,0x6F,0x4C,0x88])
#Pibo_HASH = 0x7767
#Booster88_UID = bytes([0x42,0x6F,0x4C,0x50]) 60172
Booster_HASH = 0x733F
#Pibo_UID = bytes([0x42,0x6F,0x4C,0x50]) #60172
#Pibo_HASH = 0x733F

#暫定
CS_HASH = 0xFFFF   #init
#CS_HASH = 0xCF1F   #CS2
#CS_HASH = 0x8B68   #CS3
HASH_Data = {CS_HASH:'CS3 ',Booster_HASH:'BoSr', Pi88_HASH:'RbPi', Lk88_HASH:'Lk88'}

Can_Send_Buffer = []
Can_Send_Delay = 0

bus = can.interface.Bus(can_interface, bustype='socketcan')

#tag_lok = {(b'\x32\x0f\x72\x96\x19'): 'タンク',
#           (b'\x32\x0f\x72\x96\x14'): 'お菓子'}
tag_lok = {'320f729619': 'タンク車　',
           '320f729613': '絵描き貨車',
           '320f729614': 'お菓子貨車'}

while True:
    #*********************************************************************    
    #    CanBus の処理
    message = bus.recv(0.1)
    if not message is None:
        get_cmd = (message.arbitration_id >> 16) & 0x00FF
        get_hash = message.arbitration_id & 0xFFFF
        get_dlc = message.dlc
        get_data = message.data
#        ana_cmd = analysis_can_data(get_cmd,get_hash,get_dlc,get_data)

        if get_cmd == 0x77:
            print('Tag:',get_data[0:5].hex(),'->',tag_lok[get_data[0:5].hex()],'  Can Recive: Cmd:',hex(get_cmd),'Tag:',hex(get_data[0]),hex(get_data[1]),hex(get_data[2]),hex(get_data[3]),hex(get_data[4]),' Cnt:',int(get_data[6]*0x100+get_data[7]))

    