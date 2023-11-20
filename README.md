# :rocket: Hostel WiFi Feedback System

## Introduction

In response to persistent WiFi issues within our hostels, the Hostel WiFi Feedback System has been developed as a streamlined solution. This system aims to simplify the process of reporting problems, ensuring prompt resolutions, and ultimately enhancing the internet experience for students.

## Key Features

### 1. User-Friendly Portals

- **Separate Logins:** The system provides distinct logins for administrators, wardens, and students, ensuring a tailored user experience.

### 2. :computer: Student Complaints

- **Easy Reporting:** Students can effortlessly report WiFi issues such as slow speeds or disconnections through a user-friendly interface.

### 3. :clipboard: Warden Verification

- **Preventing Duplicates:** Wardens play a crucial role in reviewing and confirming reported issues, thereby avoiding the duplication of efforts.

### 4. :rocket: Fast Resolution

- **Administrative Action:** Administrators and Hostel Chiefs are equipped to swiftly address problems reported by students, providing timely updates on issue resolution.

## Benefits

- **Simplicity:** The system is designed for easy navigation and use by all stakeholders involved.
  
- **Transparency:** Students have the ability to track the progress of their reported complaints, promoting a transparent communication channel.

## Technology Stack

- **Language:** Python
- **Database:** MySQL
- **Framework:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Hosting:** [pythonanywhere.com](https://www.pythonanywhere.com/)

## Next Generation Database Systems

Utilizing modern technologies for data management, the system incorporates a robust database system to ensure efficiency and scalability.

## :zap: Student Workflow

| Step | Action          | Description                                           |
|------|------------------|-------------------------------------------------------|
| 1    | :rocket: Start Page       | Begin at the start page.                               |
| 2    | :man_student: Student Login    | Log in with student credentials.                       |
| 3    | :bar_chart: Student Dashboard| Access the student dashboard.                           |
| 4    | :mega: Report WiFi Issue| Click on "Report WiFi Issue" to open the complaint form.|
| 5    | :pencil: Complaint Form   | Fill out the complaint form with issue details.        |
| 6    | :rocket: Submit Complaint | Submit the complaint to the system.                    |
| 7    | :white_check_mark: Confirmation Page| Receive a confirmation message.                        |
| 8    | :door: Logout           | Log out from the system.                                |
| 9    | :checkered_flag: End Page         | Reach the end of the workflow.                          |

## :clipboard: Warden Workflow

| Step | Action           | Description                                           |
|------|-------------------|-------------------------------------------------------|
| 1    | :rocket: Start Page        | Begin at the start page.                               |
| 2    | :man_office_worker: Warden Login      | Log in with warden credentials.                         |
| 3    | :bar_chart: Warden Dashboard  | Access the warden dashboard.                            |
| 4    | :mag: Verify Complaint  | Review and verify student complaints.                  |
| 5    | :white_check_mark: Verification Complete | Mark the complaint as verified.                    |
| 6    | :mega: Confirmation Page | Receive a confirmation message.                        |
| 7    | :door: Logout            | Log out from the system.                                |
| 8    | :checkered_flag: End Page          | Reach the end of the workflow.                          |

## :gear: Admin Workflow

| Step | Action            | Description                                           |
|------|--------------------|-------------------------------------------------------|
| 1    | :rocket: Start Page         | Begin at the start page.                               |
| 2    | :man_technologist: Admin Login        | Log in with admin credentials.                          |
| 3    | :bar_chart: Admin Dashboard    | Access the admin dashboard.                             |
| 4    | :mag: Resolve Complaint  | Review and resolve student complaints.                 |
| 5    | :white_check_mark: Complaint Resolved  | Mark the complaint as resolved.                         |
| 6    | :pencil: Update Status      | Update the status of the complaint.                    |
| 7    | :mega: Confirmation Page  | Receive a confirmation message.                        |


# Hostel WiFi Feedback System

## Introduction

In response to persistent WiFi issues within our hostels, the Hostel WiFi Feedback System has been developed as a streamlined solution. This system aims to simplify the process of reporting problems, ensuring prompt resolutions, and ultimately enhancing the internet experience for students.

## Project Structure


This structure represents the organization of the Hostel WiFi Feedback System project.

**Key Directories and Files:**
- `registration/`: Django project folder.
  - `manage.py`: Django management script.
  - `registration/`: Django app folder.
    - `__init__.py`: Python package initialization file.
    - `settings.py`: Django project settings.
    - `urls.py`: URL configurations.
    - `asgi.py` and `wsgi.py`: ASGI and WSGI entry points.

- `app/`: Django app folder.
  - `__init__.py`: Python package initialization file.
  - `admin.py`: Django admin configurations.
  - `apps.py`: Django app configurations.
  - `migrations/`: Folder for database migrations.
  - `models.py`: Django models for the app.
  - `tests.py`: Unit tests for the app.
  - `views.py`: Django views for the app.

- `requirements.txt`: List of project dependencies.
- `README.md`: Project documentation.

| 8    | :door: Logout             | Log out from the system.                                |
| 9    | :checkered_flag: End Page           | Reach the end of the workflow.                          |


This comprehensive documentation outlines the Hostel WiFi Feedback System, covering its introduction, key features, benefits, technology stack, and detailed workflows for students, wardens, and administrators. The system promises to address WiFi issues effectively, ensuring a seamless internet experience for all hostel residents. :rocket:



## Prerequisites
Before running the project, make sure you have the following installed:

- Python
- Django

## Setup Instructions
1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/wifi_feedback.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd wifi_feedback
    ```

3. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup
5. **Apply migrations:**
    ```bash
    python registration/manage.py migrate
    ```

## Run the Development Server
6. **Start the development server:**
    ```bash
    python registration/manage.py runserver
    ```
    The project will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Access the Application
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **App URL:** [http://127.0.0.1:8000/app/](http://127.0.0.1:8000/app/)

## Stop the Development Server
7. **To stop the development server, press `Ctrl+C` in the terminal.**

## Deactivate the Virtual Environment
8. **If you used a virtual environment, deactivate it:**
    ```bash
    deactivate
    ```
##You can download the report at
[Download PDF](https://github.com/SHRISHRIKANT/Wifi_feedback/blob/main/205223006_project.pdf)

Now, you have successfully set up and run the Hostel WiFi Feedback System. Feel free to explore the application and make any necessary configurations for your specific use case.
