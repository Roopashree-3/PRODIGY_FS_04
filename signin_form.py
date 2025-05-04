import flet as ft
class SignInForm:
    def __init__(self, submit_values, btn_signup):
        self.submit_values = submit_values
        self.btn_signup = btn_signup
        self.text_user = ft.TextField(label="User Name")
        self.text_password = ft.TextField(label="Password", password=True, can_reveal_password=True)

    def btn_signin(self, e):
        if not self.text_user.value:
            self.text_user.error_text = "Name cannot be blank!"
            self.text_user.update()
        if not self.text_password.value:
            self.text_password.error_text = "Password cannot be blank!"
            self.text_password.update()
        if self.text_user.value and self.text_password.value:
            self.submit_values(self.text_user.value, self.text_password.value)

    def build(self):
        signin_image = ft.Container(
            content=ft.Icon(name=ft.icons.PERSON, color=ft.colors.BLUE, size=100),
            width=120,
            height=120,
            bgcolor=ft.colors.BLACK45,
            border_radius=10,
        )
        return ft.Container(
            width=500,
            height=560,
            bgcolor=ft.colors.BLACK87,
            padding=30,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Column(
                [
                    signin_image,
                    ft.Text(value="Sign in", text_align=ft.TextAlign.CENTER, size=30),
                    self.text_user,
                    self.text_password,
                    ft.Container(height=10),
                    ft.ElevatedButton(
                        text="Sign in", color=ft.colors.WHITE, width=150, height=50, on_click=self.btn_signin
                    ),
                    ft.Container(height=20),
                    ft.Row(
                        controls=[
                            ft.Text(value="Don't have an account?"),
                            ft.TextButton(text="Sign Up Here", on_click=self.btn_signup)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    @property
    def view(self):
        return self.build()
