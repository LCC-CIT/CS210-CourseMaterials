# load_knowledge_base.py
# Module to load the knowledge base from a CSV file for the medical diagnosis expert system.
import csv

def load_knowledge_base_from_csv(csv_path):
    """
    Loads rules from a CSV file with a guaranteed header row.
    Each row is returned as a dictionary with keys matching the header (e.g. 'IF', 'AND', 'THEN', 'RESULT_TYPE').
    No parsing or transformation is performed; the result is a list of dictionaries.
    """
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rules = [dict(row) for row in reader]
    return rules
