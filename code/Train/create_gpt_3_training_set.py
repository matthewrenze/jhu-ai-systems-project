# Import libraries
import os
import json

# Set the folder and file paths
exclude_module = "all"
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
script_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Scripts"
slide_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Slides"
output_file_name = f"script-to-slide-model-{exclude_module}.json"
output_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\GPT-3"
output_file_path = output_folder_path + "\\" + output_file_name

# Create a function to return the key (module ID and section ID) for a file name
def get_key(file_name):
    prefix = file_name.split(".")[0].split(" - ")[0]
    module_id = prefix.split("-")[0].strip()
    section_id = prefix.split("-")[1].strip()
    return module_id, section_id

# Print an initial status
print("Starting fine-tuning training set creation ...")

# Get all scripts with ".txt" extensions in all subfolders
scripts_map = {}
for root, dirs, file_names in os.walk(script_folder_path):
    for file_name in file_names:
        if file_name.endswith(".txt"):
            key = get_key(file_name)
            file_path = script_folder_path + "\\" + file_name
            scripts_map[key] = file_path

# Get all slides with ".md" extensions in all subfolders
slides_map = {}
for root, dirs, file_names in os.walk(slide_folder_path):
    for file_name in file_names:
        if file_name.endswith(".md"):
            key = get_key(file_name)
            file_path = slide_folder_path + "\\" + file_name
            slides_map[key] = file_path

# Create the output text
output = ""

for key in scripts_map:

    if key[0] == exclude_module:
        print(f"Skipping module {key[0]}-{key[1]} ...")
        continue

    # Print a status update
    print(f"Creating fine-tuning prompt and completion for {key[0]}-{key[1]} ...")

    # Get the script and slide file paths
    script_file_path = scripts_map[key]
    slide_file_path = slides_map[key]

    # Read the script file
    with open(script_file_path, "r", encoding="utf-8") as file:
        script = file.read()

    # Read the slide file
    with open(slide_file_path, "r", encoding="utf-8") as file:
        slides = file.read()

    # Split the presentations into slides
    script_slide_count = script.split("\n---\n")
    slides_slide_count = slides.split("\n---\n")

    # Check that the number of slides is the same
    if len(script_slide_count) != len(slides_slide_count):
        raise Exception(f"Number of slides in example script and slides do not match for {key[0]}-{key[1]}.")

    # Replace the script in the prompt
    prompt = script + "\n\n[[END]]\n\n"

    # Replace the slide in the prompt
    # Note: Need to prefix with a space and end with two newlines
    completion = " \n" + slides + "\n\n[[END]]\n\n"

    # Create the prompt and completion JSON
    prompt_json = {"prompt": prompt, "completion": completion}

    output += json.dumps(prompt_json) + "\n"

    # Provide a status update
    print(f"Created fine-tuning prompt and completion for {key[0]}-{key[1]}.")

with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(output)

# Provide a final status
print("Finished fine-tuning training set creation.")

