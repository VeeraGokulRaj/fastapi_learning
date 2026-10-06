"""
Production settings for fastapi-learning project.
"""

from .base import *  # noqa: F403
from .base import SITE_URL, env


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = "DENY"
USE_X_FORWARDED_HOST = True

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=[SITE_URL],
)
