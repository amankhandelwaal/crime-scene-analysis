import os
import xml.etree.ElementTree as ET

# The class we're detecting in the dataset
classes = ["pistol"]  # Only "pistol" for this dataset

def convert(size, box):
    """ Convert box coordinates from VOC to YOLO format """
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(xml_file, output_dir):
    """ Convert a single xml file to YOLO format """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    
    # Output txt file for YOLO
    txt_file = os.path.join(output_dir, os.path.splitext(os.path.basename(xml_file))[0] + '.txt')
    
    with open(txt_file, 'w') as out_file:
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), 
                 float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            out_file.write(f"{cls_id} {' '.join([str(a) for a in bb])}\n")

def convert_dataset(xml_dir, output_dir):
    """ Convert all xml files in a directory """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith(".xml"):
            convert_annotation(os.path.join(xml_dir, xml_file), output_dir)

# Example usage:
# xml_directory = "C:\\Users\\amank\\projects\\crime-scene-analysis\\data\\pistol\\val\\label"  # Replace with actual path to your XML files
# output_directory = "C:\\Users\\amank\\projects\\crime-scene-analysis\\data\\pistol\\val\\labels"  # Replace with path for YOLO txt files
# xml_directory1 = "C:\\Users\\amank\\projects\\crime-scene-analysis\\data\\pistol\\train\\label"  # Replace with actual path to your XML files
# output_directory1 = "C:\\Users\\amank\\projects\\crime-scene-analysis\\data\\pistol\\train\\labels"  
xml_directory2 = r"C:\Users\amank\projects\crime-scene-analysis\data\similar_handled_objects\train\xmls"  # Replace with actual path to your XML files
output_directory2 = r"C:\Users\amank\projects\crime-scene-analysis\data\similar_handled_objects\train\labels"  

# convert_dataset(xml_directory, output_directory)
# convert_dataset(xml_directory1, output_directory1)
convert_dataset(xml_directory2, output_directory2)