import os
import shutil
# Define the old class names in the vandalism dataset
old_classes = [
    'destroying_things', 'hammer', 'pushing_bike', 'bin', 'dashing_the_fence',
    'store', 'trafficlights', 'dashing_fence', 'scratching_the_car', 'bike',
    'hitting_the_side_window', 'car', 'person', 'street', 'breaking_the_door',
    'fallen_bike', 'crime', 'criminal', 'hitting_the_door', 'fence'
]

# Define the new class map with only the necessary classes
new_class_map = {
    'destroying_things': 0,
    'hammer': 1,
    'bike': 2,
    'car': 3,
    'person': 4,
    'breaking_the_door': 5,
    'criminal': 6
}

# Paths to the directories containing labeled datasets
source_dir = 'C:/Users/amank/projects/crime-scene-analysis/data/vandalism'
combined_data_dir = 'C:/Users/amank/projects/crime-scene-analysis/data/vandalism_modified'
os.makedirs(os.path.join(combined_data_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(combined_data_dir, 'labels'), exist_ok=True)

# Function to update labels based on the new class map
def update_label_file(label_lines):
    updated_lines = []
    for line in label_lines:
        parts = line.strip().split()
        if len(parts) > 0:
            old_class_index = int(parts[0])
            # Map old class to new class index if it's in the new map
            old_class_name = old_classes[old_class_index]
            if old_class_name in new_class_map:
                new_class_index = new_class_map[old_class_name]
                parts[0] = str(new_class_index)
                updated_lines.append(' '.join(parts))
    return updated_lines

# Process each dataset directory and update labels accordingly
def process_directory(source_dir):
    for dataset_type in ['train', 'val', 'test']:
        images_dir = os.path.join(source_dir, dataset_type, 'images')
        labels_dir = os.path.join(source_dir, dataset_type, 'labels')

        if not os.path.exists(images_dir) or not os.path.exists(labels_dir):
            print(f"Skipping {dataset_type} in {source_dir} as the folders do not exist.")
            continue

        for filename in os.listdir(images_dir):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                # Move image file
                new_filename = f"{dataset_type}_{filename}"
                shutil.copy(os.path.join(images_dir, filename), os.path.join(combined_data_dir, 'images', new_filename))
                
                # Move and update label file
                label_file = filename.rsplit('.', 1)[0] + '.txt'
                if os.path.exists(os.path.join(labels_dir, label_file)):
                    with open(os.path.join(labels_dir, label_file), 'r') as file:
                        lines = file.readlines()

                    # Update the label file based on the new class index
                    updated_lines = update_label_file(lines)
                    
                    # Save the updated label file
                    if updated_lines:
                        with open(os.path.join(combined_data_dir, 'labels', new_filename.rsplit('.', 1)[0] + '.txt'), 'w') as file:
                            file.writelines(updated_lines)

# Process the vandalism directory
print("Processing vandalism dataset...")
process_directory(source_dir)

# Save the new class map for future reference
with open(os.path.join(combined_data_dir, 'class_map.txt'), 'w') as f:
    for class_name, class_index in new_class_map.items():
        f.write(f"{class_index}: {class_name}\n")

print("Vandalism dataset has been successfully processed and labels updated.")
