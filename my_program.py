import sys
from pathlib import Path

script_dir = Path(__file__).parent
local_lib_path = script_dir / "local_lib"
sys.path.insert(0, str(local_lib_path))

from path import Path as PathPie

print("=== Python Program Executing ===")
print("The 'path' module was successfully loaded from the 'local_lib' folder.")

test_obj = PathPie("sample_output_directory")
print(f"Intuitive wrapper verification -> Object created: {repr(test_obj)}")
