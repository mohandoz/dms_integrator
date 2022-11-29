from auth import fastapi_users

current_active_admin = fastapi_users.current_user(active=True, superuser=True)

current_active_user = fastapi_users.current_user(active=True)
