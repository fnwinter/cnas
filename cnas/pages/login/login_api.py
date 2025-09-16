import json
from flask import request, jsonify, session
from pages.page import page

class login_api(page):
    def __init__(self, filename="login.html"):
        super().__init__(filename)

    def check_login(self):
        try:
            # JSON 데이터 파싱
            print("check_login ??? ")
            data = request.get_json()
            print("data",data)
            
            if not data:
                return jsonify({
                    'success': False,
                    'message': '요청 데이터가 없습니다.'
                }), 400
            
            email = data.get('email')
            password = data.get('password')
            remember_me = data.get('rememberMe', False)
            print(email, password, remember_me)
            
            # 필수 필드 검증
            if not email or not password:
                return jsonify({
                    'success': False,
                    'message': '이메일과 비밀번호를 모두 입력해주세요.'
                }), 400
            
            # 로그인 검증 (임시 로직 - 실제로는 데이터베이스에서 확인)
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
    
    def verify_login(self, email, password):
        """
        로그인 검증 함수
        실제 구현에서는 데이터베이스에서 사용자 정보를 확인해야 합니다.
        현재는 임시로 하드코딩된 값으로 검증합니다.
        """
        # 임시 테스트 계정 (실제로는 데이터베이스에서 확인)
        test_accounts = {
            'fnwinter@gmail.com': 'test1234',
            'admin@cnas.com': 'admin123',
            'user@cnas.com': 'user123'
        }
        
        # 이메일과 비밀번호 확인
        if email in test_accounts and test_accounts[email] == password:
            return True
        
        return False
    def __str__(self):
        self.check_login()
        return self.html
