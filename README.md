# API-ENDPOINT
# BE-01: Build Your First API Endpoint

A simple FastAPI application built as part of the Backend AI Engineering Track.

## Tech Stack

* Python 3
* FastAPI
* Uvicorn

## Project Structure

```text
API-ENDPOINT/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/gopaljee302/API-ENDPOINT.git
cd API-ENDPOINT
```

2. Create and activate a virtual environment:

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The server will be available at:

```
http://127.0.0.1:8000
```

## API Endpoints

### GET /

Returns a welcome message.

**Response**

```json
{
  "message": "Hello Backend AI Engineering!"
}
```

### GET /health

Returns the application health status.

**Response**

```json
{
  "status": "ok"
}
```

## Interactive API Documentation

FastAPI automatically generates API documentation.

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

## Testing

Using PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/
Invoke-RestMethod http://127.0.0.1:8000/health
```

Or using curl:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
```

## Author

**Gopal Jee**

Backend AI Engineering Track – Week 1 (BE-01)
