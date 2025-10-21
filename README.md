# Nutrition-Assistant
🧠 AI Nutrition Assistant

An AI-powered Nutrition Assistant that analyzes food images and provides personalized dietary insights using cutting-edge computer vision and language understanding models.

Built for speed, accuracy, and scalability, this project integrates a Vision Transformer (ViT) for food recognition and Google Gemini API for conversational diet analysis — all wrapped in a modern Streamlit interface.

🚀 Features

🍽️ Food Recognition: Detects and classifies dishes from food images using a fine-tuned ViT model (88% accuracy on Food-101).

🗣️ Natural Language Queries: Leverages Google Gemini API to handle user questions and generate dietary recommendations in real time.

⚡ Optimized Performance: Utilizes Redis caching and session management to reduce API latency by 40%.

📊 Dietary History & Analytics: Tracks user dietary history and trending food data through optimized PostgreSQL and Redis interactions.

🌐 Interactive UI: Built with Streamlit for a clean, responsive, and user-friendly web interface.

🏗️ System Architecture
User (Streamlit UI)
        │
        ▼
REST API (FastAPI / Flask)
        │
 ┌──────┴────────┐
 │ Vision Model  │── ViT (Hugging Face)
 │ NLP Model     │── Google Gemini API
 └──────┬────────┘
        │
    Redis Cache
        │
 PostgreSQL Database


🧰 Tech Stack
Component	Technology
Frontend	Streamlit
Backend API	Python (Flask / FastAPI)
AI Models	Vision Transformer (ViT), Google Gemini API
Database	PostgreSQL
Caching & Sessions	Redis
Dataset	Food-101
Deployment	Docker / Render / AWS (optional)



⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Arn412/AI-Nutrition-Assistant.git
cd AI-Nutrition-Assistant


2️⃣ Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Configure Environment Variables
Create a .env file with the following keys:

GEMINI_API_KEY=your_gemini_api_key
REDIS_URL=redis://localhost:6379
DATABASE_URL=postgresql://user:password@localhost:5432/nutrition_db


5️⃣ Run the App
streamlit run app.py





🧪 Example Use

Upload a food image 🍕

The AI model identifies the dish (e.g., Margherita Pizza).

Gemini API provides insights like:

Calorie estimate

Macronutrient breakdown

Health rating

Dietary suggestions


📈 Performance Highlights

✅ 88% model accuracy on the Food-101 dataset.

⚡ 40% lower latency via Redis caching.

📊 Real-time tracking of popular and trending foods.



🧠 Future Enhancements

Integration with wearable devices (Fitbit, Apple Health) for activity-based suggestions.

Addition of custom diet plans (keto, vegan, etc.).

Support for voice-based queries.

Multi-language support for global users.


📬 Contact

Author: Abhignan Reddy
📧 rabhignan@gmail.com


