Pibo_UID = bytes([0x42,0x6F,0x4C,0x88])
Pibo_HASH = 0x7767

#Pi88_UID = 0x53383BF7
Pi88_UID = bytes([0x53,0x38,0x3B,0x88])
#Pi88_UID = bytes([0x53,0x38,0x3B,0xF4])    #Link88
Pi88_HASH = 0x4730
#Pi88_HASH = 0x474C　　#Link88

#暫定（CS3）
CS_HASH = 0xFFFF   #init
#CS_HASH = 0xCF1F   #CS2
#CS_HASH = 0x8B68   #CS3

#uint16_t generateHash(uint32_t uid) {
#    uint16_t hash, highword, lowword;

#    highword = uid >> 16;
#    lowword = uid & 0xFFFF;
#    hash = highword ^ lowword;
#    hash = (((hash << 3) & 0xFF00) | 0x0300) | (hash & 0x7F);
#    return hash;
#}


Lok_DATA = [
            [[0x00,0x00,0x04],[0x01,0x01,0x01,0x00,0xA8]],
            [[0x00,0x01,0x04],[0x14,0x01,0x00,0x40,0x8D]],
            [[0x00,0x02,0x04],[0x16,0x01,0x89,0x80,0x2d]],
            [[0x10,0x02,0x05],[0x00,0x83,0x00,0x1,0xCA],[0x96,0x65]],
            [[0x00,0x03,0x04],[0x18,0x36,0x2F,0x36,0x5E]],#Pi88_UI#Pi88_UID = 0x53383BF7
            [[0x10,0x03,0x0D],[0x20,0x44,0x65,0x20,0x81],[0x31,0x35,0x33,0x30,0x4A],[0x31,0x00,0x00,0x00,0x5B],[0x00,0xF3]],
            [[0x00,0x04,0x04],[0x17,0x03,0x04,0x05,0x43]],
            [[0x10,0x04,0x0D],[0x13,0x16,0x1D,0x1F,0xAB],[0x23,0x24,0x00,0x00,0xD5],[0x00,0x00,0x00,0x00,0xD1],[0x00,0xF3]],
            [[0x00,0x0C,0x04],[0x01,0x02,0x01,0x00,0x97]],
            [[0x00,0x10,0x04],[0x01,0x03,0x01,0x00,0x82]],
            
            [[0x00,0x14,0x04],[0x01,0x04,0x01,0x00,0xE9]],
            [[0x00,0x15,0x04],[0x10,0x03,0x03,0xC0,0x85]],
            [[0x00,0x16,0x04],[0x12,0x01,0x00,0x00,0xB0]],
            [[0x00,0x17,0x04],[0x13,0x02,0x00,0x00,0xE4]],
            [[0x00,0x18,0x04],[0x10,0x00,0x00,0x00,0x73]],
            [[0x00,0x1B,0x04],[0x10,0x08,0x08,0x00,0xE3]],
            [[0x00,0x19,0x04],[0x12,0x00,0x00,0x00,0xA5]],
            [[0x00,0x1A,0x04],[0x13,0x00,0x00,0x00,0xCE]],
            [[0x00,0x1B,0x04],[0x10,0x08,0x08,0x00,0xE3]],
            [[0x00,0x1C,0x04],[0x12,0x00,0x04,0x00,0xB9]],
            [[0x00,0x1D,0x04],[0x12,0x00,0x04,0x00,0xB9]],

            [[0x00,0x1E,0x04],[0x10,0x07,0x26,0x00,0xEA]],
            [[0x00,0x1F,0x04],[0x12,0x00,0x08,0x00,0x9D]],#Pi88_UID = 0x53383BF7
            [[0x00,0x20,0x04],[0x13,0x00,0x08,0x00,0xF6]],
            [[0x00,0x21,0x04],[0x10,0x0B,0x0B,0x00,0xD5]],#Pi88_UID = 0x53383BF7
            [[0x00,0x22,0x04],[0x12,0x40,0x00,0x00,0xFE]],

            [[0x00,0x23,0x04],[0x13,0x40,0x00,0x00,0x95]],
            [[0x00,0x24,0x04],[0x10,0x07,0x07,0x01,0x0C]],
            [[0x00,0x25,0x04],[0x12,0x00,0x01,0x00,0xA2]],
            [[0x00,0x26,0x04],[0x13,0x00,0x01,0x00,0xC9]],
            [[0x00,0x27,0x04],[0x10,0x03,0x03,0x40,0x05]],

            [[0x00,0x28,0x04],[0x12,0x08,0x00,0x00,0x0D]],
            [[0x00,0x29,0x04],[0x13,0x08,0x00,0x00,0x66]],
            [[0x00,0x2A,0x04],[0x10,0x87,0x26,0x00,0x5C]],
            [[0x00,0x2B,0x04],[0x12,0x00,0x10,0x00,0xD5]],
            [[0x00,0x2C,0x04],[0x13,0x00,0x10,0x00,0xBE]],

            [[0x00,0x2D,0x04],[0x10,0x03,0x03,0x80,0xC5]],
            [[0x00,0x2E,0x04],[0x12,0x04,0x00,0x00,0xF1]],
            [[0x00,0x2F,0x04],[0x13,0x04,0x00,0x00,0x9A]],

            [[0x00,0x30,0x04],[0x10,0x87,0x07,0x0F,0xB4]],
            [[0x00,0x31,0x04],[0x12,0x00,0x00,0x00,0xA5]],
            [[0x00,0x32,0x04],[0x13,0x00,0x00,0x00,0xCE]],
            [[0x00,0x33,0x04],[0x10,0x07,0x07,0x08,0x05]],
            [[0x00,0x34,0x04],[0x12,0x00,0x20,0x00,0x45]],
            [[0x00,0x35,0x04],[0x13,0x00,0x20,0x00,0x2E]],
            [[0x00,0x36,0x04],[0x10,0x87,0x07,0x13,0xA8]],
            [[0x00,0x37,0x04],[0x12,0x00,0x00,0x80,0x25]],
            [[0x00,0x38,0x04],[0x13,0x00,0x00,0x80,0x4E]],
            [[0x00,0x39,0x04],[0x10,0x07,0x29,0x03,0xC4]],
            [[0x00,0x3A,0x04],[0x12,0x00,0x00,0x20,0x85]],
            [[0x00,0x3B,0x04],[0x13,0x00,0x00,0x20,0xEE]],
            [[0x00,0x3C,0x04],[0x10,0x07,0x07,0x02,0x0F]],
            [[0x00,0x3D,0x04],[0x12,0x00,0x00,0x00,0xA5]],
            [[0x00,0x3E,0x04],[0x13,0x00,0x00,0x00,0xCE]],
            [[0x00,0x3F,0x04],[0x10,0x0A,0x0A,0x00,0xC7]],
            [[0x00,0x40,0x04],[0x13,0x00,0x00,0x00,0xCE]],
            [[0x00,0x41,0x04],[0x13,0x80,0x00,0x00,0x78]],
            [[0x00,0x42,0x04],[0x10,0x07,0x07,0x2F,0x22]],
            [[0x00,0x43,0x04],[0x12,0x00,0x02,0x00,0xAB]],
            [[0x00,0x44,0x04],[0x13,0x00,0x02,0x00,0xC0]],
            [[0x00,0x45,0x04],[0x10,0x00,0x00,0x00,0x73]],
            [[0x00,0x46,0x04],[0x12,0x00,0x00,0x00,0xA5]],
            [[0x00,0x47,0x04],[0x13,0x00,0x00,0x00,0xCE]],
            [[0x00,0x48,0x04],[0x10,0x00,0x00,0x00,0x73]],
            [[0x00,0x49,0x04],[0x12,0x00,0x00,0x00,0xA5]],
            [[0x00,0x4A,0x04],[0x13,0x00,0x00,0x00,0xCE]],
            [[0x00,0x4B,0x04],[0x00,0x00,0x00,0x00,0xD1]],
            [[0x00,0x4C,0x04],[0x01,0x05,0x01,0x00,0xFC]],
            [[0x00,0x4D,0x04],[0x10,0x01,0x00,0x00,0x66]],
            [[0x00,0x4E,0x04],[0x13,0x0F,0x0F,0x00,0x20]],
            [[0x00,0x4E,0x04],[0x13,0x0F,0x0F,0x00,0x20]],
            [[0x00,0x4F,0x04],[0x17,0x0A,0xFF,0x03,0x17]],
            [[0x00,0x50,0x04],[0x18,0x32,0x00,0x00,0xF1]],
            [[0x00,0x74,0x04],[0x01,0x08,0x01,0x00,0x15]],
            [[0x00,0x75,0x04],[0x10,0xFF,0x00,0x00,0xA4]],
            [[0x00,0x7C,0x04],[0x01,0x07,0x01,0x00,0xD6]],
            [[0x00,0x7D,0x04],[0x10,0x01,0x00,0x00,0x66]],
            [[0x00,0x7E,0x04],[0x11,0x01,0x00,0x00,0x0D]],
            [[0x00,0x7F,0x04],[0x12,0x00,0x01,0x00,0xA2]],
            [[0x00,0x80,0x04],[0x14,0x64,0x87,0x00,0xE5]],
            [[0x00,0x81,0x04],[0x10,0x00,0x00,0x00,0x73]],
            [[0x00,0x82,0x04],[0x11,0x00,0x00,0x00,0x18]],
            [[0x00,0x83,0x04],[0x12,0x00,0x01,0x00,0xA2]],
            [[0x00,0x84,0x04],[0x14,0x00,0x00,0x00,0xD8]],
            [[0x00,0x85,0x04],[0x10,0x03,0x00,0x00,0x4C]],
            [[0x00,0x86,0x04],[0x11,0x17,0x00,0x00,0x24]],
            [[0x00,0x87,0x04],[0x12,0x00,0x01,0x00,0xA2]],
            [[0x00,0x88,0x04],[0x13,0x7C,0x95,0x97,0xE5]],
            [[0x00,0x8C,0x04],[0x01,0x09,0x01,0x00,0x00]],
            [[0x00,0x90,0x04],[0x01,0x0A,0x01,0x00,0x3F]],
            [[0x00,0x91,0x04],[0x10,0x00,0xFF,0xFF,0x7F]],
            [[0x00,0x92,0x04],[0x11,0x00,0x00,0x00,0x18]],
            [[0x00,0x93,0x04],[0x12,0x00,0x00,0x05,0xA0]],
            [[0x00,0x94,0x04],[0x13,0x00,0x00,0x19,0xD7]],
            [[0x00,0x95,0x04],[0x14,0x0A,0x7E,0x00,0x27]],
            [[0x00,0x96,0x04],[0x15,0x00,0xFF,0xFF,0xE5]],
            [[0x00,0x97,0x04],[0x10,0x00,0xFF,0xFF,0xE5]],
            [[0x00,0x98,0x04],[0x17,0x00,0x2C,0x00,0xA1]],
            [[0x00,0x99,0x04],[0x18,0x04,0x4C,0x00,0x95]],
            [[0x00,0x9A,0x04],[0x19,0x00,0x00,0x00,0x49]],
            [[0x00,0x9B,0x04],[0x1A,0x00,0x00,0x00,0xF4]],
            [[0x00,0x9C,0x04],[0x1B,0x00,0x29,0x00,0x40]],
            ]

