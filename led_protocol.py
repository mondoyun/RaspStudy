print(__name__)

class ProtocolPacket:
    def packet_start(self, Head_of_Frame = b'\x7E\x01', Screen_ID = b'\xFE\xFE'):
        return Head_of_Frame + Screen_ID

    def packet_end(self, crc = b'\xFF\xFF', eof = b'\x7E\x00'):
        return crc + eof

    def power_ondata(self, Data_length = b'\x00\x0B', Cmd_event = b'\x50\x57\x4F\x4E',
              Sub_Cmd_ID = b'\x02', len = b'\x00', program_id = b'\x00\x00\x00\x00\x00'): 
        return Data_length + Cmd_event + Sub_Cmd_ID + len + program_id
    
    def power_offdata(self, Data_length = b'\x00\x0B', Cmd_event = b'\x50\x57\x4F\x4E',
              Sub_Cmd_ID = b'\x03', len = b'\x00', program_id = b'\x00\x00\x00\x00\x00'): 
        return Data_length + Cmd_event + Sub_Cmd_ID + len + program_id