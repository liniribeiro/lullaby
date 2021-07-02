from lullaby.settings import PORT

bind = f"0.0.0.0:{PORT}"
workers = 2
worker_connections = 1000
max_requests = int(workers * worker_connections)
keepalive = 2
max_requests_jitter = 5
timeout = 40
