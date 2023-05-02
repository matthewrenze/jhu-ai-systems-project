# Import libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Hide future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Set the file and folder paths
root_folder_path = "C:\\Users\\Matthew\\Dropbox\\Personal\\School\\JHU\\Systems\\Project"
input_folder_path = root_folder_path + "\\Data\\Evaluation\\Intro to Data for Data Science\\Logs"
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

    # Get the result ID from the file name
    file_name = os.path.basename(input_file_path)
    file_name = file_name.replace("-log.csv", "")

    # Insert the result as the first column
    input_data.insert(0, "Result ID", file_name)

    # Add the input data to the output data
    data = data.append(input_data)

# Filter out any error messages
data = data[data["Error Message"].isnull()]

# Group durations by result ID and aggregate
totals = data.groupby("Result ID").agg({
    "Prompt Tokens": sum,
    "Completion Tokens": sum,
    "Total Tokens": "sum"})

# Create an empty data frame
costs = pd.DataFrame()

def add_costs_for_gpt_3_x(costs, model_name, training_cost, price_per_1000_tokens):

    # Compute the costs
    price_per_token = price_per_1000_tokens / 1000
    model_totals = totals.loc[model_name]
    model_total_tokens = model_totals["Total Tokens"]
    model_total_cost = training_cost + (model_total_tokens * price_per_token)

    # Add a new row in the costs data frame
    costs.loc[model_name, "Model"] = model_name
    costs.loc[model_name, "Training Cost"] = training_cost
    costs.loc[model_name, "Prompt Tokens"] = None
    costs.loc[model_name, "Price per Prompt Token"] = None
    costs.loc[model_name, "Prompt Cost"] = None
    costs.loc[model_name, "Completion Tokens"] = None
    costs.loc[model_name, "Price per Completion Token"] = None
    costs.loc[model_name, "Completion Cost"] = None
    costs.loc[model_name, "Total Tokens"] = model_total_tokens
    costs.loc[model_name, "Price per Token"] = price_per_token
    costs.loc[model_name, "Total Cost"] = model_total_cost

    # Return the row
    return costs.loc[model_name]

def add_costs_for_gpt_4(
        costs,
        model_name,
        price_per_1000_prompt_tokens,
        price_per_1000_completion_tokens):

    # Compute the costs
    price_per_prompt_token = price_per_1000_prompt_tokens / 1000
    price_per_completion_token = price_per_1000_completion_tokens / 1000
    model_totals = totals.loc[model_name]
    model_prompt_tokens = model_totals["Prompt Tokens"]
    model_completion_tokens = model_totals["Completion Tokens"]
    model_prompt_cost = model_prompt_tokens * price_per_prompt_token
    model_completion_cost = model_completion_tokens * price_per_completion_token
    model_total_tokens = model_prompt_tokens + model_completion_tokens
    model_total_cost = model_prompt_cost + model_completion_cost

    # Add a new row in the costs data frame
    costs.loc[model_name, "Model"] = model_name
    costs.loc[model_name, "Training Cost"] = None
    costs.loc[model_name, "Prompt Tokens"] = model_prompt_tokens
    costs.loc[model_name, "Price per Prompt Token"] = price_per_prompt_token
    costs.loc[model_name, "Prompt Cost"] = model_prompt_cost
    costs.loc[model_name, "Completion Tokens"] = model_completion_tokens
    costs.loc[model_name, "Price per Completion Token"] = price_per_completion_token
    costs.loc[model_name, "Completion Cost"] = model_completion_cost
    costs.loc[model_name, "Total Tokens"] = model_total_tokens
    costs.loc[model_name, "Price per Token"] = None
    costs.loc[model_name, "Total Cost"] = model_total_cost

# Compute total price for GPT 3.x models
add_costs_for_gpt_3_x(costs, "gpt-3-in-sample", 3.72, 0.12)
add_costs_for_gpt_3_x(costs, "gpt-3.5-in-sample", 0.0, 0.002)
add_costs_for_gpt_4(costs, "gpt-4-in-sample", 0.03, 0.06)

# Replace "in-sample" with empty string
costs["Model"] = costs["Model"].str.replace("-in-sample", "")

# Capitalize GPT
costs["Model"] = costs["Model"].str.replace("gpt", "GPT")

# Drop the index (so that the rows are numbers not strings for plotting)
costs = costs.reset_index(drop=True)

# Create a plot of total cost
ax = costs.plot.bar(
    x="Model",
    y="Total Cost",
    figsize=(10, 5))
plt.title("Total Cost by Model")
plt.xlabel("Model")
plt.ylabel("Total Cost ($)")
plt.xticks(rotation=0)
plt.subplots_adjust(
    left=0.1,
    right=0.9)
plt.legend().remove()

# Add labels to the top center of each bar
for patch in ax.patches:
    x = patch.get_x() + patch.get_width() / 2
    y = patch.get_height()
    label = "${:.2f}".format(y)
    y_position = y - 0.05*max(costs['Total Cost'])
    ax.text(x, y, label, ha="center", va="bottom", color="black")

# Save the plot as an SVG file
cost_svg_file_path = output_folder_path + "\\SVG\\" + "total-cost-by-model.svg"
plt.savefig(cost_svg_file_path, format="svg")

# Save the plot as a PNG file
cost_png_file_path = output_folder_path + "\\PNG\\" + "total-cost-by-model.png"
plt.savefig(cost_png_file_path, format="png")

# Show the plot
plt.show()

# Save the data as a CSV file
cost_csv_file_path = output_folder_path + "\\CSV\\" + "total-cost-by-model.csv"
costs.to_csv(cost_csv_file_path, index=False)





