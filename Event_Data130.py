#04:toを複数に
#05:表示ｘｙ大幅変更
#06:ヤード設定中　最内側GラインのG1を設定
#07:ヤードIn追加　Ver30
#105 20230408：S4Rデータ修正
#123:S88のTri 削除

S88_Sw_Data = {
#ヤード入口                                                                      x=x-7 y=y+12
        21063: {'Name':'YAInExi','Bus':2, 'No':1063, 'Befor':99, 'After':99, 'xyz':[4,0,4], 'Exit':0x3078, 'Lamp3':0x30b1},
#YADO
        21049: {'Name':'YA1Exit','Bus':2, 'No':1049, 'Befor':99, 'After':99, 'xyz':[4,1,4], 'Exit':0x306d, 'Lamp3':0x30b3},
        21050: {'Name':'YA2Exit','Bus':2, 'No':1050, 'Befor':99, 'After':99, 'xyz':[4,2,4], 'Exit':0x306e, 'Lamp3':0x30b5},
        21051: {'Name':'YA3Exit','Bus':2, 'No':1051, 'Befor':99, 'After':99, 'xyz':[4,3,4], 'Exit':0x306f, 'Lamp3':0x30b7},

        22033: {'Name':'YA1 In' ,'Bus':2, 'No':2033, 'Befor':99, 'After':99, 'xyz':[3,1,4], 'in':21049},
        22034: {'Name':'YA2 In' ,'Bus':2, 'No':2034, 'Befor':99, 'After':99, 'xyz':[3,2,4], 'in':21050},
        22035: {'Name':'YA3 In' ,'Bus':2, 'No':2035, 'Befor':99, 'After':99, 'xyz':[3,3,4], 'in':21051},
#ヤード出口センサー
        22054: {'Name':'YAoutEx','Bus':2, 'No':2054, 'Befor':99, 'After':99, 'xyz':[4,5,5], 'Exit':0x3077,'Lamp3':0x30CF},
        22053: {'Name':'YAoutIn','Bus':2, 'No':2053, 'Befor':99, 'After':99, 'xyz':[3,5,5], 'in':22054},
#G Line
        21041: {'Name':'G1 Exit','Bus':2, 'No':1041, 'Befor':99, 'After':99, 'xyz':[4,0,5], 'Exit':0x3069,'Lamp3':0x30C7},
        22064: {'Name':'G1 In'  ,'Bus':2, 'No':2064, 'Befor':99, 'After':99, 'xyz':[3,0,5], 'in':21041},

        21046: {'Name':'G2OutEx','Bus':2, 'No':1046, 'Befor':99, 'After':99, 'xyz':[4,1,5], 'Exit':0x3061,'Lamp3':0x30C9},
        21011: {'Name':'G2OutIn','Bus':2, 'No':1011, 'Befor':99, 'After':99, 'xyz':[3,1,5], 'in':21046},

        21045: {'Name':'G2In Ex','Bus':2, 'No':1045, 'Befor':99, 'After':99, 'xyz':[4,2,5], 'Exit':0x3060,'Lamp3':0x30CB},
        21012: {'Name':'G2In In','Bus':2, 'No':1012, 'Befor':99, 'After':99, 'xyz':[3,2,5], 'in':21045},
        
        22028: {'Name':'G3 Exit','Bus':2, 'No':2028, 'Befor':99, 'After':99, 'xyz':[4,3,5], 'Exit':0x3068,'Lamp3':0x30F5},
        21009: {'Name':'G4 Exit','Bus':2, 'No':1009, 'Befor':99, 'After':99, 'xyz':[4,4,5], 'Exit':0x3064,'Lamp3':0x3081},
#O Line
        21004: {'Name':'O3 Exit','Bus':2, 'No':1004, 'Befor':99, 'After':99, 'xyz':[4,0,0], 'Exit':0x305e, 'Lamp3':0x30ad},
        21003: {'Name':'O2 Exit','Bus':2, 'No':1003, 'Befor':99, 'After':99, 'xyz':[4,1,0], 'Exit':0x305d, 'Lamp3':0x30ab},
        21002: {'Name':'O1 Exit','Bus':2, 'No':1002, 'Befor':99, 'After':99, 'xyz':[4,2,0], 'Exit':0x305c, 'Lamp3':0x30a9},
        21007: {'Name':'O3 In  ','Bus':2, 'No':1007, 'Befor':99, 'After':99, 'xyz':[3,0,0], 'in':21004},
        21006: {'Name':'O2 In  ','Bus':2, 'No':1006, 'Befor':99, 'After':99, 'xyz':[3,1,0], 'in':21003},
        21005: {'Name':'O1 In  ','Bus':2, 'No':1005, 'Befor':99, 'After':99, 'xyz':[3,2,0], 'in':21002},
#S Station
        22025: {'Name':'S1 Exit','Bus':2, 'No':2025, 'Befor':99, 'After':99, 'xyz':[4,3,3], 'Exit':0x3054, 'Lamp3':0x3095},
        22026: {'Name':'S2 Exit','Bus':2, 'No':2026, 'Befor':99, 'After':99, 'xyz':[4,2,3], 'Exit':0x3055, 'Lamp3':0x3097},
        22001: {'Name':'S1 In'  ,'Bus':2, 'No':2001, 'Befor':99, 'After':99, 'xyz':[3,3,3], 'in':22025},
        22002: {'Name':'S2 In'  ,'Bus':2, 'No':2002, 'Befor':99, 'After':99, 'xyz':[3,2,3], 'in':22026},

        22005: {'Name':'S3 Exit','Bus':2, 'No':2005, 'Befor':99, 'After':99, 'xyz':[4,1,3], 'Exit':0x3056, 'Lamp3':0x3099},
#        22003: {'Name':'S3 In'  ,'Bus':2, 'No':2003, 'Befor':99, 'After':99, 'xyz':[3,1,3], 'in':22005},
        #S4R　ヤードへ　　　S4L　山かM123か
        22004: {'Name':'S4RExit','Bus':2, 'No':2004, 'Befor':99, 'After':99, 'xyz':[4,4,3], 'Exit':0x3052, 'Both':0x308f},
        22006: {'Name':'S4LExit','Bus':2, 'No':2006, 'Befor':99, 'After':99, 'xyz':[4,0,3], 'Exit':0x3053, 'Both':0x308d},

#M Line
        21022: {'Name':'M3 Out' ,'Bus':2, 'No':1022, 'Befor':99, 'After':99, 'xyz':[5,0,1], 'Exit':0x305a},
        21020: {'Name':'M2 Out' ,'Bus':2, 'No':1020, 'Befor':99, 'After':99, 'xyz':[5,1,1], 'Exit':0x3059},
        21018: {'Name':'M1 Out' ,'Bus':2, 'No':1018, 'Befor':99, 'After':99, 'xyz':[5,2,1], 'Exit':0x3058},
        21021: {'Name':'M3 Exit','Bus':2, 'No':1021, 'Befor':99, 'After':99, 'xyz':[4,0,1], 'Exit':None, 'Lamp3':0x30a3},
        21019: {'Name':'M2 Exit','Bus':2, 'No':1019, 'Befor':99, 'After':99, 'xyz':[4,1,1], 'Exit':None, 'Lamp3':0x30a1},
        21017: {'Name':'M1 Exit','Bus':2, 'No':1017, 'Befor':99, 'After':99, 'xyz':[4,2,1], 'Exit':None, 'Lamp3':0x309f},
        21025: {'Name':'M3 In'  ,'Bus':2, 'No':1025, 'Befor':99, 'After':99, 'xyz':[3,0,1], 'in':21021},
        21024: {'Name':'M2 In'  ,'Bus':2, 'No':1024, 'Befor':99, 'After':99, 'xyz':[3,1,1], 'in':21019},
        21023: {'Name':'M1 In'  ,'Bus':2, 'No':1023, 'Befor':99, 'After':99, 'xyz':[3,2,1], 'in':21017}
    }

