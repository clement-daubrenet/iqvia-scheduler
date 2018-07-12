# iqvia-scheduler
A task scheduler

# Installation

- redis-server installed
- virtualenv env -p python3
- source env/bin/activate
- pip install -r requirements.txt

# Run locally

- contact API running on http://0.0.0.0:7000/ (or update config.py)
- redis-server running on localhost:6379 (or update config,py)
- Launch the worker: celery -A celery_worker:celery worker --loglevel=INFO
- Launch the beat: celery -A celery_worker:celery beat --loglevel=INFO

# The tasks

- The 2 tasks are in tasks/tasks.py
- This tasks are scheduled in celery_worker.py
