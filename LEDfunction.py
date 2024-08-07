class LedFunction:
    
    # 문자출력횟수
    def Looptime(self):
        looptimes = ('\x00','\x01','\x02','\x03','\x04',
                 '\x05','\x06','\x07','\x08','\x09',
                 '\x0A')
        for index, i in enumerate(looptimes, start=1):
            print(f"looptimes {index} = '\\x{i.encode().hex()}'")

    # Looptime - 반복 횟수 (23 - 5)

    # times_always = '\x00'
    # times_one = '\x01'
    # times_two = '\x02'
    # times_three = '\x03'
    # times_four = '\x04'
    # times_five = '\x05'
    # times_six = '\x06'
    # times_seven = '\x07'
    # times_eight = '\x08'
    # times_nine = '\x09'
    # times_ten = '\x0A'

    # 문자출력방식
    def Action(self):
        actiones = ('\x01','\x02','\x03','\x04','\x05','\x06',
                  '\x07','\x08','\x09','\x0A','\x0B','\x0C',
                  '\x0D','\x0E','\x0F','\x10','\x11')
        for index, i in enumerate(actiones, start = 1):
            print(f"actioncount {index} = '\\x{i.encode().hex()}'")

    # Action - LED 화면 움직임 (20 - 5)

    # action_hold = '\x01'    고정
    # action_rotate = '\x02'  좌 <ㅡ 우
    # action_rotate_right = '\x03'    좌 ㅡ> 우 (text도 좌에서부터 출력됨)
    # action_shutter = '\x04'     중앙에서부터 사이드로 점차 퍼지면서,,?
    # action_snow = '\x05'    눈 내리듯이 위에서 아래로
    # action_sparkle = '\x06'     반짝반짝 사라졌다가 생김
    # action_triangle = '\x07'    첫 text부터 위에서 아래로 생김
    # action_wide = '\x08'    좌 <ㅡ 우 는 같은데 늘어졌다가 원래 사이즈로?
    # action_roll_left = '\x09'   좌 <ㅡ 우 인데 속도가 빠름
    # action_roll_right ='\x0A'   좌 ㅡ> 우 (text 변경이 되지 않음)
    # action_roll_up = '\x0B'     아래에서 위로 text 올라옴
    # action_roll_down = '\x0C'   위에서 아래로 text 내려감
    # action_wipe_left = '\x0D'   끝 text부터 처음 text까지 순서대로    (한 번 생기고 만다)
    # action_wipe_right = '\x0E'  첫 text부터 끝 text까지 순서대로      (한 번 생기고 만다)
    # action_wipe_down = '\x0F'   text가 상단부터 하단까지
    # action_wipe_up = '\x10'     중앙에서 위아래(동시에)로 text생성
    # action_hold_flash = '\x11'  제자리에서 깜빡임

    # 문자출력속도
    def StrSpeed(self):
        strSpeeds = ('\x00','\x01','\x02','\x03','\x04','\x05')
        print("값이 클수록 속도가 줄어듭니다.")
        for index, i in enumerate(strSpeeds, start = 1):
            print(f"strSpeed {index} = '\\x{i.encode().hex()}'")
    
    # Speed - Action 값에 대한 속도값 (21 - 5)
    
    # speed_fast = '\x00'
    # speed_two = '\x01'
    # speed_three = '\x02'
    # speed_four = '\x03'
    # speed_five = '\x04'
    # speed_six = '\x05'

    # 문자색깔
    def FontColor(self):
        strColors = ('\x00','\x01','\x02','\x03',
                     '\x04','\x05','\x06','\x07')
        for index, i in enumerate(strColors, start = 1):
            print(f"strColor {index} = '\\x{i.encode().hex()}'")

    # Font Color - 글꼴 색 지정 (27 - 5)

    # color_default = '\x00'
    # color_red = '\x01'
    # color_green = '\x02'
    # color_yellow = '\x03'
    # color_blue = '\x04'
    # color_pink = '\x05'
    # color_cyan = '\x06'
    # color_white = '\x07'

# 호출방식
# LedFunction().StrSpeed()