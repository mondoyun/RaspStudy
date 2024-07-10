# # 문자열을 바이트로 변환
# byte_data = bytes("안녕하세요", encoding='euc-kr')
# int_data = int.from_bytes(byte_data, byteorder='big')
# byte_length = len(byte_data)
# # Length = 18 + int_data
# # DataLength = 5 + Length
# # print(Length)
# print(byte_data)
# print(int_data)
# print(byte_length)
# # 결과 출력



# # 영어 문자열 정의
# #en_str = "test"
# # 문자열을 \x00 형식으로 변환
# #byte_data = ''.join([f'\\x{ord(char):02x}' for char in en_str])
# # 결과 출력
# #print(byte_data)

# 한글 문자열
<<<<<<< HEAD
koreanSTR = '안녕하세요'
=======
koreanSTR = '공사현장입니다'
>>>>>>> 6092cdeca1a422f3ddfaf1b95f2dcfdd2881bbca

# EUC-KR로 인코딩한 바이트 데이터
encodingByte = koreanSTR.encode('euc-kr')
print("인코딩데이터 : ", encodingByte)
encodingBytelen = len(encodingByte)
print(encodingBytelen)
hex_representation = ' '.join([f'{byte:02X}' for byte in encodingByte])
print(hex_representation)
bytes_representation = ''.join([f'\\x{byte}' for byte in hex_representation.split()])
print(bytes_representation)

<<<<<<< HEAD
byte_data = bytes([28])
print("하이0", byte_data)  
byte_data1 = b'ddddddddddd'
byte_data2 = b'ggggggggggg'
byte_data3 = byte_data1 + byte_data2
byte_data3_len = len(byte_data3)
print("하이1", byte_data3_len)
byte_data3_len1 = bytes([byte_data3_len])
print("하이2", byte_data3_len1)
=======
>>>>>>> 6092cdeca1a422f3ddfaf1b95f2dcfdd2881bbca



