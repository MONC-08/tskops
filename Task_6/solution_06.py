import os
import shutil

source_file = "app.log"

#  check if the source file exists
if os.path.exists(source_file):
    
    for i in range(1, 6):
        new_file = f"app_{i}.log"
        shutil.copy(source_file, new_file)
        print(f"Created: {new_file}")

else:
    print("app.log not found")
