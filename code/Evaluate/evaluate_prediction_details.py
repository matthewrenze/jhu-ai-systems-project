# Import libraries
import re
import os
import csv
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set the folder and file paths
version_number = "3"
results_id = f"gpt-{version_number}-in-sample"
predicted_folder_name = f"GPT-{version_number} In-Sample"
output_file_name = results_id + " (details).csv"
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
predicted_folder_path = root_folder_path + "\\Data\\Predictions\\Intro to Data for Data Science\\" + predicted_folder_name
actual_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Slides"
script_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Scripts"
output_folder_path = root_folder_path + "\\Data\\Evaluation\\Intro to Data for Data Science\\Details"
output_file_path = output_folder_path + "\\" + output_file_name

# Create a function to return the key (module ID and section ID) for a file name
def get_key(file_name):
    prefix = file_name.split(".")[0].split(" - ")[0]
    module_id = prefix.split("-")[0].strip()
    section_id = prefix.split("-")[1].strip()
    return module_id, section_id

# Create a function to count the number of slides
def count_slides(text):
    return len(re.findall(r"---", text, flags=re.MULTILINE))

def get_slide(slide):
    return slide

def get_header(slide):
    return slide

def get_class(slide):
    match = re.search(r"<!-- _class: ([a-zA-Z0-9-]+) -->", slide)
    if match is None:
        return None
    return match.group(1)

def get_title(slide):
    match = re.search(r"^# (.*)", slide, flags=re.MULTILINE)
    if match is None:
        return None
    return match.group(1)

def get_body(slide):
    body = ""
    skip = False
    lines = slide.split("\n")
    for line in lines:

        # Skip empty line
        if line == "":
            continue

        # Skip MARP header
        if line.startswith("marp: true") \
                or line.startswith("title: ") \
                or line.startswith("theme: "):
            continue

        # Skip MARP directives
        if re.match(r"^<!--.*-->$", line):
            continue

        # Skip title
        if re.match(r"^# .+$", line):
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

        body += line + "\n"

    return body

def get_image_alt_text(slide):
    image_regex = re.compile(r"(!\[.*\]\(.*\))")
    image_matches = image_regex.findall(slide)
    images = "".join(image_matches).strip()
    return images

def get_footer(slide):
    match = re.search(r"<!-- _footer: ([a-zA-Z0-9-]+) -->", slide, flags=re.MULTILINE)
    if match is None:
        return None
    return match.group(1)

def get_notes(slide):
    notes_regex = re.compile(r"<!--\n([\s\S]+?)\n-->")
    notes_matches = notes_regex.findall(slide)
    notes = "".join(notes_matches).strip()
    return notes

# Create a function to compute the BLEU score
def get_bleu_score(predicted, reference):
    # Tokenize the sentences
    predicted_tokens = predicted.split()
    reference_tokens = reference.split()

    # Create a smoothing function
    smoothing = SmoothingFunction().method1

    # Calculate the BLEU score
    bleu_score = sentence_bleu(
        [reference_tokens],
        predicted_tokens,
        smoothing_function=smoothing,
        weights=(0.60, 0.30, 0.20, 0.10))

    return bleu_score

def get_rouge_scores(predicted, reference):

    # Create a scorer
    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"],
        use_stemmer=True)

    # Calculate the scores
    scores = scorer.score(reference, predicted)

    return scores

def get_similarity_score(predicted, reference):

    # Create a vectorizer
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer to the texts
    tfidf_matrix = vectorizer.fit_transform([predicted, reference])

    # Calculate the cosine similarity
    similarity_score = cosine_similarity(tfidf_matrix)

    return similarity_score[0][1]

# Print initial status
print("Starting presentation evaluations ...")

# Get all predicted presentations
predicted_presentations = {}
for root, dirs, file_names in os.walk(predicted_folder_path):
    for file_name in file_names:
        if file_name.endswith(".md"):
            key = get_key(file_name)
            file_path = predicted_folder_path + "\\" + file_name
            with open(file_path, "r", encoding="utf-8") as file:
                predicted_presentations[key] = file.read()

# Get all actual (ground-truth) presentations
reference_presentations = {}
for root, dirs, file_names in os.walk(actual_folder_path):
    for file_name in file_names:
        if file_name.endswith(".md"):
            key = get_key(file_name)
            file_path = actual_folder_path + "\\" + file_name
            with open(file_path, "r", encoding="utf-8") as file:
                reference_presentations[key] = file.read()

