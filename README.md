# Automatically Generating Lecture Slides with Generative Pretrained Transformers
**Author:** Matthew Renze  
**Class:** EN.705.603  
**Date:** 2023-04-07

## Abstract
In this paper, we explore the automation of script-to-slide generation using three Generative Pretrained Transformer (GPT) models. We created a training set of script-slide pairs using a single source presentation. Next, we created three GPT models using this training data. We used custom fine-tuning for GPT-3 and few-shot learning for GPT-3.5 and GPT-4. These three models used the on-sample training scripts to generate test slides. To assess the relative performance of each model, we compared the generated slides against the training slides and scripts. GPT-4 outperformed the other models in terms of accuracy, similarity, and relevance. However, it underperformed the other models on runtime performance and cost efficiency. This research demonstrates the potential of using GPT models to automate lecture slide generation highlighting areas for further investigation and improvement. All code, data, and supplemental materials are available on GitHub.

## Paper
- [Automatically Generating Lecture Slides with Generative Pretrained Transformers](research-paper.pdf)

## Code
- [Collect](code/Collect/) - contains the data collection scripts
- [Prepare](code/Prepare/) - contains all data pre-processing scripts
- [Train](code/Train/) - contains all model training scripts
- [Predict](code/Predict/) - contains all prediction scripts
- [Evaluate](code/Evaluate/) - contains all evaluation scripts
- [Analyze](code/Analyze/) - contains all analysis scripts
- [Misc](code/Misc/) - contains all misc utility scripts

## Data
- [PowerPoint](data/PowerPoint/) - contains all original PowerPoint presentations
- [Markdown](data/Markdown/) - contains all converted markdown files in raw form
- [Source](data/Source/) - contains all manually cleaned markdown presentation files
- [Training](data/Training/) - contains all model training data and few-shot learning examples
- [Predictions](data/Predictions/) - contains all generated slides from GPT-3, GPT-3.5, and GPT-4
- [Evaluation](data/Evaluation/) - contains all evaluation data and runtime logs
- [Templates](data/Templates/) - contains the CSS template used to styled markdown slides

## Analysis
- [CSV](analysis/csv/) - contains analysis output data in tabular form
- [PNG](analysis/png/) - contains PNG images of data visualizations
- [SVG](analysis/svg/) - contains SVG files for data visualizations

## Notes
 - To render Marp markdown files into HTML, PDF, PNG, TXT, etc. please see [Marp - Markdown Presentation Ecosystem](https://marp.app/)
 - To view Marp markdown files in VS Code, please see [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
 
