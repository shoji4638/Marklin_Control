#Pi88_107.py からコピー
#04:SW情報表示
#05:辞書型に変更
#08:GUI充実 思うところに表示　トリガー:複数可
#09:CAN送信をストック化
#10:CAN送信を複数ストック化
#11:信号機の状態変更 Cmd(0x17)追加
#12:NotAnd追加など　正常　220308
#14:cmdのDebug表示見直し
#20:データ配列に、EventのOnOffを追加 テスト中
#21:ランプ
#22:ヤードなど追加
#23:
#24:ACS_Data 配列変更
#25:Dataファイル分けるEvent_Data01 ほぼいけるがタイミングで閉鎖区間に侵入するエラーあり
#26:M-S3ほぼ完璧
#27:
#28:バグ修正：Loopの集合Lampの判断を入れる O123−S12　M123-S3の同時　動作OK
#29:to を複数対応　Event_Data04　更新 ヤード１２OK
#30:ヤードin 追加　Event＿Data07 08:OK
#31:Stooop時可視化 EventData09　Tri大幅変更
#40:Data構造変更　Event_Data10
#43:Both機能追加　Event_Data14-> G2In Out:Event_Data15
#44:Can Buffer改善
#100:開発再開、機関車画像
#101:画像ボタンTEST、#102機関車ファンクション基本OK
#103:画像ボタンTEST中 #104:Lamp3画像
#105:Lok表示TEST　Event_Data101.py
#106:From Toとか　ゴニョゴニョ　#107:続き テストOK
#108:O123,M123 S12 S3 OK
#110:6x25 に #112 山エリア周回　整理　Event_Data104
#112:山G3追加　G4LNG  #113 EXITをBOTH対応
#120:GUIのデータ構造変更 'xy'->'xyz'
#121:機関車登録 #123 LokSAVE OK #124 Lok_Locationテスト中
#125:#126:#127 lok_list[0] = station.png lok_list[99] = 99.png未定豚
#127:S88＿Sw＿Datan　['Tri']を消す -2:Lamp3まで動作確認OK
#128:Bothを作り込むよ BothもOK　Event_Data124（最高のデキ）
#130:Lokステータス表示追加 #131:OK #132:init_gui_01を分離 #134OK
#135:init_gui_03と連動／機関車ファンクションOK #機関車　方向　スピード　開発中
#137:init_gui_05と連動 #138:init_gui_06と連動　機関車 方向　スピード　OK
#140:SIDを使用

#from getch import getch, pause
import readchar
import sys
import can
import PySimpleGUI as sg
import time
import requests
import random
import pickle #JSONでデータ(辞書型など)保存用
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
#sg.theme('BluePurple')
sg.theme('LightBlue1')
#sg.theme_previewer()
# OFFボタン図
toggle_btn_off = b'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'

# ONボタン図
toggle_btn_on = b'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'

down = graphic_off = True
#S88_Sw_Disp = [21002,21003,21004,21005,21006,21007]

#for x in S88_Sw_Disp:
#    S88_Sw_Data[x] = [x//10000,x%10000,99,99]
print('S88_Sw_Data{}=',S88_Sw_Data)

layout = []

#S88_Sw_Data_list = list(S88_Sw_Data)
#print(Station_Data_list)
#print(S88_Sw_Data_list)
layout_insert = []
Disp_Location = {}
lok_to = {}

#Disp_Size = [13,12]
Disp_Size = [6,9,6]
#if init_sw_sk[0] == False:
#lok_data = {}
address_temp = 0

#######################################################
## 初期化
cslok_data = make_lok_data()
init_lok_data('lok/',cslok_data)
#pprint.pprint(cslok_data)
#for address_row in cslok_data:
#    print(address_row,cslok_data[address_row]['icon'])
#sys.exit()

if True:

    print('New Display Data！！！')
#    print(ACS_list)
    #ACDデータからGUIデータ（Disp_Locationを作成）
    for group in range(Disp_Size[2]):
        for row in range(Disp_Size[1]):
            for col in range(Disp_Size[0]):
                color_temp = 'sky blue'
                type_temp = 'none'
                ACS_ID_temp = 0x00
                for row_ACS_Data in ACS_Data.items():
#                    print(row_ACS_Data)
#                    if row_ACS_Data[1]['xyz'][0] == col and row_ACS_Data[1]['xyz'][1] == row and row_ACS_Data[1]['xyz'][2] == group:
                    if [col,row,group] == row_ACS_Data[1]['xyz']:
                        print(row,col,group,row_ACS_Data[0],row_ACS_Data[1]['Type'],row_ACS_Data[1][0x0101]['color'])
                        color_temp = 'White'
                        type_temp = row_ACS_Data[1]['Type']
                        ACS_ID_temp = row_ACS_Data[0]
                        break
                Disp_Location.setdefault(f'{col:1}{row:1}{group:1}',{'ACS_ID':ACS_ID_temp,'color':color_temp, 'Type':type_temp})
#                if [col,row,group] == [5,0,3]:
#                    print(row_ACS_Data,Disp_Location['503'])
#                    sys.exit()

    print('S88 Display Data！！！')
#    S88_Sw_list = (list(S88_Sw_Data.items()))
#    print(ACS_list)
    #ACDデータからGUIデータ（Disp_Locationを作成）
    for group in range(Disp_Size[2]):
        for row in range(Disp_Size[1]):
            for col in range(Disp_Size[0]):
                for row_S88_Sw in S88_Sw_Data.items():
#                    print('row_S88_Sw:',row_S88_Sw)
#                    if row_S88_Sw[1]['xyz'][0] == col and row_S88_Sw[1]['xyz'][1] == row and row_S88_Sw[1]['xyz'][2] == group and 'Lok' in row_S88_Sw[1].keys():
                    if [col,row,group] == row_S88_Sw[1]['xyz'] and 'Exit' in row_S88_Sw[1].keys():
#                        Disp_Location.setdefault(f'{col:1}{row:1}{group:1}',{'ACS_ID':row_S88_Sw[1]['Tri']['Lamp3'], 'color': 'sky blue', 'Type': 'Lok', 'Lok_Name': None})
                        if 'Lamp3' in row_S88_Sw[1].keys():
                            Disp_Location[f'{col:1}{row:1}{group:1}'] = {'ACS_ID':row_S88_Sw[1]['Lamp3'], 'Type':'lok', 'color': 'sky blue' }
                            ACS_Data[row_S88_Sw[1]['Lamp3']]['lok_num'] = 0
                            print('S88_Sw_Data->Disp_Location[{}{}{}] = {}\n  ->S88_Sw_Data:{}\n  Lok_Name:?? :{}'.format(row,col,group,Disp_Location[f'{col:1}{row:1}{group:1}'],row_S88_Sw[0],row_S88_Sw[1]['Lamp3']))
                        elif 'Both' in row_S88_Sw[1].keys():
                            Disp_Location[f'{col:1}{row:1}{group:1}'] = {'ACS_ID':row_S88_Sw[1]['Both'], 'Type':'lok', 'color': 'sky blue' }
                            ACS_Data[row_S88_Sw[1]['Both']]['lok_num'] = 0
                            print('S88_Sw_Data->Disp_Location[{}{}{}] = {}\n  ->S88_Sw_Data:{}\n  Lok_Name:?? :{}'.format(row,col,group,Disp_Location[f'{col:1}{row:1}{group:1}'],row_S88_Sw[0],row_S88_Sw[1]['Both']))
                        else:
                            print('Skip:',row_S88_Sw[1])
                        break

else:
    with open('Disp_Location.json','rb') as fp:
        Disp_Location = pickle.load(fp)
        print('Disp_Location Load')
    with open('ACS_Data.json','rb') as fp:
        ACS_data = pickle.load(fp)
        print('ACS_Data Load')

#Disp_Location['0402']= {'color':'yellow','ID':'21003'}
#print('Disp_Location:',Disp_Location['503'])
#print(Disp_Location['0202'])

start_time = time.perf_counter() * 1000

#layout = [[sg.Button(f'{col:02},{row:02}',size=(4,2) ,enable_events=True,key=f'bt{col:02}{row:02}',
#        button_color=('white',Disp_Location[f'{col:02}{row:02}']['color'])) for col in range(Disp_Size[0])] for row in range(Disp_Size[1])]
#filelist = os.listdir(path)

Disp_Location,window,lok_list,flame_list,icon_list = gui_init(Disp_Size,Disp_Location,ACS_Data,cslok_data)

#while True:
#    event, values = window.read(timeout=50,timeout_key='-guitimeout-')

def reset_data():
    Disp_Location = {}
#Disp_Location.setdefault(str((f'{col:02}'),1) for col in range(4))
#print((f'{col:02}{row:02}',f'{col}') for col in range(4) for row in range(10))
#ACS_list = (list(ACS_Data.values()))
    ACS_list = (list(ACS_Data.items()))

    for group in range(Disp_Size[2]):
        for row in range(Disp_Size[1]):
            for col in range(Disp_Size[0]):
                color_temp = 'sky blue'
                type_temp = 'none'
                ACS_ID_temp = 0x00
                for row_ACS_Data in ACS_list:
