"""
The State design pattern.
In Python this is done dynamically by changing the __class__ attribute.
Author : Anand B Pillai <anandpillai@letterboxes.org>
License: Public Domain
Ref: http://harkablog.com/dynamic-state-machines.html
"""

# States of a computer

class ComputerState:
    """ Abstract base class of state of a computer """
    
    name = "state"
    allowed = []
    
    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current:',self,' => switched to new state',state.name) 
            self.__class__ = state
        else:
            print('Current:',self,' => switching to',state.name,'not possible.')

    def __str__(self):
        return self.name
    
class Off(ComputerState):
    """ State being switched off """

    name = "off"
    allowed = ['on']

class On(ComputerState):
    """ State of being powered on and working """

    name = "on"
    allowed = ['off','suspend','hibernate']

class Suspend(ComputerState):
    """ State of being in suspended mode after switched on """

    name = "suspend"
    allowed = ['on']

class Hibernate(ComputerState):
    """ State of being in hibernation after powered on """

    name = "hibernate"
    allowed = ['on']

class Computer:
    """ A class representing a computer """

    def __init__(self, model='HP'):
        self.model = model
        # State of the computer - default is off.
        self.state = Off()

    def change(self, state):
        """ Change state """

        self.state.switch(state)

if __name__ == "__main__":
    comp = Computer()
    # Switch on
    comp.change(On)
    # Switch off
    comp.change(Off)

    # Switch on again
    comp.change(On)
    # Suspend
    comp.change(Suspend)
    # Try to hibernate - cannot!
    comp.change(Hibernate)
    # switch on back
    comp.change(On)
    # Finally off
    comp.change(Off)
