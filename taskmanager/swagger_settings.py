#from drf_yasg import openapi

# SWAGGER_SETTINGS = {
#     'SECURITY_DEFINITIONS': {
#         'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header',
#             'description': "JWT Authorization header using the Bearer scheme. Example: 'Bearer <your_token>'",
#         }
#     },
#     'USE_SESSION_AUTH': False,  # ✅ VERY IMPORTANT - disables CSRF/session login
#     'PERSIST_AUTH': True,       # ✅ optional: keeps token across reloads
# }

SPECTACULAR_SETTINGS = {
    'TITLE': 'Task Management API',
    'DESCRIPTION': 'API for managing tasks with JWT authentication.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,

    'SECURITY': [{'BearerAuth': []}],
    'COMPONENTS': {
        'securitySchemes': {
            'BearerAuth': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT',
            }
        }
    },
}