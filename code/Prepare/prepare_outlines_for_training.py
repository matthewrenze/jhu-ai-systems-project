# Import libraries
import re
import os

# Open the markdown file
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
input_folder_path = root_folder_path + "\\Data\\Source\\Intro to Data for Data Science"
output_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Outlines\\"

# Print initial status
print("Beginning outline preparation ...")

# Get all files with ".md" extensions in all subfolders
input_file_paths = []
for root, dirs, file_names in os.walk(input_folder_path):
    for file_name in file_names:
        if file_name.endswith(".md"):
            input_file_paths.append(os.path.join(root, file_name))

# Create output folder if it does not exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Prepare each script for training
for input_file_path in input_file_paths:

    # Print status update
    print("Preparing outline " + input_file_path + " ...")

    # Read the input markdown file
    with open(input_file_path, "r", encoding="utf-8") as f:
        input = f.read()

    # Split markdown into slides
    slides = input.split("\n---\n")

    # Create loop variables
    output = ""
    skip = False

    # Extract the outline from the slides
    for slide in slides:
        lines = slide.split("\n")
        for line in lines:

            # Skip the first slide
            if slides.index(slide) == 0:
                continue

            # Skip empty line
            if line == "":
                continue

            # Skip MARP directives
            if re.match(r"^<!--.*-->$", line):
                continue

            # Skip images
            if re.match(r"^!\[.*\]\(.*\)$", line):
                continue

            # Skip tables
            if re.match(r"^\|", line):
                continue

            # Skip notes
            if line == "<!--":
                skip = True
                continue
            elif line == "-->":
                skip = False
                continue

            if skip:
                continue

            # Add title as level 0
            if slides.index(slide) == 1:
                if re.match(r"^#.*", line):
                    line = line.replace("# ", "")
                    output += line + "\n"
                    continue

            # Add headings as level 1
            if re.match(r"^#.*", line):
                line = line.replace("# ", "")
                output += " - " + line + "\n"

            # Add text as level 2
            else:
                output += "   - " + line + "\n"

    # Create the output file name
    parent_folder_name = os.path.basename(os.path.dirname(input_file_path))
    input_file_name = os.path.basename(input_file_path)
    output_file_name = parent_folder_name[0] + "-" + input_file_name[0] + " - outline.txt"

    # Create output file path
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Save the outline to a file
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(output)

    # Print status update
    print("Saved outline to " + output_file_name)

# Print final status
print("Outline preparation complete.")