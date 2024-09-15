# Fruit.ai

Fruit.ai is a health manager product that provides various services including a chatbot, translator, and FAQ management system.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication
- Fruit chatbot
- Language translation
- FAQ management system
- Responsive design for mobile and desktop

## Technologies Used

- Frontend:
  - React.js
  - Styled-components for styling
  - Axios for API requests
- Backend:
  - FastAPI (Python)
  - SQLAlchemy for database operations
- Database:
  - PostgreSQL (provided by Railway)
- Deployment:
  - Frontend: Vercel
  - Backend: Railway

## Getting Started

### Prerequisites

- Node.js (v14 or later)
- Python (v3.9 or later)
- npm or yarn
- Railway CLI

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/daman0403/fruit-ai.git
   cd fruit-ai
   ```

2. Set up the backend:

   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the frontend:

   ```
   cd ../frontend
   npm install  # or yarn install
   ```

4. Set up environment variables:
   - Create a `.env` file in the frontend directory
   - Add `REACT_APP_API_URL=http://localhost:8000` (for local development)

## Usage

1. Run the backend server:

   ```
   cd fruit-ai-backend
   uvicorn main:app --reload
   ```

2. In a new terminal, run the frontend development server:

   ```
   cd fruit-ai-frontend
   npm start  # or yarn start
   ```

3. Open your browser and navigate to `http://localhost:3000`

## API Endpoints

- `GET /faqs`: Retrieve all FAQs
- `GET /faqs/{faq_id}`: Retrieve a specific FAQ
- `POST /faqs`: Create a new FAQ
- `PUT /faqs/{faq_id}`: Update an existing FAQ
- `DELETE /faqs/{faq_id}`: Delete an FAQ

For detailed API documentation, run the backend server and visit `http://localhost:8000/docs`

## Deployment

### Backend Deployment (Railway)

1. Install Railway CLI: `npm i -g @railway/cli`
2. Login to Railway: `railway login`
3. Initialize Railway project: `railway init`
4. Deploy: `railway up`
5. Current project is deployed on `https://fruit-ai-production.up.railway.app/docs`

### Frontend Deployment (Vercel)

1. Install Vercel CLI: `npm i -g vercel`
2. Login to Vercel: `vercel login`
3. Deploy: `vercel --prod`
4. Current project is deployed on `https://vercel.com/daman-goyals-projects/fruit-ai/BR8S1sGSL7BVPyhKWffiitDjGCL9`

Remember to set the `REACT_APP_API_URL` environment variable in your Vercel project settings to your Railway backend URL.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
