# QR Code Generator Application

This project is a QR Code Generator application built using FastAPI. It provides a REST API for generating and retrieving QR codes, while storing metadata in a PostgreSQL database and utilizing Redis for caching. Additionally, it employs a Celery worker to manage expired QR codes.

## Features

- Generate QR codes using the `qrcode` library.
- Store QR code metadata in a PostgreSQL database.
- Cache QR code data using Redis for improved performance.
- Background task management with Celery for cleaning up expired QR codes.

## Project Structure

```
qr-code-generator-app
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes
│   │   │   └── qr_code.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── qr_code_service.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── session.py
│   ├── cache
│   │   ├── __init__.py
│   │   ├── redis_cache.py
│   ├── worker
│   │   ├── __init__.py
│   │   ├── celery_worker.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── config.py
│   └── types
│       └── index.py
├── alembic
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── README
├── celeryconfig.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── alembic.ini
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd qr-code-generator-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Update the database configuration in `src/utils/config.py`.
   - Run the Alembic migrations:
     ```
     alembic upgrade head
     ```

5. Start the Redis server and Celery worker:
   ```
   redis-server
   celery -A src.worker.celery_worker worker --loglevel=info
   ```

6. Run the FastAPI application:
   ```
   uvicorn src.api.main:app --reload
   ```

## Usage

- **Generate a QR Code**: Send a POST request to `/qr-code/generate` with the necessary data.
- **Retrieve a QR Code**: Send a GET request to `/qr-code/{id}` to get the QR code by its ID.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.