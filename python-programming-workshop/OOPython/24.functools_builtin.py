
import types
import functools
builtin_functions = [obj for name, obj in vars(builtins).items()
                     if isinstance(obj, types.BuiltinFunctionType(functools)]
print("The builtin functions in python are\n")
print(dir(builtin_functions),end="  ")
print("\n\n")