Bo88_DATA = [[
        [0x03,0x01,0x00,0x00, 0x00,0x00,Pibo_UID[2]-0x32,Pibo_UID[3]], #301 000C0000  0000@UID3-0x32 UID4 Booster88(SNr.6736)(0x1A50)
        [0x36,0x30,0x31,0x37, 0x34,0x00,0x00,0x00], #60174
        [0x42,0x6F,0x6F,0x73, 0x74,0x65,0x72,0x20],   # Booster
        [0x36,0x30,0x31,0x37, 0x34,0x00,0x00,0x00],    # 60174
        [0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00],    #
        [Pibo_UID[0],Pibo_UID[1],Pibo_UID[2],Pibo_UID[3], 0x00,0x00,0x00,0x00], #HASH UID      0004   link88
        [], #306
        [], #307
        []
    ],[
        [0x01,0xFD,0x30,0xF0, 0xE0,0xC0,0x00,0x00], 
        [0x02,0x36,0x02,0x4E, 0x02,0x65,0x02,0x89],    # 6Ne
        [0x54,0x52,0x41,0x43, 0x4B,0x00,0x30,0x2E],    # TRACK
        [0x30,0x30,0x00,0x35, 0x2E,0x35,0x30,0x00],    #00 0 5.50
        [0x41,0x00,0x00,0x00, 0x00,0x00,0x00,0x00],
        [Pibo_UID[0],Pibo_UID[1],Pibo_UID[2],Pibo_UID[3], 0x01,0x00,0x00,0x00],
        [], #306
        [], #307
        []
    ],[
        [0x03,0xFD,0xC0,0x0C, 0x30,0xC0,0x00,0x00],
        [0x00,0xC2,0x00,0xFC, 0x02,0x1F,0x02,0x93],
        [0x56,0x4F,0x4C,0x54, 0x00,0x31,0x30,0x2E],  # VOLT
        [0x30,0x30,0x00,0x32, 0x37,0x2E,0x30,0x30],  # 00 27.00
        [0x00,0x56,0x00,0x00, 0x00,0x00,0x00,0x00],
        [Pibo_UID[0],Pibo_UID[1],Pibo_UID[2],Pibo_UID[3], 0x02,0x00,0x00,0x00],
        [], #306
        [], #307
        []
    ],[
        [0x04,0x00,0x0C,0x08, 0xF0,0xC0,0x00,0x00],
        [0x00,0x79,0x00,0x91, 0x00,0xA9,0x00,0xC1],  # 0 y 
        [0x54,0x45,0x4D,0x50, 0x00,0x30,0x2E,0x30],  # TEMP
        [0x00,0x38,0x30,0x2E, 0x30,0x00,0x43,0x00],
        [Pibo_UID[0],Pibo_UID[1],Pibo_UID[2],Pibo_UID[3], 0x03,0x00,0x00,0x00],
        [], #306
        [], #307
        [], #308
        []
    ],[
        [0x01,0x01,0x03,0x02, 0x00,0x00,0x00,0x00],
        [0x54,0x72,0x61,0x66, 0x6F,0x3A,0x00,0x36],  # Trafo: 6
        [0x30,0x30,0x35,0x32, 0x00,0x36,0x30,0x30],  # 0052 600
        [0x36,0x31,0x00,0x36, 0x30,0x31,0x30,0x31],  # 61 60101
        [Pibo_UID[0],Pibo_UID[1],Pibo_UID[2],Pibo_UID[3], 0x04,0x00,0x00,0x00],
        [], #306
        [], #307
        [], #307
        []
    ]
]

