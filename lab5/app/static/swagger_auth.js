// static/swagger_auth.js

// Variable to store the CSRF token globally for use in the request interceptor
let csrfToken = null;

// Function to handle the token authorization in Swagger UI
function setAuthToken(accessToken, newCsrfToken) {
    if (window.ui && window.ui.authActions) {
        // 1. Store the CSRF token locally
        csrfToken = newCsrfToken;
        
        // 2. Set the Bearer token in the Swagger UI's authorization state
        window.ui.authActions.authorize({
            BearerAuth: {
                name: 'Authorization',
                schema: {
                    type: 'apiKey',
                    in: 'header',
                    name: 'Authorization',
                    description: 'Enter: Bearer <JWT token>'
                },
                value: `Bearer ${accessToken}` // The value needs to be in "Bearer <token>" format
            }
        });
        console.log("Swagger UI: Tokens successfully stored (Access and CSRF).");
    }
}

// Interceptor 1: Response Interceptor (For automatic pasting and CSRF storage)
window.swaggerResponseInterceptor = (response) => {
    // Check if the response is from a successful token generation endpoint
    if ((response.url.endsWith('/login') || response.url.endsWith('/register')) && 
        (response.status === 200 || response.status === 201)) {
        
        try {
            const json = JSON.parse(response.data);
            const accessToken = json.access_token;

            if (accessToken) {
                // To get the CSRF token, we must decode the JWT payload.
                // JWT format is header.payload.signature (base64 encoded)
                const payload = accessToken.split('.')[1];
                const decodedPayload = JSON.parse(atob(payload));
                const tokenCsrf = decodedPayload.csrf;

                if (tokenCsrf) {
                    setAuthToken(accessToken, tokenCsrf);
                }
            }
        } catch (e) {
            console.error("Error processing response for token/CSRF storage:", e);
        }
    }
    
    return response;
};

// Interceptor 2: Request Interceptor (For automatically adding Bearer and X-CSRF-TOKEN headers)
window.swaggerRequestInterceptor = (req) => {
    // 1. Add Bearer Token (Existing Logic)
    if (window.ui && req.url && req.method) {
        const security = window.ui.security().toJS();
        const bearerAuth = security.find(s => s.get('BearerAuth'));

        if (bearerAuth) {
            const tokenValue = bearerAuth.getIn(['BearerAuth', 'value']);
            if (tokenValue && tokenValue.startsWith('Bearer ')) {
                req.headers['Authorization'] = tokenValue;
            }
        }
    }
    
    // 2. Add CSRF Token (NEW LOGIC)
    // Check if the csrfToken has been stored and if this is a request that needs a body (like POST, PUT, DELETE)
    // Flask-JWT-Extended usually only requires CSRF for non-GET requests.
    if (csrfToken && req.method !== 'GET' && req.method !== 'OPTIONS' && req.method !== 'HEAD') {
        req.headers['X-CSRF-TOKEN'] = csrfToken;
        console.log("Swagger UI: Added X-CSRF-TOKEN header.");
    }
    
    return req;
};