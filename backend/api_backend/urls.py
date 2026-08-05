from django.urls import path

from .views import (
    PredictView, HealthView,
    model_info, what_if_analysis,
    decision_boundary_data, sample_customers,
)

urlpatterns = [
    #  Production endpoints 
    path('predict/', PredictView.as_view(), name='predict'),
    path('health/', HealthView.as_view(), name='health'),

    #  Legacy endpoints (frontend compatibility) 
    path('model-info/', model_info, name='model_info'),
    path('what-if/', what_if_analysis, name='what_if_analysis'),
    path('decision-boundary/', decision_boundary_data, name='decision_boundary_data'),
    path('sample-customers/', sample_customers, name='sample_customers'),
]
