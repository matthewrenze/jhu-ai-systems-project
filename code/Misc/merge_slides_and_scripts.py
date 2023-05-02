# Import libraries
import os

# Set the folder and file paths
exclude_module = "all"
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
script_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Scripts"
slide_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Slides"
output_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Merged"

# Create a function to return the key (module ID and section ID) for a file name
def get_key(file_name):
    prefix = file_name.split(".")[0].split(" - ")[0]
    module_id = prefix.split("-")[0].strip()
    section_id = prefix.split("-")[1].strip()
    return module_id, section_id

# Print an initial status
print("Starting merge of slides and scripts ...")

# Get all slides with ".md" extensions in all subfolders
slides = {}
for root, dirs, file_names in os.walk(slide_folder_path):
    for file_name in file_names:
        if file_name.endswith(".md"):
            key = get_key(file_name)
            file_path = slide_folder_path + "\\" + file_name
            with open(file_path, "r", encoding="utf-8") as file:
                slides[key] = file.read()

# Get all scripts with ".txt" extensions in all subfolders
scripts = {}
for root, dirs, file_names in os.walk(script_folder_path):
    for file_name in file_names:
        if file_name.endswith(".txt"):
            key = get_key(file_name)
            file_path = script_folder_path + "\\" + file_name
            with open(file_path, "r", encoding="utf-8") as file:
                scripts[key] = file.read()

# Create the output folder if it does not exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Loop through the slides and scripts
for key in slides:

    # Print a status update
    print(f"Merging slides and script for {key[0]}-{key[1]} ...")

    # Get the slide and script
    slide = slides[key]
    script = scripts[key]

    # Split the slides and scripts on "---"
    slide_block = slides[key].split("\n---\n")
    script_block = scripts[key].split("\n---\n")

    # If the slides and scripts are not the same length, skip
    if len(slide_block) != len(script_block):
        print(f"Skipping {key[0]}-{key[1]} due to mismatched slide and script lengths.")
        continue

    # Create the output text
    output = ""

    # Loop through the slides and scripts and merge them
    for i in range(len(slide_block)):

        # Handle the first slide
        if i == 0:
            output += slide_block[i].strip()

        # Handle the remaining slides
        else:
            output += "\n" \
                + slide_block[i].strip() \
                + "\n\n<!--\n" \
                + script_block[i].strip() \
                + "\n-->\n"

        if i < len(slide_block) - 1:
            output += "\n---\n"

    # Create the output file name
    output_file_name = f"{key[0]}-{key[1]} - merged.md"

    # Create the output file path
    output_file_path = output_folder_path + "\\" + output_file_name

    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(output)

        # Provide a status update
        print(f"Merged slides and script to {output_file_name}.")

# Provide a final status
print("Finished fine-tuning dataset creation.")