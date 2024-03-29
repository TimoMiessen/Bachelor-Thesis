# An Analysis of Possible Bias Against Women of Color in Commercial Image Content Moderation Systems

Type: Bachelor's Thesis

Author: Timo Miessen

1st Examiner: Herr Prof. Dr. Lessmann

2nd Examiner: Herr Prof. Dr. Fabian

![Fairness_Criteria](https://github.com/TimoMiessen/Bachelor-Thesis/assets/147314402/18ae7f3b-9afd-43f5-b98c-128cce3211ec)

![Fairness_Criteria_Intersectionality](https://github.com/TimoMiessen/Bachelor-Thesis/assets/147314402/7144bf6e-1f13-4865-818b-e4bcae7a04fc)

## Table of Content

- Summary
- Working with the repo
- Reproducing Results

## Summary

In today's digital landscape, AI technologies and commercial content moderation systems are essential for managing the vast amounts of User Generated Content. To understand their effectiveness, this study conducted a systematic examination, focusing on the fairness of decisions made by these systems. An intersectional approach was adopted, acknowledging the multi-faceted biases that can arise from overlapping social categorizations. Notably, a specialized image dataset was developed specifically for this study. The findings reveal that, despite the advanced capabilities of these AI models, potential biases and prejudices can still manifest in their decisions, emphasizing the need for continuous refinement and oversight.

Keywords: Machine Learning · Algorithmic Fairness · Commercial Image Content Moderation · Intersectionality · Algorithmic Content Moderation

## Working with the repo

The experiment was conducted using Python3 version 3.11

## Reproducing results

### Data Aquisition
All 4 systems used in the study come with pre-trained models. These models are accessible via the specific APIs provided by the respective developers Amazon, Google, Microsoft and Sightengine.
To engage with the APIs and utilize the models, sample codes have been provided by the developers. These codes serve as an interface to send images for analysis to the models.
In an advanced step, these provided sample codes have been modified and expanded to ensure a more efficient interaction with the APIs. This enhancement allows not just the submission of individual images but entire directories or folders for the analysis. The respective files are "amazon.py", "google.py", "microsoft.py" and "sightengine.py".
To generate the data, download the image set provided via Google Drive (https://drive.google.com/drive/folders/1OrMFmdRLCAngOfNO5r1uO2tG5787cicy?usp=sharing). Then simply adjust the codes by inserting the directory the images are stored in.

### Data Analysis
Upon execution of these adjusted codes, the generated CSV files ("amazon_results.csv", "google_results.csv", "microsoft_results.csv" and "sightengine_results.csv") were imported into an Excel file that catalogues all image instances, characterised with the variables defined in Table 3.1. All labels, with the exception of the "Suggestive / Racy" label, were removed to maintain the focus of the study. The analysis was then continued within these individual Excel files. The distinct probabilities provided by the models were converted into binary values (0 or 1) based on various threshold values, as detailed in Section 3.4. Subsequently, group-specific confusion matrices were manually constructed, serving as the foundation upon which performance metrics were calculated. The corresponding files are "Amazon_Rekognition_data", "Google_SafeSearch_data", "Google_SafeSearch_data_Standard2", "Microsoft_ContentModerator_data", "Microsoft_ContentModerator_data_Standard2" and "Sightengine_data".

### Excel File Structure
All Excel files adhere to a consistent structure. The "Whole" worksheet houses the comprehensive dataset including all instances. Subsequent worksheets are filtered based on individual sensitive attributes and their respective combinations, for instance, sheets dedicated to all female instances or all men of color. The final three worksheets are pivotal; they encompass all group-specific confusion matrices, the applied performance metrics and an overview of the metrics.


