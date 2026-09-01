
import sys
from  pathlib import Path

print("=== Python Program Executing ===")

sys.path.insert(0, str(Path(__file__).parent / "local_lib"))

from path import Path as p 

print("The 'path' module was successfully loaded from the 'local_lib' folder.")



path_obj = p("folder")

path_obj.mkdir_p()

new_file = path_obj / "file.txt"

new_file.touch()

new_file.write_text("Text written from the python file", encoding='utf-8')

content = new_file.read_text(encoding='utf-8')

print(f"\nContent: {content}")

