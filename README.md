
# 🇮🇳 Project Kisan: Your AI Agronomy Ally 🌱
### A Submission for the Agentic AI Day Hackathon 

**Project Kisan is an agentic AI-powered assistant built on Google Cloud that acts as a digital agronomist, price analyst, and policy navigator — all in one, for every farmer in India.**

---

## 👥 Team Details

- **Team Name:** 0101
- **Team Leader:** Bisal Prasad
- **Problem Statement:** 4th - "Providing farmers with expert help on demand"

---

## 🎯 The Problem: A Farmer's Silent Struggle

Imagine Rohan, a young farmer in Karnataka. His tomato crop shows strange yellow spots. Prices at the local mandi are dropping. Government subsidies? He doesn't know where to start. What he needs isn’t another app — he needs an ally.
<img width="1548" height="812" alt="image" src="https://github.com/user-attachments/assets/e9de465b-4b23-40f5-85b7-8fb3f4b7a8f0" />

Farmers today face a disconnected web of challenges:
- **Delayed Expertise:** Waiting days for agronomists, risking up to 40% of their crop yield.
- **Language & Literacy Barriers:** Most digital tools are in English or Hindi, leaving out a vast majority of regional dialect speakers.
- **Connectivity Issues:** High internet costs and power outages make cloud-based solutions unreliable in rural areas.
- **Information Overload:** Juggling multiple apps and websites for weather, market prices, and government schemes is inefficient and confusing.

---

## 💡 The Solution: An Agentic AI Ecosystem

Project Kisan is not just another app; it's a proactive partner that plans, reasons, and acts on the farmer's behalf. We designed a multi-agent architecture where specialized AI agents—built using **Google's Agent Development Kit (ADK)**—operate autonomously, communicate seamlessly, and work together to provide holistic support.

### What Makes It Agentic? 🤖
For us, an agent is a proactive partner. Project Kisan can:
- **Detect** plant diseases instantly by scanning crops.
- **Advise** on market price drops based on macro indicators.
- **Prompt** farmers before subsidy windows close.
- **Plan, Reason, and Act** proactively as their intelligent ally.

---

## ✨ Key Features

Project Kisan offers a suite of features through specialized, collaborating agents:

### 1. Crop Health Agent 🌿
- **Multimodal Disease Diagnosis:** Snap a photo, and our Gemini Vision-powered agent identifies the disease.
- **Localized Treatment Plans:** Get recommendations for organic and chemical treatments available locally.
- **Voice-First Guidance:** Receive step-by-step instructions in your native language.

### 2. Market Insights Agent 📈
- **Real-Time Mandi Prices:** Ingests live data from sources like Agmarknet.
- **Predictive Forecasting:** Uses weather data and technical indicators to forecast price movements.
- **Actionable Recommendations:** Advises farmers to "SELL NOW" or "HOLD" with clear justifications.

### 3. Government Schemes Agent 🏛️
- **Natural Language Q&A:** Ask about agricultural schemes and loans in your own words.
- **Automated Eligibility Matching:** Scrapes government portals and matches schemes to your profile.
- **Simplified Applications:** Pre-fills subsidy forms to make access easier than ever.

### 4. Dynamic Crop Calendar Agent 🗓️
- **Smart Scheduling:** Generates optimal sowing and harvesting windows based on climate data.
- **Dynamic Updates:** Adjusts recommendations based on real-time weather and monsoon shifts.
- **Voice-Powered Queries:** Get date advisories anytime, even offline.

### 🚀 Cross-Cutting Features
- **Multilingual Voice-First UX:** Eliminates literacy and language barriers.
- **Offline-First Architecture:** Caches data to ensure the app works in low-connectivity areas.
- **Context-Aware Orchestration:** Built with **Vertex AI Agent Builder** to manage the complex workflows between agents.

---

## 🛠️ Architecture & Technology

Project Kisan is built on a robust, scalable Google Cloud architecture. The core of our system is the **Google Agent Development Kit (ADK)**, which allows us to define and orchestrate our specialized agents with tools like `SequentialAgent` and `ParallelAgent`.

### Our Agentic AI Models in Action:

#### 1. Crop Disease Detection Agent
Uses a **Perceive-Reason-Augment-Talk (PRAT)** framework. It perceives the plant's condition via an image, reasons using a fine-tuned Gemini Vision model, augments the diagnosis with local data, and talks to the farmer in their native language.

