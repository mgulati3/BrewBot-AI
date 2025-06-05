# BrewBot AI Coffee Shop

A full-stack AI–powered coffee shop application featuring a modular, agent-driven Python backend (deployed on RunPod) and a React Native (Expo) mobile frontend. Users can chat with the bot to browse the menu, place orders, receive personalized recommendations, and complete a simulated checkout—all in a warm, coffee-shop aesthetic.

---

## Table of Contents

1. [Features](#features)  
2. [Architecture & Tech Stack](#architecture--tech-stack)  
3. [Prerequisites](#prerequisites)  
4. [Installation & Setup](#installation--setup)  
   - [Backend (Python/RunPod)](#backend-pythonrunpod)  
   - [Frontend (Expo/React Native)](#frontend-exporeact-native)  
5. [Usage](#usage)  
   - [Running Backend Locally](#running-backend-locally)  
   - [Deploying to RunPod](#deploying-to-runpod)  
   - [Launching the Mobile App](#launching-the-mobile-app)  
6. [Environment Variables](#environment-variables)  
7. [Project Structure](#project-structure)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## Features

- **Agent-Based Chatbot**  
  - GuardAgent filters out off-topic messages.  
  - ClassificationAgent chooses between “order” or “recommendation” flows.  
  - OrderTakingAgent guides users step-by-step, collects items, calculates totals, and triggers recommendations.  
- **Prompt Engineering & RAG**  
  - Custom system prompts for each agent.  
  - Pinecone vector store retrieves relevant menu/context at runtime.  
- **Market Basket Recommendation**  
  - Apriori–based engine suggests “frequently bought together” items.  
  - Real-time recommendations surfaced as interactive cards.  
- **RunPod + Docker Deployment**  
  - Multi–architecture Docker image serves LLM inference and embedding endpoints.  
  - Deployed on RunPod for scalable, low–latency hosting.  
- **React Native Frontend (Expo)**  
  - Chat UI with user/bot bubbles, typing indicators, and interactive cards.  
  - Cart/Checkout page with quantity selectors, tax calculations, and a simulated “Pay Now” confirmation.  
  - Responsive design: bottom–tab navigator on mobile.  
- **Firebase & Pinecone Integration**  
  - Firebase Auth/Firestore for user session management (optional, can be disabled).  
  - Pinecone for vector similarity search in RAG.

---

## Architecture & Tech Stack

### Backend  
- **Language & Framework:** Python 3.8 (slim)  
- **Agents & Logic:**  
  - **GuardAgent** – Filters inappropriate/irrelevant messages.  
  - **ClassificationAgent** – Routes user input to order–or recommendation–flow.  
  - **DetailsAgent** – Performs retrieval–augmented generation (RAG) with Pinecone.  
  - **OrderTakingAgent** – Manages interactive ordering, calculates totals, and calls recommendations.  
- **LLM & Embeddings:**  
  - `openai` Python SDK to call Chat endpoint (e.g., Llama–3–Instruct on RunPod).  
  - Pinecone for real-time embeddings (vector store).  
- **Containerization:** Docker (multi–arch build using `docker buildx`)  
- **Cloud Deployment:** RunPod (API endpoint and worker).  
- **Data/Recommendations:** Apriori algorithm in Python (market basket analysis).  
- **Environment Config:** `.env` with RunPod, Pinecone, Firebase credentials.

### Frontend  
- **Framework:** React Native (Expo SDK 51)  
- **Navigation & Routing:** `expo-router` v3.5  
- **Styling:** Tailwind via `nativewind` + custom color palette (coffee tones)  
- **Components:**  
  - `MessageList`, `ChatBubble`, `MenuCard`, `RecommendationCard`, `CartContext`, etc.  
  - `react-native-responsive-screen` for adaptive sizing.  
  - `react-native-gesture-handler`, `react-native-reanimated`, `react-native-safe-area-context`, `react-native-screens`.  
  - `@expo/vector-icons` for icons.  
- **State Management:** React Context (Cart + Chat history)  
- **Network:** `axios` for HTTP calls to BrewBot AI backend  
- **Extras:**  
  - Toast notifications via `react-native-root-toast`  
  - Firebase Auth/Firestore (optional)

---

## Prerequisites

- **Backend:**  
  - Python 3.8+  
  - Docker (with Buildx support for multi–arch)  
  - RunPod account & API key  
  - Pinecone account & API key  
  - (Optional) Firebase project & credentials

- **Frontend:**  
  - Node.js 18+ (npm or Yarn)  
  - Expo CLI (`npm install -g expo-cli`)  
  - Watchman (macOS only) – `brew install watchman`

- **Mobile/Emulator:**  
  - Xcode (with Command–Line Tools) for iOS Simulator  
  - Android Studio + AVD for Android Emulator  
  - Expo Go (Android/iOS) on physical device

---
