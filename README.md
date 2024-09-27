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
<pre> git clone https://github.com/laasya-konidala/Fetch_Challenge.git  </pre>
<pre> cd Fetch_Challenge  </pre>


2. Install Required Python Packages
<pre> pip install fastapi uvicorn pydantic </pre>
This will install FastAPI for building the API, Uvicorn as the server, and Pydantic for request validation.

3. Run the FastAPI Server
Once everything is set up, you can run the server with Uvicorn in your terminal:
<pre> uvicorn service:app --reload --host 0.0.0.0 --port 8000 </pre>

### How to Use the API
You can interact with the API using curl requests. Below are the available endpoints and their usage.

1. Add Points: adds points from a payer at a timestamp.

Endpoint: POST /add

Example request using curl:

<pre> curl -X POST "http://localhost:8000/add" \
     --header "Content-Type: application/json" \
     --data "{\"payer\": \"DANNON\", \"points\": 1000, \"timestamp\": \"2022-11-01T14:00:00Z\"}" </pre>
     
2. Spend Points: spend points from the balance, following the FIFO rule based on the timestamps.

Endpoint: POST /spend

Example request using curl:

<pre> curl -X POST "http://localhost:8000/spend" \
     --header "Content-Type: application/json" \
     --data "{\"points\": 500}" </pre>
     
Response: A list of payers and the points spent.

<pre> [
  { "payer": "DANNON", "points": -100 },
  { "payer": "UNILEVER", "points": -200 }
] </pre>

Error Handling: If you try to spend more points than available, the API will return a 400 status code and a message "Not enough points to spend!".

3. Get Balance: retrieve the current balance of points for each payer.

Endpoint: GET /balance

Example request using curl:

<pre> curl -X GET "http://localhost:8000/balance" </pre>
 
Response:
<pre> {
  "DANNON": 1000,
  "UNILEVER": 0,
  "MILLER COORS": 5300
}  </pre>

### Understanding the Code
core.py: This file contains the core business logic for adding, spending, and retrieving point balances.

request_body.py: Contains Pydantic models for validating incoming request data.

service.py: Defines the API endpoints for adding points, spending points, and getting the current balance.
