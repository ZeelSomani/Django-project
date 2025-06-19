# Django-project

# Book API
A Django RESTful API for managing books with file uploads and API key-based authentication.

## Setup Instructions
```bash
git clone <repo-url>
cd book_api
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Sample .env Format
```env
API_KEYS=valid-key
DEBUG=True
```

## API Key Configuration
API key is checked via `X-API-Key` header. Valid keys are set in the `.env` file like:
```env
API_KEYS=valid-key1,valid-key2
```

## Postman Tests
- Create Book (valid)
- Upload Cover Image
- Get Book with Cover
- Invalid API Key Access
- Upload Invalid File Type

