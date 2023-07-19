import multiprocessing

# Flask application module
app = 'app:app'  # Replace 'app' with the name of your Flask application object (e.g., 'myapp:app')

# Gunicorn config
bind = '127.0.0.1:8000'  # Replace with the IP address and port you want to bind Gunicorn to
workers = multiprocessing.cpu_count() * 2 + 1  # Number of Gunicorn worker processes
threads = 2  # Number of threads per worker (optional, only for synchronous workers)
worker_class = 'gthread'  # 'gthread' for synchronous workers (requires the 'gevent' library) or 'sync' for asynchronous workers
timeout = 60  # Timeout for worker connections
keepalive = 2  # Number of seconds to keep an idle connection open
max_requests = 1000  # Number of requests a worker will process before restarting
accesslog = '-'  # '-' to log to stdout, or a filename for access logs
errorlog = '-'  # '-' to log to stderr, or a filename for error logs
loglevel = 'info'  # Log level ('debug', 'info', 'warning', 'error', 'critical')

# SSL configuration (optional, uncomment if you want to use SSL)
# keyfile = 'path/to/your/ssl/keyfile.pem'
# certfile = 'path/to/your/ssl/certfile.pem'