#                print(row_ACS_Data)
                    if row_ACS_Data[1]['xyz'][0] == col and row_ACS_Data[1]['xyz'][1] == row and row_ACS_Data[1]['xyz'][2] == group:
                        print(row,col,group,row_ACS_Data[0],row_ACS_Data[1]['Type'],row_ACS_Data[1][0x0101]['color'])
                        color_temp = 'white'
                        type_temp = row_ACS_Data[1]['Type']
                        ACS_ID_temp = row_ACS_Data[0]
                        break
                Disp_Location.setdefault(f'{col:1}{row:1}{group:1}',{'ACS_ID':ACS_ID_temp,'color':color_temp, 'Type':type_temp})
#    print('Stop!!!')
#    sys.exit()

def save_data():
    with open('Disp_Location.json','wb') as fp:
        pickle.dump(Disp_Location, fp)
        print('Disp_Location SAVE')
#    with open('ACS_Data.json','wb') as fp:
#        pickle.dump(ACS_Data, fp)
#        print('ACS_Data SAVE')

def load_lok_data():

    with open('ACS_Data.bin','rb') as fp:
        ACS_Data_Load = pickle.load(fp)
        print('Load [Lok_location]:',ACS_Data_Load)
        for num,ACS_Data_Load_row in enumerate(ACS_Data_Load.items()):
#            print(num,Disp_Location_row[1])
            if 'lok_num' in ACS_Data_Load_row[1].keys():
            
#                if Disp_Location_row[1]['Lok_num'] == 99:
                lok_num_temp = ACS_Data_Load_row[1]['lok_num']
                xyz_temp = ACS_Data_Load_row[1]['xyz']
                xyz_temp[0] += 2
                print(xyz_temp,ACS_Data[ACS_Data_Load_row[0]]['After'],end="")
                if lok_num_temp != 0 and ACS_Data[ACS_Data_Load_row[0]]['After'] == 1:
#                        print(Disp_Location_row[1])
#                        ACS_Data[ACS_Data_Load_row[0]]['lok_num'] = lok_num_temp
                    print(ACS_Data_Load_row[1],lok_num_temp,)
                    window[f'bt{xyz_temp[0]:1}{xyz_temp[1]:1}{xyz_temp[2]:1}'].update(image_filename=lok_list[lok_num_temp]['lok_name'],button_color=(flame_list[xyz_temp[2]][3], flame_list[xyz_temp[2]][3]))

#                        sys.exit()
                else:
                    lok_num_temp = 0
                    print('No lok')
                    window[f'bt{xyz_temp[0]:1}{xyz_temp[1]:1}{xyz_temp[2]:1}'].update(image_filename=lok_list[lok_num_temp]['lok_name'],button_color=(flame_list[xyz_temp[2]][3], flame_list[xyz_temp[2]][3]))
                
                ACS_Data[ACS_Data_Load_row[0]]['lok_num'] = lok_num_temp
#                    if 'Lamp3' in S88_Sw_Data[Disp_Location_row[1]['sw1']]['Tri'].keys()
#                        print(ACS_Data[S88_Sw_Data[Disp_Location_row[1]['sw1']]['Tri']['Lamp3']][])
#                    elif 'Both' in S88_Sw_Data[Disp_Location_row[1]['sw1']]['Tri'].keys()





while True:
    #*********************************************************************    
    #    GUI の処理
    
    event, values = window.read(timeout=50,timeout_key='-guitimeout-')
    if event in (None,):
        print(event,values)
    location_temp = window['-Lok_Lo-'].DisplayText
    if event in (None,):
        break
    elif event in '-guitimeout-':
#        update_text = 'Pi88_ID:'+str(Pi88_ID)
        update_text = 'Pi88_ID: '+str(Pi88_ID)
        window['-ID-'].update(update_text)
        window['-status-'].update('{},{},{}'.format(init_sw_sk[0],init_sw_sk[1],load_lok_status))
#        window['-pi88_mode-'].update(update_text)
#        update_text = str(pibo_mode[1])
#        window['-pibo_mode-'].update(update_text)

        if debug_l >= 10:
            print('*',end='')
    elif event == '実行ボタン':
        update_text = "Button clicked."
        # 表示内容を更新する際はウィジェットに指定されたkeyの値に.update("文字列")を入れることで可能
        window['-TEXT-'].update(update_text)
#    elif event[0:2] == 'sw':
#        print(event,values[event])
    elif event[0:4] == '-lok':
        if event[0:5] == '-lokb':
#            print(int(event[5:8]),cslok_data[int(event[5:8])])
            uid_temp = int(event[5:9],16)
            LokGui_arr = [
                {'wkey': '-Lokt-'       , 'fstr': ''        , 'lok_dict': 'name'},
                {'wkey': '-Lok_adresse-', 'fstr': 'Address:', 'lok_dict': 'adresse'},
                {'wkey': '-Lok_typ-'    , 'fstr': 'Type:'   , 'lok_dict': 'typ'},
                {'wkey': '-Lok_mfxuid-' , 'fstr': 'MfxUID:' , 'lok_dict': 'mfxuid'},
                {'wkey': '-Lok_uid-'    , 'fstr': 'UID:'    , 'lok_dict': 'uid'},
                {'wkey': '-Lok_tachomax-','fstr': 'tachoMax:','lok_dict': 'tachomax'},
                {'wkey': '-Lok_velocity-','fstr': 'Speed:' , 'lok_dict': 'velocity'},
                {'wkey': '-Lok_vmax-'   , 'fstr': 'Vmax:'   , 'lok_dict': 'vmax'},
                {'wkey': '-Lok_vmin-'   , 'fstr': 'Vmin:'   , 'lok_dict': 'vmin'},
                {'wkey': '-Lok_richtung-'   , 'fstr': 'Dire:'   , 'lok_dict': 'richtung'},
                {'wkey': '-Lok_av-'   , 'fstr': 'AcelV:'   , 'lok_dict': 'av'},
                {'wkey': '-Lok_bv-'   , 'fstr': 'BrekV:'   , 'lok_dict': 'bv'},
                ]
#            LokGui_chenge(uid_temp,)
            
 #           window['-Lokt-'].update(cslok_data[uid_temp]['name'])
            window['-Lokb-'].update(image_filename='lok/org/'+cslok_data[uid_temp]['icon']+'.png')
#            window['-Lok_adresse-'].update('Address:'+ cslok_data[uid_temp]['adresse'])
#            window['-Lok_typ-'].update('Type:'+ cslok_data[uid_temp]['typ'])
            for LokGui in LokGui_arr:
                if cslok_data[uid_temp].get(LokGui['lok_dict']) != None:
                    if type(cslok_data[uid_temp][LokGui['lok_dict']]) is int:
                        window[LokGui['wkey']].update(LokGui['fstr']+ str(cslok_data[uid_temp][LokGui['lok_dict']]))
                    else:
                        window[LokGui['wkey']].update(LokGui['fstr']+ cslok_data[uid_temp][LokGui['lok_dict']])
                else:
                    window[LokGui['wkey']].update(LokGui['fstr']+ '????')
                
#            window['-Lok_mfxuid-'].update('MfxID:'+ cslok_data[uid_temp].get('mfxuid'))
#            window['-Lok_uid-'].update('UID:'+ cslok_data[uid_temp]['uid'])
#            window['-Lok_velocity'].update('Velocity:'+ cslok_data[uid_temp]['velocity'])
            
#            direction_temp = 3
#            print(uid_temp,direction_temp)
#            Can_Send_Buffer.append([300 ,{'id':0x000A_0000, 'HASH':0x8b68, 'dlc':5, 'data':[0x00,0x00,uid_temp >> 8,uid_temp & 0xff,direction_temp]}])
#            Can_Send_Buffer.append([300 ,{'id':0x000A_0000, 'HASH':0x8b68, 'dlc':4, 'data':[0x00,0x00,uid_temp >> 8,uid_temp & 0xff]}])
#            Can_Send_Buffer.append([300 ,{'id':0x000C_0000, 'HASH':0x8b68, 'dlc':5, 'data':[0x00,0x00,uid_temp >> 8,uid_temp & 0xff,0]}])
                    
        elif event[0:5] == '-lokf':
            uid_temp = int(event[7:11],16)
            print(uid_temp,cslok_data[uid_temp])
#            func_temp = cslok_data[int(event[6:9])]['funktionen']['nr='+event[5:6]]
            func_temp = cslok_data[uid_temp]['funktionen'][int(event[5:7])]
#            func_typ_temp = func_temp['typ']
            if func_temp['value'] == None:
                func_temp['value'] = False
            func_temp['value'] = not func_temp['value'] 
            print(uid_temp,func_temp,func_temp['typ'],func_temp['value'])
            Can_Send_Buffer.append([300 ,{'id':0x000C_0000, 'HASH':0x8b68, 'dlc':6, 'data':[0x00,0x00,uid_temp >> 8,uid_temp & 0xff,int(event[5:7]), func_temp['value']]}])
