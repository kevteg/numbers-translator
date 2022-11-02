from apps.translator.views.number_to_english import NumberToEnglish
from django.urls import path


urlpatterns = [
    path('', NumberToEnglish.as_view()),
]
