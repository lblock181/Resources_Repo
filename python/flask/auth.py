## https://blog.teclado.com/protecting-endpoints-in-flask-apps-by-requiring-login/

"""
 decorator for protecting routes
 withing flask app, use after route config @app.route('admin', method=['POST','GET'])
"""
def login_required(func) -> Callable:
        @functools.wraps(func)
        def secure_func(*args, **kwargs) -> Callable:
            if 'session' not in request.cookies or not ctrl.validate_user(request.cookies['session']):
                return redirect(url_for('api.login', next=request.url))
            return func(*args, **kwargs)
        return secure_func