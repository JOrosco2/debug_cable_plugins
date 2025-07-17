from plugin_system.base_device import CLIInterface
import serial
import serial.tools.list_ports
import time

plugin_info = {
    "name":"Santec Debug Cable",
    "type":"CLI_Cable",
    "class":"Santec_Debug"
}

class Santec_Debug(CLIInterface):
    @classmethod
    def can_connect(cls):
        ports = serial.tools.list_ports.comports()
        if len(ports) == 1:
            print(f"Found {ports[0].device} - {ports[0].description}")
            conn = serial.Serial(ports[0].device, baudrate=115200,timeout=1)
            return (ports[0].device,conn)
        elif len(ports) > 1:
            print(f"Found the following Serial Devices:")
            for i in ports:
                print(f"{i.device} - {i.description}")
            port = input(f"Which serial port would you like to use (enter name i.e. COM3): ")
            while "COM" not in port:
                port = input(f"ERROR! Please enter one of the ports listed above: ")
                conn = serial.Serial(port,baudrate=115200,timeout=1)
                return(port,conn)
        else:
            return None #No serial ports connected 

    def __init__(self,conn):
        self.conn = conn
   
    def connect(self):
        pass

    def write_reg(self,reg = "", data = ""):
        self.conn.write(("writereg "+reg+" "+data+"\r\n").encode())
        time.sleep(0.1)
        resp = self.conn.read_all().decode(errors="ignore") #deal with echo

    
    """
    Reads a register value, returns the response with the command echo and '$' stripped
    The caller needs to deal with the result (formatting/bit shifting/etc)
    """
    def read_reg(self, reg = ""):
        cmd = "readreg " + reg
        self.conn.write((cmd+"\r\n").encode())
        time.sleep(0.1)
        resp = self.conn.read_all().decode(errors="ignore")
        lines = resp.splitlines()
        #format the response so only the value is given
        clean_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith(cmd) and line.strip() != "$" and line.strip() != "<CLI INITIALIZED>" and line.strip() != f"$ {cmd}"]
        if clean_lines:
            #if tehre is more than 1 value in the response return them all, otherwise just return the single index (not as an array)
            #programs that use this plugin will need to filter through the responses properly
            return clean_lines if len(clean_lines) > 1 else clean_lines[0]
        else:
            return "No data received"

    def read_port(self):
        return self.conn.port

