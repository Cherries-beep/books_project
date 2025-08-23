INSTALLED_APPS = (
    'rest_framework',
    'drf_spectacular', # для генерации документации OpenAPI/Swager UI
    'books',
)

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}