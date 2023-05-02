# Import libraries
import re
import os

# Open the markdown file
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project\\"
input_folder_path = root_folder_path + "\\Data\\Source\\Intro to Data for Data Science"
output_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Scripts\\"

# Print initial status
print("Beginning script preparation ...")

# Get all files with ".md" extensions in the input folder
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
    print("Preparing script " + input_file_path + " ...")

    # Get the titles for the script header
    course_title = os.path.basename(input_folder_path)
    module_title = os.path.basename(os.path.dirname(input_file_path))
    presentation_title = os.path.basename(input_file_path).replace(".md", "")

    # Create the script header
    output = "---\n"
    output += f"course: {course_title}\n"
    output += f"module: {module_title}\n"
    output += f"title: {presentation_title}"

    # Read the input markdown file
    with open(input_file_path, "r", encoding="utf-8") as f:
        input = f.read()

    # Split markdown into slides
    slides = input.split("\n---\n")

    # Extract the notes from the slides
    for slide in slides:

        # Get all notes
        notes_regex = re.compile(r"<!--\n([\s\S]+?)\n-->")
        notes_matches = notes_regex.findall(slide)
        notes = "".join(notes_matches).strip()

        # Clean the animation directives
        animation_regex = r"\[(X|\d+(-|\s*)\d*)\] "
        notes = re.sub(animation_regex, "", notes)

        # Clean the leading spaces
        leading_space_regex = r"^\s+"
        notes = re.sub(leading_space_regex, "", notes)

        # Replace special characters
        notes = notes.replace("\x0b", "\n") \
            .replace("’", "'") \
            .replace("“", "\"") \
            .replace("”", "\"") \
            .replace("…", "...") \
            .replace("–", "-") \
            .replace("✔", "x")
        notes = notes.strip()

        # Add the notes to the output
        output += notes

        # Add a separator between slides except for the last slide
        if slide != slides[-1]:
            output += "\n\n---\n\n"

    # Create the output file name
    parent_folder_name = os.path.basename(os.path.dirname(input_file_path))
    input_file_name = os.path.basename(input_file_path)
    output_file_name = parent_folder_name[0] + "-" + input_file_name[0] + " - script.txt"

    # Create output file path
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Save the notes to a file
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(output)

    # Print status update
    print("Saved script to " + output_file_name)

# Print final status
print("Script preparation complete.")