#### 2. Market Insights Agent
Employs a **Reactive-Reasoning-Planning-Tool Use-Proactivity (RRPTP)** method. It reacts to queries, reasons over market signals using Gemini 2.5, plans a selling strategy, uses tools like BigQuery ML and APIs, and proactively alerts the farmer.

#### 3. Government Schemes Agent
Follows a **Crawl-Vectorize-Retrieve-Advise (CVRA)** pipeline. It crawls government sites, vectorizes the content using Gemini embeddings for storage in AlloyDB, retrieves relevant schemes via vector search, and advises the farmer.

### 💻 Tech Stack
- **AI/ML:** Vertex AI Agent Builder, Gemini API, Gemini Vision, Vertex AI Vector Search, BigQuery ML
- **Speech & Language:** Google Cloud Speech-to-Text, Text-to-Speech, Translation API
- **Backend & Data:** FastAPI, AlloyDB, Firestore, Cloud Storage
- **Infrastructure:** Google Kubernetes Engine, Cloud Functions, Cloud Run, Pub/Sub, Eventarc
- **Frontend:** React, Tailwind CSS, Kotlin (for Android)

---

## 🌟 Why Project Kisan is Different

| Competitor Gap | Our Edge with Project Kisan |
| :--- | :--- |
| **No True End-to-End Solution** | An integrated ecosystem of agents provides continuous, context-aware recommendations. |
| **Limited Language Support** | Full voice support in multiple local dialects reaches farmers who don't use keyboards. |
| **Requires Constant Connectivity** | An offline-first architecture ensures the app is reliable even with poor internet. |
| **Manual Subsidy Discovery** | Our automated agent scrapes, parses, and matches farmers to all relevant government schemes. |
| **Expensive Subscription Models** | Core features are free, with low-cost tiers for advanced analytics, ensuring accessibility for all. |

---

## 🛠️ Tech Stack & Architecture

Project Kisan is a full-stack application leveraging the power of Google Cloud and modern development tools.

- **Frontend:** React, Vite, Tailwind CSS
- **Backend:** Python, FastAPI
- **AI/ML:**
  - **Google Agent Development Kit (ADK):** For building and orchestrating our multi-agent system.
  - **Google Gemini Models:** The core reasoning engine for all our agents.
  - **Vertex AI:** For deploying and managing our AI models.
  - **Google Discovery Engine:** For our vectorized RAG implementation for government schemes.
- **Database & Storage:** Firebase & Firestore for real-time data synchronization and user management.
- **Speech & Language:** Google Cloud Speech-to-Text & Text-to-Speech for our voice-first interface.

---

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### 1. Environment Setup

Create a `.env` file in the `backend` directory and populate it with the necessary API keys and credentials:

```env
# Google Cloud
GOOGLE_AUTH_CREDENTIALS="path/to/your/kisan-466906-575fadd46b5c.json"

# Mandi Data API (data.gov.in)
URL="https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
API="579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b"

# OpenWeatherMap API
WEATHER_API_KEY="your_weather_api_key"
```

### 2. Backend Setup

Navigate to the backend directory and install the required Python packages.

```bash
cd backend
pip install -r requirements.txt
```

To run the FastAPI server, use the following command:

```bash
adk web (for adk interface) / adk api_server (for frontend + backend)
```
The backend will be accessible at `http://127.0.0.1:8000`.

### 3. Frontend Setup

Navigate to the frontend directory, install the dependencies, and start the development server.

```bash
cd frontend
npm install
npm run dev
```
The frontend application will be running at `http://localhost:5173`.

-

## 🙏 Credits & References

- **Google ADK:** [ai.google.dev](https://ai.google.dev/)
- **MobilePlantViT Paper:** [arxiv.org/abs/2503.16628](https://arxiv.org/abs/2503.16628)
- **Data Sources:**
  - Government Mandi Prices: [data.gov.in](https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi)
  - Agmarknet: [agmarknet.gov.in](https://agmarknet.gov.in/)
  - Nasdaq Data Link: [data.nasdaq.com/tools/api](https://data.nasdaq.com/tools/api)
  - PMKSY: [pmksy.gov.in](https://pmksy.gov.in/apply)





Get started by customizing your environment (defined in the .idx/dev.nix file) with the tools and IDE extensions you'll need for your project!

Learn more at https://developers.google.com/idx/guides/customize-idx-env
