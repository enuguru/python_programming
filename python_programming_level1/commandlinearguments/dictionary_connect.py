import argparse
import os
from collections import ChainMap

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}
print(command_line_args)
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

d = ChainMap(command_line_args, os.environ, defaults)

print(d)