Pi88_DATA = [[
        [0x00,0x0C,0x00,0x00, 0x00,0x00,Pi88_UID[2]-0x38,Pi88_UID[3]], #301 000C0000  0000@UID3-56@UID4 Link88(SNr.1012) 244(0xF4)
#        [0x00,0x0C,0x00,0x00, 0x00,0x00,0x03,0xF7], #301 000C0000  0000@UID3-56@UID4
#        [0x00,0x02,0x00,0x00, 0x00,0x00,0x9A,0x6B], #301 00020000  0000@UID3-56@UID4
        [0x36,0x30,0x38,0x38, 0x33,0x2D,0x31,0x00], #302@36303838  33000000 6088 3-1
        [0x4c,0x69,0x6e,0x6b, 0x20,0x53,0x38,0x38], #303 4C696E6B  20533838 Link@@S88
#      {0x53,0x68,0x6f,0x6a, 0x69,0x20,0x38,0x38}, #303 53696E6B  20533838 Shoj@@i88
#        [0x48,0x52,0x53,0x20, 0x57,0x69,0x46,0x69], #303 53696E6B  20533838 HRS @WiFi
        [0x20,0x38,0x38,0x00, 0x00,0x00,0x00,0x00], #304@20383800  00000000  88
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x00,0x04,0x00,0x00], #HASH UID      0004   link88
#        [0x53,0x38,0x3B,0xF7, 0x00,0x04,0x00,0x00], #HASH UID      0004 Pi88
        [], #306
        [], #307
        []
    ],[                                             #index:01 07
#      {0x01,0x02,0x00,0x00, 0x00,0x1F,0x00,0x10}, #301 02020000 001f0000
#        {0x4C,0xC3,0xA4,0x6E, 0x67,0x65,0x20,0x42}, #302@4cc3a46e 67652042 La:n ge B
#        {0x75,0x73,0x20,0x31, 0x20,0x28,0x52,0x4A}, #303 75732031 2028524a us 1  (RJ
#        {0x34,0x35,0x2D,0x31, 0x29,0x00,0x30,0x00}, #304@34352d31 29003000 45-1 ) 0 
#        {0x33,0x31,0x00,0x00, 0x00,0x00,0x00,0x00}, #305@33310000 00000000 31
#        {0x53,0x38,0xF0,0x6B, 0x01,0x05,0x00,0x00}, #HASH UID     0105
#
        [0x01,0x01,0x02,0x00, 0x00,0x00,0x00,0x02], #301 01010200 000000 00:Einzel? 01:Tastatur    
        [0x41,0x75,0x73,0x77, 0x65,0x72,0x74,0x75], #302 41757377 65727475 Ausw ertu
        [0x6E,0x67,0x20,0x31, 0x20,0x2D,0x20,0x31], #303 6e672031 202d2031 ng 1  - 1
        [0x36,0x00,0x45,0x69, 0x6E,0x7A,0x65,0x6C], #304@36004569 6e7a656c 6 Ei nzel
        [0x6E,0x00,0x54,0x61, 0x73,0x74,0x61,0x74], #305 6e005461 73746174 n Ta stat
        [0x75,0x72,0x6D,0x61, 0x74,0x72,0x69,0x78], #306@75726d61 74726978 urma trix
        [0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00], #307@00000000 00000000
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x01,0x07,0x00,0x00], #HASH UID     0107

    ],[                                             #index:02 05
        [0x02,0x02,0x00,0x00, 0x00,0x1F,0x00,0x05], #301 02020000 001f0000 
        [0x4C,0xC3,0xA4,0x6E, 0x67,0x65,0x20,0x42], #302@4cc3a46e 67652042 La:n ge B
        [0x75,0x73,0x20,0x32, 0x20,0x28,0x52,0x4A], #303 75732031 2028524a us 1  (RJ
        [0x34,0x35,0x2D,0x31, 0x29,0x00,0x30,0x00], #304@34352d31 29003000 45-1 ) 0 
        [0x33,0x31,0x00,0x00, 0x00,0x00,0x00,0x00], #305@33310000 00000000 31
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x02,0x05,0x00,0x00], #HASH UID     0205
        [], #307
        []
    ],[                                             #index:03 05
        [0x03,0x02,0x00,0x00, 0x00,0x1F,0x00,0x00], #301 03020000 001f0000
        [0x4C,0xC3,0xA4,0x6E, 0x67,0x65,0x20,0x42], #302@4cc3a46e 67652042 La:n ge B
        [0x75,0x73,0x20,0x32, 0x20,0x28,0x52,0x4A], #303 75732032 2028524a us 2  (RJ
        [0x34,0x35,0x2D,0x32, 0x29,0x00,0x30,0x00], #304@34352d32 29003000 45-1 ) 0 
        [0x33,0x31,0x00,0x00, 0x00,0x00,0x00,0x00], #305 33310000 00000000 31
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x03,0x05,0x00,0x00], #HASH UID     0305
        [], #307@H
        []
    ],[                                             #index:04 05
        [0x04,0x02,0x00,0x00, 0x00,0x1F,0x00,0x00], #301 04020000 001f0000 L4-2 Min:0 Max:31 Set:0
        [0x4C,0xC3,0xA4,0x6E, 0x67,0x65,0x20,0x42], #302@4cc3a46e 67652042 La:n ge B
        [0x75,0x73,0x20,0x33, 0x20,0x28,0x36,0x2D], #303 75732033 2028362d us 3  (6-
        [0x50,0x6F,0x6C,0x69, 0x67,0x29,0x00,0x30], #304@506f6c69 67290030 Poli g) 0
        [0x00,0x33,0x31,0x00, 0x00,0x00,0x00,0x00], #305@00333100 00000000  31
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x04,0x05,0x00,0x00], #HASH UID     0405
        [], #307@H
        []
    ],[                                             #index:05 06
        [0x05,0x02,0x00,0x0A, 0x03,0xE8,0x00,0x64], #301 0502000a 03e80064 L5-2 Min:10 Max:1000 Set:100
        [0x5A,0x79,0x6B,0x6C, 0x75,0x73,0x7A,0x65], #302 5a796b6c 75737a65 Zykl usze
        [0x69,0x74,0x20,0x42, 0x75,0x73,0x20,0x31], #303 69742042 75732031 it B us 1
        [0x20,0x28,0x52,0x4A, 0x34,0x35,0x2D,0x31], #304 2028524a 34352d31  (RJ 45-1
        [0x29,0x00,0x31,0x30, 0x00,0x31,0x30,0x30], #305 29003130 00313030 ) 10  100
        [0x30,0x00,0x6D,0x73, 0x00,0x00,0x00,0x00], #306 30006d73 00000000 0 ms
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x05,0x06,0x00,0x00], #HASH UID     0506
        []
    ],[                                             #index:06 06
        [0x06,0x02,0x00,0x0A, 0x03,0xE8,0x00,0x64], #301 0602000a 03e80064
        [0x5A,0x79,0x6B,0x6C, 0x75,0x73,0x7A,0x65], #302 5a796b6c 75737a65
        [0x69,0x74,0x20,0x42, 0x75,0x73,0x20,0x32], #303 69
        [0x20,0x28,0x52,0x4A, 0x34,0x35,0x2D,0x32], #304@H
        [0x29,0x00,0x31,0x30, 0x00,0x31,0x30,0x30], #305@H
        [0x30,0x00,0x6D,0x73, 0x00,0x00,0x00,0x00], #306@H
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x06,0x06,0x00,0x00], #END
        []
    ],[                                             #index:07 06
        [0x07,0x02,0x00,0x0A, 0x03,0xE8,0x00,0x64], #301 Z
        [0x5A,0x79,0x6B,0x6C, 0x75,0x73,0x7A,0x65], #302@¢
        [0x69,0x74,0x20,0x42, 0x75,0x73,0x20,0x33], #303 H
        [0x20,0x28,0x36,0x2D, 0x50,0x6F,0x6C,0x69], #304@H
        [0x67,0x29,0x00,0x31, 0x30,0x00,0x31,0x30], #305@H
        [0x30,0x30,0x00,0x6D, 0x73,0x00,0x00,0x00], #306@H
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x07,0x06,0x00,0x00], #END
        []
    ],[                                             #index:08 05
        [0x08,0x02,0x00,0x64, 0x03,0xE8,0x00,0xA7], #301 Z
        [0x42,0x69,0x74,0x7A, 0x65,0x69,0x74,0x20], #302@¢
        [0x53,0x38,0x38,0x00, 0x31,0x30,0x30,0x00], #303 H
        [0x31,0x30,0x30,0x30, 0x00,0xC2,0xB5,0x73], #304@H
        [0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00], #305@H
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x08,0x05,0x00,0x00], #END
        [], #307@H
        []
    ],[                                             #index:09 05
        [0x09,0x02,0x00,0x0A, 0x03,0xE8,0x00,0x64], #301
        [0x5A,0x79,0x6B,0x6C, 0x75,0x73,0x7A,0x65], #302
        [0x69,0x74,0x20,0x31, 0x20,0x2D,0x20,0x31], #303
        [0x36,0x00,0x31,0x30, 0x00,0x31,0x30,0x30], #304
        [0x30,0x00,0x6D,0x73, 0x00,0x00,0x00,0x00], #305
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x09,0x05,0x00,0x00], #END
        [], #307
        []
    ],[                                             #index:0a 05
        [0x0A,0x02,0x00,0x0A, 0x00,0x64,0x00,0x25], #301
        [0x5A,0x79,0x6B,0x6C, 0x75,0x73,0x7A,0x65], #302
        [0x69,0x74,0x20,0x54, 0x61,0x73,0x74,0x61], #303
        [0x74,0x75,0x72,0x00, 0x31,0x30,0x00,0x31], #304
        [0x30,0x30,0x00,0x6D, 0x73,0x00,0x00,0x00], #305
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x0a,0x05,0x00,0x00], #END
        [], #307
        []
    ],[                                             #index:0b 04
        [0x0B ,0x02 ,0x00 ,0x00 ,0x00 ,0x08 ,0x00 ,0x00], #301
        [0x53 ,0x70 ,0x61 ,0x6C ,0x74 ,0x65 ,0x6E ,0x20], #302
        [0x54 ,0x61 ,0x73 ,0x74 ,0x61 ,0x74 ,0x75 ,0x72], #303
        [0x00 ,0x30 ,0x00 ,0x38 ,0x00 ,0x00 ,0x00 ,0x00], #304
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3], 0x0B, 0x04], #END
        [], #306
        [], #307
        []
    ],[                                             #index:0c 04
        [0x0C ,0x02 ,0x00 ,0x00 ,0x00 ,0x0F ,0x00 ,0x00], #301
        [0x5A ,0x65 ,0x69 ,0x6C ,0x65 ,0x6E ,0x20 ,0x54], #302
        [0x61 ,0x73 ,0x74 ,0x61 ,0x74 ,0x75 ,0x72 ,0x00], #303
        [0x30 ,0x00 ,0x31 ,0x35 ,0x00 ,0x00 ,0x00 ,0x00], #304
        [Pi88_UID[0],Pi88_UID[1],Pi88_UID[2],Pi88_UID[3],0x0C,0x04], #END
        [], #306
        [], #307
        []
    ]
]

