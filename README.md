BEI TOPPER'S CLUB

**Overview:**
  BEI TOPPER'S CLUB is a Flask-based web application designed to manage user accounts and subjects associated with various semesters. The application allows users 
  to register, log in, and view subject details, while admins can add and manage subjects. The project uses PostgreSQL for database management. It also includes an admin
  portal where admins can manage subjects and other related data.

**Features:**
  - User Registration: Users can sign up with their username, email, password, and semester details.
  - User Login: Users can log in to access and view subjects relevant to their semester.
  - Subject Descriptions: Users can access detailed descriptions of subjects, including average marks, study days, and available resources.
  - Session Management: Both users and admins can log in and out of the application.
  - Admin Portal:Admins can log in and manage subjects. Admin credentials are predefined in the application.
  - Subject Management: Admins have the ability to add new subjects and view a list of existing ones
  - Database Intergration:The application connects to a hosted PostgreSQL database to store user, semester, and subject information.
    


**Technologies Used:**
  Flask: Web framework for Python.
  
  psycopg2: PostgreSQL database adapter for Python.
  
  HTML/CSS: For creating the web pages.
  
  PostgreSQL: Database for storing user, semester, and subject information.

**Prerequisites:**
  Before you begin, ensure you have the following installed on your machine:
  
  -Python 3.x 
  
  -Flask
  
  -psycopg2
  
  -PostgreSQL


**Setup**:
**1. Clone the Repository:**

    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    
**2. Install Dependencies:**

    Create a virtual environment and install required packages:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    
**3. Database Configuration:**

    The project uses a **hosted PostgreSQL database**.
    
    - **Database Name**: final_dbms
    
    - **User**: final_dbms_user
    
    - **Password**: kiyFsG55ZbMbw59HJi49ere5c8bOQBHf
    
    - **Host**: dpg-cqq3a02j1k6c73da6nbg-a.oregon-postgres.render.com
    
    - **Port**: 5432
    
  Ensure that your PostgreSQL database is properly set up with the correct credentials.
  
**4.Run Migrations:**

     Make sure your PostgreSQL database schema is up-to-date by running any necessary migrations.
     
**5.Run the Application:**

    python app.py
    
**The application will be available at http://127.0.0.1:5000/.**


**Usage**:
  1. Home Page: Access the home page to navigate to sign-up or login options.
  2. Sign Up: Visit /sign to create a new account. You will need to provide a username, email, password, and semester.
  3. Login: Go to /loginhello to log in with your credentials, including email, username, password, and semester.
  4. User Dashboard: After logging in, you will be redirected to /user, where you can view subjects related to your semester.
  5. Subject Description: Click on a subject to view its detailed description, including average marks, study days, and resources.
  6. Admin Functions: Log in as an admin at /adminsign to manage subjects. Admins can add new subjects through /admin/subjects.
  7. Logout: Use the /logout route to end your session.

   
**API Endpoints**:
  - /: Home page
  - /sign: User registration
  - /loginhello: User login
  - /user: User dashboard
  - /subject/<int:subject_id>erec: Subject description
  - /logout: Log out
  - /adminsign: Admin login
  - /admin/subjects: Admin subject management

  

**Application Structure**:
  main.py: The main application file containing routes and logic.
  templates/: Directory containing HTML templates for rendering web pages.
       home.html: Homepage.
       sign.html: User registration page.
       loginhello.html: User login page.
       subject.html: User's subject page.
       subject_description.html: Page showing details about a subject.
       adminsign.html: Admin login page.
       admin_subjects.html: Admin page for managing subjects.
  
    
**Admin Portal**
  **Admin Credentials**:
    The following are the predefined admin credentials:
    
    Admin 1:
    
    Email: agrimaregmi2004@gmail.com
    Password: Agrima11
    
    Admin 2:
    
    Email: pratistha.sapkota123@gmail.com
    Password: Pratistha21
    
    Admin 3:
    
    Email: sanskriti.khatiwada@gmail.com
    Password: Sanskriti37
  
**Admin Features**:

  Add Subjects: Admins can add new subjects by entering the subject name and the semester it belongs to.
  View Subjects: Admins can view a list of all subjects in the database.
  
**Potential Issues**:
  1. Database Connectivity:  correct database credentials and verify network access. Making sure that PostgreSQL allows connections from your application.
  2. Security: Avoiding hardcoding sensitive information.Validating all inputs to prevent SQL injection.
  3. Validation and Error Handling: Validate user inputs and handle errors gracefully to avoid crashes and provide clear feedback.
  4. Session Management: Secure session data with HTTPS and secure cookies.
  5. Database Schema and Migrations: Keep the database schema up-to-date and ensure data integrity. Run migrations as needed.

 **contribution of each member**:
   1.AGRIMA: FRONT END OF subject_description.html, admin_subjects.html,BACKEND for connecting adminsign.html and subject_description.html.
   2.SANSKRITI:FRONT END OF home.html,sign.html,loginhello.html, BACKEND for connecting home.html AND sign.html.
   3.PRATISTHA:FRONT END OF subject.html,BACKEND FOR Userlogin page, User's subject page.



**Contribution**:

To contribute to this project, please fork the repository, make your changes, and submit a pull request. For detailed contribution guidelines, refer to CONTRIBUTING.md.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For questions or feedback, please contact agrimaregmi2004@gmail.com,pratistha.sapkota123@gmail.com,sanskritikhatiwada002@gmail.com



