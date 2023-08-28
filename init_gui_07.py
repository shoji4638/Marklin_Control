#01:gui初期画面を切り離し
#02:Tab導入、Tab2にLok画面にする
#03:整理／機関車ファンクションOK
#04:機関車 方向　スピード　開発中
#07;event_140と連動　SIDを使用

#import sys
import glob
from imp import source_from_cache
from PIL import Image
import os
import PySimpleGUI as sg
#from urllib.request import urlopen
import urllib.error
import urllib.request
import sys
#from get_icons import download_file_to_dir

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def download_file_to_dir(url, dst_dir,filename):
    download_file(url, os.path.join(dst_dir, os.path.basename(filename)))

############################################################
## Tab2:Lok画面作成
##  DB BR 103
##  機 関 車　の 絵
##  064 --------o----
##  F0  F1  F2  F3
############################################################
def make_lok_gui(uid,filename,cslok_data_row):
#    temp_fn = [ for fn_num in range(4)]
    filename_arr = []
#    print(cslok_data_row['funktionen'])
    for i in range(4):
        fn_temp = cslok_data_row['funktionen'][i]['typ']
        filename_arr.append('icon/FktIcon_i_gr_'+ f'{fn_temp:02}'+'.png')
    if os.path.exists(filename) != True:
        print('Not exit file:',filename)
        filename = path_lok+'99.png'
#    print(filename_arr,)
    layout_temp = [ 
#        [sg.Text(cslok_data_row['name']),sg.Text('UID:'+ cslok_data_row['uid'])],
#        [sg.Text(cslok_data_row['name'])],
        [sg.Button(image_filename=filename,key=f'-lokb{uid:04x}-',button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1)],
#        [sg.Text('000',key=f'-lokv{uid:04x}-'),sg.Slider((0,100),default_value=50,key=f'-loks{uid:04x}-',orientation='h',disable_number_display=True,enable_events=True)],
        [sg.Button('<00',key=f'-lokv{uid:04x}-',enable_events=True)
                 ,sg.Slider((0,100),default_value=50,key=f'-loks{uid:04x}-',orientation='h',disable_number_display=True,enable_events=True)],
        [sg.Button(image_filename=filename_arr[0],key=f'-lokf00{uid:04x}-'
                ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[1],key=f'-lokf01{uid:04x}-'
                ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[2],key=f'-lokf02{uid:04x}-'
                ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[3],key=f'-lokf03{uid:04x}-'
                ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),]
#         sg.Button('F2',key=f'-lokf2{num:03}-',button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1)]
        ]
    
    return layout_temp

############################################################
## CSに登録されている機関車データを読み出し
## 辞書型のlok_dataを返す。 
def make_lok_data():
    url = 'http://192.168.50.3/config/lokomotive.cs2'
    #url = 'http://192.168.50.3/config/magnetartikel.cs2'
    #url = 'http://192.168.50.3/config/fahrstrasse.cs2'
    #url = 'http://192.168.50.3/config/gleisbild.cs2'
    #url = 'http://192.168.50.3/app/assets/lok/picture.png'
    #url = 'http://192.168.50.3/fctions/FktIcon_a_we_X.png'
    #url = 'http://192.168.50.3/fctions/FktIcon_a_ge_X.png'
    #url = 'http://192.168.50.3/fctions/FktIcon_i_we_20.png'    #WE= 
    #url = 'http://192.168.50.3/fctions/FktIcon_i_gr_20.png'

    cslok_data = {}
    cslok_data_temp = {}
    csfunction_temp = {}
    csfunction_array = {}
    with urllib.request.urlopen(url) as res:
        text = res.read().decode('utf-8')
        for text_row in text.splitlines():
            text_row = text_row.strip()
    #        print(text_row,end='')
            if '[lokomotive]' == text_row:  #先頭Header->飛ばす
    #            print('->skip')
                continue
            elif 'version' == text_row:
    #            print('->skip')
                continue
            elif 'lokomotive' == text_row:
                if cslok_data_temp != {}:
#                    print(cslok_data_temp)
                    cslok_data_temp['funktionen'] = csfunction_temp
