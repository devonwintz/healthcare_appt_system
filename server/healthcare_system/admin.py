from django.contrib import admin
from django.apps import apps

# Get all models
models = apps.get_app_config('healthcare_system').get_models()

# Loop through models and register each
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass