import os

try:
    os.makedirs('Tools')
except FileExistsError:
    print("Directory already exists")
except Exception as e:
    print("Failed to create directory - {e}")