#            window[event].update(image_filename='icon/FktIcon_a_ge_'+f'{func_typ_temp:02}.png',button_color=(sg.theme_background_color(), sg.theme_background_color()))

#            msg = can.Message(arbitration_id=0x000C_8B68, dlc=6, data=[0x00,0x00,0x40,0x1D,0x03,0x01], is_extended_id=True)
#            msg = can.Message(arbitration_id=0x000C_8B68, dlc=6, data=[0x00,0x00,uid_temp>>8,uid_temp&0xFF,int(event[5:6]),0x01], is_extended_id=True)
#            send = 1
        #スライダー
        elif event[0:5] == '-loks':
            uid_temp = int(event[5:9],16)
            if cslok_data[uid_temp]['tachomax'] == 10:
                logic_speed = int(values[event])*10   #10-> *1000/100 %
                real_speed = int(values[event])
                print(f'{uid_temp:04x} ',real_speed,'% ',logic_speed)
            else:
                real_speed = int(values[event])*cslok_data[uid_temp]['tachomax']//100
                logic_speed = real_speed*1000//cslok_data[uid_temp]['tachomax']
                print(f'{uid_temp:04x} ',real_speed,'km/h ',logic_speed)
            Can_Send_Buffer.append([300 ,{'id':0x0008_0000, 'HASH':0x8b68, 'dlc':6, 'data':[0x00,0x00,uid_temp >> 8,uid_temp & 0xff,logic_speed>>8,logic_speed&0xff]}])
#            window['-lokv'+event[5:]].update('<'+ str(real_speed))

        elif event[0:5] == '-lokv':
            uid_temp = int(event[5:9],16)
            before_richtung = cslok_data[uid_temp]['richtung']
#            if cslok_data[uid_temp]['richtung'] == 0:
#                cslok_data[uid_temp]['richtung'] = 1
#            else:
#                cslok_data[uid_temp]['richtung'] = 0
            cslok_data[uid_temp]['richtung'] = not cslok_data[uid_temp]['richtung']
            print('Speed:',cslok_data[uid_temp]['velocity'],'Dir:',before_richtung,'->',cslok_data[uid_temp]['richtung'])
            
            Can_Send_Buffer.append([300 ,{'id':0x000A_0000, 'HASH':0x8b68, 'dlc':5, 'data':[0x00,0x00,uid_temp >> 8,uid_temp & 0xff,cslok_data[uid_temp]['richtung']+1]}])
#            Can_Send_Buffer.append([300 ,{'id':0x000B_0000, 'HASH':0x8b68, 'dlc':4, 'data':[0x00,0x00,uid_temp >> 8,uid_temp & 0xff]}])

#            window['']

        #レイアウト上の機関車を登録処理
    elif event[:10] == '-setlokpng' and location_temp[:3] == 'bt4':
#        elif location_temp[:3] == 'bt4':
##         window[].update(update_text)event[4:6]
##        Disp_Location[location_temp[2:5]]['Lok_Name'] = lok_filenames[int(event[4:6])]
        ACS_ID_Temp = Disp_Location[location_temp[2:5]]['ACS_ID']
        print(f'Lok Click: {event} {ACS_ID_Temp:04X}',lok_list[int(event[10:14],16)],end='')
#        print(ACS_Data[ACS_ID_Temp]['lok_num'])
        ACS_Data[ACS_ID_Temp]['lok_num'] = int(event[10:14],16)
        print(ACS_Data[ACS_ID_Temp]['lok_num'])
#            print('Lok Click:',event,ACS_ID_Temp,ACS_Data[ACS_ID_Temp]['lok_num'],lok_list[int(event[4:6])]['lok_name'])
        window[window['-Lok_Lo-'].DisplayText].update(image_filename=lok_list[int(event[10:14],16)]['lok_name'],button_color=(sg.theme_background_color(), sg.theme_background_color()))

        #機関車のデータべーズにSIDを登録
#        SID_Temp = window['-SID-'].DisplayText
#        if SID_Temp[0:2] == '0x': 
#            window[f'-SID{int(event[4:6]):03}-'].update(SID_Temp)
#            lok_list[int(event[4:6])]['SID'] = int(SID_Temp, 0)
#            print(lok_list[int(event[4:6])])
#            window[f'-SID{int(event[4:6]):03}-'].update('ABCD')

#    elif event[0:4] == '-SID':
#        print(event)
#        window[event].update(button_text='ABC')
#       window.find_element(event).Update(button_color=('gray','gray'))
#        window.find_element(event).Update('ABC')
#        sys.exit()

#        if event == '-lok08-':
##        msg = can.Message(arbitration_id=0x00000000+CS_HASH, dlc=6, data=[0x00,0x00,0x00,0x0d,0x03,0x01], is_extended_id=True)
#            msg = can.Message(arbitration_id=0x000C_8B68, dlc=6, data=[0x00,0x00,0x40,0x0B,0x00,0x01], is_extended_id=True)
#            send = 1
##        Can_Send_Buffer.append([300 ,{'id':0x000C_8b68, 'HASH':0x8b68, 'dlc':6, 'data':[0x00,0x00,0x00,0x0b,0x00,0x01]}])
#        elif event == '-lok10-':
#            SID = 0x4014
#            lok_data[SID][1] ^= 1 #On:1-Off:0 反転
##        print(lok_data[SID])
##        print(lok_data[SID]['bt_color'][lok_data[SID][1]])
#            bt_color = ['gray',lok_data[SID]['bt_color'][lok_data[SID][1]]]
#            print('SID:{0:02d} {1} {2}'.format(SID,lok_data[SID],bt_color))
##        msg = can.Message(arbitration_id=0x00000000+CS_HASH, dlc=6, data=[0x00,0x00,0x00,0x0d,0x03,0x01], is_extended_id=True)
##        msg = can.Message(arbitration_id=0x000C_8B68, dlc=6, data=[0x00,0x00,SID>>8,SID&0xFF,0x01,lok_data[SID][1]], is_extended_id=True)
##        send = 1
#            Can_Send_Buffer.append([300 ,{'id':0x000C_0000, 'HASH':0x8b68, 'dlc':6, 'data':[0x00,0x00,SID>>8&0xFF,SID&0xFF,0x01,lok_data[SID][1]]}])
##        window.find_element(event).Update(button_color=(bt_color))
#            window.find_element(event).Update(button_color=(bt_color))

    elif event[0:2] == 'bt':
        print('bt:',event[2:5],'list:',event[2:5] in Disp_Location)
        sw_color = ['gray','gray']
        ACS_ID_Temp = Disp_Location[event[2:6]]['ACS_ID']
        if Disp_Location[event[2:5]]['Type'] == 'Lamp3':
            if Disp_Location[event[2:5]]['color'] == 'white':
                sw_color = ['gray','red']
            elif Disp_Location[event[2:5]]['color'] == 'red':
                sw_color = ['gray','green']
            elif Disp_Location[event[2:5]]['color'] == 'green':
                sw_color = ['gray','yellow']
            elif Disp_Location[event[2:5]]['color'] == 'yellow':
                sw_color = ['gray','white']
            window.find_element(event).update(image_data=toggle_btn_on)
            #window.find_element(event).Update(button_color=(sw_color))

        elif  Disp_Location[event[2:5]]['Type'] == 'LampBlue':
            if Disp_Location[event[2:5]]['color'] != 'blue':
                sw_color = ['gray','blue']
                Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,(ACS_ID_Temp & 0xFF000000) // 0x1000000,(ACS_ID_Temp & 0xFF0000) //0x10000,0x01,0x01]}])
                Disp_Location[event[2:5]]['color'] = 'blue'
            else:
                sw_color = ['gray','gray']
                Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,(ACS_ID_Temp & 0xFF000000) // 0x1000000,(ACS_ID_Temp & 0xFF0000) //0x10000,0x00,0x01]}])
                Disp_Location[event[2:5]]['color'] = 'gray'
            window.find_element(event).Update(button_color=(sw_color))

        elif  Disp_Location[event[2:5]]['Type'] == 'SW1':
            
            if Disp_Location[event[2:5]]['color'] != 'green':
                sw_color = ['gray','green']
                window.find_element(event).update(image_data=toggle_btn_on)
