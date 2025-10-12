import csv
from io import StringIO
from typing import List, Set, Dict, Any
from knowledge_base import IF_KEY, THEN_KEY

def load_rules(csv_content: str) -> List[Dict[str, Any]]:
    """
    Loads rules from the CSV content.
    Each rule is parsed into a dictionary with keys: 'if' (set of conditions) and 'then' (new fact).
    """
    rules = []
    content = csv_content.strip()      # Remove leading/trailing whitespace
    # Assume there is not a header row, parse positional columns: IF(two columns) THEN, GOAL
    csv_reader = csv.reader(StringIO(content))
    for row in csv_reader:
        # Skip empty rows
        is_empty_row = not row
        all_cells_blank = all(not cell.strip() for cell in row)
        if is_empty_row or all_cells_blank:
            continue

        # Map positional columns
        if_val = row[0].strip() if len(row) > 0 else ''
        and_val = row[1].strip() if len(row) > 1 else ''
        then_val = row[2].strip() if len(row) > 2 else ''
        goal_val = row[3].strip() if len(row) > 3 else ''

        if not if_val:
            continue

        conditions = {if_val}
        if and_val:
            conditions.add(and_val)

        rules.append({
            IF_KEY: conditions,
            THEN_KEY: then_val,
            "is_goal": bool(goal_val)
        })
    return rules


def load_rules_from_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Read rules from a CSV file path and return parsed rules list.
    Supports both header and header-less CSV files.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read() # read the file into a string
    return load_rules(content)

def forward_chaining_inference(rules: List[Dict[str, Any]], initial_facts: List[str], verbose: bool = False) -> Set[str]:
    """
    Performs forward chaining on the facts and rules to derive new facts.

    Parameters:
    - rules: list of rule dicts with 'if' as set and 'then' as conclusion
    - initial_facts: list of starting facts
    - verbose: optional flag to enable progress printing (default False)

    Returns:
    - set of derived facts (including initial ones)
    """
    # Initialize the set of known facts
    facts = set(initial_facts)

    # The loop continues as long as new facts are being added
    new_fact_added = True
    iteration = 0

    # Forward chaining occurs in this main loop: repeatedly scan and apply rules
    while new_fact_added:
        new_fact_added = False
        iteration += 1

        if verbose:
            print(f"--- Iteration {iteration} ---")

        for rule in rules:
            conditions_met = rule[IF_KEY].issubset(facts)
            new_fact = rule[THEN_KEY]

            # 1. Check IF condition (Pattern Matching)
            if conditions_met:
                # 2. IF rule is met AND the conclusion is new (Action/Assertion)
                if new_fact not in facts:
                    facts.add(new_fact)
                    new_fact_added = True
                    if verbose:
                        # The chain extends here: a new fact is added, potentially triggering other rules
                        print(f"  [APPLY] Rule: {rule['if']} -> {new_fact}")

        if verbose:
            print(f"  Current Derived Facts: {sorted(list(facts))}\n")

    return facts


def extract_goals(rules: List[Dict[str, Any]], facts: Set[str]) -> List[str]:
    """
    Return the list of rule conclusions that are marked as goals and present in facts.
    """
    return [r[THEN_KEY] for r in rules if r.get('is_goal') and r[THEN_KEY] in facts]

# --- Main Program Execution ---

# Load the knowledge base from CSV file in the same directory
CSV_FILE = 'MedicalDiagnosis.csv'

# Try to load rules from the CSV file path; fall back to empty rules on error
try:
    knowledge_base = load_rules_from_file(CSV_FILE)
except FileNotFoundError:
    print(f"Warning: {CSV_FILE} not found. No rules loaded.")
    knowledge_base = []

# --- Scenario 1: Influenza ---
patient_facts_1 = ['fever', 'cough', 'body_aches']
final_facts_1 = forward_chaining_inference(knowledge_base, patient_facts_1)

# Extract goal results
goal_recommendations_1 = extract_goals(knowledge_base, final_facts_1)

print("====================================")
print(f"FINAL RESULT (Scenario 1: {patient_facts_1})")
print(f"Recommendations: {goal_recommendations_1 if goal_recommendations_1 else 'None'}")
print("====================================")

# --- Scenario 2: Food Poisoning ---
patient_facts_2 = ['no_appetite', 'stomach_pain']
final_facts_2 = forward_chaining_inference(knowledge_base, patient_facts_2)

# Extract goal results
goal_recommendations_2 = extract_goals(knowledge_base, final_facts_2)

print("====================================")
print(f"FINAL RESULT (Scenario 2: {patient_facts_2})")
print(f"Recommendations: {goal_recommendations_2 if goal_recommendations_2 else 'None'}")
print("====================================")
