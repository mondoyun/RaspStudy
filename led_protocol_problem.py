print(__name__)

class ProtocolPacket:
    Head_of_Frame = b'\x7E\x01'
    Screen_ID = b'\xFE\xFE'
    crc = b'\xFF\xFF'
    eof = b'\x7E\x00'

    def packet_start(self, Head_of_Frame, Screen_ID):

        self.Head_of_Frame = Head_of_Frame
        self.Screen_ID = Screen_ID
        return Head_of_Frame + Screen_ID

    def packet_end(self, crc, eof):

        self.crc = crc
        self.eof = eof
        return crc + eof

    def power_ondata(self, Data_length, Cmd_event,Sub_Cmd_ID, len, program_id): 

        Data_length = b'\x00\x0B'
        Cmd_event = b'\x50\x57\x4F\x4E'
        Sub_Cmd_ID = b'\x02'
        len = b'\x00'
        program_id = b'\x00\x00\x00\x00\x00'

        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.program_id = program_id
        return Data_length + Cmd_event + Sub_Cmd_ID + len + program_id
    
    def power_offdata(self, Data_length, Cmd_event, Sub_Cmd_ID, len, program_id): 
        
        Data_length = b'\x00\x0B'
        Cmd_event = b'\x50\x57\x4F\x4E'
        Sub_Cmd_ID = b'\x03'
        len = b'\x00'
        program_id = b'\x00\x00\x00\x00\x00'

        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
        self.program_id = program_id
        return Data_length + Cmd_event + Sub_Cmd_ID + len + program_id
    
    def init_event(self, Data_length, Cmd_event, Sub_Cmd_ID, len, program_id):
        
        Data_length = b'\x00\x08'
        Cmd_event = b'\x45\x56\x45\x4E'
        Sub_Cmd_ID = b'\x01'
        len = b'\x02'
        program_id = b'\x04\x00'

        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
        self.program_id = program_id
        return Data_length + Cmd_event + Sub_Cmd_ID + len + program_id
    
    def send_text(self,Head_of_Frame,Screen_ID,Data_length,Cmd_event,Sub_Cmd_ID,len,crc,eof,):
        # 12(4값고정+8구조고정)+31+4 
        Data = b'\x01\x00\x00\x40\x00\x00\x10{action\x01}{speed\x00}\x00{times\x00}\x01\x00\x00\x01\x00\x01\x00\x02\x00\x68\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64'
        {Head_of_Frame},{Screen_ID},{Data_length},{Cmd_event},{Sub_Cmd_ID},{len\x1F},여기서부터crc전까지31개{},{},{},{action},{},{crc},{eof}
        self.Data = Data
        return Data
    
    def start_windows(self, Data_length, Cmd_event, Sub_Cmd_ID, len, Reserved_Wnd, Reserved):
        
        Data_length = b'\x00\x08'
        Cmd_event = b'\x45\x56\x45\x4E'
        Sub_Cmd_ID = b'\x07'
        len = b'\x02'
        Reserved_Wnd = b'\xFF'
        Reserved = b'\x00'

        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
        self.Reserved_Wnd = Reserved_Wnd
        self.Reserved = Reserved
        return Data_length + Cmd_event + Sub_Cmd_ID + len + Reserved_Wnd + Reserved
        

    
        

    