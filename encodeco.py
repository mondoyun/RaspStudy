# s = "안녕하세요"
# encoded_s = s.encode('utf-8')
# print(encoded_s)
# b = b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'
# decoded_b = b.decode('utf-8')
# print(decoded_b)
txt4 = '안녕하세요 파이썬'.encode('euc-kr')
bytes('안녕', encoding='euc-kr')
bytearray('안녕', encoding='cp949')
print(txt4)
print(bytes)
print(bytearray)

