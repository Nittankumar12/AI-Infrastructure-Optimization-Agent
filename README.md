# 🚀 Azure Infrastructure Optimizer (AI-Powered)

This project is a **full-stack application** that helps organizations optimize their cloud infrastructure costs and performance using **AI-powered recommendations from Groq**. It consists of:

- **Frontend (React.js)**: Upload infrastructure & usage data and submit a prompt.
- **Backend (Spring Boot - Java)**: Processes uploaded CSV files, interacts with Groq API, and returns recommendations.
- **AI Integration (Groq API)**: Analyzes infrastructure & usage patterns and provides AI-powered suggestions.

---

## 📌 Features

✅ Upload **infrastructure** and **usage** CSV files  
✅ Submit a **prompt** for AI-powered analysis  
✅ Backend processes & merges data  
✅ AI model suggests **cost & performance optimizations**  
✅ **Real-time response from Groq API**  
✅ Clean & structured recommendations  

---

## 🚀 Setup Instructions

### 🛠️ 1. Prerequisites

Ensure you have the following installed:

- [Node.js](https://nodejs.org/) (For React Frontend)
- [Java 17+](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) (For Spring Boot Backend)
- [Maven](https://maven.apache.org/) (To build Java Backend)
- [Python 3](https://www.python.org/) (For testing Groq API)
- **Groq API Key** (Sign up at [Groq](https://groq.com/) and get your key)

---

### 🖥️ 2. Backend Setup (Spring Boot API)

1️⃣ Navigate to the `backend` folder:
cd backend

2️⃣ Create a .env file and add your Groq API Key:
GROQ_API_KEY=your_groq_api_key_here

3️⃣ Build & Run the Backend:
mvn clean install
mvn spring-boot:run
📌 Backend will be running at: http://localhost:8080

🎨 3. Frontend Setup (React UI)

1️⃣ Navigate to frontend folder:
cd frontend

2️⃣ Install dependencies:
npm install

3️⃣ Start the React app:
npm start
📌 Frontend will be running at: http://localhost:3000

🧪 4. Testing AI Recommendations with Python

1️⃣ Navigate to the project root folder
2️⃣ Run the Python script with sample CSV files:
python test_groq.py
3️⃣ Modify test_groq.py to use your own CSV files.

🔗 API Endpoints
POST	/api/optimize	Upload CSV files & receive AI recommendations

🧠 How It Works
User uploads two CSV files (infrastructure.csv, usage.csv).
User submits a prompt (e.g., "Help me optimize my infrastructure").
Backend processes data and sends it to Groq API.
Groq AI analyzes the organization’s infrastructure & usage.
AI provides cost & performance optimization suggestions.


🔥 Sample Response from Groq AI
**AI Recommendations:**
1. Reduce VM count by 20% for cost savings.
2. Switch to Spot VMs for non-critical workloads.
3. Optimize PostgreSQL queries to reduce database latency.
4. Enable MFA for admin users to improve security.

📂 Sample CSV Files
Find sample data in the demo data/ folder


