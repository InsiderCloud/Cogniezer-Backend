# Gunicorn configuration file
import multiprocessing
from dotenv import load_dotenv
import os

load_dotenv()

max_requests = 1000
max_requests_jitter = 50
port = os.getenv("PORT")

log_file = "-"

bind = f"0.0.0.0:{port}"

worker_class = "uvicorn.workers.UvicornWorker"
workers = 1