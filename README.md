# An Analysis of Possible Bias Against Women of Color in Commercial Image Content Moderation Systems

Type: Bachelor's Thesis

Author: Timo Miessen

1st Examiner: Herr Prof. Dr. Lessmann

2nd Examiner: Herr Prof. Dr. Fabian

## Table of Content

- Summary
- Working with the Image Content Moderation systems' API

## Summary

In today's digital landscape, AI technologies and commercial content moderation systems are essential for managing the vast amounts of User Generated Content. To understand their effectiveness, this study conducted a systematic examination, focusing on the fairness of decisions made by these systems. An intersectional approach was adopted, acknowledging the multi-faceted biases that can arise from overlapping social categorizations. Notably, a specialized image dataset was developed specifically for this study. The findings reveal that, despite the advanced capabilities of these AI models, potential biases and prejudices can still manifest in their decisions, emphasizing the need for continuous refinement and oversight.

Keywords: Machine Learning · Algorithmic Fairness · Commercial Image Content Moderation · Intersectionality · Algorithmic Content Moderation

## Working with the repo

The experiment was conducted using Python3 version 3.11

## Reproducing results

All 4 systems used in the study come with pre-trained models. These models are accessible via the specific APIs provided by the respective developers Amazon, Google, Microsoft and Sightengine.
To engage with the APIs and utilize the models, sample codes have been provided by the developers. These codes serve as an interface to send images for analysis to the models.
In an advanced step, these provided sample codes have been modified and expanded to ensure a more efficient interaction with the APIs. This enhancement allows not just the submission of individual images but entire directories or folders for the analysis. 
