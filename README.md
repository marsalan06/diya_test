---

# Healthcare Appointment System

This project is a Django-based REST API for managing healthcare appointments. It allows for the creation, management, and querying of Patients, Counsellors, and Appointments, ensuring that both patients and counsellors can only have one active appointment at a time.

## Features

- REST API for CRUD operations on Patients, Counsellors, and Appointments.
- Soft deletion for Patients, Counsellors, and Appointments.
- Active status filtering for listing endpoints.
- Constraints to ensure a user cannot have more than one active appointment.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/marsalan06/diya_test.git
cd healthproject
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Run the development server**

```bash
python manage.py runserver
```

The API should now be accessible at `http://127.0.0.1:8000/api/`.

## API Endpoints

### Patients

- **List Patients**: `GET /api/patients/`
- **Create Patient**: `POST /api/patients/`
- **Retrieve Patient**: `GET /api/patients/{id}/`
- **Update Patient**: `PUT /api/patients/{id}/`
- **Delete (Soft) Patient**: `DELETE /api/patients/{id}/`

### Counsellors

- **List Counsellors**: `GET /api/counsellors/`
- **Create Counsellor**: `POST /api/counsellors/`
- **Retrieve Counsellor**: `GET /api/counsellors/{id}/`
- **Update Counsellor**: `PUT /api/counsellors/{id}/`
- **Delete (Soft) Counsellor**: `DELETE /api/counsellors/{id}/`

### Appointments

- **List Appointments**: `GET /api/appointments/`
- **Create Appointment**: `POST /api/appointments/`
- **Retrieve Appointment**: `GET /api/appointments/{id}/`
- **Update Appointment**: `PUT /api/appointments/{id}/`
- **Delete (Soft) Appointment**: `DELETE /api/appointments/{id}/`

