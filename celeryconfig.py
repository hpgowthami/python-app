from celery import Celery

celery_app = Celery(
    'qr_code_generator',
    broker='redis://localhost:6379/0',
    backend='db+postgresql://user:password@localhost/dbname',
)

celery_app.conf.update(
    task_routes={
        'worker.celery_worker.clean_expired_qr_codes': 'default',
    },
    result_expires=3600,
)