from pages.page import page

from components.elements.html import html
from components.elements.body import body
from components.elements.para import para
from components.elements.div import div

from components.elements.script import script
from components.elements.button import button

from components.widgets.head_builder import head_builder

class index(page):
    def __init__(self):
        pass

    def __str__(self):
        # 로그인 상태 확인
        user_id = self.get_session("user_id")
        if user_id is None:
            # 로그인되지 않은 경우 로그인 페이지로 리다이렉트
            return self.redirect_to_login()
        
        # 로그인된 경우 기존 인덱스 페이지 표시
        with html(head_builder()) as _html:
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
        """로그인 페이지로 리다이렉트하는 HTML을 반환합니다."""
        redirect_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>리다이렉트 중...</title>
        </head>
        <body>
            <script>
                window.location.href = '/login';
            </script>
            <p>로그인이 필요합니다. 로그인 페이지로 이동 중...</p>
            <a href="/login">로그인 페이지로 이동</a>
        </body>
        </html>
        """
        return redirect_html
