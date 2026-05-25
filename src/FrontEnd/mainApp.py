import flet as ft
from typing import Optional

from views.home_view import home_view
from views.login_view import login_view
from views.register_view import register_view

class LogiMathApp:
    # ================== APP PRINCIPAL ================== #
    def __init__(self):
        self.current_user: Optional[dict] = None
        self.current_user_id: Optional[int] = None

    def run(self):
        ft.app(target=self.main)

    def set_user(self, user, user_id):
        self.current_user = user
        self.current_user_id = user_id

    def main(self, page: ft.Page):

        page.title = "LogiMath"

        page.window_width = 400
        page.window_height = 750

        def go_to_login():
            page.clean()

            page.add(
                login_view(
                    page,
                    self.navigate,
                    self.set_user,
                )
            )

            page.update()

        def go_to_register():
            page.clean()

            page.add(
                register_view(
                    page,
                    self.navigate,
                )
            )

            page.update()

        def go_to_home():
            page.clean()

            page.add(
                home_view(
                    page,
                    self.navigate,
                    self.current_user,
                )
            )

            page.update()

        self.navigate = {
            "login": go_to_login,
            "register": go_to_register,
            "home": go_to_home,
        }

        go_to_login()


if __name__ == "__main__":
    app = LogiMathApp()
    app.run()