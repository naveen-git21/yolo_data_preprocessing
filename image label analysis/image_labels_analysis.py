"""
    This script is beneficial during the data preprocessing stage of projects involving object detection,
    especially when using YOLO. By comparing the contents of image and label folders, 
    it helps identify missing files,
    thus ensuring data consistency and avoiding errors during model training.
"""
import os

def list_filenames(directory):
    """
    Function to list filenames (without extensions) in a directory
    """
    filenames = []
    for root, _, files in os.walk(directory):
        for file in files:
            filename, _ = os.path.splitext(file)
            filenames.append(filename)
    return filenames

def compare_folders(folder1, folder2):
    """
    Function to compare filenames (without extensions) in two folders
    """
    filenames1 = set(list_filenames(folder1))
    filenames2 = set(list_filenames(folder2))
    
    missing_filenames1 = filenames2 - filenames1
    missing_filenames2 = filenames1 - filenames2
    
    num_files1 = len(filenames1)
    num_files2 = len(filenames2)
    
    """print("Total number of files in", folder1, ":", num_files1)
    print("Total number of files in", folder2, ":", num_files2)"""

    if not missing_filenames1 and not missing_filenames2:
        print("Folders are identical.")
    else:
        if missing_filenames1:
            print("Filenames missing in", folder1, ":", missing_filenames1)
        if missing_filenames2:
            print("Filenames missing in", folder2, ":", missing_filenames2)

# Paths to the folders containing images and labels
image_folder = "C:\\Users\\warri\\OneDrive\\Desktop\\ML_project\\uzi\\images"
label_folder = "C:\\Users\\warri\\OneDrive\\Desktop\\ML_project\\uzi\\labels"
# Count the number of files in each folder
num_files_image_folder = len(os.listdir(image_folder))
num_files_label_folder = len(os.listdir(label_folder))

# Print the number of files in each folder
print("Total number of files in", image_folder, ":", num_files_image_folder)
print("Total number of files in", label_folder, ":", num_files_label_folder)

# Compare the folders
compare_folders(image_folder, label_folder)
