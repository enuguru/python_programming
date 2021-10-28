
# this program is an example for implmenting polymorphism
# in python
# this progarm creates a list of objects and then calls them
# to find out that the appropriate derived class functions are
# called when called through the base class

class Modem:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def SendData(self):          # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
    def ReceiveData(self):       # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class BroadbandModem(Modem):
    def SendData(self):           
        return 'BroadbandModem sending data'
    def ReceiveData(self):       
        return 'BroadbandModem receiving data'

class WiFiModem(Modem):
    def SendData(self):              
        return 'WiFiModem sending data'
    def ReceiveData(self):          
        return 'WiFiModem receiving data'

class WirelessModem(Modem):
    def SendData(self):              
        return 'WirelessModem sending data'
    def ReceiveData(self):          
        return 'WirelessModem receiving data'

class DialUpModem(Modem):
    def SendData(self):              
        return 'DialUpModem sending data'
    def ReceiveData(self):          
        return 'DialUpModem receiving data'

mymodems = [BroadbandModem('WiFi is HiFi'),
           WiFiModem('Broadband is fast'),
           WirelessModem('Wireless is compact'),
           DialUpModem('DialUpModem is old style')]

print('\n')

for modem in mymodems:
    print(modem.name + ': ' + modem.SendData())
    print(modem.name + ': ' + modem.ReceiveData())
    print('\n')
