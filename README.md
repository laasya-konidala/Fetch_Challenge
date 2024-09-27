# Fetch Backend Challenge
This project is a simple API for managing point transactions from different payers. It allows users to add points, spend points, and retrieve their current point balance from different payers. 

### Features

**Add Points**: Add points from specific payers with a timestamp.

**Spend Points**: Spend points in a First-In-First-Out (FIFO) order based on the transaction timestamps.

**Retrieve Balance**: Retrieve the current balance of points for each payer.

### Prerequisites

Before running this project, make sure you have the following installed:

Python (Version 3.7 or higher)
If you don't have Python installed, you can download it from the official Python website: https://www.python.org/downloads/

pip (Python Package Manager)
This usually comes with Python, but if not, follow the instructions here to install it: https://pip.pypa.io/en/stable/installation/

### Step-by-Step Installation and Setup
1. Clone the repository to your local machine using git
<pre> ```bash curl -X POST "http://localhost:8000/add" --header "Content-Type: application/json" --data "{\"payer\": \"DANNON\", \"points\": 1000, \"timestamp\": \"2022-11-01T14:00:00Z\"}" ``` </pre>
First, clone the project to your local machine using git:

bash
Copy code
git clone https://github.com/your-repo/points-management-api.git
Navigate to the project directory:

bash
Copy code
cd points-management-api
2. Install Required Python Packages
Install the necessary dependencies using pip:

bash
Copy code
pip install fastapi uvicorn pydantic
This will install FastAPI for building the API, Uvicorn as the server, and Pydantic for request validation.

3. Run the FastAPI Server
Once everything is set up, you can run the server with Uvicorn:

bash
Copy code
uvicorn service:app --reload --host 0.0.0.0 --port 8000
The server will start at http://localhost:8000.
The --reload flag ensures that the server restarts automatically when you make changes during development.
The --host 0.0.0.0 makes it accessible on your network, and --port 8000 sets the port.
How to Use the API
You can interact with the API using curl or any HTTP client like Postman. Below are the available endpoints and their usage.

1. Add Points
Adds points from a payer with a timestamp.

Endpoint: POST /add
Request Body: JSON
Example request using curl:

bash
Copy code
curl -X POST "http://localhost:8000/add" \
     --header "Content-Type: application/json" \
     --data "{\"payer\": \"DANNON\", \"points\": 1000, \"timestamp\": \"2022-11-01T14:00:00Z\"}"
2. Spend Points
Spend points from the balance, following the FIFO rule based on the timestamps.

Endpoint: POST /spend
Request Body: JSON
Example request using curl:

bash
Copy code
curl -X POST "http://localhost:8000/spend" \
     --header "Content-Type: application/json" \
     --data "{\"points\": 500}"
Response: A list of payers and the points spent.
json
Copy code
[
  { "payer": "DANNON", "points": -100 },
  { "payer": "UNILEVER", "points": -200 }
]
Error Handling: If you try to spend more points than available, the API will return a 400 status code and a message "Not enough points to spend!".
3. Get Balance
Retrieve the current balance of points for each payer.

Endpoint: GET /balance
Response: JSON map of payer balances.
Example request using curl:

bash
Copy code
curl -X GET "http://localhost:8000/balance"
Response:
json
Copy code
{
  "DANNON": 1000,
  "UNILEVER": 0,
  "MILLER COORS": 5300
}
Example Usage
To add points to the account:

bash
Copy code
curl -X POST "http://localhost:8000/add" \
     --header "Content-Type: application/json" \
     --data "{\"payer\": \"DANNON\", \"points\": 1000, \"timestamp\": \"2022-11-01T14:00:00Z\"}"
To check the current balance:

bash
Copy code
curl -X GET "http://localhost:8000/balance"
To spend points:

bash
Copy code
curl -X POST "http://localhost:8000/spend" \
     --header "Content-Type: application/json" \
     --data "{\"points\": 20}"
Understanding the Code
core.py: This file contains the core business logic for adding, spending, and retrieving point balances.

add_points(payer, points, timestamp): Adds points for a payer.
spend_points(points): Spends points using FIFO (first-in, first-out) based on transaction time.
retrieve_balance(): Retrieves the current balance of points from all payers.
request_body.py: Contains Pydantic models for validating incoming request data.

AddPoints: Validates data for adding points (payer, points, timestamp).
SpendPoints: Validates the amount of points to spend.
main.py: Defines the API endpoints for adding points, spending points, and getting the current balance.
