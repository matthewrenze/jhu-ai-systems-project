# Import libraries
import re
import os

# Open the markdown file
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
input_folder_path = root_folder_path + "\\Data\\Source\\Intro to Data for Data Science"
output_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Presentations\\"

# Print initial status
print("Beginning slide preparation ...")

# Get all files with ".md" extensions in all subfolders
input_file_paths = []
for root, dirs, file_names in os.walk(input_folder_path):
    for file_name in file_names:
        if file_name.endswith(".md"):
            input_file_paths.append(os.path.join(root, file_name))

# Create output folder if it does not exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Prepare each slide for training
for input_file_path in input_file_paths:

    # Print status update
    print("Preparing slides " + input_file_path + " ...")

    # Read the input markdown file
    with open(input_file_path, "r", encoding="utf-8") as f:
        input = f.read()

    # Replace "(images/...)" with "(images/placeholder.png)"
    image_regex = re.compile(r"\(images/.*\)")
    output = image_regex.sub("(images/placeholder.png)", input)

    # Clean the animation directives
    animation_regex = r"\[(X|\d+(-|\s*)\d*)\] "
    output = re.sub(animation_regex, "", output)

    # Create the output file name
    parent_folder_name = os.path.basename(os.path.dirname(input_file_path))
    input_file_name = os.path.basename(input_file_path)
    output_file_name = parent_folder_name[0] + "-" + input_file_name[0] + " - presentation.md"

    # Create output file path
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Save the notes to a file
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(output)

    # Print status update
    print("Saved slides to " + output_file_name)

# Print final status
print("Slide preparation complete.")