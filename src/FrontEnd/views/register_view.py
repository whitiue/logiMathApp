import flet as ft
from services.api_services import create_user


def register_view(page, navigate):

    name_input = ft.TextField(label="Nombre", width=300)

    email_input = ft.TextField(label="Email", width=300)

    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        width=300,
    )

    status_text = ft.Text("", size=12, color="red")

    def handle_register(e):

        name = name_input.value.strip()
        email = email_input.value.strip()
        password = password_input.value.strip()

        if not name or not email or not password:
            status_text.value = "Completa todos los campos"
            page.update()
            return

        try:

            response = create_user(name, email)

            if response.status_code == 200:
                status_text.value = "Registro exitoso"
            else:
                status_text.value = "Error en el registro"

        except Exception as ex:
            status_text.value = str(ex)

        page.update()

    return ft.Column(
        controls=[
            ft.Text(
                "Crear Cuenta",
                size=28,
                weight="bold",
            ),

            ft.Divider(height=20),

            name_input,
            email_input,
            password_input,
            status_text,

            ft.ElevatedButton(
                "Registrarse",
                width=300,
                on_click=handle_register,
            ),

            ft.TextButton(
                "Volver",
                on_click=lambda e: navigate["login"](),
            ),
        ],
        horizontal_alignment="center",
        alignment="center",
        spacing=15,
    )