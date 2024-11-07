# Notes-Ninja

Notes-Ninja is a robust web application designed for students and educators to manage notes and take quizzes, with a focus on physics and chemistry. It provides personalized note-taking, quiz functionality, and secure Google login with OAuth.

## Key Features

- **User Authentication**: Secure login via Flask-Login and Google OAuth.
- **Notes Management**: Organize physics and chemistry notes in a structured system.
- **Quizzes**: Practice quizzes with random shuffling and performance tracking.
- **Google OAuth Integration**: Easy login/logout with Google accounts.
- **Database Support**: Fully integrated PostgreSQL database for storing user and quiz data.
- **Responsive Design**: Optimized for both desktop and mobile users.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **OAuth**: Google OAuth using Flask-OAuthlib
- **Session Management**: Flask-Login, Sessions
- **Database**: PostgreSQL for user, note, and quiz storage
- **Deployment**: Tried Vercel & Render but, None for now.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Bibhav48/Note-Ninja.git
    cd Note-Ninja
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up PostgreSQL and create a `.env` file with your credentials:

    ```bash
    DATABASE_URL=<your-postgresql-url>
    GOOGLE_CLIENT_ID=<your-client-id>
    GOOGLE_CLIENT_SECRET=<your-client-secret>
    ```

4. Run the app:

    ```bash
    python app.py
    ```

## Usage

1. Visit `http://localhost:5000/` to access the app.
2. Log in with Google to access your personalized notes and quizzes.
3. Browse the **Notes** section for organized physics and chemistry materials.
4. Test your knowledge with quizzes in the **Quiz** section and track your progress.

## Folder Structure

- `app.py`: Main Flask app and routing logic.
- `static/`: Includes note files and quiz questions.
- `templates/`: HTML templates for rendering web pages.
- `requirements.txt`: Project dependencies.

## Future Enhancements

- **Advanced Quiz Features**: Introduce additional quiz types and live performance stats.
- **Additional Subjects**: Expand to cover more subjects.
- **Real-Time Collaboration**: Allow for group note sharing and collaborative quiz creation.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance Notes-Ninja.

## Demo

Below we've added some pictures as a demo of the website.

Landing page

![image](https://github.com/user-attachments/assets/e63e0e28-19f2-47fb-abfe-8a3d43d2dc4f)

![image](https://github.com/user-attachments/assets/0a685721-fbad-4fd1-b2bd-5bab6d42c85b)

Login interface

![image](https://github.com/user-attachments/assets/25f85196-24e0-46dc-8b96-342a3e7bf80f)

![image](https://github.com/user-attachments/assets/5cd28396-dd7d-4e57-a3ed-cd24c1d1cc56)

![image](https://github.com/user-attachments/assets/0eeea18e-e956-45fd-a8d3-be533b92fd74)

Notes interface

![image](https://github.com/user-attachments/assets/8faa9bea-1792-4a07-ba3c-36422aa4317b)

![image](https://github.com/user-attachments/assets/08d951bd-fbb5-4061-8e72-5c7b5e327cbe)

![image](https://github.com/user-attachments/assets/6ac3a90d-8c1c-4193-9005-ac243d23ff75)

Quiz interface

![image](https://github.com/user-attachments/assets/c0c7e5a9-8025-4e8d-96c2-8eeb8cb61111)

Quiz answers interface

![image](https://github.com/user-attachments/assets/ac71b8b8-9532-4342-87d8-1c7ab4b5418a)
