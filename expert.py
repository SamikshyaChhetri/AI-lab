class Symptom:
    def __init__(self, name, question):
        self.name = name
        self.question = question

class Rule:
    def __init__(self, symptoms, condition):
        self.symptoms = symptoms
        self.condition = condition

class ExpertSystem:
    def __init__(self, symptoms, rules):
        self.symptoms = symptoms
        self.rules = rules

    def ask_questions(self):
        answers = {}
        for symptom in self.symptoms:
            answer = input(symptom.question + " (yes/no): ").lower()
            while answer not in ['yes', 'no']:
                print("Please enter 'yes' or 'no'.")
                answer = input(symptom.question + " (yes/no): ").lower()
            answers[symptom.name] = (answer == 'yes')
        return answers

    def diagnose(self, answers):
        for rule in self.rules:
            if all(answers[symptom] for symptom in rule.symptoms):
                return rule.condition
        return "Unknown"

# Define symptoms
symptom1 = Symptom("fever", "Do you have a fever?")
symptom2 = Symptom("cough", "Do you have a cough?")
symptom3 = Symptom("fatigue", "Do you feel tired or fatigued?")

# Define rules
rule1 = Rule(["fever", "cough"], "You may have a cold.")
rule2 = Rule(["fever", "fatigue"], "You may have the flu.")

# Create the expert system
symptoms = [symptom1, symptom2, symptom3]
rules = [rule1, rule2]
expert_system = ExpertSystem(symptoms, rules)

# Run the expert system
print("Please answer the following questions:")
answers = expert_system.ask_questions()
diagnosis = expert_system.diagnose(answers)
print("Diagnosis:", diagnosis)
