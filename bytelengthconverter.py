# 이벤트 전송 메세지
DataLength = b'\x00\x2B' # 가변 데이터 # 5,6
CmdEvent = b'\x45\x56\x45\x4E' # 7,8,9,10
SubCmdID = b'\x06' # 이벤트 메세지 전송 # 11
Length = b'\x28'# 가변 데이터 # 12
Windows_Number = b'\x01' # 13
X_POSITION = b'\x00\x00' # 14, 15
W_WIDTH_PIXELS = b'\x40\x00' # 16, 17
Y_POSITION = b'\x00' # 18
H_HEIGHT_PIXELS = b'\x10' # 19
Action = b'\x02' #20
Speed = b'\x00'#21
StaySeconds = b'\x00' #22
LoopTimes = b'\x03' #23
MemoryPosition = b'\x01' #24
MultiLinesDisp = b'\x00' #25
Align = b'\x00' # 26
fontColor = b'\x01' # 가변 데이터 #27
ReservedFontMode = b'\x00' #28
FontAscii = b'\x01\x00' #29
FontAsian = b'\x02\x00' #30 
InputFixData = b'\x5B\x46\x54\x35\x30\x31\x5D' #31
UserInputData = b'\xbe\xee\xb6\xbb\xb0\xd4\xc7\xd4\xbc\xf6\xb8\xa6\xbf\xac\xb0\xe1\xc7\xd2\xb1\xee' #32
sendTexts = (Windows_Number+X_POSITION+W_WIDTH_PIXELS+Y_POSITION+H_HEIGHT_PIXELS+Action+Speed+StaySeconds+
            LoopTimes+MemoryPosition+MultiLinesDisp+Align+fontColor+ReservedFontMode+FontAscii+FontAsian)

DataLength = CmdEvent + SubCmdID + Length + sendTexts + InputFixData + UserInputData
num2 = len(DataLength)
print("이것의 길이 : ",num2)
numB = num2
byte2 = numB.to_bytes(2, byteorder='big')
formatted2 = ''.join(f'\\x{byte:02x}' for byte in byte2)
print("DataLength 값 : ", formatted2)
print()
num = sendTexts + InputFixData + UserInputData
num1 = len(sendTexts + InputFixData + UserInputData)
print("이것의 길이 : ",num1)
numA = num1
byte1 = numA.to_bytes(1, byteorder='big')
formatted1 = ''.join(f'\\x{byte:02x}' for byte in byte1)
print("Length 값 : ", formatted1)

