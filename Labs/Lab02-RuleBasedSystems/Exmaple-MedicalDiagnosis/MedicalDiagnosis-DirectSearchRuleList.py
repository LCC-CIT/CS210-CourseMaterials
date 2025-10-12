from knowledge_base import IF_KEY, THEN_KEY

# This program demonstrates simple rule-based classification (Pattern Matching)

KNOWLEDGE_BASE = [
    # Rule 1:Flu/Cold symptoms
    {"if": {"fever", "cough", "sore_throat"}, "then": "Diagnosis: Common Cold - Recommend hot tea."},
    
    # Rule 2: Migraine
    {"if": {"headache", "nausea"}, "then": "Diagnosis: Migraine - Recommend dark room and quiet rest."},
    
    # Rule 3: Food Poisoning
    {"if": {"no_appetite", "stomach_pain"}, "then": "Diagnosis: Food Poisoning - Recommend bland diet and hydration."},
    
    # Rule 4: Fever
    {"if": {"fever"}, "then": "Diagnosis: Unknown Fever - Recommend taking temperature hourly."},
]

def direct_lookup_inference(rules, patient_facts):
    """
    Performs a single-pass search (lookup) for a matching rule.
    """
    facts_set = set(patient_facts)

    # The system only iterates through the rules once.
    for rule in rules:
        conditions_needed = rule[IF_KEY]

        # Pattern Matching: Check if ALL conditions needed by the rule
        # are present in the patient's facts.
        conditions_met = conditions_needed.issubset(facts_set)

        if conditions_met:
            # We found a direct match! Return the immediate conclusion.
            return rule[THEN_KEY]

    # If the loop finishes without finding a match:
    return "Diagnosis: Undetermined. No direct rule matched all symptoms."

# --- Main Program Execution ---

# Scenario 1: Simple Cold (matches Rule 1)
patient_facts_1 = ['fever', 'cough', 'sore_throat', 'body_aches'] # Extra fact doesn't hurt
result_1 = direct_lookup_inference(KNOWLEDGE_BASE, patient_facts_1)

print("\n====================================")
print(f"RESULT 1: {result_1}")
print("====================================")

# Scenario 2: Migraine (matches Rule 2)
patient_facts_2 = ['headache', 'nausea']
result_2 = direct_lookup_inference(KNOWLEDGE_BASE, patient_facts_2)

print("\n====================================")
print(f"RESULT 2: {result_2}")
print("====================================")

# Scenario 3: Only Fever (matches Rule 4, since it's the simplest match)
patient_facts_3 = ['fever', 'restless']
result_3 = direct_lookup_inference(KNOWLEDGE_BASE, patient_facts_3)

print("\n====================================")
print(f"RESULT 3: {result_3}")
print("====================================")
