import os

blood_stains_dataset_dir = 'C:/Users/amank/projects/crime-scene-analysis/data/blood_stains'

# New label mappings for blood and bloodstain
label_mappings = {
    '0': '9',  # blood
    '1': '10'  # bloodstain
}

def update_label_file(label_file_path, label_mappings):
    with open(label_file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) > 0:
            if parts[0] in label_mappings:
                parts[0] = label_mappings[parts[0]]  # Update the label based on mapping
            updated_lines.append(' '.join(parts))

    with open(label_file_path, 'w') as file:
        file.writelines('\n'.join(updated_lines) + '\n')


for dataset_type in ['train', 'val', 'test']:
    labels_dir = os.path.join(blood_stains_dataset_dir, dataset_type, 'labels')

    if not os.path.exists(labels_dir):
        print(f"Skipping {dataset_type} as the labels folder does not exist.")
        continue

    for label_file in os.listdir(labels_dir):
        if label_file.endswith('.txt'):
            label_file_path = os.path.join(labels_dir, label_file)
            update_label_file(label_file_path, label_mappings)
            print(f"Updated {label_file} in {dataset_type} dataset.")

print("All blood and bloodstain labels have been successfully updated.")
