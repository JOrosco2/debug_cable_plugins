import pytest
from plugins.santec_calif_debug_cable_plugin import Santec_Debug

port, conn = Santec_Debug.can_connect()
plugin = Santec_Debug(conn)

print(f"Running TEST SANTEC CALIF DEBUG CABLE")

"""
def test_can_connect():
   port = plugin.read_port()
   assert isinstance(port,str)
   print(f"\n***********"+port+"***********\n")

def test_update_sequence():
   get_response()
   update_reg("src.hp.plr","0x0032")
   update_reg("src.hp.save", "0x00")
   get_response()
   update_reg("src.hp.plr","0x0132")
   update_reg("src.hp.save","0x01")
   get_response()
   update_reg("src.hp.plr","0x0091")
   update_reg("src.hp.save","0x00")
   update_reg("src.hp.plr","0x01A1")
   update_reg("src.hp.save","0x01")
   get_response()

def update_reg(reg: str, val: str):
   plugin.write_reg(reg,val)
   
def get_response():  
   resp = plugin.read_reg("src.hp.plr")
   #assert isinstance(resp,str)
   print(f"\nPLR:***********"+resp+"***********\n")
   int_resp = int(resp)
   hex_resp = hex(int_resp)
   bin_resp = bin(int_resp)
   print(f"PLR_HEX:***********"+str(hex_resp)+"***********")
   print(f"PLR_BIN:***********"+str(bin_resp)+"***********")

   ch1_hex_resp = int_resp & 0xFF
   ch2_hex_resp = (int_resp >> 8) & 0xFF
   print(f"PLR_HEX CH1:***********"+str(hex(ch1_hex_resp))+"***********")
   print(f"PLR_HEX CH2:***********"+str(hex(ch2_hex_resp))+"***********")
   print(f"PLR_DEC CH1:***********"+str((ch1_hex_resp))+"***********")
   print(f"PLR_DEC CH2:***********"+str((ch2_hex_resp))+"***********")


   resp = plugin.read_reg("src.hp.vtec")
   print(f"VTEC:***********"+resp+"***********")
   int_resp = int(resp)
   hex_resp = hex(int_resp)
   bin_resp = bin(int_resp)
   print(f"\nVTEC_HEX:***********"+str(hex_resp)+"***********\n")
   print(f"\nVTEC_BIN:***********"+str(bin_resp)+"***********\n")

   ch1_hex_resp = int_resp & 0xFFFF
   ch2_hex_resp = (int_resp >>  16) & 0xFFFF
   print(f"\nVTEC_HEX CH1:***********"+str(hex(ch1_hex_resp))+"***********\n")
   print(f"\nVTEC_HEX CH2:***********"+str(hex(ch2_hex_resp))+"***********\n")
   print(f"\nVTEC_DEC CH1:***********"+str((ch1_hex_resp))+"***********\n")
   print(f"\nVTEC_DEC CH2:***********"+str((ch2_hex_resp))+"***********\n")
"""   

def test_opm_read():
    resp = plugin.read_reg("meas.raw")
    print(resp)
   



    
