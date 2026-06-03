class SymptomChecker:

    def assess(self, symptoms):

        symptoms = symptoms.lower()

        if "chest pain" in symptoms:
            return {
                "severity": "HIGH",
                "recommendation":
                "Immediate consultation advised"
            }

        if "fever" in symptoms:
            return {
                "severity": "MEDIUM",
                "recommendation":
                "Monitor symptoms and consult doctor"
            }

        return {
            "severity": "LOW",
            "recommendation":
            "General observation"
        }