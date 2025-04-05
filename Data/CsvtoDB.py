import pandas as pd
import sqlite3

# Read the CSV file into a pandas DataFrame
jobSkills = pd.read_csv(r"C:\Users\vigne\.cache\kagglehub\datasets\asaniczka\1-3m-linkedin-jobs-and-skills-2024\versions\2\job_skills.csv")
print(jobSkills.head())

jobSummary = pd.read_csv(r"C:\Users\vigne\.cache\kagglehub\datasets\asaniczka\1-3m-linkedin-jobs-and-skills-2024\versions\2\job_summary.csv")
print(jobSummary.head())

jobPostings = pd.read_csv(r"C:\Users\vigne\.cache\kagglehub\datasets\asaniczka\1-3m-linkedin-jobs-and-skills-2024\versions\2\linkedin_job_postings.csv")
print(jobPostings.head())