def message_data_print(OnOff,CanID,Hash,Data):
    if OnOff == True:
        r = format(CanID, '03x') + ' ' + format(Hash,'04x') + '[' + str(len(Data)) + ']'
        for w in range(0,8):
            try:
                r = r + ' ' + format(Data[w], '02x')
            except:
                r = r + '   '
        print(r,end=':')
    else:
        r = None
    return r

#def gui_event(event,values)

cmd_list = [
    'System Main_Cmd(0)',       #CanID:0x00
    'System Main_Cmd(1)',
    'Lok Discovery  (0)',       #CanID:0x02    
    'Lok Discovery  (1)',    
    'Mfx Bind       (0)',       #CanID:0x04
    'Mfx Bind       (1)',    
    'Mfx Verify     (0)',       #CanID:0x06
    'Mfx Verify     (1)',    
    'Lok Speed      (0)',       #CanID:0x08
    'Lok Speed      (1)',    
    'Lok Direction  (0)',       #CanID:0x0A
    'Lok Direction  (1)',    
    'Lok Function   (0)',       #CanID:0x0C
    'Lok Function   (1)',    
    'Read Config    (0)',       #CanID:0x0E
    'Read Config    (1)',    
    'Write Config   (0)',       #CanID:0x10
    'Write Config   (1)',    
    'Unknown 0x12   (0)',       #CanID:0x12
    'Unknown 0x13   (1)',       #CanID:0x13
    'Unknown 0x14   (0)',       #CanID:0x14
    'Unknown 0x15   (1)',       #CanID:0x15
    'SwitchAccsesary(0)',       #CanID:0x16
    'SwitchAccsesary(1)',       #CanID:0x17
    'SwitchConfig   (0)',       #CanID:0x18
    'SwitchConfig   (1)',       #CanID:0x19
    'Unknown 0x1A   (0)',       #CanID:0x1A
    'Unknown 0x1B   (1)',       #CanID:0x1B
    'Unknown 0x1C   (0)',       #CanID:0x1C
    'Unknown 0x1D   (1)',       #CanID:0x1D
    'Unknown 0x1E   (0)',       #CanID:0x1E
    'Unknown 0x1F   (1)',       #CanID:0x1F   
    'S88 Polling    (0)',       #CanID:0x20
    'S88 Polling    (1)',       #CanID:0x21
    'S88 Event      (0)',       #CanID:0x22
    'S88 Event      (1)',       #CanID:0x23    
    'SX1 Event      (0)',       #CanID:0x24
    'SX1 Event      (1)',       #CanID:0x25    
    'Unknown 0x26   (0)',       #CanID:0x26
    'Unknown 0x27   (1)',       #CanID:0x27
    'Unknown 0x28   (0)',       #CanID:0x28
    'Unknown 0x29   (1)',       #CanID:0x29
    'Unknown 0x2A   (0)',       #CanID:0x2A
    'Unknown 0x2B   (1)',       #CanID:0x2B
    'Unknown 0x2C   (0)',       #CanID:0x2C
    'Unknown 0x2D   (1)',       #CanID:0x2D
    'Unknown 0x2E   (0)',       #CanID:0x2E
    'Unknown 0x2F   (1)',       #CanID:0x2F
    'Ping           (0)',       #CanID:0x30
    'Ping           (1)',       #CanID:0x31
    'Update Offer   (0)',       #CanID:0x32
    'Update Offer   (1)',       #CanID:0x33
    'Read ConfigData(0)',       #CanID:0x34
    'Read ConfigData(1)',       #CanID:0x35
    'Bootloader_CAN (0)',       #CanID:0x36
    'Bootloader_CAN (1)',       #CanID:0x37
    'Bootloader_Rail(0)',       #CanID:0x38
    'Bootloader_Rail(1)',       #CanID:0x39
    'Status Constitu(0)',       #CanID:0x3A
    'Status Constitu(1)',       #CanID:0x3B
    'Unknown 0x3C   (0)',       #CanID:0x3C
    'Unknown 0x3D   (1)',       #CanID:0x3D
    'Unknown 0x3E   (0)',       #CanID:0x3E
    'Unknown 0x3F   (1)',       #CanID:0x3F
    'Data Query     (0)',       #CanID:0x40
    'Data Query     (1)',       #CanID:0x41
    'Data Stream    (0)',       #CanID:0x42
    'Data Stream    (1)',       #CanID:0x43
    'Connect6021    (0)',       #CanID:0x44
    'Connect6021    (1)',       #CanID:0x45
    'Unknown 0x46   (0)',       #CanID:0x46
    'Unknown 0x47   (1)',       #CanID:0x47
    'Unknown 0x48   (0)',       #CanID:0x48
    'Unknown 0x49   (1)',       #CanID:0x49
    'Unknown 0x4A   (0)',       #CanID:0x4A
    'Unknown 0x4B   (1)',       #CanID:0x4B
    'Unknown 0x4C   (0)',       #CanID:0x4C
    'Unknown 0x4D   (1)',       #CanID:0x4D
    'Unknown 0x4E   (0)',       #CanID:0x4E
    'Unknown 0x4F   (1)',       #CanID:0x4F
    'Unknown 0x50   (0)',       #CanID:0x50
    'Unknown 0x51   (1)',       #CanID:0x51
    'Unknown 0x52   (0)',       #CanID:0x52
    'Unknown 0x53   (1)',       #CanID:0x53
    'Unknown 0x54   (0)',       #CanID:0x54
    'Unknown 0x55   (1)',       #CanID:0x55
    'Unknown 0x56   (0)',       #CanID:0x56
    'Unknown 0x57   (1)',       #CanID:0x57
    'Unknown 0x58   (0)',       #CanID:0x58
    'Unknown 0x59   (1)',       #CanID:0x59
    'Unknown 0x5A   (0)',       #CanID:0x5A
    'Unknown 0x5B   (1)',       #CanID:0x5B
    'Unknown 0x5C   (0)',       #CanID:0x5C
    'Unknown 0x5D   (1)',       #CanID:0x5D
    'Unknown 0x5E   (0)',       #CanID:0x5E
    'Unknown 0x5F   (1)',       #CanID:0x5F
    'Unknown 0x60   (0)',       #CanID:0x60
    'Unknown 0x61   (1)',       #CanID:0x61
    'Unknown 0x62   (0)',       #CanID:0x62
    'Unknown 0x63   (1)',       #CanID:0x63
    'Unknown 0x64   (0)',       #CanID:0x64
    'Unknown 0x65   (1)',       #CanID:0x65
    'Unknown 0x66   (0)',       #CanID:0x66
    'Unknown 0x67   (1)',       #CanID:0x67
    'Unknown 0x68   (0)',       #CanID:0x68
    'Unknown 0x69   (1)',       #CanID:0x69
    'Unknown 0x6A   (0)',       #CanID:0x6A
    'Unknown 0x6B   (1)',       #CanID:0x6B
    'Unknown 0x6C   (0)',       #CanID:0x6C
    'Unknown 0x6D   (1)',       #CanID:0x6D
    'Unknown 0x6E   (0)',       #CanID:0x6E
    'Unknown 0x6F   (1)',       #CanID:0x6F
    'Unknown 0x70   (0)',       #CanID:0x70
    'Unknown 0x71   (1)',       #CanID:0x71
    'Unknown 0x72   (0)',       #CanID:0x72
    'Unknown 0x73   (1)',       #CanID:0x73
    'Unknown 0x74   (0)',       #CanID:0x74
    'Unknown 0x75   (1)',       #CanID:0x75
    'Unknown 0x76   (0)',       #CanID:0x76
    'Unknown 0x77   (1)',       #CanID:0x77
    'Unknown 0x78   (0)',       #CanID:0x78
    'Unknown 0x79   (1)',       #CanID:0x79
    'Unknown 0x7A   (0)',       #CanID:0x7A
    'Unknown 0x7B   (1)',       #CanID:0x7B
    'Unknown 0x7C   (0)',       #CanID:0x7C
    'Unknown 0x7D   (1)',       #CanID:0x7D
    'Unknown 0x7E   (0)',       #CanID:0x7E
    'Unknown 0x7F   (1)',       #CanID:0x7F
    ]

