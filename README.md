# Fetch Backend Challenge 🚀
This project is a simple API for managing point transactions from different payers. It allows users to add points, spend points, and retrieve their current point balance from different payers. Below is a guide to help you set it up and interact with the API smoothly.

### Features ✨

**Add Points**: Add points from specific payers, associated with a timestamp.  
**Spend Points**: Spend points in a First-In-First-Out (FIFO) order based on the transaction timestamps.  
**Retrieve Balance**: Retrieve the current balance of points for each payer.

---

### Prerequisites 🛠️

Before running this project, make sure you have the following installed:

- **Python (Version 3.7 or higher)**: You can download Python from the official [Python website](https://www.python.org/downloads/).  
- **pip (Python Package Manager)**: pip usually comes with Python. If it’s not installed, you can follow the instructions [here](https://pip.pypa.io/en/stable/installation/).

---

### Step-by-Step Installation and Setup ⚙️

#### 1. Clone the Repository  
To start, clone the repository to your local machine using git and navigate into the project folder:

<pre>
  <code id="code1">git clone https://github.com/laasya-konidala/Fetch_Challenge.git</code>
  <button onclick="copyToClipboard('#code1')">Copy</button>
</pre>

<pre>
  <code id="code2">cd Fetch_Challenge</code>
  <button onclick="copyToClipboard('#code2')">Copy</button>
</pre>

<script>
function copyToClipboard(element) {
  var $temp = document.createElement("textarea");
  document.body.appendChild($temp);
  $temp.value = document.querySelector(element).textContent;
  $temp.select();
  document.execCommand("copy");
  document.body.removeChild($temp);
}
</script>


> *The first command downloads the project to your machine, and the second command moves you into the project directory.*

---

#### 2. Install Required Python Packages 📦  
Install the necessary Python packages using pip to get the project dependencies installed:

<pre> pip install fastapi uvicorn pydantic </pre>

> *This command installs FastAPI (for the API), Uvicorn (for the server), and Pydantic (for request validation).*

---

#### 3. Run the FastAPI Server 🚀  
After installing the dependencies, run the server using Uvicorn:

<pre> python -m uvicorn service:app --reload --host 0.0.0.0 --port 8000 </pre>

> *The server will run on your local machine at port 8000, and the `--reload` flag allows hot reloading during development.*

---

### How to Use the API 🖥️  
You can interact with the API using curl requests. Below are the available endpoints and how to use them:

#### Add Points: Adds points from a payer at a timestamp.

- **Endpoint**: POST /add

<pre> curl -X POST \"http://localhost:8000/add\" \  
     --header \"Content-Type: application/json\" \  
     --data \"{\\\"payer\\\": \\\"DANNON\\\", \\\"points\\\": 1000, \\\"timestamp\\\": \\\"2022-11-01T14:00:00Z\\\"}\" </pre>

---

#### Spend Points: Spend points from the balance, following the FIFO rule based on the timestamps.

- **Endpoint**: POST /spend

<pre> curl -X POST \"http://localhost:8000/spend\" \  
     --header \"Content-Type: application/json\" \  
     --data \"{\\\"points\\\": 500}\" </pre>

---

#### Get Balance: Retrieve the current balance of points for each payer.

- **Endpoint**: GET /balance

<pre> curl -X GET \"http://localhost:8000/balance\" </pre>

---

### Understanding the Code 📂

- **core.py**: This file contains the core business logic for adding, spending, and retrieving point balances.  
- **request_body.py**: Contains Pydantic models for validating incoming request data.  
- **service.py**: Defines the API endpoints for adding points, spending points, and retrieving the current balance.
