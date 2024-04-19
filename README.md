# wikipedia_loop
In Wikipedia, there is a well-known phenomenon called the "Wikipedia Loop," where clicking the first link in the main body text of a Wikipedia article .
# Wikipedia Loop Checker

This Django project implements a REST API endpoint that calculates the number of requests required to reach the "Philosophy" page from a given Wikipedia URL while recording the path of visited pages along the way.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/wikipedia-loop-checker.git
   ```

//Navigate to the project directory:

<!-- cd wikipedia-loop-checker
Create and activate a virtual environment (optional but recommended): -->

<!-- python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
Install the required dependencies: -->

<!--pip install -r requirements.txt
Usage
Start the Django development server:  -->

<!-- python manage.py runserver
Send a POST request to the /api/wikipedia-loop/ endpoint with the url parameter containing the Wikipedia URL to start the loop: -->

<!-- POST /api/wikipedia-loop/
Content-Type: application/json -->