sub_cmd_list = [
    'System Stop:',     #SubCmd 0x00
    'System Go  :',     #SubCmd 0x01
    'System Halt:',     #SubCmd 0x02
    'L_Emergency:',     #SubCmd 0x03
    'Lok Stop   :',     #SubCmd 0x04
    'LokDataProt:',     #SubCmd 0x05
    'SwTimeAcces:',     #SubCmd 0x06
    'FastReadMFX:',     #SubCmd 0x07
    'Track Protc:',     #SubCmd 0x08
    'SysMFXCount:',     #SubCmd 0x09
    'SysOverLoad:',     #SubCmd 0x0A
    'Sys Status :',     #SubCmd 0x0B
    'Sys ID_Nr  :',     #SubCmd 0x0C
    ]

def analysis_can_data(CanID,Hash,Dlc,Data):
    Cmd = CanID // 2
    rw = CanID % 2
    r = 0
    Debug_Msg = ''
#    print(hex(Cmd),hex(CanID),rw,end='')

    if CanID == 0x80:
        print('CMD=0x80 Mfx New?Res? -> ',end='')
        r = 0x80
    else:
#        print(cmd_list[CanID],end=':')
        Debug_Msg += 'CanID:'+hex(CanID)[2:] + ' ' + cmd_list[CanID]

        if Cmd == 0x00 or Cmd == 0x01:
          if Dlc > 4:
            sub_cmd = Data[4]
            try:
                print(sub_cmd_list[sub_cmd])
                if sub_cmd == 0x0C and rw == 1 and Pi88_UID == Data[0:4]:
                    print('Get pi88_ID=',end='')
                    r = 0xFF0C

                elif sub_cmd == 0x0B and Dlc == 6:
                    print('SubCmd 0x0B:DLC:',Dlc,' Data[0:4]:',hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]),hex(Data[5]))
                    r = 0xFF0B
                elif sub_cmd == 0x0B and Dlc == 7:
                    print('SubCmd 0x0B:DLC:',Dlc,' Data[0:7]:',hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]),hex(Data[5]),hex(Data[6]))
                    r = 0xFF0B
                elif sub_cmd == 0x0B and Dlc == 8:
                    print('SubCmd 0x0B:DLC:',Dlc,' Data[0:8]:',hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]),hex(Data[5]),hex(Data[6]),hex(Data[7]))
                    r = 0xFF0B
                elif sub_cmd == 0x03:
                    print('Lok Emagency Stop:'+hex(Data[2]*0x100+Data[3]))
                    r = 0xFF03
                elif sub_cmd == 0x0C and Dlc == 5:
                    print('SubCmd 0x0C:DLC:',Dlc,' Data[0:5]:',hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]))
                    r = 0xFF0C
                elif sub_cmd == 0x0C and Dlc == 7:
                    print('SubCmd 0x0C:DLC:',Dlc,' Data[0:7]:',hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]),hex(Data[5]),hex(Data[6]))
                    r = 0xFF0C
                    
            except:
                if sub_cmd == 0x80:
                    print('System Reset')
                elif sub_cmd == 0x30:
                    if Data[5] == 0x00:
                        print('MfxSeek End')
                        r = 0x0300
                    elif Data[5] == 0x01:
                        print('MfxSeek Start')
                        r = 0x0301
                    elif Data[5] == 0x02:
                        print('MfxSeek 0x02')
                        r = 0x0302
                else:
                    print('Unknown SubCmd:',hex(sub_cmd))
                    
        elif CanID == 0x01 and Data[4] == 0x0c:
            print('Cmd:0x00 SubCmd:0x0c')
            r = 0xfe0c
    #    elif Cmd == '0x00':
    #    elif Cmd == '0x00':
        elif CanID == 0x03 and Dlc == 5:
            print('Mfx UID Verify Completed',end=":")
            r = 0x03
        elif CanID == 0x04:
            print('Mfx BIND',end=":")
            r = 0x04
        elif CanID == 0x06:
            print('Mfx Verify',end=":")
            r = 0x06
        elif CanID == 0x08:
            print('Lok Speed',end=":")
            r = 0x08
        elif CanID == 0x0A:
            print('Lok Directin',end=":")
            r = 0x0A
        elif CanID == 0x0C:
