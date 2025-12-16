from flask import Flask, render_template_string
import yaml
import os
from my_project.database import db
from my_project.sportsman.routes.__init__ import register_routes
from flasgger import Swagger
from flask_jwt_extended import JWTManager

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {"title": "My API", "version": "1.0"},
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter: Bearer <JWT token>"
        }
    }
}

# Custom Swagger UI with embedded JavaScript
CUSTOM_SWAGGER_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Swagger UI</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('flasgger.static', filename='swagger-ui.css') }}">
    <link rel="icon" type="image/png" href="{{ url_for('flasgger.static', filename='favicon-32x32.png') }}" sizes="32x32"/>
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="{{ url_for('flasgger.static', filename='swagger-ui-bundle.js') }}"></script>
    <script src="{{ url_for('flasgger.static', filename='swagger-ui-standalone-preset.js') }}"></script>
    <script>
        window.onload = function() {
            console.log('Swagger UI initializing...');
            
            const ui = SwaggerUIBundle({
                url: "{{ url_for('flasgger.apispec_1') }}",
                dom_id: '#swagger-ui',
                deepLinking: true,
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIStandalonePreset
                ],
                plugins: [
                    SwaggerUIBundle.plugins.DownloadUrl
                ],
                layout: "StandaloneLayout",
                
                // Request interceptor - adds Authorization + CSRF token
                requestInterceptor: (req) => {
                    console.log('🔵 Request interceptor called for:', req.url);
                    
                    const token = localStorage.getItem('jwt_token');
                    if (token) {
                        console.log('✅ Token found in localStorage');
                        req.headers['Authorization'] = 'Bearer ' + token;
                        
                        try {
                            // Decode JWT payload to extract CSRF
                            const payload = JSON.parse(atob(token.split('.')[1]));
                            console.log('📦 JWT Payload:', payload);
                            
                            if (payload.csrf) {
                                req.headers['X-CSRF-TOKEN'] = payload.csrf;
                                console.log('✅ Added X-CSRF-TOKEN header:', payload.csrf);
                            } else {
                                console.log('⚠️ No CSRF claim in token');
                            }
                        } catch (e) {
                            console.error('❌ Failed to parse JWT:', e);
                        }
                    } else {
                        console.log('⚠️ No token in localStorage');
                    }
                    
                    console.log('📤 Final request headers:', req.headers);
                    return req;
                },
                
                // Response interceptor - stores JWT after login
                responseInterceptor: (res) => {
                    console.log('🟢 Response interceptor called for:', res.url);
                    console.log('📥 Response status:', res.status);
                    
                    // Check if this is a login response with a token
                    if (res.obj && res.obj.access_token) {
                        localStorage.setItem('jwt_token', res.obj.access_token);
                        console.log('✅ Token stored in localStorage');
                        console.log('🔑 Token:', res.obj.access_token.substring(0, 50) + '...');
                        
                        // Decode and show the payload
                        try {
                            const payload = JSON.parse(atob(res.obj.access_token.split('.')[1]));
                            console.log('📦 Stored token payload:', payload);
                        } catch (e) {
                            console.error('❌ Failed to decode stored token:', e);
                        }
                    }
                    
                    return res;
                }
            });
            
            window.ui = ui;
            console.log('✅ Swagger UI initialized');
        };
    </script>
</body>
</html>
'''

def create_app():
    app = Flask(__name__)

    jwt = JWTManager()

    config_path = os.path.join(os.path.dirname(__file__), "../config/config.yml")
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = config.get('jwt_secret_key', 'nklnknl')
    
    # CRITICAL: Disable CSRF in JWT
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    
    db.init_app(app)
    jwt.init_app(app)
    register_routes(app)
    
    # Initialize Swagger with template
    swagger = Swagger(app, template=SWAGGER_TEMPLATE)
    
    # Override the Swagger UI route with custom HTML
    @app.route('/apidocs/')
    def custom_swagger_ui():
        return render_template_string(CUSTOM_SWAGGER_HTML)
    
    return app