# In-Memory Library API

## 1. Project Title & Goal
A simple REST API built using FastAPI to manage a library's book inventory using in-memory storage.

## 2. Setup Instructions
1. Install dependencies:
   pip install -r requirements.txt
2. Run the application:
   uvicorn main:app --reload
3. Open Swagger UI:
   http://127.0.0.1:8000/docs

## 3. The Logic (How I thought)

**Why did I choose this approach?**  
I chose FastAPI because it is lightweight, fast, and provides automatic Swagger documentation, which makes testing REST APIs very easy. Since the requirement was strict in-memory storage, I used a Python list to store book records during runtime.

**What was the hardest bug you faced, and how did you fix it?**  
The hardest issue was handling duplicate book IDs. Initially, books with the same ID were being added multiple times. I fixed this by checking the existing in-memory list before inserting a new book and throwing an HTTP 400 error if a duplicate ID is found.

## 4. Output Screenshots
Below is the screenshot showing a successful GET request returning the list of books added using the API.

![API Output Screenshot](screenshot.png)

## 5. Future Improvements
If I had 2 more days, I would:
- Add update (PUT) functionality for books
- Add basic input validation and error logging
- Persist data using SQLite instead of in-memory storage
