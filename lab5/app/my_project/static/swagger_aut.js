
function setAuthToken(token) {
    if (window.ui && window.ui.authActions) {
        window.ui.authActions.authorize({
            BearerAuth: {
                name: 'Authorization',
                schema: {
                    type: 'apiKey',
                    in: 'header',
                    name: 'Authorization',
                    description: 'Enter: Bearer <JWT token>'
                },
                value: `Bearer ${token}` 
            }
        });
        console.log("Swagger UI: Token automatically authorized.");
    }
}

window.swaggerResponseInterceptor = (response) => {
    if (response.url.endsWith('/auth/login') && response.status === 200) {
        try {
            const json = JSON.parse(response.data);
            const accessToken = json.access_token;
            
            if (accessToken) {
                setAuthToken(accessToken);
            }
        } catch (e) {
            console.error("Error parsing login response for auto-auth:", e);
        }
    }
    
    if (response.url.endsWith('/auth/register') && response.status === 201) {
        try {
            const json = JSON.parse(response.data);
            const accessToken = json.access_token;
            
            if (accessToken) {
                setAuthToken(accessToken);
            }
        } catch (e) {
            console.error("Error parsing register response for auto-auth:", e);
        }
    }

    return response;
};


window.swaggerRequestInterceptor = (req) => {
    if (req.url && req.method) {
        const security = window.ui.security().toJS();

        const bearerAuth = security.find(s => s.get('BearerAuth'));

        if (bearerAuth) {
            const tokenValue = bearerAuth.getIn(['BearerAuth', 'value']);

            if (tokenValue && tokenValue.startsWith('Bearer ')) {
                req.headers['Authorization'] = tokenValue;
            }
        }
    }
    return req;
};