import flet as ft


def login_view(page, navigate, set_user):

    username_input = ft.TextField(
        label="Usuario",
        width=300,
    )

    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        width=300,
    )

    status_text = ft.Text("", size=12, color="red")

    def handle_login(e):

        username = username_input.value.strip()
        password = password_input.value.strip()

        if not username or not password:
            status_text.value = "Completa todos los campos"
            page.update()
            return

        status_text.value = "Iniciando sesión..."
        page.update()

        # Login simulado
        set_user(
            {
                "name": username,
            },
            1,
        )

        navigate["home"]()

    return ft.Column(
        controls=[
            ft.Text(
                "LogiMath",
                size=32,
                weight="bold",
            ),

            ft.Divider(height=20),

            username_input,
            password_input,
            status_text,

            ft.ElevatedButton(
                "Iniciar Sesión",
                width=300,
                on_click=handle_login,
            ),

            ft.TextButton(
                "¿No tienes cuenta? Regístrate",
                on_click=lambda e: navigate["register"](),
            ),
        ],
        horizontal_alignment="center",
        alignment="center",
        spacing=15,
    )