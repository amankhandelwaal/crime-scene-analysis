import os
import shutil

# Define paths to the directories containing labeled datasets
datasets = {
    'vandalism': 'C:/Users/amank/projects/crime-scene-analysis/data/vandalism',
    'knives': 'C:/Users/amank/projects/crime-scene-analysis/data/knife',
    'pistol': 'C:/Users/amank/projects/crime-scene-analysis/data/pistol',
    'blood_stains': 'C:/Users/amank/projects/crime-scene-analysis/data/blood_stains'
}

# Define the combined dataset directory
combined_data_dir = 'C:/Users/amank/projects/crime-scene-analysis/data/combined_dataset'
os.makedirs(combined_data_dir, exist_ok=True)
os.makedirs(os.path.join(combined_data_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(combined_data_dir, 'labels'), exist_ok=True)

# Define the final class map
class_map = {
    0: 'destroying_things',
    1: 'hammer',
    2: 'bike',
    3: 'car',
    4: 'person',
    5: 'breaking_the_door',
    6: 'criminal',
    7: 'knives',
    8: 'pistol',
    9: 'blood',
    10: 'bloodstain'
}

# Function to copy and update labels
def update_and_copy_files(source_dir, dataset_type, class_offset):
    images_dir = os.path.join(source_dir, dataset_type, 'images')
    labels_dir = os.path.join(source_dir, dataset_type, 'labels')

    if not os.path.exists(images_dir) or not os.path.exists(labels_dir):
        print(f"Skipping {dataset_type} in {source_dir} as the folders do not exist.")
        return

    for filename in os.listdir(images_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Copy image file
            new_filename = f"{dataset_type}_{filename}"
            shutil.copy(os.path.join(images_dir, filename), os.path.join(combined_data_dir, 'images', new_filename))
            
            # Copy and update label file
            label_file = filename.rsplit('.', 1)[0] + '.txt'
            if os.path.exists(os.path.join(labels_dir, label_file)):
                with open(os.path.join(labels_dir, label_file), 'r') as file:
                    lines = file.readlines()

                updated_lines = []
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) > 0 and parts[0].isdigit():
                        # Update the class index by adding the class_offset
                        new_class_index = int(parts[0]) + class_offset
                        parts[0] = str(new_class_index)
                        updated_lines.append(' '.join(parts))

                # Save the updated label file
                if updated_lines:
                    with open(os.path.join(combined_data_dir, 'labels', new_filename.rsplit('.', 1)[0] + '.txt'), 'w') as file:
                        file.writelines('\n'.join(updated_lines) + '\n')

# Process each dataset
class_offsets = {
    'vandalism': 0,         # vandalism classes start at 0
    'knives': 7,            # knives class starts at 7
    'pistol': 8,            # pistol class starts at 8
    'blood_stains': 9       # blood_stains classes start at 9
}

for dataset_name, dataset_dir in datasets.items():
    print(f"Processing {dataset_name} dataset...")
    for dataset_type in ['train', 'val', 'test']:
        update_and_copy_files(dataset_dir, dataset_type, class_offsets[dataset_name])

# Save the class map for future reference
with open(os.path.join(combined_data_dir, 'class_map.txt'), 'w') as f:
    for class_index, class_name in class_map.items():
        f.write(f"{class_index}: {class_name}\n")

print("All datasets have been successfully combined into a single dataset.")
