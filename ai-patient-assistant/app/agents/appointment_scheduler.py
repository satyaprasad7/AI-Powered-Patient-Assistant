from app.services.ehr_service import EHRService

class AppointmentScheduler:

    def __init__(self):

        self.ehr = EHRService()

    def schedule(self, patient_name):

        slot = self.ehr.get_available_slots()[0]

        return self.ehr.book_appointment(
            patient_name,
            slot
        )