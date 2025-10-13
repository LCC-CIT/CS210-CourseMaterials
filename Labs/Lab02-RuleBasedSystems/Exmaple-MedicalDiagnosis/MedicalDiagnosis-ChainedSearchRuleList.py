from knowledge_base import IF_KEY, THEN_KEY, RESULT_TYPE_KEY, RESULT_TYPE_DIAGNOSIS, RESULT_TYPE_RECOMMENDATION

# Example Expert System for Medical Diagnosis
# Using Forward Chaining with Chained Search Rules
# Initial code from Gemini Flash 2.5
# Major refactoring by Brian Bird, October 11, 2025

# HARDCODED KNOWLEDGE BASE (Rules)
# The rules are defined as a list of dictionaries. 
# 'if': A set of facts (strings) required to trigger the rule.
# 'then': The new fact (string) derived when the rule fires.
# 'result_type': Indicates the type of fact: diagnosis or recommendation, 
#    either one could be a final goal.

KNOWLEDGE_BASE = [
    # Rule 1: Suspect Flu
    {
        "if": {"fever", "cough"}, 
        "then": "suspect_flu", 
        "result_type": "INTERMEDIATE"
    },
    
    # Rule 2: Suspect Migraine
    {
        "if": {"headache", "nausea"}, 
        "then": "suspect_migraine", 
        "result_type": "INTERMEDIATE"
    },
    
    # Rule 3: Diagnosis Influenza (Chain step 1: needs 'suspect_flu' derived from R1)
    {
        "if": {"suspect_flu", "body_aches"}, 
        "then": "diagnosis_influenza", 
        "result_type": "DIAGNOSIS"
    },
    
    # Rule 4: Diagnosis Common Cold (Chain step 1, no further chaining for reccommendation)
    {
        "if": {"suspect_flu", "sore_throat"}, 
        "then": "diagnosis_common_cold", 
        "result_type": "DIAGNOSIS"
    },

    # Rule 5: Diagnosis Migraine (Chain step 1: needs 'suspect_migraine' derived from R2)
    {
        "if": {"suspect_migraine", "light_sensitivity"}, 
        "then": "diagnosis_migraine", 
        "result_type": "DIAGNOSIS"
    },

    # Rule 6: Recommendation for Influenza (Chain step 2: needs 'diagnosis_influenza' derived from R3)
    {
        "if": {"diagnosis_influenza"}, 
        "then": "recommend_rest", 
        "result_type": "RECCOMENDATION"
    },
    
    # Rule 7: Recommendation for Migraine (Chain step 2: needs 'diagnosis_migraine' derived from R2)
    {
        "if": {"diagnosis_migraine"}, 
        "then": "recommend_dark_room", 
        "result_type": "RECCOMENDATION"
    },

    # Rule 8: Diagnosis Food Poisoning (No chain, direct diagnosis)
    {
        "if": {"no_appetite", "stomach_pain"}, 
        "then": "diagnosis_food_poisoning", 
        "result_type": "DIAGNOSIS"
    },
]

def get_diagnosis(initial_facts):
    """
    Get the diagnoses and recommendations based on initial facts.

        Parameters:
    - initial_facts: iterable (typically a list) of starting fact strings.
    Returns:
    - Dictionary with diagnoses and recommendations
        The dictionary contains the derived facts and goal recommendations as lists.
    """

    # Perform forward chaining inference
    derived_facts = forward_chaining_inference(KNOWLEDGE_BASE, initial_facts)
    # Extract diagnoses and recommendations
    results = extract_goals(KNOWLEDGE_BASE, derived_facts)

    return results


def forward_chaining_inference(rules, initial_facts):
    """
    Performs the core Forward Chaining inference process.

    Parameters:
    - rules: iterable (typically a list) of rules. 
        Each rule is a dictionary with keys 'if', 'then', and 'is_goal'.
    - initial_facts: iterable (typically a list) of starting fact strings.

    Returns:
    - List of derived facts
        The list of facts derived from the initial facts and rules (excluding the initial facts).
    """
    # Convert the list of facts into a set for fast lookup and easy modification.
    facts = set(initial_facts)

    # This variable controls the main loop (The Forward Chain).
    # If a rule fires and adds a new fact, this is set to True, and the loop repeats.
    new_fact_added = True
    iteration = 0

    # FORWARD CHAINING LOOP: Repeats until no new facts are found in a complete iteration.
    while new_fact_added:
        new_fact_added = False  # Reset the flag for the start of the new iteration
        iteration += 1

        # Iterate through all rules to see if any are triggered by matching the conditions.
        for rule in rules:
            conditions_needed = rule[IF_KEY]  # use the key 'if' to get the set of conditions
            new_fact = rule[THEN_KEY]         # use the key 'then' to get the conclusion

            # Are all conditions_needed currently present in the 'facts' set?
            conditions_met = conditions_needed.issubset(facts)

            if conditions_met:
                # Only add the new fact if it's not already in the set facts.
                if new_fact not in facts:
                    facts.add(new_fact)
                    new_fact_added = True   # This tells the 'while' loop to run again.

    # Return only the derived facts (exclude initial facts) as a list
    derived_facts = list(facts - set(initial_facts))
    return derived_facts


def extract_goals(rules, final_facts):
    """
    Finds all facts that were derived AND are marked as a diagnosis or recommendation in the rules.

    Parameters:
    - rules: List (or iterable) of rule dicts with 'then' and 'result_type' keys
    - final_facts: List (or iterable) of fact strings derived by the inference process.

    Returns:
    - Dictionary with 'diagnoses' and 'recommendations' keys, each mapping to a list of facts.
    """
    diagnoses = []
    recommendations = []
    
    for rule in rules:
        fact = rule[THEN_KEY]
        result_type = rule[RESULT_TYPE_KEY]
        if fact in final_facts:
            if result_type == RESULT_TYPE_DIAGNOSIS:
                diagnoses.append(fact)
            elif result_type == RESULT_TYPE_RECOMMENDATION:
                recommendations.append(fact)
    
    return {"diagnoses": diagnoses, "recommendations": recommendations}


# --- Main Program ---

print("--- Scenario 1: Influenza Chain ---")
patient_facts_1 = ['fever', 'cough', 'body_aches']
goal_recommendations_1 = get_diagnosis(patient_facts_1)
print(f"Diagnoses: {goal_recommendations_1.get('diagnoses') or 'None'}")
print(f"Recommendations: {goal_recommendations_1.get('recommendations') or 'None'}")
print()

print("--- Scenario 2: Common Cold ---")
patient_facts_2 = ['fever', 'cough', 'sore_throat']
goal_recommendations_2 = get_diagnosis(patient_facts_2)
print(f"Diagnoses: {goal_recommendations_2.get('diagnoses') or 'None'}")
print(f"Recommendations: {goal_recommendations_2.get('recommendations') or 'None'}")
print()

print("--- Scenario 3: Migraine ---")
patient_facts_3 = ['headache', 'nausea', 'light_sensitivity']
goal_recommendations_3 = get_diagnosis(patient_facts_3)
print(f"Diagnoses: {goal_recommendations_3.get('diagnoses') or 'None'}")
print(f"Recommendations: {goal_recommendations_3.get('recommendations') or 'None'}")
print()

print("--- Scenario 4: Food Poisoning ---")
patient_facts_4 = ['no_appetite', 'stomach_pain']
goal_recommendations_4 = get_diagnosis(patient_facts_4)
print(f"Diagnoses: {goal_recommendations_4.get('diagnoses') or 'None'}")
print(f"Recommendations: {goal_recommendations_4.get('recommendations') or 'None'}")
