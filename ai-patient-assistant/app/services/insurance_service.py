class InsuranceService:

    def verify_coverage(self, policy_id):

        return {
            "policy_id": policy_id,
            "coverage": "Active",
            "copay": "$25"
        }