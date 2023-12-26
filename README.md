
# Advanced Django Rest Framework Learning

This is the project I am creating for learning the advanced DRF concepts 


## Installation

celery worker 

```bash
celery storefront -A worker --loglevel==info
```
Celery Beat (For Periodic tasks)
```bash
celery storefront -A beat
```

Monitoring Celery tasks - (Flower)
```bash
celery storefront -A flower
```

Automated testing
```bash
pytest
```

Automated continuous testing 
```bash
ptw  - (short for pytest watch)
```

Run Locust to test performance 
```bash
locust -f locustfiles/browse_products.py
```