#                    cslok_data[int(cslok_data_temp['adresse'],16)] = cslok_data_temp
                    cslok_data[int(cslok_data_temp['uid'],16)] = cslok_data_temp
                cslok_data_temp = {}
                csfunction_temp = {}
    #            print('\nlok_data_temp:',lok_data_temp)
            elif '..' == text_row[0:2]:
                if '..nr' == text_row[0:4]:
                    function_key = int(text_row[5:])
                    csfunction_temp[function_key] = {'typ':0, 'value':None}
    #                print('\nfunction_key:',function_temp)
                    continue
                text_row_temp = text_row.split('=')
                csfunction_temp[function_key][text_row_temp[0][2:]] = int(text_row_temp[1])
            elif '.' == text_row[0]:
                text_row_temp = text_row.split('=')
                if '.minor' == text_row_temp[0]:
    #                print('->skip')
                    continue
                elif '.funktionen' == text_row_temp[0][0:11]:
    #                print(function_temp)
                    continue

                if 'tachomax' == text_row_temp[0][1:] or 'velocity' == text_row_temp[0][1:]:
                    cslok_data_temp[text_row_temp[0][1:]] = int(text_row_temp[1])
                else:
                    cslok_data_temp[text_row_temp[0][1:]] = text_row_temp[1]

    return cslok_data


