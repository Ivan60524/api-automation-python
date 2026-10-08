# API Test Automation - Python, Requests & Pytest

## 📌 Project Overview
This project contains an automated API testing suite built from scratch using **Python**, the **`requests`** library, and the **`pytest`** framework. It validates backend reliability by executing the full **CRUD** (Create, Read, Update, Delete) lifecycle against the Reqres API.

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Testing Framework:** Pytest
* **HTTP Client:** Requests library
* **Target API:** Reqres (https://reqres.in)
* **IDE:** Visual Studio Code (VS Code)

## 🧪 Automated Test Scenarios (`test_reqres.py`)
1. **`test_get_users_status_code` (Read):** Sends a GET request, asserts a `200 OK` status code, validates response time performance (< 1.0s), and parses JSON payloads to verify specific user data.
2. **`test_create_user` (Create):** Sends a POST request with a custom JSON payload (`Ivan Suarez Alva`, `Lead QA Automation Engineer`), asserts a `201 Created` status code, and verifies that the returned attributes match.
3. **`test_update_user` (Update):** Sends a PUT request to modify an existing resource, asserts a `200 OK` status code, and validates the updated job title in the response.
4. **`test_delete_user` (Delete):** Sends a DELETE request and validates a `204 No Content` status code.

## 🚀 How to Run This Project Locally
1. Clone this repository:
   ```bash
   git clone [https://github.com/Ivan60524/api-automation-python.git](https://github.com/Ivan60524/api-automation-python.git)
