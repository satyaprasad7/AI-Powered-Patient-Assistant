class EHRService:

    def get_available_slots(self):

        return [
            "2026-06-05 10:00 AM",
            "2026-06-05 02:00 PM",
            "2026-06-06 11:00 AM"
        ]

    def book_appointment(self, patient_name, slot):

        return {
            "patient": patient_name,
            "slot": slot,
            "status": "Confirmed"
        }