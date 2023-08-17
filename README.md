# WhiteBoardApp

Real-Time Whiteboard Application
This Django-based web application provides users with a real-time collaborative whiteboard experience, allowing them to create and manage whiteboards, and draw together in real-time.

Features
User Authentication: User registration and authentication are handled using the built-in Django authentication system. Email verification ensures secure access.

Whiteboard Creation and Management: Users can create new whiteboards, each with a unique identifier. API endpoints are available for creating, listing, and retrieving whiteboard details.

Real-time Drawing and Collaboration: Real-time drawing and collaboration on the whiteboard are facilitated through WebSocket-based communication. Users can connect to a whiteboard's WebSocket channel to draw and see each other's actions in real-time.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/prabhratirastogi/WhiteBoardApp.git
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the database settings in settings.py.

Run migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the application at http://127.0.0.1:8000/.

API Endpoints
Create a New Whiteboard: POST /api/whiteboards/
List All Whiteboards: GET /api/whiteboards/
Retrieve Whiteboard Details: GET /api/whiteboards/<whiteboard_id>/
WebSocket Communication
Real-time drawing and collaboration are achieved through WebSocket channels. Connect to a whiteboard's WebSocket channel using the following URL format:


Contributions are welcome! Please fork the repository and create a pull request
