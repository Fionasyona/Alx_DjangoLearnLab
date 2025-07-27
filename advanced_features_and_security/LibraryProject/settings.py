AUTH_USER_MODEL = 'accounts.CustomUser'

# ---------------------------------------
# HTTPS and Secure Communication Settings
# ---------------------------------------

# Force all traffic over HTTPS
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS

# Use HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply to subdomains
SECURE_HSTS_PRELOAD = True  # Allow domain to be included in browser preload lists

# Secure Cookies
SESSION_COOKIE_SECURE = True  # Session cookie only sent over HTTPS
CSRF_COOKIE_SECURE = True  # CSRF cookie only sent over HTTPS

# Additional Security Headers
X_FRAME_OPTIONS = 'DENY'  # Protect against clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME-sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filter in browsers

# Recommended in production to only accept cookies via HTTPS
CSRF_TRUSTED_ORIGINS = ['https://yourdomain.com']  # Update this to match your domain

# Ensure DEBUG is False in production!
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']  # Add your production domain/IP
