from .views import company_all, company_info, company_vacancies, vacancy_all, vacancy_info, top_vacancies

from django.urls import path

urlpatterns = [
    path('companies/', company_all),
    path('companies/<int:company_id>/', company_info),
    path('companies/<int:company_id>/vacancy/', company_vacancies),
    path('vacancies/', vacancy_all),
    path('vacancies/<int:vacancy_id>/', vacancy_info),
    path('vacancies/topten/', top_vacancies),
    
]