Loop_Data = {
#O123-S12 代表Lamp　　 To[  ], Sw 　
        0x309b: [{'Sw_id':0x30e7,'Row':0 , 'Wait':0, 'From':0x30ad, 'To':0x3097, 'Tri':[[300],[0x00,0x00,0x30,0x04,0x00,0x01]]},
                 {'Sw_id':0x30e7,'Row':1 , 'Wait':0, 'From':0x30ab, 'To':0x3097, 'Tri':[[300],[0x00,0x00,0x30,0x04,0x00,0x01]]},
                 {'Sw_id':0x30e7,'Row':2 , 'Wait':0, 'From':0x30a9, 'To':0x3097, 'Tri':[[300],[0x00,0x00,0x30,0x04,0x00,0x01]]},
                 {'Sw_id':0x30e7,'Row':3 , 'Wait':0, 'From':0x30ad, 'To':0x3095, 'Tri':[[300],[0x00,0x00,0x30,0x04,0x01,0x01]]},
                 {'Sw_id':0x30e7,'Row':4 , 'Wait':0, 'From':0x30ab, 'To':0x3095, 'Tri':[[300],[0x00,0x00,0x30,0x04,0x01,0x01]]},
                 {'Sw_id':0x30e7,'Row':5 , 'Wait':0, 'From':0x30a9, 'To':0x3095, 'Tri':[[300],[0x00,0x00,0x30,0x04,0x01,0x01]]}],
#S12-O123
        0x30af: [{'Sw_id':0x30a6,'Row':0 , 'Wait':0, 'From':0x3097, 'To':0x30ad, 'Tri':[[300],[0x00,0x00,0x30,0x10,0x01,0x01],[0x00,0x00,0x30,0x1a,0x01,0x01]]},
                 {'Sw_id':0x30a6,'Row':1 , 'Wait':0, 'From':0x3095, 'To':0x30ad, 'Tri':[[300],[0x00,0x00,0x30,0x10,0x01,0x01],[0x00,0x00,0x30,0x1a,0x01,0x01]]},
                 {'Sw_id':0x30a6,'Row':2 , 'Wait':0, 'From':0x3097, 'To':0x30ab, 'Tri':[[300],[0x00,0x00,0x30,0x10,0x00,0x01],[0x00,0x00,0x30,0x1a,0x01,0x01]]},
                 {'Sw_id':0x30a6,'Row':3 , 'Wait':0, 'From':0x3095, 'To':0x30ab, 'Tri':[[300],[0x00,0x00,0x30,0x10,0x00,0x01],[0x00,0x00,0x30,0x1a,0x01,0x01]]},
                 {'Sw_id':0x30a6,'Row':4 , 'Wait':0, 'From':0x3097, 'To':0x30a9, 'Tri':[[300],[0x00,0x00,0x30,0x30,0x01,0x01],[0x00,0x00,0x30,0x1a,0x00,0x01]]},
                 {'Sw_id':0x30a6,'Row':5 , 'Wait':0, 'From':0x3095, 'To':0x30a9, 'Tri':[[300],[0x00,0x00,0x30,0x30,0x01,0x01],[0x00,0x00,0x30,0x1a,0x00,0x01]]}],
#Yout-S3
        0x30a7: [{'Sw_id':0x30EA,'Row':0 , 'Wait':0, 'From':0x30CF, 'To':0x3099, 'Tri':[[300],[0x00,0x00,0x30,0x00,0x00,0x01]]},
#M123-S3
                 {'Sw_id':0x30E6,'Row':1 , 'Wait':0, 'From':0x309F, 'To':0x3099, 'Tri':[[300],[0x00,0x00,0x30,0x0b,0x01,0x01]]},
                 {'Sw_id':0x30E6,'Row':2 , 'Wait':0, 'From':0x30A1, 'To':0x3099, 'Tri':[[300],[0x00,0x00,0x30,0x0b,0x01,0x01]]},
                 {'Sw_id':0x30E6,'Row':3 , 'Wait':0, 'From':0x30A3, 'To':0x3099, 'Tri':[[300],[0x00,0x00,0x30,0x0b,0x01,0x01]]},
#M123-G1
                 {'Sw_id':0x30EB,'Row':4 , 'Wait':0, 'From':0x309F, 'To':0x30C7, 'Tri':[[300],[0x00,0x00,0x30,0x0b,0x00,0x01]]},
                 {'Sw_id':0x30EB,'Row':5 , 'Wait':0, 'From':0x30A1, 'To':0x30C7, 'Tri':[[300],[0x00,0x00,0x30,0x0b,0x00,0x01]]},
                 {'Sw_id':0x30EB,'Row':6 , 'Wait':0, 'From':0x30A3, 'To':0x30C7, 'Tri':[[300],[0x00,0x00,0x30,0x0b,0x00,0x01]]},
#G1-Out-S3R-Yade
                 {'Sw_id':0x30E5,'Row':7 , 'Wait':0, 'From':0x30C7, 'To':0x30B1, 'Tri':[[300],[0x00,0x00,0x30,0x1C,0x00,0x01],[0x00,0x00,0x30,0x33,0x00,0x01],[0x00,0x00,0x30,0x0E,0x01,0x01],[0x00,0x00,0x30,0x28,0x01,0x01],[0x00,0x00,0x30,0x56,0x01,0x01],[0x00,0x00,0x30,0x99,0x01,0x01]]},
#G4-G1
                 {'Sw_id':0x30ED,'Row':8 , 'Wait':0, 'From':0x3081, 'To':0x30C7, 'Tri':[[300],[0x00,0x00,0x30,0x0b,0x00,0x01]]}],
#G2->G3        
        0x30F5: [{'Sw_id':0x30ED,'Row':0 , 'Wait':0, 'From':0x30C9, 'To':0x30F5, 'Tri':[[300],[0x00,0x00,0x30,0x1b,0x01,0x01]]},
                 {'Sw_id':0x30ED,'Row':1 , 'Wait':0, 'From':0x30CB, 'To':0x30F5, 'Tri':[[300],[0x00,0x00,0x30,0x1b,0x00,0x01]]}],
#G3->G4
        0x3083: [{'Sw_id':0x30ED,'Row':0 , 'Wait':0, 'From':0x30F5, 'To':0x3081, 'Tri':[[300],[0x00,0x00,0x30,0x1b,0x01,0x01]]}],
#S3-M123
        0x309d: [{'Sw_id':0x30a5,'Row':0 , 'Wait':0, 'From':0x3099, 'To':0x309f, 'Tri':[[300],[0x00,0x00,0x30,0x0d,0x00,0x01]]},
                 {'Sw_id':0x30a5,'Row':1 , 'Wait':0, 'From':0x3099, 'To':0x30a1, 'Tri':[[300],[0x00,0x00,0x30,0x27,0x00,0x01],[0x00,0x00,0x30,0x0d,0x01,0x01]]},
                 {'Sw_id':0x30a5,'Row':2 , 'Wait':0, 'From':0x3099, 'To':0x30a3, 'Tri':[[300],[0x00,0x00,0x30,0x27,0x01,0x01],[0x00,0x00,0x30,0x0d,0x01,0x01]]},
#S4L-M123                 
                 {'Sw_id':0x30a5,'Row':3 , 'Wait':0, 'From':0x308D, 'To':0x309f, 'Tri':[[300],[0x00,0x00,0x30,0x0d,0x00,0x01],[0x00,0x00,0x30,0x20,0x00,0x01],[0x00,0x00,0x30,0x021,0x01,0x01]]},
                 {'Sw_id':0x30a5,'Row':4 , 'Wait':0, 'From':0x308D, 'To':0x30a1, 'Tri':[[300],[0x00,0x00,0x30,0x27,0x00,0x01],[0x00,0x00,0x30,0x0d,0x01,0x01],[0x00,0x00,0x30,0x20,0x00,0x01],[0x00,0x00,0x30,0x021,0x01,0x01]]},
                 {'Sw_id':0x30a5,'Row':5 , 'Wait':0, 'From':0x308D, 'To':0x30a3, 'Tri':[[300],[0x00,0x00,0x30,0x27,0x00,0x01],[0x00,0x00,0x30,0x0d,0x01,0x01],[0x00,0x00,0x30,0x20,0x00,0x01],[0x00,0x00,0x30,0x021,0x01,0x01]]}],
#Y12345-Yout
        0x30ef: [{'Sw_id':0x30E9,'Row':0 , 'Wait':0, 'From':0x30B3 ,'To':0x30CF, 'Tri':[[300],[0x00,0x00,0x30,0x4C,0x00,0x01]]},
                 {'Sw_id':0x30E9,'Row':1 , 'Wait':0, 'From':0x30B5 ,'To':0x30CF, 'Tri':[[300],[0x00,0x00,0x30,0x4C,0x00,0x01]]},
                 {'Sw_id':0x30E9,'Row':2 , 'Wait':0, 'From':0x30B7 ,'To':0x30CF, 'Tri':[[300],[0x00,0x00,0x30,0x4C,0x00,0x01]]}],

#        0x30C7: [[0x30C7],
#                 {'Sw_id':0x30eb, 'Wait':0,'From':[0x309f,0x30a1,0x30a3] ,'Tri':[[300],[0x00,0x00,0x30,0x0b,0x00,0x01]]}],
##G1-YAdown
##        0x30f1: [{'Sw_id':0x30E5,'Row':0 , 'Wait':0, 'From':0x30c7, 'To':0x30B1, 'Tri':[[300],[0x00,0x00,0x30,0x18,0x01,0x01],[0x00,0x00,0x30,0x09,0x01,0x01],[0x00,0x00,0x30,0x28,0x00,0x01]]}],
#G1-S4R（ヤードへ）
        0x308B: [{'Sw_id':0x30E5,'Row':0 , 'Wait':0, 'From':0x30C7, 'To':0x308F, 'Tri':[[300],[0x00,0x00,0x30,0x53,0x01,0x01],[0x00,0x00,0x30,0x09,0x01,0x01],[0x00,0x00,0x30,0x28,0x00,0x01]]},
#G1-S4L(山へ)
                 {'Sw_id':0x30ED,'Row':1 , 'Wait':0, 'From':0x30C7, 'To':0x308D, 'Tri':[[300],[0x00,0x00,0x30,0x52,0x01,0x01],[0x00,0x00,0x30,0x09,0x00,0x01],[0x00,0x00,0x30,0x28,0x00,0x01]]}],
#S4L->G2In
        0x30CD: [{'Sw_id':0x30ED,'Row':0 , 'Wait':0, 'From':0x308D, 'To':0x30C9, 'Tri':[[300],[0x00,0x00,0x30,0x1E,0x01,0x01],[0x00,0x00,0x30,0x20,0x01,0x01],[0x00,0x00,0x30,0x21,0x01,0x01]]},
#   -G2Out
                 {'Sw_id':0x30ED,'Row':1 , 'Wait':0, 'From':0x308D, 'To':0x30CB, 'Tri':[[300],[0x00,0x00,0x30,0x1E,0x00,0x01],[0x00,0x00,0x30,0x20,0x01,0x01],[0x00,0x00,0x30,0x21,0x01,0x01]]}],
#S4R-YAdown
        0x30F1: [{'Sw_id':0x30E5,'Row':0 , 'Wait':0, 'From':0x308F, 'To':0x30B1, 'Tri':[[300],[0x00,0x00,0x30,0x18,0x01,0x01]]}],
#YAdown-Y12345(Yin)
        0x30D2: [{'Sw_id':0x30E5,'Row':0 , 'Wait':0, 'From':0x30B1, 'To':0x30B3, 'Tri':[[300],[0x00,0x00,0x30,0x4a,0x01,0x01],[0x00,0x00,0x30,0x49,0x01,0x01]]},
                 {'Sw_id':0x30E5,'Row':0 , 'Wait':0, 'From':0x30B1, 'To':0x30B5, 'Tri':[[300],[0x00,0x00,0x30,0x4b,0x01,0x01],[0x00,0x00,0x30,0x4a,0x00,0x01],[0x00,0x00,0x30,0x49,0x01,0x01]]},
                 {'Sw_id':0x30E5,'Row':0 , 'Wait':0, 'From':0x30B1, 'To':0x30B7, 'Tri':[[300],[0x00,0x00,0x30,0x4b,0x00,0x01],[0x00,0x00,0x30,0x4a,0x00,0x01],[0x00,0x00,0x30,0x49,0x01,0x01]]}]
#        0x30D2: [[0x30B3,0x30B5,0x30b7],
#                 {'Sw_id':0x30E5, 'Wait':0,'From':[0x30b1]}]
        }
    
