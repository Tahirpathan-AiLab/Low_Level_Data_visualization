## Code Description

This script is designed to automate the process of **loading, visualizing, merging, and exporting multiple Excel datasets** using Python. It leverages **Pandas** for data manipulation, **Matplotlib** for visualization, and **Glob** for efficiently handling multiple files.

### Overview

The workflow begins by importing the required libraries and reading an Excel dataset (`fsi-2020.xlsx`). The first column is set as the DataFrame index to provide a structured representation of the data.

A selected column from the dataset is then visualized using a **line chart**, allowing quick exploration of trends and patterns.

Next, the script automatically scans a specified directory for all `.xlsx` files using the **Glob** module. Each Excel file is loaded into a DataFrame and combined into a single dataset using `pandas.concat()`, eliminating the need to merge files manually.

Once the combined dataset is created, the **Total** column is visualized to provide an overall view of the aggregated data.

Finally, the processed dataset is exported in both **Excel** and **CSV** formats, making it ready for further analysis, reporting, or integration with other applications.

---

## Key Features

* Reads Excel files using **Pandas**
* Sets the first column as the DataFrame index
* Visualizes selected columns with **Matplotlib**
* Automatically detects all Excel files in a directory
* Merges multiple datasets into a single DataFrame
* Performs trend visualization on the combined dataset
* Exports processed data to **Excel** and **CSV**
* Simple, reusable, and scalable workflow for data preprocessing

---

## my Workflow

<p align="center">
  <img src="https://img.shields.io/badge/1-Import%20Libraries-4CAF50?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/2-Load%20Excel%20Dataset-2196F3?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/3-Set%20Index%20Column-FF9800?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/4-Visualize%20Selected%20Data-E91E63?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/5-Read%20Multiple%20Excel%20Files-9C27B0?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/6-Merge%20Datasets-00BCD4?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/7-Visualize%20Combined%20Data-795548?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/8-Export%20to%20Excel%20%26%20CSV-4CAF50?style=for-the-badge"/>
</p>

---

## which Technologies I Used

<p align="center">
  <img src="https://skillicons.dev/icons?i=python" alt="Python"/>
  <img src="https://skillicons.dev/icons?i=vscode" alt="VS Code"/>
  <img src="https://skillicons.dev/icons?i=git" alt="Git"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Glob-00599C?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Microsoft%20Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>
</p>


## Output

After successful execution, the script generates:

* **visualized_data.xlsx** – Processed Excel dataset
* **visualized_data.csv** – Processed CSV dataset
* Line charts for both individual and combined datasets

This project demonstrates an efficient and scalable approach to data preprocessing, visualization, and dataset consolidation, making it suitable for data analytics, reporting, and exploratory data analysis (EDA) workflows.
