import importlib
import pathlib
import os

FUNCTIONS = {}

__functions_dir = os.path.dirname(os.path.realpath(__file__))
for function_file in os.listdir(__functions_dir):
    if not function_file.endswith(".py") or function_file == "__init__.py":
        continue

    print(f"Importing {function_file}...", end=" ")
    funcmod = importlib.import_module("." + os.path.basename(function_file)[:-3], "functions")
    print(f"{len(funcmod.EXPORTED_FUNCTIONS)} function(s) found")
    for func_name in funcmod.EXPORTED_FUNCTIONS:
        FUNCTIONS[func_name] = funcmod.EXPORTED_FUNCTIONS[func_name]
