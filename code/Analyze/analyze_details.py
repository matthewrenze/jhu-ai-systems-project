# Import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt

# Hide future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Set the file and folder paths
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
input_folder_path = root_folder_path + "\\Data\\Evaluation\\Intro to Data for Data Science\\Details"
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

# Create a composite score
data["Composite Score"] = (data["BLEU Score"] \
    + data["ROUGE-1 f-score"] \
    + data["ROUGE-2 f-score"] \
    + data["ROUGE-L f-score"] \
    + data["Cosine Similarity"]) / 5

# Filter out presentations where slide counts didn't match
data = data[data["Slide ID"].notna()]

# Get all elements (i.e. filter out slides)
data = data[data["Element Name"] != "slide"]

# Filter out notes (since I've excluded them from the predictions)
data = data[data["Element Name"] != "notes"]

# Exclude all columns except Results ID, Element Name, and Score
data = data[["Results ID", "Element Name", "Composite Score"]]

# Replace "in-sample" with empty string
data["Results ID"] = data["Results ID"].str.replace("-in-sample", "")

# Capitalize GPT
data["Results ID"] = data["Results ID"].str.replace("gpt", "GPT")

# Get the unique results IDs
results_ids = data["Results ID"].unique()

# Set the order of the elements for the plot
element_order = ["header", "class", "title", "images", "body", "footer"]

# Create a new figure with subplots
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

# Create a subplot for each group
for i, result_id in enumerate(results_ids):

    # Filter the data by results ID
    result_data = data[data["Results ID"] == result_id]

    # Get the average composite score for each element
    result_totals = result_data.groupby("Element Name").mean()

    # Reorder the elements on the x-axis
    result_totals = result_totals.reindex(element_order)

    # Plot the results
    result_totals.plot(
        kind="bar",
        ax=axs[i])
    axs[i].set_title(result_id)
    axs[i].set_ylim(0, 1)
    axs[i].set_xlabel("Element")
    if i == 0:
        axs[i].set_ylabel("Average Composite Score")
    axs[i].legend().remove()

    # Rotate the x-axis labels and right align them
    for tick in axs[i].get_xticklabels():
        tick.set_rotation(20)
        tick.set_horizontalalignment("right")

# Adjust the spacing between subplots
plt.subplots_adjust(
    bottom=0.15,
    left=0.1,
    right=0.9)


# Save the plot as an SVG file
element_svg_file_path = output_folder_path + "\\SVG\\" + "element-scores-by-model.svg"
plt.savefig(element_svg_file_path, format="svg")

# Save the plot as a PNG file
element_png_file_path = output_folder_path + "\\PNG\\" + "element-scores-by-model.png"
plt.savefig(element_png_file_path, format="png")

# Show the plot
plt.show()

# Get the average composite score for each element
summary = data.groupby(["Results ID", "Element Name"]).mean()
summary = summary.reset_index()

# Save the data frame as a CSV file
element_csv_file_path = output_folder_path + "\\CSV\\" + "element-scores-by-model.csv"
summary.to_csv(element_csv_file_path, index=False)