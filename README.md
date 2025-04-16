# Olive-challenge

Integration of Dog Breeds list to display using Django and external API.

## Prerequisites

### Option A: Using Docker
- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed (usually included with Docker Desktop).

### Option B: Without Docker
- Python 3.8 or later installed
- [pip](https://pip.pypa.io/en/stable/installation/)
- (Recommended) Virtualenv

---

## Steps to Run the Application

### 1. Clone the Repository

```
git clone https://github.com/rohanmandhanya/dog-breeds.git
cd dog-breeds
```

### 2. Run the Application Using Docker Compose
```
docker-compose up
```
The web app will be exposed on port 8000, and the endpoints will be accessible at http://localhost:8000

### 3. Run the Application without Docker
#### a. Set up virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### b. Install dependencies
```
pip install -r requirements.txt
```

#### c. Apply migrations (no models, but standard Django setup)
```
python manage.py migrate
```

#### d. Run the Django development server
```
python manage.py runserver
```

The web app will be exposed on port 8000, and the endpoints will be accessible at http://localhost:8000