# Get the scripts
scripts = {}
for root, dirs, file_names in os.walk(script_folder_path):
    for file_name in file_names:
        if file_name.endswith(".txt"):
            key = get_key(file_name)
            file_path = script_folder_path + "\\" + file_name
            with open(file_path, "r", encoding="utf-8") as file:
                scripts[key] = file.read()

# Create output folder if it does not exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

output_header = [
    "Results ID",
    "Module ID",
    "Section ID",
    "Slide ID",
    "Element Name",
    "BLEU Score",
    "ROUGE-1 f-score",
    "ROUGE-2 f-score",
    "ROUGE-L f-score",
    "Cosine Similarity",
    "Predicted",
    "Reference"]

output_rows = []

for key in predicted_presentations.keys():

    # Print status update
    print("Starting evaluation for " + key[0] + "-" + key[1] + " ...")

    # Get the predicted and reference presentations
    predicted = predicted_presentations[key]
    reference = reference_presentations[key]
    script = scripts[key]

    # Get the number of slides
    predicted_slide_count = count_slides(predicted)
    reference_slide_count = count_slides(reference)
    slide_count_difference = abs(predicted_slide_count - reference_slide_count)
    slide_count_error = round(abs(predicted_slide_count - reference_slide_count) / reference_slide_count, 2)

    # Split the presentations into slides
    predicted_slides = predicted.split("\n---\n")
    reference_slides = reference.split("\n---\n")

    # Create a map of element names and functions
    element_map = {
        "slide": get_slide,
        "header": get_header,
        "class": get_class,
        "title": get_title,
        "body": get_body,
        "images": get_image_alt_text,
        "notes": get_notes,
        "footer": get_footer,}

    # Only evaluate slides if the number of slides is the same
    if slide_count_difference != 0:
        output_row = [results_id, key[0], key[1], "", "", "", "", "", "", "", ""]
        output_rows.append(output_row)
        continue

    # Loop through the slides
    for i in range(len(predicted_slides)):

        # Get the predicted and reference slides
        predicted_slide = predicted_slides[i].strip()
        reference_slide = reference_slides[i].strip()

        # Hack to remove the first line of the first slide
        # This is so all slides have the same format
        if i == 0:
            predicted_slide = predicted_slide.replace("---\n", "")
            reference_slide = reference_slide.replace("---\n", "")

        for element_name, element_function in element_map.items():

            # Only get the header if on the first slide
            if i != 0 and element_name == "header":
                continue

            # Get the predicted and reference element values
            predicted_value = element_function(predicted_slide)
            reference_value = element_function(reference_slide)

            # If predicted element doesn't exist, set it to "None"
            # Note: this is to avoid empty vocabulary for cosine similarity
            if predicted_value == "":
                predicted_value = None

            # If reference element doesn't exist, set it to "None"
            if reference_value == "":
                reference_value = None

            # Are the predicted and reference values the same?
            if predicted_value == reference_value:
                element_equality = 1

            # Get the similarity scores
            if predicted_value is None and reference_value is None:
                bleu_score = ""
                rouge_scores = ""
                rouge_1_score = ""
                rouge_2_score = ""
                rouge_l_score = ""
                similarity = None
            elif predicted_value is None or reference_value is None:
                bleu_score = 0.0
                rouge_scores = 0.0
                rouge_1_score = 0.0
                rouge_2_score = 0.0
                rouge_l_score = 0.0
                similarity = 0.0
            else:
                bleu_score = round(get_bleu_score(predicted_value, reference_value), 2)
                rouge_scores = get_rouge_scores(predicted_value, reference_value)
                rouge_1_score = round(rouge_scores["rouge1"].fmeasure, 2)
                rouge_2_score = round(rouge_scores["rouge2"].fmeasure, 2)
                rouge_l_score = round(rouge_scores["rougeL"].fmeasure, 2)
                similarity = round(get_similarity_score(predicted_value, reference_value), 2)

            # Add the output row
            output_row = [
                results_id,
                key[0],
                key[1],
                i,
                element_name,
                bleu_score,
                rouge_1_score,
                rouge_2_score,
                rouge_l_score,
                similarity,
                predicted_value,
                reference_value]

            # Add the output row to the list
            output_rows.append(output_row)

    # Print status update
    print("Finished evaluating " + key[0] + "-" + key[1])

# Write the output CSV file
with open(output_file_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(output_header)
    writer.writerows(output_rows)

# Print final status
print("Finished presentation evaluations.")