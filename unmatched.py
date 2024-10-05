import os

def clean_unmatched_files(images_dir, xmls_dir):
    # Get lists of files in both directories
    image_files = set(os.listdir(images_dir))
    xml_files = set(os.listdir(xmls_dir))

    # Extract file names without extensions
    image_file_names = {os.path.splitext(f)[0] for f in image_files}
    xml_file_names = {os.path.splitext(f)[0] for f in xml_files}

    # Find unmatched files
    images_to_delete = image_file_names - xml_file_names
    xmls_to_delete = xml_file_names - image_file_names

    # Delete unmatched image files
    for file_name in images_to_delete:
        file_path = os.path.join(images_dir, file_name + '.jpg')  # Adjust extension as needed
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted unmatched image file: {file_path}")

    # Delete unmatched XML files
    for file_name in xmls_to_delete:
        file_path = os.path.join(xmls_dir, file_name + '.xml')
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted unmatched XML file: {file_path}")

if __name__ == "__main__":
    # Specify your directories here
    images_directory = r'C:\Users\amank\projects\crime-scene-analysis\data\similar_handled_objects\train\images'
    xmls_directory = r'C:\Users\amank\projects\crime-scene-analysis\data\similar_handled_objects\train\xmls'

    # Run the cleanup function
    clean_unmatched_files(images_directory, xmls_directory)
