# Import libraries
import os
import csv
import openai
import re
from datetime import datetime

# Set the file and folder paths
version_number = "4"
model_engine = "gpt-4" if version_number == "4" else "gpt-3.5-turbo"
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
system_prompt_file_path = root_folder_path + f"\\Data\\Training\\Intro to Data for Data Science\\GPT-{version_number}\\system-prompt.txt"
example_script_folder_path = root_folder_path + f"\\Data\\Training\\Intro to Data for Data Science\\GPT-{version_number}\\Examples\\Scripts"
example_slide_folder_path = root_folder_path + f"\\Data\\Training\\Intro to Data for Data Science\\GPT-{version_number}\\Examples\\Slides"
input_script_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Scripts"
output_slide_folder_path = root_folder_path + f"\\Data\\Predictions\\Intro to Data for Data Science\\GPT-{version_number} In-Sample"
log_file_name = f"gpt-{version_number}-in-sample-log.csv"
log_folder_path = root_folder_path + f"\\Data\\Evaluation\\Intro to Data for Data Science\\Logs"
log_file_path = log_folder_path + "\\" + log_file_name

# Set API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Create the model
max_tokens = 350
temperature = 0.00

# Create a function to return the key (module ID and section ID) for a file name
def get_key(file_name):
    prefix = file_name.split(".")[0].split(" - ")[0]
    module_id = prefix.split("-")[0].strip()
    section_id = prefix.split("-")[1].strip()
    return module_id, section_id

# Print initial status
print(f"Starting GPT-{version_number} predictions ...")

# Create the output folder if it does not exist
if not os.path.exists(output_slide_folder_path):
    os.makedirs(output_slide_folder_path)

# Create the log folder if it does not exist
if not os.path.exists(os.path.dirname(log_file_path)):
    os.makedirs(os.path.dirname(log_file_path))

# Get all example scripts with ".txt" extensions in all subfolders
example_scripts_map = {}
for root, dirs, file_names in os.walk(example_script_folder_path):
    for file_name in file_names:
        if file_name.endswith(".txt"):
            key = get_key(file_name)
            file_path = example_script_folder_path + "\\" + file_name
            example_scripts_map[key] = file_path

# Get all example slides with ".md" extensions in all subfolders
example_slides_map = {}
for root, dirs, file_names in os.walk(example_slide_folder_path):
    for file_name in file_names:
        if file_name.endswith(".md"):
            key = get_key(file_name)
            file_path = example_slide_folder_path + "\\" + file_name
            example_slides_map[key] = file_path

# Create the chat messages
header_messages = []

# Get the system prompt
with open(system_prompt_file_path, "r", encoding="utf-8") as file:
    system_prompt = file.read()

# Create the system message
system_message = {"role": "system", "content": system_prompt}

# Add the system message to the messages
header_messages.append(system_message)

# Create examples from script-slide pairs
for key in example_scripts_map:

    # Print a status update
    print(f"Creating example for {key[0]}-{key[1]} ...")

    # Get the script and slide file paths
    example_script_file_path = example_scripts_map[key]
    example_slides_file_path = example_slides_map[key]

    # Read the script file
    with open(example_script_file_path, "r", encoding="utf-8") as file:
        example_script = file.read()

    # Read the slide file
    with open(example_slides_file_path, "r", encoding="utf-8") as file:
        example_slides = file.read()

    # Split the presentations into slides
    example_script_slide_count = example_script.split("\n---\n")
    example_slides_slide_count = example_slides.split("\n---\n")

    # Check that the number of slides is the same
    if len(example_script_slide_count) != len(example_slides_slide_count):
        raise Exception(f"Number of slides in example script and slides do not match for {key[0]}-{key[1]}.")

    # Create the example user-assistant message pair
    user_message = {"role": "user", "content": example_script}
    assistant_message = {"role": "assistant", "content": example_slides}

    # Add the user-assistant message pair to the messages
    header_messages.append(user_message)
    header_messages.append(assistant_message)

    # Provide a status update
    print(f"Created example for {key[0]}-{key[1]}.")

# Create a CSV header for the log file
log_header = [
    "Date-Time",
    "Module ID",
    "Section ID",
    "Prompt Tokens",
    "Completion Tokens",
    "Total Tokens",
    "Start Date-Time",
    "End Date-Time",
    "Duration (s)",
    "Input Script",
    "Output Slides",
    "Error Message"]

# Write the header to the log file
with open(log_file_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(log_header)

# Get all input scripts with ".txt" extensions in all subfolders
input_scripts_map = {}
for root, dirs, file_names in os.walk(input_script_folder_path):
    for file_name in file_names:
        if file_name.endswith(".txt"):
            key = get_key(file_name)
            file_path = input_script_folder_path + "\\" + file_name
            input_scripts_map[key] = file_path

# Use each input script to predict each output slides
for key in input_scripts_map:

    # # DEBUG: DELETE ME
    if not(key[0] == "X" and key[1] == "X"):
        print(f"DEBUG: Skipping prediction for {key[0]}-{key[1]} ...")
        continue

    # Print status update
    print(f"Predicting slides for {key[0]}-{key[1]} ...")

    # Get the script file path
    input_script_file_path = input_scripts_map[key]

    # Get the input script for prediction
    with open(input_script_file_path, "r", encoding="utf-8") as file:
        script = file.read()

    # Create the messages
    messages = header_messages.copy()

    # Create the user message
    user_message = {"role": "user", "content": script}

    # Add the user message to the messages
    messages.append(user_message)

    try:

        # Get the start time
        start_time = datetime.now()

        # Generate the prediction response
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature)

        # Get the response
        output = response.choices[0].message.content

        # Get the end time
        end_time = datetime.now()

        # Get the duration
        duration = end_time - start_time

        # Print the usage
        print(f"Usage:")
        print(f"Prompt: {response.usage['prompt_tokens']}")
        print(f"Completion: {response.usage['completion_tokens']}")
        print(f"Total: {response.usage['total_tokens']}")

        # Create the log row
        log_row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            key[0],
            key[1],
            response.usage["prompt_tokens"],
            response.usage["completion_tokens"],
            response.usage["total_tokens"],
            start_time.strftime("%Y-%m-%d %H:%M:%S"),
            end_time.strftime("%Y-%m-%d %H:%M:%S"),
            duration.total_seconds(),
            script,
            output,
            ""]

        # Write the log row to the log file
        with open(log_file_path, "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(log_row)

    except Exception as ex:

        # Get the total number of requested tokens
        numbers = re.findall(r'\d+', ex.args[0])
        total_tokens = numbers[1]

        # Create the log row
        log_row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            key[0],
            key[1],
            "",
            "",
            total_tokens,
            start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "",
            "",
            script,
            "",
            ex]

        # Write the log row to the log file
        with open(log_file_path, "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(log_row)

        # Print the error
        print(f"ERROR: {ex}")
        continue

    # Get the output file path
    script_file_name = input_script_file_path.split("\\")[-1]
    output_file_name = script_file_name.replace("script.txt", "slides.md")
    output_file_path = os.path.join(output_slide_folder_path, output_file_name)

    # Write the predicted slides to a file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(output)

    # Print status update
    print("Saving slides to " + output_file_name + ".")

# Print final status
print(f"Finished GPT-{version_number} predictions.")