#            Debug_Msg += ' Hash:' + hex(Hash) + ' Dlc:' + hex(Dlc) + ' Data:' + hex(Data[0]) 
            Debug_Msg += 'CanID 0x0C Hash:{0:4X} Dlc:{1:02X} Data:{2:02X} {3:02X} {4:02X} {5:02X} {6:02X} {7:02X}'.format(Hash,Dlc,Data[0],Data[1],Data[2],Data[3],Data[4],Data[5])
            r = 0x0C
        elif CanID == 0x0D:
#
            r = 0x0D
        elif CanID == 0x0E:
            print('Read Cfg',end=":")
            r = 0x0E
        elif CanID == 0x0F:
            print('Data Chk')
            r = 0x0F
        elif CanID == 0x22:
            print('S88 Event -> ',end='')
            r = 0x22
        elif CanID == 0x23:
            print('S88 Event? -> ',end='')
            r = 0x23
            
        elif CanID == 0x30 and Dlc == 0:
            print('Ping Request all',hex(CanID),hex(Hash),Dlc)
            r = 0x30
            
        elif CanID == 0x31 and Dlc == 8:
#            Debug_Msg += 'Ping Repr.'
#            print('Ping Repr.')
            print('Ping Anser',hex(CanID),hex(Hash),Dlc,hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]),hex(Data[5]),hex(Data[6]),hex(Data[7]))
            r = 0x31

    #    elif Cmd == '0x00':
    #    elif Cmd == '0x00':
        elif CanID == 0x36 and Dlc == 0:
            print('Bootloader Request?',hex(CanID),hex(Hash),Dlc)
            r = 0x36
        elif CanID == 0x36 and Dlc == 5:
            print('Bootloader ReAnser',hex(CanID),hex(Hash),Dlc,hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]))
            r = 0x36

        elif CanID == 0x37 and Dlc == 8:
            print('Bootloader Anser:',hex(CanID),hex(Hash),Dlc,hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]),hex(Data[5]),hex(Data[6]),hex(Data[7]))
            r = 0x37

        elif CanID == 0x3A and Dlc == 5:
            print('Cmd 0x3A Request:',hex(CanID),hex(Hash),Dlc,hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]))
            r = 0x3A

        elif CanID == 0x3B and Dlc == 8:
            print('Cmd 0x3B Anser:',hex(CanID),hex(Hash),Dlc,hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]),hex(Data[5]),hex(Data[6]),hex(Data[7]))
            r = 0x3B

        elif CanID == 0x77:
            print('Cmd 0x77 Anser:',hex(CanID),hex(Hash),Dlc,hex(Data[0]),hex(Data[1]),hex(Data[2]),hex(Data[3]),hex(Data[4]),hex(Data[5]),hex(Data[6]),hex(Data[7]))
            r = 0x77

        else:
            print('Unknow!!! ',hex(CanID),hex(Hash),Dlc,Data[0],Data[1])

    print(Debug_Msg)
    return r
