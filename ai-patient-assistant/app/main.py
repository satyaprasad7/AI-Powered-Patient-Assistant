from app.agents.symptom_checker import SymptomChecker
from app.agents.appointment_scheduler import AppointmentScheduler
from app.agents.medical_faq import MedicalFAQ
from app.agents.insurance_advisor import InsuranceAdvisor

def run_patient_assistant(
        patient,
        symptoms,
        question,
        policy):

    symptom_agent = SymptomChecker()

    appointment_agent = AppointmentScheduler()

    faq_agent = MedicalFAQ()

    insurance_agent = InsuranceAdvisor()

    assessment = symptom_agent.assess(
        symptoms
    )

    appointment = appointment_agent.schedule(
        patient
    )

    answer = faq_agent.answer(
        question
    )

    insurance = insurance_agent.check(
        policy
    )

    return {
        "assessment": assessment,
        "appointment": appointment,
        "faq": answer,
        "insurance": insurance
    }

if __name__ == "__main__":

    output = run_patient_assistant(
        "Satya",
        "fever and chest pain",
        "What is chest pain?",
        "POL123"
    )

    print(output)