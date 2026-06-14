import os
from PIL import Image

dataset_path = "../datasets"

print("Checking dataset...")

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        file_path = os.path.join(root, file)

        try:
            with Image.open(file_path) as img:
                img.verify()  # check if valid
        except Exception:
            print(" Removing corrupted:", file_path)
            os.remove(file_path)

print(" Dataset cleaned successfully!")