############################################################
## CSに登録されている機関車の絵とローカルに保存しているデータの照合
## 辞書型のlok_dataを返す。 
def change_size(y_height = 120,x_fix = 240,from_file='',to_dir='/home/shoji/python/lok/lok_m/'):

    img = Image.open(from_file)
    if (img.width*y_height//img.height <= x_fix):
        print(img.width, img.height,' => small ', img.width*y_height//img.height,y_height)
        img.thumbnail((img.width*y_height//img.height,y_height), Image.ANTIALIAS)
#      ftitle, fext = os.path.splitext(f)
        a1,a2 = os.path.split(from_file)
        c = Image.new('RGBA', (x_fix,img.height) , (255, 255,255, 0))
        c.paste(img,((x_fix-img.width)//2,0))

    else:
        print('  (',img.width, img.height,') => big (', img.width*y_height//img.height,'>',x_fix,y_height,')')
        img.thumbnail((img.width*y_height//img.height,y_height), Image.ANTIALIAS)
#      img.resize((img.width*y_height//img.height,y_height), Image.BILINEAR)
        if img.height < y_height:
            temp_height = y_height - img.height
        else:
            temp_height = 0
        c = Image.new('RGBA', (x_fix,y_height) , (255, 255,255, 0))
#      c = img.crop((img.width - x_fix, 0, img.width, x_len))
        c.paste(img,(x_fix-img.width ,temp_height))
#      ftitle, fext = os.path.splitext(from_file)
        a1,a2 = os.path.split(from_file)
    #          a1 = '/home/shoji/python/lok/lok/'
    #ファイル名に「s_」を付けて、縮小した画像を保存する
    c.save(to_dir + a2)


############################################################
## 機関車 画面データ初期化
def init_lok_data(source_dir= 'lok/',lok_data={}):

    #make lok_data
#    lok_data = make_lok_data()
    url_lok = 'http://192.168.50.3/system/lokbilder/download/'

    for lok in lok_data.items():
#        print(lok[0],lok[1]['icon'])
        if not os.path.exists(source_dir+ 'org/'+ lok[1]['icon'] + '.png'):
            download_file_to_dir(url_lok + urllib.parse.quote(lok[1]['icon'])+ '.png', source_dir+ 'org/', lok[1]['icon']+ '.png')
            print('Download locofile:',lok[1]['icon'],end='')
        else:
            print('Exit loco:',lok[1]['icon'],end='')
            
        #Tab2 用の機関車ICON作成
        if not os.path.exists(source_dir+ 'lok_m/'+ lok[1]['icon'] + '.png'):
            change_size(80,240,source_dir+ 'org/'+lok[1]['icon']+ '.png','/home/shoji/python/lok/lok_m/')
        else:
            print('Loco lok_mpng data OK',end='')
            
        #Tab1 用の機関車 小ICON作成
        if not os.path.exists(source_dir+ 'lok_s/'+ lok[1]['icon'] + '.png'):
            change_size(40,120,source_dir+ 'org/'+lok[1]['icon']+ '.png','/home/shoji/python/lok/lok_s/')
        else:
            print('Loco lok_s png data OK')



############################################################
## GUI画面作成
def gui_init(Disp_Size,Disp_Location,ACS_Data,cslok_data):
    
    Pi88_UID = bytes([0x53,0x38,0x3B,0x88])
    Pi88_ID = Pi88_UID[3]

    lok_xy = [4,3]

    #print=sg.Print
    #print(os.path.dirname(__file__))
    #print(f'__file__: {__file__}')
#    path_icon = 'lok/icon/'
    path_icon = 'icon/'
    ####################################
    #Tab1 機関車データ作成  機関車選択画面
    path_lok = 'lok/lok/'
#    lok_filenames = glob.glob(path_lok + '/s_*.png')
    

    layout_lok = []
    lok_list = {}

    lok_list[0] = {'lok_name': path_lok + 'station.png'}
    layout_lok.append([sg.Text('0000'),sg.Button(image_filename=lok_list[0]['lok_name'], key='-lok0000-', button_color = ['white','white']),sg.Text('0.png'),])
    for sid,values in cslok_data.items():
        print(f'{sid:04X}','lok/lok_s/'+cslok_data[sid]['icon']+'.png')
   
#    for i,lok_filename_row in enumerate(lok_filenames,1):
        lok_list[sid] = {'lok_name': 'lok/lok_s/'+values['icon']+'.png'}
#        layout_lok.append([sg.Text(str(i)),sg.Text(str(lok_list[i]['SID'])),sg.Button(image_filename=lok_filename_row, key=f'-lok{i:02}-', button_color = ['white','white']),sg.Text(os.path.splitext(os.path.basename(lok_filename_row))[0]),])
        layout_lok.append([sg.Text(f'{sid:04X}',key=f'-setlokSID{sid:03}-'),sg.Button(image_filename='lok/lok_s/'+values['icon']+'.png', key=f'-setlokpng{sid:04X}-', button_color = ['white','white']),])
#        layout_lok.append([sg.Text(str(i)),sg.Button(f'{lok_list[i]['SID']:04X}',key=f'-SID{i:04X}-'),sg.Button(image_filename=lok_filename_row, key=f'-lok{i:02}-', button_color = ['white','white']),sg.Text(os.path.splitext(os.path.basename(lok_filename_row))[0]),])
    lok_list[0xFFFF] = {'lok_name': 'lok/lok_s/'+'FFFF.png'}
    layout_lok.append([sg.Text('FFFF'),sg.Button(image_filename=lok_list[0xFFFF]['lok_name'], key='-setlokpngFFFF-', button_color = ['white','white']),sg.Text('99.png'),])

    print('lok_list=',lok_list)
    #sys.exit()

    icon_list = {
    #    'Lamp3':['InOFF.png','InON.png'],
        'Lamp3' :['NONE.png','STOP.png'],
        'Lamp32':['GO.png','WAIT.png'],
        
        'Lamp2':['ON.png','OFF.png'],
        'Sig'  :['Sig_STOP2.png','Sig_GO2.png'],    
        'ONOFF3'  :['OFF3.png','ON3.png'],    
        }

    flame1 = []
    flame2 = []
    flame3 = []
    flame4 = []
    flame5 = []
    flame6 = []
    flameicon = []

    flame_list = [
        [flame1 , 3,'St.auBen','LightYellow'],
        [flame2 , 3,'St.innen','LightBlue'],
        [flame3 , 1,'St.Berg','light pink'],
        [flame4 , 5,'St.Hbf','light green'],
        [flame5 , 5,'Yado','light gray'],
        [flame6 , 6,'Hof','lightYellow'],
        ]

    for group,fla in enumerate(flame_list):
    #for row in range(Disp_Size[1]):
      row = 0
      for ind in range(fla[1]):
        layout_temp = []
        for col in range(Disp_Size[0]):
            print('col,row,group=',col,row,group,Disp_Location[f'{col:1}{row:1}{group:1}'])
            if 'lok' in Disp_Location[f'{col:1}{row:1}{group:1}']['Type']:
    #            layout_temp.append(sg.Button(image_filename=path_lok + Disp_Location[f'{col:1}{row:1}{group:1}']['lok'], key=f'bt{col:1}{row:1}{group:1}' ,button_color=(fla[3], fla[3]), border_width=0))
                print('Debug:',ACS_Data[Disp_Location[f'{col:1}{row:1}{group:1}']['ACS_ID']]['lok_num'])
                layout_temp.append(sg.Button(image_filename=lok_list[ACS_Data[Disp_Location[f'{col:1}{row:1}{group:1}']['ACS_ID']]['lok_num']]['lok_name'], key=f'bt{col:1}{row:1}{group:1}' ,button_color=(fla[3], fla[3]), border_width=0))
    #            sys.exit()
            elif 'SW1' == Disp_Location[f'{col:1}{row:1}{group:1}']['Type']:
                layout_temp.append(sg.Button(image_data=toggle_btn_off, key=f'bt{col:1}{row:1}{group:1}' ,button_color=(fla[3], fla[3]), border_width=0))
    #        elif (Disp_Location[f'{col:1}{row:1}{group:1}']['type'] == 'Lamp3'):
    #            layout_temp.append(sg.Button(image_filename=path_icon + icon_list['Lamp3'][0], key=f'bt{col:1}{row:1}{group:1}' ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0))
            elif 'Lamp3'== Disp_Location[f'{col:1}{row:1}{group:1}']['Type']:
                layout_temp.append(sg.Button(image_filename=path_icon + icon_list['Lamp3'][0], key=f'bt{col:1}{row:1}{group:1}' ,button_color=(fla[3], fla[3]), border_width=0))
            elif 'Sig' == Disp_Location[f'{col:1}{row:1}{group:1}']['Type']:
                layout_temp.append(sg.Button(image_filename=path_icon + icon_list['Sig'][0], key=f'bt{col:1}{row:1}{group:1}' ,button_color=(fla[3], fla[3]), border_width=0))
            elif 'ONOFF3' == Disp_Location[f'{col:1}{row:1}{group:1}']['Type']:
                layout_temp.append(sg.Button(image_filename=path_icon + icon_list['ONOFF3'][0], key=f'bt{col:1}{row:1}{group:1}' ,button_color=(fla[3], fla[3]), border_width=0))
                Disp_Location[f'{col:1}{row:1}{group:1}']['After'] = 0
            else:
    #            sg.Button(f'{col:1}{row:1}{group:1}',size=(4,2) ,enable_events=True,key=f'bt{col:1}{row:1}{group:1}',
    #            button_color=('white',Disp_Location[f'{col:1}{row:1}{group:1}']['color']))
                layout_temp.append(sg.Button(f'{col:1}{row:1}{group:1}',size=(1,1) ,pad=((6,6),(0,0)),enable_events=True,key=f'bt{col:1}{row:1}{group:1}',button_color=(fla[3], fla[3]), border_width=0))
    #        if col == 5 or col == 12 :
    #            if Disp_Location[f'{col:1}{row:1}{group:1}']['ACS_ID'] != 0:
    #                layout_temp.append(sg.Text(ACS_Data[Disp_Location[f'{col:1}{row:1}{group:1}']['ACS_ID']]['Name']))
    #    print(layout_temp)
    #    layout.append(layout_temp)
        fla[0].append(layout_temp)
        row += 1
    #  print('fla:',fla[0])

    layout_temp = []
    layout_temp1 = []
    layout_temp2 = []

    #for col in range(30):
    #    layout_lok.append([sg.Button(image_filename=lok_filenames[lok_num], key=f'-lok{col:02}-', button_color = ['white','white']),sg.Text(os.path.splitext(os.path.basename(lok_filenames[lok_num]))[0]),])
    #    lok_num +=  1
    #layout_temp1.append(layout_lok)
    lok_num = 0
    layout_temp1.append([sg.Text('Type(name):LinkS88('+str((Pi88_UID[2]-56)*256+Pi88_UID[3])+')  '),sg.Text('Pi88_ID: '+str(Pi88_ID),key='-ID-'),sg.Text('Task',key='-TASK-'),sg.Text('Lok_Location',key='-Lok_Lo-')])

    ##layout.append([sg.Checkbox('Can Read Log',enable_events=True,key='can_read',default=True),sg.Checkbox('Can Write Log',enable_events=True,key='can_write')])
    layout_temp1.append([sg.Button('LOAD',size=(10,1),button_color=("white", "blue")),
                        sg.Button('SAVE',size=(10,1),button_color=("white", "blue")),
                        sg.Button('RESET',size=(10,1),button_color=("white", "blue")),
                        sg.Button('SCAN',size=(10,1),button_color=("white", "blue")),
                        sg.Button('-LOKSAVE-',size=(10,1),button_color=("white", "blue"))])
    layout_temp1.append([sg.Button('TEST 00',size=(10,1),button_color=("white", "blue")),
                        sg.Button('TEST 01',size=(10,1),button_color=("white", "blue")),
                        sg.Button('-LOKLOAD-',size=(10,1),button_color=("white", "blue"))])
    layout_temp1.append([sg.Text('status:???????',key='-status-')])

    #layout.append([sg.Text('　グラフィック版　'),sg.Button('', image_data=toggle_btn_off, key='-TOGGLE-GRAPHIC-',button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)])
    layout_temp2 = []
    layout_temp2.append([sg.Button('', image_filename=path_icon+'EmergencyStop.png', key='-TOGGLE-GRAPHIC-',button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)])

    flameicon = [
        [sg.Frame('',layout_temp1),sg.Frame('',layout_temp2)]
    #    [sg.Frame('',layout_temp2)]
        ]
    #    [sg.Column(flame_list[1][0],flame_list[1][2])]
    #    ]
    #layout = [
    #    [sg.Column(flame_list[0][0])],
    #    [sg.Column(flame_list[1][0])]
    #    ]
    #左のトレインインジケータ
    layout_temp1 = [
        [sg.Frame(flame_list[0][2],flame_list[0][0], background_color=flame_list[0][3])],
        [sg.Frame(flame_list[1][2],flame_list[1][0], background_color=flame_list[1][3])],
        [sg.Frame(flame_list[2][2],flame_list[2][0], background_color=flame_list[2][3])],
        [sg.Frame(flame_list[3][2],flame_list[3][0], background_color=flame_list[3][3])],
        ]

    #中央のトレインインジケータ
    layout_temp2 = [
        [sg.Frame(flame_list[4][2],flame_list[4][0], background_color=flame_list[4][3])],
        [sg.Frame(flame_list[5][2],flame_list[5][0], background_color=flame_list[5][3])],
    ]

    layout_tab1 = [
        [sg.Column(layout_temp1), sg.Column(layout_temp2),  sg.Column(layout_lok,size=(245, 600), scrollable=True)],
    #    [sg.Column(layout_temp1), sg.Column(layout_temp2),],
        [sg.Column(flameicon)],
        [sg.Button(image_filename=lok_list[0x400E]['lok_name']),sg.Text('Lok Function (xC) SID:???? Fun:?? ??',key='-lok_cmd_x0C-')],
        [sg.Text('SID: -1',key='-SID-'),sg.Text('Lok Direction(xA) SID:???? Fun:?? ??',key='-lok_cmd_x0A-')],
        [sg.Text('Lok Speed(x8) SID:???? Fun:?? ??',key='-lok_cmd_x08-')],
        
    ]
    
    #t1 = sg.Tab('backpack' ,[[sg.Image(filename='backpack.png')]])
    t1 = sg.Tab('Layout' ,layout_tab1)

#####################################################
#Tab2 作成
    layout_tab2 = []
    layout_left = []
    layout_row = []

    #機関車一覧
    for num,address_row in enumerate(cslok_data):
        print(f'{address_row:04x}',cslok_data[address_row]['icon'])

#        filename = path_lok+'s_'+cslok_data[address_row]['icon']+'.png'
        filename = 'lok/lok_m/'+cslok_data[address_row]['icon']+'.png'
        if os.path.exists(filename) != True:
            print('Not exit file:',filename)
            filename = path_lok+'99.png'            
#            layout_row.append(sg.Column(make_lok_gui(lok_line*10+lok_row,path_lok+'s_'+cslok_data[address_row]['icon']),justification='c'))
#        layout_row.append(sg.Column(make_lok_gui(address_row, filename, cslok_data[address_row]),justification='c'))
        layout_row.append(sg.Frame(cslok_data[address_row]['name'],make_lok_gui(address_row, filename, cslok_data[address_row])))
    #layout_row.append(make_lok_gui(1))
    #print(layout_row)
    #sys.exit()
        if num % lok_xy[0] == 3:
            layout_left.append(layout_row)
            layout_row = []
    if layout_row != []:
        layout_left.append(layout_row)
    

    #Tab2に大きな機関車詳細画面表示
    address_row in cslok_data.keys()
    filename_arr = []
    filename = 'test/'+cslok_data[address_row]['icon']+'.png'
    for i in range(32):
        fn_temp = cslok_data[address_row]['funktionen'][i]['typ']
        filename_arr.append('icon/FktIcon_i_gr_'+ f'{fn_temp:02}'+'.png')

    layout_temp = [         #justification='r'
        [sg.Text(cslok_data[address_row]['name'],key='-Lokt-',font=('Arial',16),justification='c')],
        [sg.Button(image_filename=filename,key='-Lokb-',button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1)],
        [sg.Button('Revers',key='-LokRv-',size=(4,1)),sg.Button('Fo',key='-LokFo-',size=(10,1)),
         sg.Text('000',key='-Lokv-'),sg.Slider((0,100),default_value=50,key='-Loks-',orientation='h',disable_number_display=True,enable_events=True)],
        [sg.Text('Dire:'+cslok_data[address_row]['richtung'],key='-Lok_richtung-'),
         sg.Text('Speed:'+str(cslok_data[address_row]['velocity']),key='-Lok_velocity-'),
         sg.Text('TachoMax:'+str(cslok_data[address_row]['tachomax']),key='-Lok_tachomax-'),],
        [sg.Text('LogicalSp:'+str(cslok_data[address_row]['velocity']),key='-Lok_velocity-'),
         sg.Text('Vmax:'+'????',key='-Lok_vmax-'),
         sg.Text('Vmix:'+'????',key='-Lok_vmin-'),],
        [sg.Text('AcelV:'+'????',key='-Lok_av-'),
         sg.Text('BrekV:'+'????',key='-Lok_bv-'),],
        [sg.Button(image_filename=filename_arr[0],key='-Lokf00-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[1],key='-Lokf01-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[2],key='-Lokf02-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[3],key='-Lokf03-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[4],key='-Lokf04-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[5],key='-Lokf05-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[6],key='-Lokf06-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[7],key='-Lokf07-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),],

        [sg.Button(image_filename=filename_arr[8],key='-Lokf08-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[9],key='-Lokf09-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[10],key='-Lokf10-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[11],key='-Lokf11-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[12],key='-Lokf12-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[13],key='-Lokf13-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[14],key='-Lokf14-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[15],key='-Lokf15-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),],
                   
        [sg.Button(image_filename=filename_arr[16],key='-Lokf16-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[17],key='-Lokf17-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[18],key='-Lokf18-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[19],key='-Lokf19-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[20],key='-Lokf20-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[21],key='-Lokf21-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[22],key='-Lokf22-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),
         sg.Button(image_filename=filename_arr[23],key='-Lokf23-'
                   ,button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1),],

        [sg.Text('Address:'+cslok_data[address_row]['adresse'],key='-Lok_adresse-')],
        [sg.Text('Type:'+cslok_data[address_row]['typ'],key='-Lok_typ-')],
        [sg.Text('UID: '+ cslok_data[address_row]['uid'],key='-Lok_uid-')],
        [sg.Text('MfxID:'+ cslok_data[address_row]['mfxuid'],key='-Lok_mfxuid-')],
        ]

    layout_tab2 = [[sg.Column(layout_left, scrollable=True),sg.Column(layout_temp,element_justification='c')]]
    
    t2 = sg.Tab('Loco' ,layout_tab2)
#    t2 = sg.Tab('pencil.png' ,[[sg.T('pencil.png')]])
    t3 = sg.Tab('Debug Page' ,[[sg.T('Debug page')]])
    
    layout=[[sg.TabGroup ([[t1 ,t2,t3 ]])]]

    print('layout:',layout)
    #sys.exit()
    # ウィンサイズはsizeに(縦の大きさ,横の大きさ)で記載
    window = sg.Window(title='Pi88 Status',font='Courier 12', size=(1600, 900),button_color=('white', 'red')).Layout(layout)

    return Disp_Location,window,lok_list,flame_list,icon_list
             