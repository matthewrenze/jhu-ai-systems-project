# Import libraries
import openai
import os
import csv
from datetime import datetime
import re

# Set the file and folder paths
include_module = "all"
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
script_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Scripts"
output_folder_path = root_folder_path + "\\Data\\Predictions\\Intro to Data for Data Science\\GPT-3 In-Sample"
log_file_name = f"gpt-3-in-sample-log.csv"
log_folder_path = root_folder_path + f"\\Data\\Evaluation\\Intro to Data for Data Science\\Logs"
log_file_path = log_folder_path + "\\" + log_file_name

# Set API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Create the model
model_engine = "davinci:ft-personal:script-to-slide-model-all-2023-04-04-19-27-45"
max_tokens = 750
temperature = 0.00
stop_token = "[[END]]"

# Create a function to return the key (module ID and section ID) for a file name
def get_key(file_name):
    prefix = file_name.split(".")[0].split(" - ")[0]
    module_id = prefix.split("-")[0].strip()
    section_id = prefix.split("-")[1].strip()
    return module_id, section_id

# Print initial status
print("Starting GPT-3 predictions ...")

# Create the output folder if it does not exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Create the log folder if it does not exist
if not os.path.exists(os.path.dirname(log_file_path)):
    os.makedirs(os.path.dirname(log_file_path))

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

# Get all scripts with ".txt" extensions in all subfolders
script_file_paths = []
for root, dirs, file_names in os.walk(script_folder_path):
    for file_name in file_names:
        if file_name.endswith(".txt"):
            file_path = script_folder_path + "\\" + file_name
            script_file_paths.append(file_path)

# Use each input script to predict each output slides
for script_file_path in script_file_paths:

    # Get the input file name
    script_file_name = script_file_path.split("\\")[-1]

    # Get the key (module ID and section ID)
    key = get_key(script_file_name)

    # Skip if not the specified module
    if include_module != "all" and key[0] != include_module:
        print(f"Skipping module {key[0]}-{key[1]} ...")
        continue

    # Print status update
    print(f"Predicting slides for {key[0]}-{key[1]} ...")

    # Get the input script for prediction
    with open(script_file_path, "r", encoding="utf-8") as file:
        script = file.read()

    # Create the prompt
    prompt = script + "\n\n[[END]]\n\n"

    try:

        # Get the start time
        start_time = datetime.now()

        # Generate the prediction response
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop_token)

        # Get the response
        output = response.choices[0].text

        # Remove all text before the first slide
        start_token = "---"
        if start_token in output:
            output = output[output.index(start_token):]

        # Remove all text after the "[[END]]" stop token
        # NOTE: This should not be necessary if everything is correct
        if stop_token in output:
            output = output[:output.index(stop_token)]

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
    output_file_name = os.path.basename(script_file_path).replace(".txt", ".md")
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Write the predicted slides to a file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(output)

    # Print status update
    print("Saving slides to " + output_file_name + ".")

# Print final status
print("Finished GPT-3 predictions.")
