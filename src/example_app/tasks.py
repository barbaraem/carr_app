from src.config.celery import app


@app.task
def celery_integration_test_task():
    return 1 / 0