#                Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,(ACS_ID_Temp & 0xFF000000) // 0x1000000,(ACS_ID_Temp & 0xFF0000) //0x10000,0x01,0x01]}])
                msg = can.Message(arbitration_id=0x0016_8B68, dlc=6, data=[0x00,0x00,(ACS_ID_Temp & 0xFF000000) // 0x1000000,(ACS_ID_Temp & 0xFF0000) //0x10000,0x01,0x01,0x01,0x01], is_extended_id=True)
                send = 1
                Disp_Location[event[2:5]]['color'] = 'green'
            else:
                sw_color = ['gray','gray']
                window.find_element(event).update(image_data=toggle_btn_off)
#                Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,(ACS_ID_Temp & 0xFF000000) // 0x1000000,(ACS_ID_Temp & 0xFF0000) //0x10000,0x00,0x01]}])
                msg = can.Message(arbitration_id=0x0016_8B68, dlc=6, data=[0x00,0x00,(ACS_ID_Temp & 0xFF000000) // 0x1000000,(ACS_ID_Temp & 0xFF0000) //0x10000,0x01,0x01,0x00,0x01], is_extended_id=True)
                send = 1
                Disp_Location[event[2:5]]['color'] = 'gray'
                
        elif  Disp_Location[event[2:5]]['Type'] == 'ONOFF3':
#            ACS_ID_Temp = Disp_Location[event[2:5]]['ACS_ID']
            ACS_Data[ACS_ID_Temp]['After'] = (ACS_Data[ACS_ID_Temp]['After'] ^ 1) & 1
            print(hex(ACS_ID_Temp))
#            msg = can.Message(arbitration_id=0x0016_8B68, dlc=6, data=[0x00,0x00, ACS_ID_Temp >> 16 ,ACS_ID_Temp & 0xFF,0x00,0x01,0x00,0x00], is_extended_id=True)
#            send = 1
            Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,ACS_ID_Temp >> 8 , ACS_ID_Temp & 0xFF,ACS_Data[ACS_ID_Temp]['After'],0x01]}])

        #4桁目 クリックしたbt4xxをバッファ入れる
        elif  Disp_Location[event[2:5]]['Type'] == 'lok':
            window['-Lok_Lo-'].update(event)

        #未知の bt
        print('Unknow bt',event[2:5],hex(Disp_Location[event[2:5]]['ACS_ID']),Disp_Location[event[2:5]])

    elif event == 'Go':
        msg = can.Message(arbitration_id=0x00000000+Pi88_HASH, dlc=5, data=[0x00,0x00,0x00,0x00,0x01], is_extended_id=True)
        send = 1
        print('Go')
    elif event == 'Stop':
        msg = can.Message(arbitration_id=0x00000000+Pi88_HASH, dlc=5, data=[0x00,0x00,0x00,0x00,0x00], is_extended_id=True)
        send = 1
        print('Stop')

    elif event == '-SEND-':
        msg = can.Message(arbitration_id=0x00310000+Pi88_HASH, dlc=4, data=bytes([int(values['-IN00-']),int(values['-IN01-']),int(values['-IN02-']),int(values['-IN03-']),int(values['-IN04-']),int(values['-IN05-']),int(values['-IN06-']),int(values['-IN07-'])]), is_extended_id=True)
        message_data_print(values['can_read'],(msg.arbitration_id >> 16) & 0x00FF,msg.arbitration_id & 0xFFFF,msg.data)
        bus.send(msg)
    elif event == 'SAVE':
        save_data()
    elif event == '-LOKSAVE-':
        with open('ACS_Data.bin','wb') as fp:
            pickle.dump(ACS_Data, fp)
            print('ACS_Data & Lok_location for BIN SAVE')

        with open('cslok_data.bin','wb') as fp:
            pickle.dump(cslok_data, fp)
            print('cslok_data for BIN SAVE')
        
#        for num,ACS_Data_row in enumerate(ACS_Data.items()):
#            print('LOKSAVE',num,ACS_Data_row[1])
#            if 'lok_num' in ACS_Data_row[1].keys():
#                print('lok_num:',num,ACS_Data_row[1]['lok_num'])
    elif event == '-LOKLOAD-':
#        lokload_data()

#def lokload_data():
        load_lok_data()


    elif event == 'TEST 00':
#        msg = can.Message(arbitration_id=0x0016_0000+Pi88_HASH, dlc=6, data=[0x00,0x00,S88_Sw_Data[sw_id]['Tri']['Lamp3']//0x100,S88_Sw_Data[sw_id]['Tri']['Lamp3']%0x100,0x01,0x01], is_extended_id=True)
        msg = can.Message(arbitration_id=0x0016_0000+Pi88_HASH, dlc=6, data=[0x00,0x00,0x30,0x00,0x00,0x01], is_extended_id=True)
        bus.send(msg)
#        msg = can.Message(arbitration_id=0x0016_0000+Pi88_HASH, dlc=6, data=[0x00,0x00,S88_Sw_Data[sw_id]['Tri']['Lamp3']//0x100,S88_Sw_Data[sw_id]['Tri']['Lamp3']%0x100,0x01,0x00], is_extended_id=True)
#        bus.send(msg)
    elif event == 'TEST 01':
#        msg = can.Message(arbitration_id=0x0016_0000+Pi88_HASH, dlc=6, data=[0x00,0x00,S88_Sw_Data[sw_id]['Tri']['Lamp3']//0x100,S88_Sw_Data[sw_id]['Tri']['Lamp3']%0x100,0x01,0x01], is_extended_id=True)
        msg = can.Message(arbitration_id=0x0016_0000+Pi88_HASH, dlc=6, data=[0x00,0x00,0x30,0x00,0x01,0x01], is_extended_id=True)
        bus.send(msg)
    elif event == 'SCAN':
        #アクセサリ更新
        for row_id in ACS_Data.keys():
            xyz_temp = ACS_Data[row_id]['xyz']
            print('row_id',row_id,' xyz_temp:',xyz_temp)
#            print(hex(row_id),xy_temp,Disp_Location[xy_temp],ACS_Data[row_id]['Type'])
            Disp_Location['{:1}{:1}{:1}'.format(xyz_temp[0],xyz_temp[1],xyz_temp[2])] = {'ACS_ID': row_id,'color':'gray','Type':ACS_Data[row_id]['Type']}
            print(hex(row_id),xyz_temp,Disp_Location['{:1}{:1}{:1}'.format(xyz_temp[0],xyz_temp[1],xyz_temp[2])],ACS_Data[row_id]['Type'])
            print(' New:',Disp_Location['{:1}{:1}{:1}'.format(xyz_temp[0],xyz_temp[1],xyz_temp[2])])

#        sorted_S88_Sw_Data = sorted(S88_Sw_Data.items())
#        print(sorted_S88_Sw_Data)
        for S88_id_temp in S88_Sw_Data.keys():
            #print(row_S88_Data[1]['Befor'])
            S88_Sw_Data[S88_id_temp]['After'] == 99
            print(S88_Sw_Data[S88_id_temp])
        
        init_sw_sk = [True,False]

    elif event == '-TOGGLE-GRAPHIC-':
        if sg.popup_yes_no('SAVE LOK DATA?') == 'Yes':
            loksave_data()
        if sg.popup_ok_cancel('Close?') == 'OK':
            sys.exit()
#        graphic_off = not graphic_off
#        window['-TOGGLE-GRAPHIC-'].update(image_data=toggle_btn_off if graphic_off else toggle_btn_on)
#
    else:
        print('Error Bottun!!!!',event,values)

    #*********************************************************************    
    #    CanBus の処理
    message = bus.recv(0.1)
    if not message is None:
        get_cmd = (message.arbitration_id >> 16) & 0x00FF
        get_hash = message.arbitration_id & 0xFFFF
        get_dlc = message.dlc
        get_data = message.data
        if debug_print > 1 :
            message_data_print(values['can_read'],get_cmd,get_hash,get_data)  #Read Can Data
