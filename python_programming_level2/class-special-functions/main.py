# main.py

import mymodule

# Accessing the module's __dict__
module_dict = mymodule.__dict__

# Print the module dictionary
for key, value in module_dict.items():
    print(f"{key}: {value}")
