from pages.page import page

from components.elements.html import html
from components.elements.body import body
from components.elements.para import para
from components.elements.div import div

from components.elements.script import script
from components.elements.button import button

from components.widgets.head_widget import head_widget

class index(page):
    def __init__(self):
        pass

    def __str__(self):
        # Check login state
        user_email = self.get_session("user_email")
        if user_email is None:
            # Not logged in: redirect to login page
            return self.redirect_to_login()
        
        # Logged in: show index page
        with html(head_widget()) as _html:
            with body() as _body:
                _body.append(para(content="index"))
                _body.append(
                    script(
                        type_="py",
                        src="static/main.py",
                        config="static/pyscript.toml"
                    )
                )
                _body.append(
                    button(
                        id_="get_joke",
                        py_click="get_joke"
                    ).set_content("button")
                )
                _body.append(
                    div(
                        id_="jokes"
                    )
                )

            _html.append(_body)
            return str(_html)
    
    def redirect_to_login(self):
        """Return HTML that redirects to the login page."""
        redirect_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Redirecting...</title>
        </head>
        <body>
            <script>
                window.location.href = '/login';
            </script>
            <p>Login required. Redirecting to login page...</p>
            <a href="/login">Go to login page</a>
        </body>
        </html>
        """
        return redirect_html
