import flet as ft
from services.api_services import get_quizzes


def home_view(page, navigate, current_user):

    quizzes_list = ft.ListView(
        spacing=10,
        auto_scroll=True,
        height=400,
    )

    status_text = ft.Text("Cargando quizzes...")

    def load_quizzes():

        try:

            response = get_quizzes()

            if response.status_code == 200:

                quizzes = response.json()

                quizzes_list.controls.clear()

                for quiz in quizzes:

                    quizzes_list.controls.append(
                        ft.ElevatedButton(
                            f"{quiz['title']} ({quiz['subject']})",
                            width=300,
                        )
                    )

                status_text.value = f"{len(quizzes)} quizzes encontrados"

            else:
                status_text.value = "Error al cargar quizzes"

        except Exception as ex:
            status_text.value = str(ex)

        page.update()

    load_quizzes()

    return ft.Column(
        controls=[

            ft.Text(
                f"Bienvenido, {current_user['name']}!",
                size=24,
                weight="bold",
            ),

            ft.Divider(height=20),

            ft.Text(
                "Quizzes Disponibles",
                size=18,
                weight="bold",
            ),

            quizzes_list,
            status_text,

            ft.ElevatedButton(
                "Actualizar",
                on_click=lambda e: load_quizzes(),
            ),

            ft.TextButton(
                "Cerrar Sesión",
                on_click=lambda e: navigate["login"](),
            ),
        ],
        spacing=15,
        padding=20,
    )