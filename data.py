import pandas as pd
import csv

FILE_PATH = 'data/ticket_data.csv'

with open(FILE_PATH, mode='a') as file:
    try:
        ticket_data = pd.read_csv(FILE_PATH)
    except pd.errors.EmptyDataError:
        ticket_data = pd.DataFrame(columns=['Reported by', 'Hospital', 'Department', 'Issue Type', 'Category', 'Subcategory', 'Short', 'Detailed', 'Resolution', 'Item'])