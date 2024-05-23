# main.py

import mymodule
import json

# Introspection
print("Module __dict__:", mymodule.__dict__)

# Dynamic Access
print("Module variable:", mymodule.__dict__['module_var'])
mymodule.__dict__['new_var'] = "New variable added"
print("New variable:", mymodule.new_var)

# Serialization
module_state = json.dumps(mymodule.__dict__)
print("Serialized module state:", module_state)

# Reflection
for name, value in mymodule.__dict__.items():
    if callable(value):
        print(f"Callable {name} found in module")

# Custom Import Mechanism
import sys

def custom_import(name):
    module = sys.modules[name]
    module.__dict__['custom_attr'] = "Custom Attribute"
    return module

mymodule = custom_import('mymodule')
print("Custom attribute:", mymodule.custom_attr)
