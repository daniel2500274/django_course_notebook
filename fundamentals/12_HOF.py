#funciones de orden superior,
#Reciben o retornan funciones.
def require_auth(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            return "Access Denied"
    return wrapper

def admin_dashboard(user):
    return f"Hallo welcome {user}"

auth_view_dashboard = require_auth(admin_dashboard)
print(auth_view_dashboard("admin"))
print(auth_view_dashboard("guest"))