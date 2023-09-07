import os

script_path = os.path.dirname(os.path.abspath(__file__))
tools = script_path + '/Tools'

try:
    os.makedirs(tools)
except FileExistsError:
    print("Directory already exists")
except Exception as e:
    print("Failed to create directory - {e}")
