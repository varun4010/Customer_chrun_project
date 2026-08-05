"""
serializers.py — DRF input validation for customer churn prediction.

Validates all 13 raw customer input fields before they reach feature
engineering or the ML pipeline.
"""

from rest_framework import serializers


class CustomerDataSerializer(serializers.Serializer):
    """
    Validates a single customer record for churn prediction.

    Field names use camelCase (API contract). The helper method
    `to_model_input()` maps them to the internal column names that
    feature_engineering.py and the sklearn pipeline expect.
    """

    CreditScore = serializers.IntegerField(min_value=300, max_value=900)
    Geography = serializers.ChoiceField(choices=['France', 'Germany', 'Spain'])
    Gender = serializers.ChoiceField(choices=['Male', 'Female'])
    Age = serializers.IntegerField(min_value=18, max_value=100)
    Tenure = serializers.IntegerField(min_value=0, max_value=10)
    Balance = serializers.FloatField(min_value=0)
    NumOfProducts = serializers.IntegerField(min_value=1, max_value=4)
    HasCrCard = serializers.IntegerField(min_value=0, max_value=1)
    IsActiveMember = serializers.IntegerField(min_value=0, max_value=1)
    EstimatedSalary = serializers.FloatField(min_value=0)
    SatisfactionScore = serializers.IntegerField(min_value=1, max_value=5)
    CardType = serializers.ChoiceField(
        choices=['SILVER', 'GOLD', 'PLATINUM', 'DIAMOND'],
    )
    PointEarned = serializers.IntegerField(min_value=0)

    def to_model_input(self) -> dict:
        """
        Convert validated API payload to the dict format expected by the
        pipeline (i.e. the column names in the training CSV).

        Must be called *after* `.is_valid()`.
        """
        d = self.validated_data
        return {
            'CreditScore': d['CreditScore'],
            'Geography': d['Geography'],
            'Gender': d['Gender'],
            'Age': d['Age'],
            'Tenure': d['Tenure'],
            'Balance': d['Balance'],
            'NumOfProducts': d['NumOfProducts'],
            'HasCrCard': d['HasCrCard'],
            'IsActiveMember': d['IsActiveMember'],
            'EstimatedSalary': d['EstimatedSalary'],
            'Satisfaction Score': d['SatisfactionScore'],
            'Point Earned': d['PointEarned'],
            'Card Type': d['CardType'],
        }
