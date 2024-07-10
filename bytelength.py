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
hangul_str = '안녕하세요'

# EUC-KR로 인코딩한 바이트 데이터
encoded_bytes = hangul_str.encode('euc-kr')

# 바이트 데이터와 더하기
original_bytes = b'Some bytes data '
result_bytes = original_bytes + encoded_bytes

# 결과의 길이
result_length = len(result_bytes)

# 바이트 데이터의 hex 값으로 표시
hex_representation = ' '.join([f'{byte:02X}' for byte in result_bytes])

# 결과 출력
print(f"Result length: {result_length} bytes")
print(f"Hex representation: {hex_representation}")


