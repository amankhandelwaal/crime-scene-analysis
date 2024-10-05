import os

paths = [
    'C:/Users/amank/projects/crime-scene-analysis/data/vandalism/train/images',
    'C:/Users/amank/projects/crime-scene-analysis/data/vandalism/val/images',
    'C:/Users/amank/projects/crime-scene-analysis/data/vandalism/test/images'
]

for path in paths:
    if not os.path.exists(path):
        print(f"Directory does not exist: {path}")
    else:
        print(f"Directory exists: {path}")
