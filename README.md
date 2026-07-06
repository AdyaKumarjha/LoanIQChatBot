LoanIQ AI Chatbot

An AI-powered Loan Portfolio Assistant built using FastAPI, HTML/CSS/JavaScript, Google Gemini API, and Machine Learning. The application provides business insights, loan analytics, predictive loan approval, and an intelligent chatbot capable of answering questions about a loan portfolio.

Features
AI Chatbot (Generative AI)
Natural language conversations
Portfolio insights
Executive summaries
Loan recommendations
Branch performance analysis
Risk analysis
Predictive AI
Predicts whether a loan is likely to be Approved or Rejected
Built using Random Forest Classifier
Uses loan attributes such as:
Region
Product
Customer Type
Loan Amount
Property Value
Bureau Score
FOIR
Analytics Dashboard

Displays:

Total Loan Cases
Approved Loans
Rejected Loans
High Risk Cases
Average Loan Amount
REST APIs

Provides APIs for:

Chat
Analytics
Prediction
Dataset Access
Tech Stack
Frontend
HTML5
CSS3
JavaScript (Vanilla)
Backend
FastAPI
Python
Machine Learning
Scikit-learn
Random Forest Classifier
LabelEncoder
AI
Google Gemini 2.5 Flash API
Data Processing
Pandas
NumPy
Deployment
Render (Backend)
Vercel (Frontend)
Clone Repository
https://github.com/AdyaKumarjha/LoanIQChatBot
Create Virtual Environment
python -m venv venv
Install Dependencies
pip install -r requirements.txt
Create a .env file (or update config.py) with your Gemini API key:
GEMINI_API_KEY=YOUR_API_KEY
Run Backend
uvicorn main:app --reload
Runs at

http://127.0.0.1:8000
Swagger API

http://127.0.0.1:8000/docs
Run Frontend
index.html
using

Live Server (VS Code)
Vercel
Any static web server

API Endpoints
POST /chat
{
    "message":"Give me portfolio summary"
}

Analytics Summary
GET /analytics/summary

Prediction
POST /predict
Example

{
  "Region":"North",
  "Product":"Home Loan",
  "Customer_Type":"Self Employed",
  "Loan_Amount":2500000,
  "Property_Value":3500000,
  "Bureau_Score":780,
  "FOIR_%":35
}

Response

{
  "prediction":"Approved"
}

AI Capabilities

The chatbot can answer questions such as:

Give portfolio summary
Which region has highest approvals?
Which loans are high risk?
Generate executive summary
Give business recommendations
Explain rejection trends
Analyze branch performance
Which product performs best?
Average loan amount
Approval ratio

Deployment

Backend

Deployed using Render
Example:
https://loaniq-chatbot.onrender.com

Frontend

Deployed using Vercel
Example:

https://loan-iq-chat-bot.vercel.app

Future Improvements
Microsoft Teams Integration
User Authentication
Database Integration (PostgreSQL/MySQL)
Chat History
PDF Report Generation
Power BI Dashboard Integration
Voice-based Chat
Role-based Access Control
Multi-language Support

Known Limitations
Uses Google Gemini Free Tier (subject to daily quota limits).
Prediction works only with categorical values present in the training dataset.
Currently uses an Excel dataset instead of a live database.

Author

Adya Kumar Jha
GitHub: https://github.com/AdyaKumarjha/LoanIQChatBot
