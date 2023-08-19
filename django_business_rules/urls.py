from __future__ import unicode_literals

from django.urls import re_path

from django_business_rules.views import BusinessRuleFormView, BusinessRuleListView


app_name = "django_business_rules"
urlpatterns = [
    re_path(
        r"^business-rule/$", BusinessRuleListView.as_view(), name="business-rule-list"
    ),
    re_path(
        r"^business-rule/(?P<pk>[0-9]+)/$",
        BusinessRuleFormView.as_view(),
        name="business-rule-form",
    ),
]