#        ana_cmd = analysis_can_data(get_cmd,get_hash,get_dlc,get_data)  #DebugのときON
        ana_cmd = get_cmd
        #機関車の制御
        #ファンクション（0xc）
        if ana_cmd == 0x0C:
            print('Lok CanID 0x0C Hash:{0:4X} Dlc:{1:01X} Data:{2:02X} {3:02X} {4:02X} {5:02X} {6:02X} {7:02X}'.format(get_hash,get_dlc,get_data[0],get_data[1],get_data[2],get_data[3],get_data[4],get_data[5]))
            window['-SID-'].update(hex(get_data[2]*0x100 + get_data[3]))
            window.find_element('-lok_cmd_x0C-').Update('Lok Function SID:{:02x}{:02x} Fun{:02x}{:02x} '.format(get_data[2],get_data[3],get_data[4],get_data[5]))
        elif ana_cmd == 0x0A:
            print('Lok CanID 0x0A Hash:{:4X} Dlc:{:01X} Data:{:02X} {:02X} {:02X} {:02X} {:02X} '.format(get_hash,get_dlc,get_data[0],get_data[1],get_data[2],get_data[3],get_data[4]))
            window['-SID-'].update(hex(get_data[2]*0x100 + get_data[3]))
            window.find_element('-lok_cmd_x0A-').Update('Lok Direction SID:{:02x}{:02x} Dir{:02x} '.format(get_data[2],get_data[3],get_data[4]))
        elif ana_cmd == 0x08:   #スピード送信
            print('Lok CanID 0x08 Hash:{0:4X} Dlc:{1:01X} Data:{2:02X} {3:02X} {4:02X} {5:02X} {6:02X} {7:02X}'.format(get_hash,get_dlc,get_data[0],get_data[1],get_data[2],get_data[3],get_data[4],get_data[5]))
            window['-SID-'].update(hex(get_data[2]*0x100 + get_data[3]))
            window.find_element('-lok_cmd_x08-').Update('Lok Function SID:{:02x}{:02x} Spe{:02x}{:02x} '.format(get_data[2],get_data[3],get_data[4],get_data[5]))

        elif ana_cmd == 0x09:    #スピード受信
            uid_temp = (get_data[2] << 8) + get_data[3]
            logic_speed = cslok_data[uid_temp]['velocity'] = (get_data[4]<<8)+get_data[5]
            print('Lok CanID 0x09 Hash:{:4X} Dlc:{:01X} Data:{:02X} {:02X} {:02X} {:02X} {:02X} {:02X} LogicSp:{:03} '.format(get_hash,get_dlc,get_data[0],get_data[1],get_data[2],get_data[3],get_data[4],get_data[5],logic_speed),end='')
            if cslok_data[uid_temp]['tachomax'] == 10:
                real_speed = logic_speed // 10
                print('Speed:{}%'.format(real_speed))
            else:
                real_speed = logic_speed * cslok_data[uid_temp]['tachomax'] // 1000
                print('Speed:{}km/h'.format(real_speed))

            if cslok_data[uid_temp]['richtung'] == True:
                window['-lokv{:04x}-'.format(uid_temp)].update(f'{real_speed:03}>',button_color=('blue', '#D0D0D0'))
            else:
                window['-lokv{:04x}-'.format(uid_temp)].update(f'<{real_speed:03}',button_color=('yellow', '#D0D0D0'))

        elif ana_cmd == 0x0B:    #方向　受信
            print('Lok CanID 0x0B Hash:{:4X} Dlc:{:01X} Data:{:02X} {:02X} {:02X} {:02X} {:02X} '.format(get_hash,get_dlc,get_data[0],get_data[1],get_data[2],get_data[3],get_data[4]),end='')
            uid_temp = (get_data[2] << 8) + get_data[3]
            cslok_data[uid_temp]['velocity'] = 0
            window['-loks{:04x}-'.format(uid_temp)].Update(0)
            
            print(' -> -lokv{:04x}- {} {}'.format(uid_temp,get_data[4],cslok_data[uid_temp]['richtung']))
            if get_data[4] == 1:
                window['-lokv{:04x}-'.format(uid_temp)].update('000>',button_color=('red', '#B0B0B0'))
                cslok_data[uid_temp]['richtung'] = True
            elif get_data[4] == 2:
#                window['-lokv{:04x}-'.format(uid_temp)].update(button_text='<',button_color=(sg.theme_background_color(), sg.theme_background_color()))
                window['-lokv{:04x}-'.format(uid_temp)].update('<000',button_color=('red', '#B0B0B0'))
                cslok_data[uid_temp]['richtung'] = False
#                window.find_element('-lokv{:04x}-'.format(uid_temp)).Update('<',button_color=(sg.theme_background_color(), sg.theme_background_color()))

        #Lok Function 受信
        elif ana_cmd == 0x0D:
#            uid_temp = get_data[2] * 0x100 + get_data[3]
            uid_temp = (get_data[2] << 8) + get_data[3]
#            uid_temp = get_data[3]
            print(f'{uid_temp:04x}',cslok_data[uid_temp])
            func_typ_temp = cslok_data[uid_temp]['funktionen'][get_data[4]]['typ']
            print('Lok CanID 0x0D Hash:{:4X} Dlc:{:01X} Data:{:02X} {:02X} {:02X} {:02X} {:02X} {:02X}'.format(get_hash,get_dlc,get_data[0],get_data[1],get_data[2],get_data[3],get_data[4],get_data[5]))

#            func_typ_temp = cslok_data[uid_temp]['funktionen'][get_data[4]]['typ']
            if get_data[5] == 0:
                window['-lokf{:02}{:04x}-'.format(get_data[4],uid_temp)].update(image_filename='icon/FktIcon_i_gr_'+f'{func_typ_temp:02}.png',button_color=(sg.theme_background_color(), sg.theme_background_color()))
            else:
#                window['-lokf{}{:03}-'.format(get_data[4],uid_temp)].update(image_filename='icon/FktIcon_a_ge_'+f'{func_typ_temp:02}.png',button_color=(sg.theme_background_color(), sg.theme_background_color()))
                window['-lokf{:02}{:04x}-'.format(get_data[4],uid_temp)].update(image_filename='icon/FktIcon_a_ge_{:02}.png'.format(func_typ_temp),button_color=(sg.theme_background_color(), sg.theme_background_color()))

#        elif
#            print('Unknow CMD:',ana_cmd)
        
        

        #S88 Change *********************************************************
        elif  ana_cmd == 0x23:
            sw_id =  get_data[0]*1000000 +get_data[1]*10000 +get_data[2]*0x100 +get_data[3]
            print('\ncmd=0x23:',get_dlc,sw_id,end=' ')
            if sw_id in S88_Sw_Data.keys():
#                print('Resp!!!!')
                S88_Sw_Data[sw_id]['Befor'] = get_data[4]
                S88_Sw_Data[sw_id]['After'] = get_data[5]
#                    row_Station_Data[1][3:5] = [get_data[4],get_data[5]]
                print('S88_Data->',S88_Sw_Data[sw_id],S88_Sw_Data[sw_id])
                print('XYZ:',S88_Sw_Data[sw_id]['xyz'])
                location_xyz = 'bt{:1}{:1}{:1}'.format(S88_Sw_Data[sw_id]['xyz'][0],S88_Sw_Data[sw_id]['xyz'][1],S88_Sw_Data[sw_id]['xyz'][2])
#                if S88_Sw_Data[sw_id]['xyz'] != [99,99,99]:
##                    sys.exit()
#    #                print('[xy]:',S88_Sw_Data[sw_id]['xyz'],'Disp_location[xxyy]:',Disp_Location['{:1}{:1}{:1}'.format(S88_Sw_Data[sw_id]['xyz'][0],S88_Sw_Data[sw_id]['xyz'][1])])
#                    if get_data[5] == 1:
#                        sw_color = ['gray','yellow']
##                        layout_temp.append(sg.Button(image_filename=path_icon + icon_list['Lamp2'][1], key=f'bt{col:02}{row:02}' ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0))
#                        window.find_element(location_xyz).update(image_filename=path_icon + icon_list['Lamp2'][0])
#
##                    print('St_Data:ON',S88_Sw_Data[sw_id])
#                    else:
#                        sw_color = ['gray','white']
##                        layout_temp.append(sg.Button(image_filename=path_icon + icon_list['Lamp2'][0], key=f'bt{col:02}{row:02}' ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0))
##                        window.find_element(location_xyz).update(image_filename=path_icon + icon_list['Lamp2'][1])
##                    if (Disp_Location['{:1}{:1}{:1}'.format(S88_Sw_Data[sw_id]['xyz'][0],S88_Sw_Data[sw_id]['xyz'][1])]['type'] == 'sw1'):
##                        sys.exit()
##                    else:
##                        window.find_element('bt{:1}{:1}{:1}'.format(S88_Sw_Data[sw_id]['xyz'][0],S88_Sw_Data[sw_id]['xyz'][1])).Update(button_color=(sw_color))
##                print(S88_Sw_Data[sw_id]['Tri'])
#####                Temp_Disp_Location = list(Disp_Location.values())
#####            print('Temp_Disp_Location:',Temp_Disp_Location)

            # Triger処理
                Tri_temp = S88_Sw_Data[sw_id]
                #閉鎖区間に電車突っ込んだ　停止せよ
                if 'in' in S88_Sw_Data[sw_id] and S88_Sw_Data[sw_id]['After'] == 1:
#                    print('Event Triger:',S88_Sw_Data[sw_id],end='')               
                    print('Event Triger_in:',S88_Sw_Data[S88_Sw_Data[sw_id]['in']]['After'])
                    if S88_Sw_Data[S88_Sw_Data[sw_id]['in']]['After'] != 0:
                        msg = can.Message(arbitration_id=0x0000_0000+Pi88_HASH, dlc=5, data=[0x00,0x00,0x00,0x00,0x00], is_extended_id=True)
                        bus.send(msg)
                        print('Stoooop!!!!')
                        sw_color = ['black','black']
                        window.find_element('bt{:1}{:1}{:1}'.format(S88_Sw_Data[sw_id]['xyz'][0],S88_Sw_Data[sw_id]['xyz'][1],S88_Sw_Data[sw_id]['xyz'][2])).Update(button_color=(sw_color))

                #閉塞区間 出たら　信号を赤に
                if 'Exit' in Tri_temp.keys() and S88_Sw_Data[sw_id]['After'] == 0:
                    if 'Both' in Tri_temp.keys():
                        print('\n\nS88 Off Both Stop!!!')
                        print('BothLamp:{:04X}/{:x}'.format(Tri_temp['Both'],ACS_Data[Tri_temp['Both']]['After']),end='')
