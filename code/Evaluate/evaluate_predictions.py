# Import libraries
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
output_file_name = results_id + ".csv"
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
predicted_folder_path = root_folder_path + "\\Data\\Predictions\\Intro to Data for Data Science\\" + predicted_folder_name
actual_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Slides"
script_folder_path = root_folder_path + "\\Data\\Training\\Intro to Data for Data Science\\Scripts"
output_folder_path = root_folder_path + "\\Data\\Evaluation\\Intro to Data for Data Science"
output_file_path = output_folder_path + "\\" + output_file_name

# Create a function to return the key (module ID and section ID) for a file name
def get_key(file_name):
    prefix = file_name.split(".")[0].split(" - ")[0]
    module_id = prefix.split("-")[0].strip()
    section_id = prefix.split("-")[1].strip()
    return module_id, section_id

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
    "Predicted Slide Count",
    "Reference Slide Count",
    "Slide Count Accuracy",
    "BLEU Score",
    "ROUGE-1 f-score",
    "ROUGE-2 f-score",
    "ROUGE-L f-score",
    "Cosine Similarity",
    "Content Relevance"]

output_rows = []

for key in predicted_presentations.keys():

    # Print status update
    print("Starting evaluation for " + key[0] + "-" + key[1] + " ...")

    # Get the predicted and reference presentations
    predicted = predicted_presentations[key]
    reference = reference_presentations[key]
    script = scripts[key]

    # Split the presentations into slides
    predicted_slides = predicted.split("\n---\n")
    reference_slides = reference.split("\n---\n")

    # Calculate the performance metrics
    predicted_slide_count = len(predicted_slides)
    reference_slide_count = len(reference_slides)
    slide_count_difference = abs(predicted_slide_count - reference_slide_count)
    slide_count_accuracy = round(1.0 - (slide_count_difference / reference_slide_count), 2)
    bleu_score = round(get_bleu_score(predicted, reference), 2)
    rouge_scores = get_rouge_scores(predicted, reference)
    rouge_1_score = round(rouge_scores["rouge1"].fmeasure, 2)
    rouge_2_score = round(rouge_scores["rouge2"].fmeasure, 2)
    rouge_l_score = round(rouge_scores["rougeL"].fmeasure, 2)
    similarity = round(get_similarity_score(predicted, reference), 2)
    relevance = round(get_similarity_score(predicted, script), 2)

    # Create the output row
    output_row = [
        results_id,
        key[0],
        key[1],
        predicted_slide_count,
        reference_slide_count,
        slide_count_accuracy,
        bleu_score,
        rouge_1_score,
        rouge_2_score,
        rouge_l_score,
        similarity,
        relevance]

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
