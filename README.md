# Impact of Govt Job Assistance Programs on Earning Power

## Project Overview

This project investigates the impact of government job assistance programs on the earning power of non-degreed individuals. The primary objective is to determine whether participation in such programs leads to higher future earnings for individuals who do not hold a college degree. This research is significant for understanding the effectiveness of alternative career pathways, such as apprenticeships, for those unable to attend college.

## Repository Structure

This repository contains the following files:

1. **data.csv** - The dataset used for the analysis.
2. **data.ipynb** - The Jupyter notebook containing the data analysis, including calculations, model fitting, and plotting results.
3. **degree.png** - An image representing the impact of education degree on earnings.
4. **prop_update.pdf** - The project update report submitted as part of the course requirements.
5. **proposal.pdf** - The project proposal outlining the research questions, dataset, and initial hypotheses.
6. **report.pdf** - The final project report detailing the methodology, analysis, results, and conclusions.

## Files Description

### data.csv
This file contains the National Supported Work Demonstration (NSW) job-training program experiment dataset. It includes 445 observations and 11 variables such as treatment status, age, education, race, marital status, and earnings for various years.

### data.ipynb
This Jupyter notebook includes:
- Bootstrap and backdoor functions for causal inference.
- Exploratory data analysis.
- Implementation of Double Machine Learning (DML) estimators.
- Code for plotting SHAP values to interpret the models.

### degree.png
An image illustrating the relationship between education degree and earnings, highlighting the positive correlation between higher education levels and increased earning potential.

### proposal.pdf
The project proposal. It outlines the problem statement, causal questions, dataset description, and expectations for the project. It serves as the initial roadmap for the research.

### prop_update.pdf
A project update report. It details the progress made, including dataset statistics, causal graph, estimation methods, and initial findings. The report also discusses challenges and next steps for the project.

### report.pdf
The final report provides a comprehensive overview of the project, including:
- Detailed code and documentation.
- Estimation implementation using DML.
- Changes since the project update.
- Interpretation of results.
- Reflections on the project, including challenges and potential future work.

## Results Summary
The analysis revealed that job assistance programs have a positive impact on future earnings, particularly for individuals with at least a high school degree. The Average Treatment Effect (ATE) indicates that program participants earned significantly more than non-participants. However, the effectiveness of the program varies depending on the educational background of the individuals.

## Future Work
Future research could focus on addressing unobserved confounding factors such as criminal records and exploring the impact of job assistance programs in the current job market. Additional datasets and refined causal models could further enhance the robustness of the findings.

## Acknowledgments
This project was conducted as part of the CS396 Causal Inference course. Special thanks to the course instructors and group members Jose Cordova, Amir Dhami, and Dennis Wu for their contributions and collaboration.

## References
- Dehejia, R. H., & Wahba, S. (2002). Propensity Score-Matching Methods for Nonexperimental Causal Studies. Review of Economics and Statistics, 84(1), 151-161.
- LaLonde, R. J. (1986). Evaluating the Econometric Evaluations of Training Programs with Experimental Data. American Economic Review, 76(4), 604-620.