#                        print('BothLamp:{:04X}/{:x}'.format(Tri_temp['Both'],ACS_Data[Tri_temp['Both']]['After']),end='')
                        if ACS_Data[Tri_temp['Both']]['After'] == 0x10:
                            Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,Tri_temp['Exit']>>8,Tri_temp['Exit']&0xFF,0x00,0x01]}])
#                            sys.exit()
                    elif Tri_temp['Exit'] != None:
                        Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,Tri_temp['Exit']>>8,Tri_temp['Exit']&0xFF,0x00,0x01]}])
                
                #S88 OnOff -> Lamp処理　と　機関車表示
                if 'Lamp3' in S88_Sw_Data[sw_id].keys():
                    #黄色？
                    ACS_Lamp3_Temp = S88_Sw_Data[sw_id]['Lamp3']
                    if S88_Sw_Data[sw_id]['After'] == 1:
                        print('S88_On_Lamp3 Triger:{:04x}'.format(ACS_Lamp3_Temp))
                        Can_Send_Buffer.append([Can_Send_Delay ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,ACS_Lamp3_Temp//0x100,ACS_Lamp3_Temp%0x100,0x01,0x01]}])
                        print('\n/n********lok_to:',lok_to)
                        print('**************:',ACS_Data[ACS_Lamp3_Temp])
                        if ACS_Lamp3_Temp in lok_to.keys():
                            #S88 ON⇒Lamp3⇒lok_toにTOにACS_IDあり
                            lok_to_temp = lok_to.pop(ACS_Lamp3_Temp)    #popで取出す
                            print(lok_to_temp)
                            print('  ***lok_to.inKey!!!:',lok_to_temp['lok_num'],lok_list[lok_to_temp['lok_num']]['lok_name'])
                            ACS_Data[ACS_Lamp3_Temp]['lok_num'] = lok_to_temp['lok_num']
                            print('******lok:{:04x} -> {:04x}'.format(lok_to_temp['From'],ACS_Lamp3_Temp))
#                                print(ACS_Data[ACS_Lamp3_Temp])
#                                print(lok_list[ACS_Data[ACS_Lamp3_Temp]]['lok_num'])
                                #sys.exit()
#                            print('********lok_to:',lok_to)
#                            print('**************:',ACS_Data[S88_Sw_Data[sw_id]['Tri']['Lamp3']])
                            window.find_element(location_xyz).update(image_filename=lok_list[lok_to_temp['lok_num']]['lok_name'],button_color=(flame_list[Tri_temp['xyz'][2]][3], flame_list[Tri_temp['xyz'][2]][3]))
#                            lok_num += 1
                        else:
                            #lok_to に無い
                            print('Scan??? lok_toに無い/不明なLok_???')
                            ACS_Data[ACS_Lamp3_Temp]['lok_num'] = 0xFFFF
                            window.find_element(location_xyz).update(image_filename=lok_list[0xFFFF]['lok_name'],button_color=(flame_list[Tri_temp['xyz'][2]][3], flame_list[Tri_temp['xyz'][2]][3]))
#                                sys.exit()

                    else:   #S88_Sw_Data[sw_id]['After'] == 0
                            #S88 off の時
                        print('S88_off_Lamp3 Triger:{:04x}'.format(ACS_Lamp3_Temp))
                        Can_Send_Buffer.append([Can_Send_Delay ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,ACS_Lamp3_Temp//0x100,ACS_Lamp3_Temp%0x100,0x00,0x01]}])
                        ACS_Data[ACS_Lamp3_Temp]['lok_num'] = 0         #lok_num[0] station.png
                        window.find_element(location_xyz).update(image_filename=lok_list[0]['lok_name'],button_color=(flame_list[Tri_temp['xyz'][2]][3], flame_list[Tri_temp['xyz'][2]][3]))

#                if 'Both' in S88_Sw_Data[sw_id]['Tri'].keys():
                if 'Both' in Tri_temp.keys():
                    print('S88_Both_Triger: {:04x}  After:{:02x}  AndLamp3:{:04x}'.format(Tri_temp['Both'],
                        ACS_Data[Tri_temp['Both']]['After'],ACS_Data[Tri_temp['Both']]['AndLamp']))
#                    sys.exit()
                    ACS_Both_Temp = S88_Sw_Data[sw_id]['Both']
                    if ACS_Data[ACS_Both_Temp]['After'] == 0x11:
                        #機関車到着　Lampを黄(0x11)−＞赤(0x01)に
                        Can_Send_Buffer.append([Can_Send_Delay ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,ACS_Both_Temp//0x100,ACS_Both_Temp%0x100,0x01,0x01]}])
                        Can_Send_Buffer.append([Can_Send_Delay ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,ACS_Data[Tri_temp['Both']]['AndLamp']//0x100,ACS_Data[Tri_temp['Both']]['AndLamp']%0x100,0x01,0x01]}])
#                        if ('lok' in ACS_Data[ACS_Both_Temp]) == False:
#                            ACS_Data[ACS_Both_Temp]['lok_num'] = lok_num
#                            window.find_element(location_xyz).update(image_filename=lok_filenames[lok_num],button_color=(sg.theme_background_color(), sg.theme_background_color()))
#                            lok_num += 1
#                        else:
#                            ACS_Data[S88_Sw_Data[sw_id]['Tri']['Lamp3']]['lok'] = lok_num
#                            window.find_element(location_xyz).update(image_filename=lok_filenames[lok_num],button_color=(sg.theme_background_color(), sg.theme_background_color()))
                        print('\n\n**Both**lok_to:',lok_to)
                        print('**************:',ACS_Data[ACS_Both_Temp])
                        if ACS_Both_Temp in lok_to:
                            print('******lok:',lok_to[ACS_Both_Temp]['lok_num'])
#                            lok_to[ACS_Both_Temp]['lok']
                            ACS_Data[ACS_Both_Temp]['lok_num'] = lok_to[ACS_Both_Temp]['lok_num']
                            print('******lok:{} -> {}'.format(lok_to_temp['From'],ACS_Both_Temp))
                                #sys.exit()
#                            print('********lok_to:',lok_to)
#                            print('**************:',ACS_Data[S88_Sw_Data[sw_id]['Tri']['Lamp3']])
                            window.find_element(location_xyz).update(image_filename=lok_list[ACS_Data[ACS_Both_Temp]['lok_num']]['lok_name'],button_color=(sg.theme_background_color(), sg.theme_background_color()))
#                            lok_num += 1

                    elif ACS_Data[ACS_Both_Temp]['After'] == 0x10:
#                    else:
                        #Lampを緑−＞白
#                        Can_Send_Buffer.append([Can_Send_Delay ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,S88_Sw_Data[sw_id]['Tri']['Both']//0x100,S88_Sw_Data[sw_id]['Tri']['Both']%0x100,0x00,0x01]}])
                        print('Both Triger:{:04x}'.format(ACS_Both_Temp))
                        Can_Send_Buffer.append([Can_Send_Delay ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,ACS_Both_Temp//0x100,ACS_Both_Temp%0x100,0x00,0x01]}])
                        ACS_Data[ACS_Both_Temp]['lok_num'] = 0
                        window.find_element(location_xyz).update(image_filename=lok_list[0]['lok_name'],button_color=(sg.theme_background_color(), sg.theme_background_color()))

                    else:
                        #Both:SCAN時など不整合の時
                        print('S88_Both_Triger:不整合')

                if init_sw_sk == [True,True]:
                    init_sw_sk[1] = False
        
#            if sw_id in Disp_Location.keys():
#                print(Disp_Location[sw_id])
                print([x] for x in Disp_Location)

        elif  ana_cmd == 0x16:
            print('CanID 0x16: HASH:{:04x} ID:{:02x}{:02x}-{:02x}{:02x}-{:02x} {:02x}'.format(get_hash,get_data[0],get_data[1],get_data[2],get_data[3],get_data[4],get_data[5]))
    #アクセサリーのコマンド受信
        if  ana_cmd == 0x17 and get_data[5] == 1:
#            print('ID:',hex(get_hash),'Bus:',get_data[0]*0x1000000+get_data[1]*0x10000+get_data[2]*0x100+get_data[3],'No4',get_data[4],'No5',get_data[5],':',get_data[6],'7', get_data[7])
            ACS_id = get_data[2] * 0x100 + get_data[3]
            print('CanID 0x17: ACS_id:{:04x} HASH:{:04x} ID:{:02x}{:02x}-{:02x}{:02x}-{:02x} {:02x}'.format(ACS_id,get_hash,get_data[0],get_data[1],get_data[2],get_data[3],get_data[4],get_data[5]))
#            print('HASH:',hex(get_hash),'ID:',get_data[0]*0x1000000+get_data[1]*0x10000+get_data[2]*0x100+get_data[3],'',get_data[4],'',get_data[5])
            if ACS_id in ACS_Data.keys():
#                ASS_Data_row = ASS_Data[ASS_id]['Tri']
#                print(ACS_Data[ACS_id]['Tri'])
                if 'Tri' in ACS_Data[ACS_id][get_data[4]*0x100+get_data[5]]:
                    Send_Delay = ACS_Data[ACS_id][get_data[4]*0x100+get_data[5]]['Tri'][0]
                    print('ACS_Data:',ACS_Data[ACS_id][get_data[4]*0x100+get_data[5]]['Tri'][1:],'  Send_Delay:',ACS_Data[ACS_id][get_data[4]*0x100+get_data[5]]['Tri'][0])
                    for ACS_Data_row in ACS_Data[ACS_id][get_data[4]*0x100+get_data[5]]['Tri'][1:]:
                        Can_Send_Buffer.append([Can_Send_Delay + Send_Delay[0] ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':ACS_Data_row}])
                    start_time = time.perf_counter() * 1000
            #ACS_Data 更新
                if (ACS_Data[ACS_id]['Type'] == 'Lamp2' and ACS_Data[ACS_id-1]['Type'] == 'Lamp3'):
#                    ACS_Data[ACS_id  ]['Befor'] = get_data[4] + 0x10
                    ACS_Data[ACS_id  ]['After'] = get_data[4] + 0x10
#                    ACS_Data[ACS_id-1]['Befor'] = get_data[4] + 0x10
                    ACS_Data[ACS_id-1]['After'] = get_data[4] + 0x10
                    window.find_element('bt{:1}{:1}{:1}'.format(ACS_Data[ACS_id]['xyz'][0],ACS_Data[ACS_id]['xyz'][1],ACS_Data[ACS_id]['xyz'][2])).Update(image_filename=path_icon + icon_list['Lamp32'][get_data[4]])                            

                elif  ACS_Data[ACS_id]['Type'] == 'Lamp3':
#                    ACS_Data[ACS_id  ]['Befor'] = get_data[4]
                    ACS_Data[ACS_id  ]['After'] = get_data[4]
#                    ACS_Data[ACS_id+1]['Befor'] = get_data[4]
                    ACS_Data[ACS_id+1]['After'] = get_data[4]
#                    window.find_element('bt{:1}{:1}{:1}'.format(ACS_Data[ACS_id]['xyz'][0],ACS_Data[ACS_id]['xyz'][1],ACS_Data[ACS_id]['xyz'][2])).Update(image_filename=path_icon + icon_list['Lamp3'][get_data[4]])                            
                    window.find_element('bt{:1}{:1}{:1}'.format(ACS_Data[ACS_id]['xyz'][0],ACS_Data[ACS_id]['xyz'][1],ACS_Data[ACS_id]['xyz'][2])).Update(image_filename=path_icon + icon_list['Lamp3'][get_data[4]])    #Lamp3 NONE：STOP                        

                elif ACS_Data[ACS_id]['Type'] == 'Sig':
                    ACS_Data[ACS_id]['After'] = get_data[4]
                    window.find_element('bt{:1}{:1}{:1}'.format(ACS_Data[ACS_id]['xyz'][0],ACS_Data[ACS_id]['xyz'][1],ACS_Data[ACS_id]['xyz'][2])).Update(image_filename=path_icon + icon_list['Sig'][get_data[4]])

                elif ACS_Data[ACS_id]['Type'] == 'ONOFF3':
                    ACS_Data[ACS_id]['After'] = get_data[4]
                    window.find_element('bt{:1}{:1}{:1}'.format(ACS_Data[ACS_id]['xyz'][0],ACS_Data[ACS_id]['xyz'][1],ACS_Data[ACS_id]['xyz'][2])).Update(image_filename=path_icon + icon_list['ONOFF3'][get_data[4]])

                else:
#                    ACS_Data[ACS_id]['Befor'] = get_data[4]
                    ACS_Data[ACS_id]['After'] = get_data[4]
#                    row_Station_Data[1][3:5] = [get_data[4],get_data[5]]
            #画面更新処理
                print(' ACS_Data->',ACS_Data[ACS_id],end='')
                print(' XYZ:',ACS_Data[ACS_id]['xyz'])
#                if ACS_Data[ACS_id]['xyz'][0:2] != [99,99]:
                try:
                    color_temp = ACS_Data[ACS_id][get_data[4]*0x100+get_data[5]]['color']
                    Disp_Location['{:1}{:1}{:1}'.format(ACS_Data[ACS_id]['xyz'][0],ACS_Data[ACS_id]['xyz'][1],ACS_Data[ACS_id]['xyz'][2])]['color'] = color_temp
                    print('color:',color_temp)
                    sw_color = ['gray',color_temp]
                    print(' Disp_Location:',Disp_Location['{:1}{:1}{:1}'.format(ACS_Data[ACS_id]['xyz'][0],ACS_Data[ACS_id]['xyz'][1],ACS_Data[ACS_id]['xyz'][2])])

#                    window.find_element('bt{:1}{:1}{:1}'.format(ACS_Data[ACS_id]['xyz'][0],ACS_Data[ACS_id]['xyz'][1],ACS_Data[ACS_id]['xyz'][2])).Update(button_color=(sw_color))
                except:
                    print('Not include [Disp?] or [xyz]!!!!')

                #集合Lamp処理　一つでも黄→黄／一つでも白→白／その他の赤、緑→赤
                if 'And' in ACS_Data[ACS_id]:
#                    print(ACS_Data[ACS_id]['AndLamp'])
                    AndLamp_id = ACS_Data[ACS_id]['AndLamp']
                    sw_color = ['gray','red']
                    for And_id in ACS_Data[ACS_id]['And']:
#                        print(ACS_Data[And_id])
#                        color_temp = Disp_Location['{:1}{:1}{:1}'.format(ACS_Data[And_id]['xyz'][0],ACS_Data[And_id]['xyz'][1],ACS_Data[And_id]['xyz'][2])]['color']
                        color_int = ACS_Data[And_id]['After']
                        print(color_int)
#                        if color_temp == 'yellow':
                        if color_int == 0x11:
                            sw_color = ['gray','yellow']
                            Can_Send_Buffer.append([100 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,AndLamp_id//0x100,AndLamp_id%0x100+1,0x01,0x01]}])
                            break
                    else:                        
                        for And_id in ACS_Data[ACS_id]['And']:
#                            color_temp = Disp_Location['{:1}{:1}{:1}'.format(ACS_Data[And_id]['xyz'][0],ACS_Data[And_id]['xyz'][1],ACS_Data[And_id]['xyz'][2])]['color']
                            color_int = ACS_Data[And_id]['After']
                            print(color_int)
                            if color_int == 0x00:
                                sw_color = ['gray','white']
                                Can_Send_Buffer.append([100 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,AndLamp_id//0x100,AndLamp_id%0x100,0x00,0x01]}])
                                break
                        else:
                            print('All Red!!!!!!')
                            Can_Send_Buffer.append([100 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,AndLamp_id//0x100,AndLamp_id%0x100,0x01,0x01]}])
                    Disp_Location['{:1}{:1}{:1}'.format(ACS_Data[And_id]['xyz'][0],ACS_Data[And_id]['xyz'][1],ACS_Data[And_id]['xyz'][2])]['color'] = sw_color[1]

                if 'And2' in ACS_Data[ACS_id]:
#                    print(ACS_Data[ACS_id]['AndLamp'])
                    AndLamp_id = ACS_Data[ACS_id]['And2Lamp']
                    sw_color = ['gray','red']
                    for And_id in ACS_Data[ACS_id]['And2']:
#                        print(ACS_Data[And_id])
                        color_temp = Disp_Location['{:1}{:1}{:1}'.format(ACS_Data[And_id]['xyz'][0],ACS_Data[And_id]['xyz'][1],ACS_Data[And_id]['xyz'][2])]['color']
                        print(color_temp)
                        if color_temp == 'yellow':
                            sw_color = ['gray','yellow']
                            Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,AndLamp_id//0x100,AndLamp_id%0x100+1,0x01,0x01]}])
                            break
                    else:                        
                        for And_id in ACS_Data[ACS_id]['And2']:
                            color_temp = Disp_Location['{:1}{:1}{:1}'.format(ACS_Data[And_id]['xyz'][0],ACS_Data[And_id]['xyz'][1],ACS_Data[And_id]['xyz'][2])]['color']
                            print(color_temp)
                            if color_temp == 'white':
                                sw_color = ['gray','white']
                                Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,AndLamp_id//0x100,AndLamp_id%0x100,0x00,0x01]}])
                                break
                        else:
                            print('All Red!!!!!!')
                            Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,AndLamp_id//0x100,AndLamp_id%0x100,0x01,0x01]}])
                    Disp_Location['{:1}{:1}{:1}'.format(ACS_Data[And_id]['xyz'][0],ACS_Data[And_id]['xyz'][1],ACS_Data[And_id]['xyz'][2])]['color'] = sw_color[1]
                    
                if 'Thr' in ACS_Data[ACS_id]:
#                    print(ACS_Data[ACS_id]['AndLamp'])
                    AndLamp_id = ACS_Data[ACS_id]['ThrLamp']
                    sw_color = ['gray','red']
                    for And_id in ACS_Data[ACS_id]['Thr']:
                        if color_temp != 'white':
                            sw_color = ['gray','white']
                            Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,AndLamp_id//0x100,AndLamp_id%0x100,0x01,0x01]}])
                            break
                    else:                
                        Can_Send_Buffer.append([300 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,AndLamp_id//0x100,AndLamp_id%0x100,0x00,0x01]}])

    ################################################
    # 送信データが 無いとき
    if send == 0:
        if init_sw_sk == [True,False]:
            sorted_S88_Sw_Data = sorted(S88_Sw_Data.items()) #新たなソートしたS88_Sw_Dataを作成
            print('S88_SCAN Command 0x22:',end='')
#            pprint.pprint(sorted_S88_Sw_Data)
            for row_S88_Data in sorted_S88_Sw_Data:
                pprint.pprint(row_S88_Data[1]['After'])
                if row_S88_Data[1]['After'] == 99 and row_S88_Data[0] > 10000:
                    print('  ->Send Command 0x22',row_S88_Data)
#                    Can_Send_Buffer.append([300 ,{'id':0x0022_0000, 'HASH':Pi88_HASH, 'dlc':4, 'data':[row_S88_Data[1]['Bus']//100,row_S88_Data[1]['Bus']%100,row_S88_Data[1]['No'] // 0x100,row_S88_Data[1]['No'] % 0x100]}])
                    msg = can.Message(arbitration_id=0x0022_0000+Pi88_HASH, dlc=4, data=[row_S88_Data[1]['Bus']//100,row_S88_Data[1]['Bus']%100,row_S88_Data[1]['No'] // 0x100,row_S88_Data[1]['No'] % 0x100])
                    bus.send(msg)
                    #print('init_sw_scan',row_S88_Data[0])
                    init_sw_sk = [True,True]
                    break
            if init_sw_sk == [True,False]:  #全てスキャン完了の時、init_sw_sk = [False,False]
                init_sw_sk[0] = False
                if load_lok_status == True:
                    load_lok_data()
                    load_lok_status = False
        else:
#        代表Lamp　SW

#Yout-S3
#        0x30a7: [{'Sw_id':0x30EA, 'Wait':0,'From':[0x30CF],'To':[0x3099]},
#M123-S3
#                 {'Sw_id':0x30E6, 'Wait':0,'From':[0x309F,0x30A1,0x30A3],'To':[0x3099], 'Tri':[[300],[0x00,0x00,0x30,0x0b,0x01,0x01]]},
#M123-G1
#                 {'Sw_id':0x30EB, 'Wait':0,'From':[0x309F,0x30A1,0x30A3],'To':[0x30C7]}],
            loop_message = ''
            for daihyou_lamp in Loop_Data.keys():
                #入線可SW
#                print('代表Lamp:',hex(daihyou_lamp),' Loop_Data:',Loop_Data[daihyou_lamp],' to:',Loop_Data[daihyou_lamp].keys())
#                print('代表Lamp:',hex(daihyou_lamp),' To:',Loop_Data[daihyou_lamp].keys())
#                loop_message += '代表Lamp:{} {} '.format(hex(daihyou_lamp),ACS_Data[daihyou_lamp]['After'])
                if ACS_Data[daihyou_lamp]['After'] == 0x0:
                #代表Lamp＝白−＞進入可               
                    from_lamp_list = []
#                    print('Loop_Data[daihyou_lamp]=',Loop_Data[daihyou_lamp])
                    for row_from_data_dic in Loop_Data[daihyou_lamp]:
#                        loop_message += '{}'.format(row_from_data_dic)
                        if ACS_Data[row_from_data_dic['Sw_id']]['After'] == 0x1:
#                            print('From:',ACS_Data[row_from_data_dic['From']]['After'],' To:',ACS_Data[row_from_data_dic['To']]['After'])
                            if  ACS_Data[row_from_data_dic['From']]['After'] == 0x1 and ACS_Data[row_from_data_dic['To']]['After'] == 0x0:
#                                print(' From id:',hex(row_from_data_dic['From']),'=',ACS_Data[row_from_data_dic['From']]['After'],end='')
#                                print(' To id:',hex(row_from_data_dic['To']),'=',ACS_Data[row_from_data_dic['To']]['After'],end='')
#                                from_lamp_list.append([row_from_data_dic['From'], row_from_data_dic])
                                from_lamp_list.append(row_from_data_dic)
#                    print('from_lamp_list=',from_lamp_list)
#
                    if len(from_lamp_list) > 0:
                        try:
#                            ch_to_temp = Loop_Data[row_loop]['To'][random.randint(0, len(Loop_Data[row_loop])+1)]
                            select_root = from_lamp_list[random.randint(0, len(from_lamp_list))]
                        except:
                            select_root = from_lamp_list[0]
                        
#                        print('Select_root From=',hex(select_root['From']),'  To=',hex(select_root['To']))    
                        wait_temp = time.perf_counter() - Loop_Data[daihyou_lamp][select_root['Row']]['Wait']
#                        sys.exit()

########################Root設定
                        if wait_temp > 50:
                            for row_wait in Loop_Data[daihyou_lamp]:
                            #Loop_Data[daihyou_lamp][select_root['Row']]['Wait'] = time.perf_counter()
                                row_wait['Wait'] = time.perf_counter()
                            #行き先'To'を黄色に
                            ACS_Data[select_root['To']  ]['After'] = 0x11
                            ACS_Data[select_root['To']+1]['After'] = 0x11                            
                            Can_Send_Buffer.append([100 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,select_root['To']//0x100,select_root['To']%0x100+1,0x01,0x01]}])
                            #ルート設定
                            for tri_list in select_root['Tri'][1:]:
                                Can_Send_Buffer.append([100 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':tri_list}])  
                            #出発元'From'を緑（青）に
                            Can_Send_Buffer.append([100 ,{'id':0x0016_0000, 'HASH':Pi88_HASH, 'dlc':6, 'data':[0x00,0x00,select_root['From']//0x100,select_root['From']%0x100+1,0x00,0x01]}])
                            loop_message = loop_message + '\n\n From:{:04X},{} To:{:04X}'.format(select_root['From'],ACS_Data[select_root['From']]['lok_num'],select_root['To'],ACS_Data[select_root['From']]['lok_num'])
#                            lok_to[select_root['To']] = {'From':select_root['From'],'lok':ACS_Data[select_root['From']]['lok']} 
                            print(ACS_Data[select_root['From']]['sw1'])
                            print('from Lok_Name:',lok_list[ACS_Data[select_root['From']]['lok_num']])
                            print('to Lok_Name:',lok_list[ACS_Data[select_root['To']]['lok_num']]['lok_name'])
                            lok_to[select_root['To']] = {'From':select_root['From'],'lok_num':ACS_Data[select_root['From']]['lok_num']} 

                            print('\nloop_message:',loop_message)
                            print('lok_to:',lok_to)
#                            sys.exit()
                            break
                        
#                        else:
#                            print('Event Loop Waiting: {:.2f}'.format(wait_temp),end='')

        if len(Can_Send_Buffer) != 0:
#            print('Can Send Buffer:',Can_Send_Buffer[0][0],'ID:',hex(Can_Send_Buffer[0][1]['id']),Can_Send_Buffer[0][1]['data'])
            print('Can Send Buffer Start  :{0:5.2f} ID:{1:04X}_{2:04X} Data:{3}'.format(Can_Send_Buffer[0][0],Can_Send_Buffer[0][1]['id']>>16,Can_Send_Buffer[0][1]['HASH'],Can_Send_Buffer[0][1]['data']))
            if Can_Send_Buffer[0][0] <= 0:
                msg = can.Message(arbitration_id=Can_Send_Buffer[0][1]['id']+Can_Send_Buffer[0][1]['HASH'], dlc=Can_Send_Buffer[0][1]['dlc'], data=Can_Send_Buffer[0][1]['data'], is_extended_id=True)
#OK                msg = can.Message(arbitration_id=0x0016_0000+Pi88_HASH, dlc=6, data=[0x00,0x00,0x30,0x00,0x01,0x01], is_extended_id=True)
#                print(Can_Send_Buffer[-1][1]['dlc'])
#                msg = can.Message(arbitration_id=Can_Send_Buffer[-1][1]['id']+Pi88_HASH, dlc=Can_Send_Buffer[-1][1]['dlc'], data=[0x00,0x00,0x30,0x00,0x01,0x01], is_extended_id=True)
                Can_Send_Buffer.pop(0)
                send = 1
#                window.F'-TASK-').Update(text='Upadte')
                window['-TASK-'].update(len(Can_Send_Buffer))
            else:
                end_time = time.perf_counter()*1000 - start_time
                start_time = time.perf_counter()*1000
                Can_Send_Buffer[0][0] -= end_time
                print('Can Send Buffer Waiting: {0:5.2f}'.format(end_time))
                
    elif send == 1:
#        print(msg)
        bus.send(msg)
        send = 0
    