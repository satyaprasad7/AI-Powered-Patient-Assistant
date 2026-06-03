from app.services.insurance_service import InsuranceService

class InsuranceAdvisor:

    def __init__(self):

        self.service = InsuranceService()

    def check(self, policy_id):

        return self.service.verify_coverage(
            policy_id
        )