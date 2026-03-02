import secrets
from flask import request, jsonify, session
from pages.page import page
from util.config import CONFIG

class login_api(page):
    def __init__(self):
        pass

    def check_login(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify({
                    'success': False,
                    'message': 'No request data.'
                }), 200
            
            email = data.get('email')
            password = data.get('password')
            remember_me = data.get('rememberMe', False)

            # Validate required fields (password is client-sent hash)
            if not email or not password:
                return jsonify({
                    'success': False,
                    'message': 'Please enter both email and password.'
                }), 200
            
            if self.verify_login(email, password):
                # Store user info in session
                self.set_session('user_id', email)
                self.set_session('user_email', email)
                
                if remember_me:
                    # Keep logged in (extend session expiry)
                    session.permanent = True
                
                return jsonify({
                    'success': True,
                    'message': 'Login successful',
                    'user': {
                        'email': email
                    }
                }), 200
            else:
                return jsonify({
                    'success': False,
                    'message': 'Invalid email or password.'
                }), 200
                
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Server error: {str(e)}'
            }), 200
    
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
        return self.check_login()