ACS_Data = {
    #ヤードdown(集合Lampと共通) Ver07追加                                  
        0x30b1: {'Type':'Lamp3','Name':'YAdown','Befor':99, 'After':99, 'xyz':[2,0,4], 'And':[0x30B1],'AndLamp':0x30F1, 'Thr':[0x3099,0x30B1],'ThrLamp':0x30F3,
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30b2: {'Type':'Lamp2','Name':'YAdown','Befor':99, 'After':99, 'xyz':[2,0,4], 'And':[0x30B1],'AndLamp':0x30F1, 'Thr':[0x3099,0x30B1],'ThrLamp':0x30F3,
                0x0101: {'color':'yellow'},
                0x0001: {'color':'green' ,'Tri':[[300],[0x00,0x00,0x30,0x78,0x01,0x01]]}},

        0x30f1: {'Type':'Lamp3','Name':'YAdown','Befor':99, 'After':99, 'xyz':[1,0,4],
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30f2: {'Type':'Lamp2','Name':'YAdown','Befor':99, 'After':99, 'xyz':[1,0,4],
                0x0101: {'color':'yellow'},
                0x0001: {'color':'green'}},

        0x3078: {'Name':'YAdown Sig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,0,4],
                0x0101: {'color':'green'},
                0x0001: {'color':'red' }},
#G1-S3R-Ya                                                              x=x-7 y=y+12
        0x30f3: {'Type':'Lamp3','Name':'YAdown','Befor':99, 'After':99, 'xyz':[1,0,4],
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30f4: {'Type':'Lamp2','Name':'YAdown','Befor':99, 'After':99, 'xyz':[1,0,4],
                0x0101: {'color':'yellow'},
                0x0001: {'color':'green'}},
    #ヤード分岐集合                                                      x=x-7 y=y+12
        0x30d2: {'Type':'Lamp3','Name':'YA in','Befor':99, 'After':99, 'xyz':[1,1,4],
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30d3: {'Type':'Lamp2','Name':'YA in','Befor':99, 'After':99, 'xyz':[1,1,4],
                0x0101: {'color':'yellow'},
                0x0001: {'color':'green'}},

        0x30e5: {'Type':'ONOFF3','Name':'YA IN SW','Befor':99, 'After':99, 'xyz':[0,1,4],
                0x0101: {'color':'green'},
                0x0001: {'color':'gray' }},

#        0x30d4: {'Type':'SW1','Name':'YA1 SW','Befor':99, 'After':99, 'xyz':[0,0,5],
#                0x0101: {'color':'green'},
#                0x0001: {'color':'gray' }},

#        0x30d5: {'Type':'SW1','Name':'YA2 SW','Befor':99, 'After':99, 'xyz':[0,1,5],
#                0x0101: {'color':'green'},
#                0x0001: {'color':'gray' }},

        0x306d: {'Name':'YA1 Sig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,1,4],
                0x0101: {'color':'green'},
                0x0001: {'color':'red' }},
#                                                                      x=x-7 y=y+12
        0x306e: {'Name':'YA2 Sig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,2,4],
                0x0101: {'color':'green'},
                0x0001: {'color':'red' }},

        0x306f: {'Name':'YA3 Sig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,3,4],
                0x0101: {'color':'green'},
                0x0001: {'color':'red' }},

        0x30b3: {'Name':'PY O1','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,1,4], 'And':[0x30b3,0x30b5,0x30b7],'AndLamp':0x30D2,
                0x0001:{'color':'white'},
                0x0101:{'color':'red'  }},
        0x30b4: {'Name':'PY O1','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,1,4], 'And':[0x30b3,0x30b5,0x30b7],'AndLamp':0x30D2,
                0x0101:{'color':'yellow'},
                0x0001:{'color':'green' ,'Tri':[[300],[0x00,0x00,0x30,0x6d,0x01,0x01]]}},

        0x30b5: {'Name':'PY O2','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,2,4], 'And':[0x30b3,0x30b5,0x30b7],'AndLamp':0x30D2,
                0x0001:{'color':'white'},
                0x0101:{'color':'red'  }},
        0x30b6: {'Name':'PY O2','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,2,4], 'And':[0x30b3,0x30b5,0x30b7],'AndLamp':0x30D2,
                0x0101:{'color':'yellow'},
                0x0001:{'color':'green' ,'Tri':[[300],[0x00,0x00,0x30,0x6e,0x01,0x01]]}},
#                                                                      x=x-7 y=y+12
        0x30b7: {'Name':'PY O3','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,3,4], 'And':[0x30b3,0x30b5,0x30b7],'AndLamp':0x30D2,
                0x0001:{'color':'white'},
                0x0101:{'color':'red'  }},
        0x30b8: {'Name':'PY O3','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,3,4], 'And':[0x30b3,0x30b5,0x30b7],'AndLamp':0x30D2,
                0x0101:{'color':'yellow'},
                0x0001:{'color':'green' ,'Tri':[[300],[0x00,0x00,0x30,0x6f,0x01,0x01]]}},
    #ヤード出口　Lamp                                                    x=x-7 y=y+12
        0x30E9: {'Type':'ONOFF3','Name':'YAout SW','Befor':99, 'After':99, 'xyz':[0,5,5],
                0x0101: {'color':'green'},
                0x0001: {'color':'gray' }},

        0x30ef: {'Type':'Lamp3','Name':'YAout','Befor':99, 'After':99, 'xyz':[1,5,5],
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30f0: {'Type':'Lamp2','Name':'YAout','Befor':99, 'After':99, 'xyz':[1,5,5],
                0x0101: {'color':'yellow'},
                0x0001: {'color':'green'}},

        0x30CF: {'Name':'YAout','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,5,5], 'And':[0x30cf],'AndLamp':0x30ef,
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30D0: {'Name':'YAout','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,5,5], 'And':[0x30cf],'AndLamp':0x30ef,
                0x0001: {'color':'green' ,'Tri':[[300],[0x00,0x00,0x30,0x77,0x01,0x01],[0x00,0x00,0x30,0x00,0x00,0x01]]},
                0x0101: {'color':'yellow'}},
        
#G Line
        #山　周回
        0x30ed: {'Name':'YAMASW','Type':'ONOFF3','Befor':99, 'After':99, 'xyz':[0,0,2],
                0x0101: {'color':'green'},
                0x0001: {'color':'gray' }},
        
        0x30eb: {'Name':'G1 SW','Type':'ONOFF3','Befor':99, 'After':99, 'xyz':[0,0,5],
                0x0101: {'color':'green'},
                0x0001: {'color':'gray' }},

        0x3069: {'Name':'G1 Sig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,0,5],
                0x0101: {'color':'green'},
                0x0001: {'color':'gray' }},

        #104:xy[5,]->xy[5,17]
        0x30C7: {'Name':'G1','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,0,5], 'And':[0x3099,0x30C7],'AndLamp':0x30a7,
                'sw1':21041,'lok_num':10,
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30C8: {'Name':'G1','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,0,5], 'And':[0x3099,0x30C7],'AndLamp':0x30a7,
                0x0001: {'color':'green'  ,'Tri':[[300],[0x00,0x00,0x30,0x69,0x01,0x01]]},
                0x0101: {'color':'yellow'}},
#                                                                      x=x-7 y=y+12
        0x30CD: {'Name':'G2','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[1,1,5],
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30CE: {'Name':'G2','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[1,1,5],
                0x0001: {'color':'green'},
                0x0101: {'color':'yellow'}},

        0x3061: {'Name':'G2outSig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,1,5],
                0x0101: {'color':'green'},
                0x0001: {'color':'gray' }},

        0x30C9: {'Name':'G2Out','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,1,5], 'And':[0x30C9,0x30CB],'AndLamp':0x30CD,
                'sw1':21046,'lok_num':7,
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30CA: {'Name':'G2Out','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,1,5], 'And':[0x30C9,0x30CB],'AndLamp':0x30CD,
                0x0001: {'color':'green'  ,'Tri':[[300],[0x00,0x00,0x30,0x61,0x01,0x01]]},
                0x0101: {'color':'yellow'}},

        0x3060: {'Name':'G2in Sig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,2,5],
                0x0101: {'color':'green'},
                0x0001: {'color':'gray' }},
#                                                                      x=x-7 y=y+12
        0x30CB: {'Name':'G2 In','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,2,5], 'And':[0x30C9,0x30CB],'AndLamp':0x30CD,
                'sw1':21045,'lok_num':10 ,
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30CC: {'Name':'G2 In','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,2,5], 'And':[0x30C9,0x30CB],'AndLamp':0x30CD,
                0x0001: {'color':'green'  ,'Tri':[[300],[0x00,0x00,0x30,0x60,0x01,0x01]]},
                0x0101: {'color':'yellow'}},
#***G3
        0x3068: {'Name':'G3 Sig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,3,5],
                0x0101: {'color':'green'},
                0x0001: {'color':'gray' }},

        0x30F5: {'Name':'G3','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,3,5],
                'sw1':21009,'lok_num':1,
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x30F6: {'Name':'G3','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,3,5],
                0x0001: {'color':'green' ,'Tri':[[300],[0x00,0x00,0x30,0x68,0x01,0x01]]},
                0x0101: {'color':'yellow'}},

#***G4L        
        0x3064: {'Name':'G4LSig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,4,5],
                0x0101: {'color':'green'},
                0x0001: {'color':'gray' }},

        0x3083: {'Name':'G4','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[1,4,5],
                0x0001: {'color':'white'},
                0x0101: {'color':'red' }},
        0x3084: {'Name':'G4','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[1,4,5],
                0x0001: {'color':'green'},
                0x0101: {'color':'yellow'}},

        0x3081: {'Name':'G4L','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,4,5], 'And':[0x3081],'AndLamp':0x3083,
            'sw1':21009,'lok_num':1,
            0x0001: {'color':'white'},
            0x0101: {'color':'red' }},
        0x3082: {'Name':'G4L','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,4,5], 'And':[0x3081],'AndLamp':0x3083,
            0x0001: {'color':'green'  ,'Tri':[[300],[0x00,0x00,0x30,0x64,0x01,0x01]]},
            0x0101: {'color':'yellow'}},
                        
#O Lin
        0x30a9: {'Name':'P O1','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,2,0], 'And':[0x30a9,0x30ab,0x30ad],'AndLamp':0x30af,
            'sw1':21002,'lok_num':1,
            0x0001:{'color':'white'},
            0x0101:{'color':'red'  }},
        0x30aa: {'Name':'P O1','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,2,0], 'And':[0x30a9,0x30ab,0x30ad],'AndLamp':0x30af,
            0x0101:{'color':'yellow', 'EventOn':1},
            0x0001:{'color':'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x5c,0x01,0x01],[0x00,0x00,0x30,0x0f,0x00,0x01]]}},

        0x305c: {'Type':'Sig','Name':'O1 Sig','Befor':99, 'After':99, 'xyz':[5,2,0],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'red'}},

        0x30ab: {'Name':'P O2','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,1,0], 'And':[0x30a9,0x30ab,0x30ad],'AndLamp':0x30af,
            'sw1':21003,'lok_num':2,
            0x0001:{'color':'white'},
            0x0101:{'color':'red'  }},
        0x30ac: {'Name':'P O2','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,1,0], 'And':[0x30a9,0x30ab,0x30ad],'AndLamp':0x30af,
            0x0101: {'color':'yellow', 'EventOn':1},
            0x0001: {'color':'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x5d,0x01,0x01],[0x00,0x00,0x30,0x0f,0x01,0x01],[0x00,0x00,0x30,0x19,0x00,0x01]]}},

        0x305d: {'Type':'Sig','Name':'O2 Sig','Befor':99, 'After':99, 'xyz':[5,1,0],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'red'}},

        0x30ad: {'Name':'P O3','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,0,0], 'And':[0x30a9,0x30ab,0x30ad],'AndLamp':0x30af,
            'sw1':21004,'lok_num':3,
            0x0001: {'color':'white'},
            0x0101: {'color':'red'  }},
        0x30ae: {'Name':'P O3','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,0,0], 'And':[0x30a9,0x30ab,0x30ad],'AndLamp':0x30af,
            0x0101: {'color': 'yellow', 'EventOn':1},
            0x0001: {'color': 'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x5e,0x01,0x01],[0x00,0x00,0x30,0x0f,0x01,0x01],[0x00,0x00,0x30,0x19,0x01,0x01]]}},

        0x305e: {'Type':'Sig','Name':'O3 Sig','Befor':99, 'After':99, 'xyz':[5,0,0],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'red'}},

#        0x30af: {'Name':'O123','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[1,0,0],
        0x30af: {'Name':'O123','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[1,0,0],
            0x0001: {'color':'white'},
            0x0101: {'color':'red'  }},
        0x30b0: {'Name':'O123','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[1,0,0],
            0x0101: {'color': 'yellow'},
            0x0001: {'color': 'green'}},

        0x30a6: {'Name':'O123st IN SW','Type':'ONOFF3','Befor':99, 'After':99, 'xyz':[0,0,0],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'gray'}},

#S Station
        0x30e7: {'Name':'S12 IN SW','Type':'ONOFF3','Befor':99, 'After':99, 'xyz':[0,2,3],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'gray'}},
        
        0x309b: {'Name':'S12st IN','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[1,2,3],
            0x0001: {'color': 'white'},
            0x0101: {'color': 'red'  }},
        0x309c: {'Name':'S12st IN','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[1,2,3],
            0x0001: {'color': 'green'},
            0x0101: {'color': 'yellow'}},
        
        0x3095: {'Name':'P S1','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,3,3], 'And':[0x3095,0x3097],'AndLamp':0x309b,
            'sw1':22025,'lok_num':0,
            0x0001: {'color':'white'},
            0x0101: {'color':'red'  }},
        0x3096: {'Name':'P S1','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,3,3], 'And':[0x3095,0x3097],'AndLamp':0x309b,
            0x0001: {'color':'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x54,0x01,0x01],[0x00,0x00,0x30,0x11,0x01,0x01]]},
            0x0101: {'color':'yellow', 'EventOn':1}},

        0x3054: {'Name':'S1 Sig','Type':'Sig','Befor':99, 'After':99, 'xyz':[5,3,3],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'red'}},

        0x3097: {'Name':'P S2','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[2,2,3], 'And':[0x3095,0x3097],'AndLamp':0x309b,
            'sw1':22026,'lok_num':0,
            0x0001: {'color':'white'},
            0x0101: {'color':'red' }},
        0x3098: {'Name':'P S2','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[2,2,3], 'And':[0x3095,0x3097],'AndLamp':0x309b,
            0x0001: {'color':'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x55,0x01,0x01],[0x00,0x00,0x30,0x11,0x00,0x01],[0x00,0x00,0x30,0x19,0x00,0x01]]},
            0x0101: {'color':'yellow', 'EventOn':1}},
 
        0x3055: {'Type':'Sig','Name':'S2 Sig','Befor':99, 'After':99, 'xyz':[5,2,3],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'red'}},

        0x30e6: {'Name':'M123-S3 SW','Type':'ONOFF3','Befor':99, 'After':99, 'xyz':[0,1,3],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'gray'}},
        
        0x30ea: {'Type':'ONOFF3','Name':'YAout-S3 SW','Befor':99, 'After':99, 'xyz':[0,0,3],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'gray'}},
        
        0x30a7: {'Type':'Lamp3','Name':'S3st IN','Befor':99, 'After':99, 'xyz':[1,1,3],
            0x0001: {'color': 'white'},
            0x0101: {'color': 'red'  }},
        0x30a8: {'Type':'Lamp2','Name':'S3st IN','Befor':99, 'After':99, 'xyz':[1,1,3],
            0x0001: {'color': 'green'},
            0x0101: {'color': 'yellow'}},
    #S3<-M123
        0x3099: {'Type':'Lamp3','Name':'P S3','Befor':99, 'After':99, 'xyz':[2,1,3], 'And':[0x3099,0x30C7],'AndLamp':0x30a7,
            'sw1':22026,'lok_num':0,
            0x0001: {'color': 'white' }, 
            0x0101: {'color': 'red'  }},
        0x309a: {'Type':'Lamp2','Name':'P S3','Befor':99, 'After':99, 'xyz':[2,1,3], 'And':[0x3099,0x30C7],'AndLamp':0x30a7,
            0x0001: {'color': 'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x56,0x01,0x01]]},
            0x0101: {'color': 'yellow'}},

        0x3056: {'Type':'Sig','Name':'S3 Sig','Befor':99, 'After':99, 'xyz':[5,1,3],
                0x0101: {'color': 'green'},
                0x0001: {'color': 'red'}},
#S4L とS4R　の集合
        0x308b: {'Type':'Lamp3','Name':'P S4','Befor':99, 'After':99, 'xyz':[1,4,3],
            0x0001: {'color': 'white'},
            0x0101: {'color': 'red'  }},
        0x308c: {'Type':'Lamp2','Name':'P S4','Befor':99, 'After':99, 'xyz':[1,4,3],
            0x0001: {'color': 'green'},
            0x0101: {'color': 'yellow'}},

    #S4L(山orM123へ)
        0x308d: {'Type':'Lamp3','Name':'S4L','Befor':99, 'After':99, 'xyz':[2,0,3], 'And':[0x308d], 'AndLamp':0x308b,
            'sw1':22006,'lok_num':9,
            0x0001: {'color': 'white' }, 
            0x0101: {'color': 'red' }},
        0x308e: {'Type':'Lamp2','Name':'S4L','Befor':99, 'After':99, 'xyz':[2,0,3], 'And':[0x308d], 'AndLamp':0x308b,
            0x0001: {'color': 'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x53,0x01,0x01]]},
            0x0101: {'color': 'yellow'}},

        0x3053: {'Type':'Sig','Name':'S4L Sig','Befor':99, 'After':99, 'xyz':[5,0,3],
                0x0101: {'color': 'green'},
                0x0001: {'color': 'red'}},

    #G1->S4L(YADE)
        0x30ec: {'Type':'ONOFF3','Name':'S4L SW','Befor':99, 'After':99, 'xyz':[0,4,3],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'gray'}},

        0x308f: {'Type':'Lamp3','Name':'S4R','Befor':99, 'After':99, 'xyz':[2,4,3], 'And':[0x308f], 'AndLamp':0x308b,
            'sw1':22004,'lok_num':4,
            0x0001: {'color': 'white' }, 
            0x0101: {'color': 'red' }},
        0x3090: {'Type':'Lamp2','Name':'S4R','Befor':99, 'After':99, 'xyz':[2,4,3], 'And':[0x308f], 'AndLamp':0x308b,
            0x0001: {'color': 'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x52,0x01,0x01]]},
            0x0101: {'color': 'yellow'}},

        0x3052: {'Type':'Sig','Name':'S4R Sig','Befor':99, 'After':99, 'xyz':[5,4,3],
                0x0101: {'color': 'green'},
                0x0001: {'color': 'red'}},

#M Line
        0x309f: {'Type':'Lamp3','Name':'P M1','Befor':99, 'After':99, 'xyz':[2,2,1], 'And':[0x309f,0x30a1,0x30a3],'AndLamp':0x309d,
           'sw1':21017,'lok_num':4, 
            0x0001: {'color': 'white'},
            0x0101: {'color': 'red'  }},
        0x30a0: {'Type':'Lamp2','Name':'P M1','Befor':99, 'After':99, 'xyz':[2,2,1], 'And':[0x309f,0x30a1,0x30a3],'AndLamp':0x309d,
            0x0001: {'color': 'green' , 'Tri':[[300],[0x00,0x00,0x30,0x58,0x01,0x01],[0x00,0x00,0x30,0x0a,0x00,0x01]]},
            0x0101: {'color': 'yellow'}},

        0x3058: {'Type':'Sig','Name':'M1 Sig','Befor':99, 'After':99, 'xyz':[5,2,1],
                0x0101: {'color': 'green'},
                0x0001: {'color': 'red'}},

        0x30a1: {'Type':'Lamp3','Name':'P M2','Befor':99, 'After':99, 'xyz':[2,1,1], 'And':[0x309f,0x30a1,0x30a3], 'AndLamp':0x309d,
            'sw1':21019,'lok_num':5,
            0x0001: {'color': 'white'},
            0x0101: {'color':'red'  }},
        0x30a2: {'Type':'Lamp2','Name':'P M2','Befor':99, 'After':99, 'xyz':[2,1,1], 'And':[0x309f,0x30a1,0x30a3], 'AndLamp':0x309d,
            0x0001: {'color':'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x59,0x01,0x01],[0x00,0x00,0x30,0x0a,0x01,0x01],[0x00,0x00,0x30,0x19,0x00,0x01]]},
            0x0101: {'color':'yellow', 'EventOn':1}},

        0x3059: {'Type':'Sig','Name':'M2 Sig','Befor':99, 'After':99, 'xyz':[5,1,1],
                0x0101: {'color': 'green'},
                0x0001: {'color': 'red'}},

        0x30a3: {'Type':'Lamp3','Name':'P M3','Befor':99, 'After':99, 'xyz':[2,0,1], 'And':[0x309f,0x30a1,0x30a3], 'AndLamp':0x309d,
            'sw1':21021,'lok_num':6,
            0x0001: {'color':'white'},
            0x0101: {'color':'red'  }},
        0x30a4: {'Type':'Lamp2','Name':'P M3','Befor':99, 'After':99, 'xyz':[2,0,1], 'And':[0x309f,0x30a1,0x30a3], 'AndLamp':0x309d,
            0x0001: {'color':'green' , 'EventOn':1, 'Tri':[[300],[0x00,0x00,0x30,0x5a,0x01,0x01],[0x00,0x00,0x30,0x0a,0x01,0x01],[0x00,0x00,0x30,0x19,0x01,0x01]]},
            0x0101: {'color':'yellow', 'EventOn':1}},

        0x305A: {'Type':'Sig','Name':'M3 Sig','Befor':99, 'After':99, 'xyz':[5,0,1],
                0x0101: {'color': 'green'},
                0x0001: {'color': 'red'}},

        0x309d: {'Name':'P M123','Type':'Lamp3','Befor':99, 'After':99, 'xyz':[1,0,1],
            0x0001: {'color':'white'},
            0x0101: {'color':'red'  }},
        0x309e: {'Name':'P M123','Type':'Lamp2','Befor':99, 'After':99, 'xyz':[1,0,1],
            0x0001: {'color':'green'},
            0x0101: {'color':'yellow'}},

        0x30a5: {'Name':'S3-M123 SW','Type':'ONOFF3','Befor':99, 'After':99, 'xyz':[0,0,1],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'gray'}},

        0x30e8: {'Type':'ONOFF3','Name':'M123-G1-S4R','Befor':99, 'After':99, 'xyz':[0,2,1],
            0x0101: {'color': 'green'},
            0x0001: {'color': 'gray'}},
        }