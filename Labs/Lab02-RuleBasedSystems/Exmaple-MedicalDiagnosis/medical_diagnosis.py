# medical_diagnosis.py
# Console interface for the medical diagnosis expert system.
# Code by Brian Bird using GitHub Copilot with GPT-4.1, 10/11/2025

from inference_engine import get_diagnosis
from knowledge_base import KNOWLEDGE_BASE, IF_KEY, AND_KEY

def main():
    # Collect all possible symptoms from the 'IF' and 'AND' properties in the knowledge base
    possible_symptoms = set()
    for rule in KNOWLEDGE_BASE:
        if IF_KEY in rule and rule[IF_KEY]:
            possible_symptoms.update(rule[IF_KEY] if isinstance(rule[IF_KEY], set) else [rule[IF_KEY]])
        if AND_KEY in rule and rule[AND_KEY]:
            possible_symptoms.add(rule[AND_KEY])
    print("Welcome to the Medical Diagnosis Expert System!")
    print("Possible symptoms:")
    print(", ".join(sorted(possible_symptoms)))
    print("Enter your symptoms, separated by commas (e.g. fever,cough,body_aches):")
    user_input = input("Symptoms: ")
    # Split input by comma, strip whitespace, and filter out empty strings
    symptoms = [s.strip() for s in user_input.split(',') if s.strip()]
    if not symptoms:
        print("No symptoms entered. Exiting.")
        return
    results = get_diagnosis(symptoms)
    diagnoses = results.get('diagnoses') or ['None']
    recommendations = results.get('recommendations') or ['None']
    print("\n--- Results ---")
    print("Diagnoses:", *diagnoses)
    print("Recommendations:", *recommendations)

if __name__ == "__main__":
    main()
