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
