## Project Description

This project aims to build a fully containerized system using Docker that integrates the Mistral Local Large Language Model (LLM) with a web application. The Mistral model serves as the core AI engine, processing natural language queries and providing insights, while the web application offers a user-friendly interface for interaction.

The system consists of three primary components:

- **Mistral Model (Dockerized)**: The Mistral model is containerized to ensure ease of deployment and consistent performance across different systems. The model is responsible for handling the natural language processing tasks.
- **Backend (Flask API)**: A Python Flask API serves as the bridge between the frontend and the Mistral model. It handles requests from the frontend, processes them, and sends them to the Mistral model for inference.
- **Frontend (React Application)**: A React-based web interface allows users to interact with the Mistral model through the backend API. The frontend is designed for ease of use and responsive design.

The project provides two primary ways to run the application:

1. **Method 1 (Using Docker Compose)**: All components are orchestrated and deployed using Docker Compose. This method ensures a seamless and consistent environment for all services.
2. **Method 2 (Running Services Separately)**: The components can be run independently, with the backend and frontend services communicating over local network configurations.

This approach provides flexibility for development and testing, ensuring that all components can be managed independently while being fully integrated.

With the Dockerized approach, the project ensures high portability, and the use of Git for version control allows efficient collaboration and tracking of changes throughout the project lifecycle.
