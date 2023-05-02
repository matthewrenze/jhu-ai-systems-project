# Import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt

# Hide future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Set the file and folder paths
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
input_folder_path = root_folder_path + "\\Data\\Evaluation\\Intro to Data for Data Science"
output_folder_path = root_folder_path + "\\Analysis"

# Get all CSV files in the input folder
input_file_paths = []
for file_name in os.listdir(input_folder_path):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder_path, file_name)
        input_file_paths.append(file_path)

# Create an empty data frame
data = pd.DataFrame()

# Read each input file and add it to the data frame
for input_file_path in input_file_paths:

    # Read the input file
    input_data = pd.read_csv(input_file_path)

    # Add the input data to the output data
    data = data.append(input_data)

# Exclude Module ID and Section ID
exclude_columns = [
    "Module ID",
    "Section ID",
    "Predicted Slide Count",
    "Reference Slide Count"]
data = data.drop(columns=exclude_columns)

# Replace "in-sample" with empty string
data["Results ID"] = data["Results ID"].str.replace("-in-sample", "")

# Capitalize GPT
data["Results ID"] = data["Results ID"].str.replace("gpt", "GPT")

# Get the average values for every column by Results ID
totals = data.groupby("Results ID").mean()

# Plot the results
totals.plot(
    kind="bar",
    figsize=(10, 5))
plt.title("Scores by Model")
plt.xlabel("Model")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.ylim(0, 1)
plt.legend(
    loc="center left",
    bbox_to_anchor=(1, 0.5))
plt.subplots_adjust(right=0.79)

# Save the plot as an SVG file
scores_svg_file_path = output_folder_path + "\\SVG\\" + "scores-by-model.svg"
plt.savefig(scores_svg_file_path, bbox_inches="tight")

# Save the plot as a PNG file
scores_png_file_path = output_folder_path + "\\PNG\\" + "scores-by-model.png"
plt.savefig(scores_png_file_path, bbox_inches="tight")

# Save the data to a CSV file
scores_csv_file_path = output_folder_path + "\\CSV\\" + "scores-by-model.csv"
totals.to_csv(scores_csv_file_path)

# Display the plot
plt.show()

# Compute the composite score
data["Composite Score"] = (
    data["Slide Count Accuracy"] \
    + data["BLEU Score"] \
    + data["ROUGE-1 f-score"] \
    + data["ROUGE-2 f-score"] \
    + data["ROUGE-L f-score"] \
    + data["Cosine Similarity"]
    + data["Content Relevance"]) / 7

# Plot the composite score
composite = data.groupby("Results ID").mean()
ax = composite.plot(
    y=["Composite Score"],
    kind="bar",
    figsize=(10, 5))
plt.xticks(rotation=0)
plt.ylim(0, 1)
plt.title("Composite Score by Model")
plt.xlabel("Model")
plt.ylabel("Average Composite Score")
plt.legend().remove()

# Add labels to the top center of each bar
for patch in ax.patches:
    x = patch.get_x() + patch.get_width() / 2
    y = patch.get_height()
    label = "{:.2f}".format(y)
    y = y - 0.05*max(composite['Composite Score'])
    ax.text(x, y, label, ha="center", va="top", color="white")

# Save the plot as an SVG file
composite_svg_file_path = output_folder_path + "\\SVG\\" + "composite-score-by-model.svg"
plt.savefig(composite_svg_file_path, bbox_inches="tight")

# Save the plot as a PNG file
composite_png_file_path = output_folder_path + "\\PNG\\" + "composite-score-by-model.png"
plt.savefig(composite_png_file_path, bbox_inches="tight")

# Display the plot
plt.show()

# Write the data to a CSV file
composite_csv_file_path = output_folder_path + "\\CSV\\" + "composite-score-by-model.csv"
composite.to_csv(composite_csv_file_path)

