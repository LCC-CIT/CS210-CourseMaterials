
# 1. HARDCODED KNOWLEDGE BASE (Rules)
# The rules are defined as a list of dictionaries. 
# The first dicitonary in each rule, with the key "if", has a set as it's value.
# 'if': A set of facts (strings) required to trigger the rule.
# 'then': The new fact (string) derived when the rule fires.
# 'is_goal': True if this fact is a final diagnosis or recommendation.

KNOWLEDGE_BASE = [
    # Rule 1: Suspect Flu
    {
        "if": {"fever", "cough"}, 
        "then": "suspect_flu", 
        "is_goal": False
    },
    
    # Rule 2: Suspect Migraine
    {
        "if": {"headache", "nausea"}, 
        "then": "suspect_migraine", 
        "is_goal": False
    },
    
    # Rule 3: Diagnosis Influenza (Chain 1 step: needs 'suspect_flu' derived from R1)
    {
        "if": {"suspect_flu", "body_aches"}, 
        "then": "diagnosis_influenza", 
        "is_goal": False
    },
    
    # Rule 4: Diagnosis Common Cold (Chain 1 step)
    {
        "if": {"suspect_flu", "sore_throat"}, 
        "then": "diagnosis_common_cold", 
        "is_goal": False
    },
    
    # Rule 5: Recommendation for Influenza (Chain 2 step: needs 'diagnosis_influenza' derived from R3)
    {
        "if": {"diagnosis_influenza"}, 
        "then": "recommend_rest", 
        "is_goal": True
    },
    
    # Rule 6: Recommendation for Migraine (Final Diagnosis)
    {
        "if": {"diagnosis_migraine"}, 
        "then": "recommend_dark_room", 
        "is_goal": True
    },
    
    # Rule 7: Diagnosis Food Poisoning (Final Diagnosis)
    {
        "if": {"no_appetite", "stomach_pain"}, 
        "then": "diagnosis_food_poisoning", 
        "is_goal": True
    },
]

def forward_chaining_inference(rules, initial_facts, verbose: bool = False):
    """
    Performs the core Forward Chaining inference process.
    The goal is to expand the 'facts' set using the 'rules'.

    Parameters:
    - rules: iterable of rule dicts with 'if' (set) and 'then' (conclusion)
    - initial_facts: iterable of starting fact strings
    - verbose: if True, prints iteration/apply/current-facts messages (default False)

    Returns:
    - set of derived facts
    """
    # Convert the list of facts into a set for fast lookup and easy modification.
    facts = set(initial_facts)
    if verbose:
        print(f"--- Starting Inference with Initial Facts: {facts} ---\n")

    # This variable controls the main loop (The Forward Chain).
    # If a rule fires and adds a new fact, this is set to True, and the loop repeats.
    new_fact_added = True
    iteration = 0

    # FORWARD CHAINING LOOP: Repeats until no new facts are found in a complete pass.
    while new_fact_added:
        new_fact_added = False  # Reset the flag for the start of the new pass
        iteration += 1

        if verbose:
            print(f"--- Iteration {iteration} ---")

        for rule in rules:
            conditions_needed = rule['if']
            new_fact = rule['then']

            # Check 1: Pattern Matching
            # Check if ALL conditions_needed are currently present in the 'facts' set.
            conditions_met = conditions_needed.issubset(facts)

            if conditions_met:
                # Check 2: Assertion/Action
                # Only add the new fact if it's not already known.
                if new_fact not in facts:
                    facts.add(new_fact)
                    new_fact_added = True
                    # This tells the 'while' loop to run again.
                    if verbose:
                        print(f"  [APPLY] Rule: Required: {conditions_needed} -> Derived: {new_fact}")

        if verbose:
            print(f"  Current Derived Facts: {sorted(list(facts))}\n")

    return facts

def extract_goals(rules, final_facts):
    """
    Finds all facts that were derived AND are marked as a 'goal' in the rules.
    This replaces the lambda/list comprehension filtering.
    """
    goal_recommendations = []
    
    for rule in rules:
        fact = rule['then']
        is_goal = rule['is_goal']
        
        # Check if the fact is a GOAL and if that fact was successfully derived
        if is_goal and fact in final_facts:
            goal_recommendations.append(fact)
            
    return goal_recommendations


# --- Main Program Execution ---

# --- Scenario 1: Influenza Chain ---
patient_facts_1 = ['fever', 'cough', 'body_aches']
final_facts_1 = forward_chaining_inference(KNOWLEDGE_BASE, patient_facts_1)

# Extract goal results using the simplified function
goal_recommendations_1 = extract_goals(KNOWLEDGE_BASE, final_facts_1)

print("====================================")
print(f"FINAL RESULT (Scenario 1: {patient_facts_1})")
print(f"Recommendations: {goal_recommendations_1 if goal_recommendations_1 else 'None'}")
print("====================================")

# --- Scenario 2: Food Poisoning ---
patient_facts_2 = ['no_appetite', 'stomach_pain']
final_facts_2 = forward_chaining_inference(KNOWLEDGE_BASE, patient_facts_2)

# Extract goal results
goal_recommendations_2 = extract_goals(KNOWLEDGE_BASE, final_facts_2)

print("====================================")
print(f"FINAL RESULT (Scenario 2: {patient_facts_2})")
print(f"Recommendations: {goal_recommendations_2 if goal_recommendations_2 else 'None'}")
print("====================================")
