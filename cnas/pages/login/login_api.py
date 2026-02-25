import secrets
from flask import request, jsonify, session
from pages.page import page
from util.config import CONFIG

class login_api(page):
    def __init__(self, filename="login/htmls/login.html"):
        super().__init__(filename)

    def check_login(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify({
                    'success': False,
                    'message': '요청 데이터가 없습니다.'
                }), 400
            
            email = data.get('email')
            password = data.get('password')
            remember_me = data.get('rememberMe', False)

            # 필수 필드 검증 (password는 클라이언트에서 보낸 해시)
            if not email or not password:
                return jsonify({
                    'success': False,
                    'message': '이메일과 비밀번호를 모두 입력해주세요.'
                }), 400
            
            if self.verify_login(email, password):
                # 세션에 사용자 정보 저장
                self.set_session('user_id', email)
                self.set_session('user_email', email)
                
                if remember_me:
                    # 로그인 상태 유지 설정 (세션 만료 시간 연장)
                    session.permanent = True
                
                return jsonify({
                    'success': True,
                    'message': '로그인 성공',
                    'user': {
                        'email': email
                    }
                }), 200
            else:
                return jsonify({
                    'success': False,
                    'message': '이메일 또는 비밀번호가 올바르지 않습니다.'
                }), 401
                
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'서버 오류가 발생했습니다: {str(e)}'
            }), 500
    
    def verify_login(self, email: str, password_hash: str) -> bool:
        """Check admin_id (email) and compare client-sent hash with stored hash."""
        admin_id = CONFIG.get("admin_id")
        stored_hash = CONFIG.get("admin_password")

        print("password_hash", password_hash)
        print("stored_hash", stored_hash)
        
        if not admin_id or not stored_hash:
            return False
        if email.strip().lower() != admin_id.strip().lower():
            return False

        return secrets.compare_digest(password_hash, stored_hash)

    def __str__(self):
        self.check_login()
        return self.html
