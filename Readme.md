# Flask Survey Application

This is a Flask-based web application designed to collect user survey data and store it both in a CSV file and in a MongoDB database. The application provides a form to capture user expenses such as utilities, entertainment, school fees, shopping, and healthcare.

## Prerequisites
Before running this application, ensure the following are installed on your local environment:
1. **Python 3.x**: Make sure Python is installed.
2. **Flask**: A Python web framework.
3. **MongoDB**: Either local installation or MongoDB Atlas.
4. **AWS Elastic Beanstalk CLI**: For deployment to AWS.
5. **pip**: Python package installer.

## File Structure
/JASMINE ONOWVIE FINAL PROJECT  
├── .elasticbeanstalk/   # Elastic Beanstalk configuration files  
├── Templates/           # HTML template files (e.g., index.html)  
├── __pycache__/         # Python cache files  
├── App.py               # Main Flask application  
├── Procfile             # Config file to run Gunicorn on Elastic Beanstalk  
├── requirements.txt     # Python package dependencies  
├── Survey_Data_Visualization.ipynb  # Notebook for data visualization  
├── income_by_age.png    # PNG image file related to data visualization  
├── user_data.csv        # CSV file storing user data  
├── user_processing.py   # Script for processing user data and saving to CSV  
└── index.html           # Frontend HTML file for the form

## Setting up the Project Locally

1. **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies:**
    To install the necessary Python dependencies, run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure MongoDB is Running:**
    If you're using a local MongoDB server, make sure it's running:
    ```bash
    mongod
    ```

    If you're using MongoDB Atlas, update the MongoDB connection string in `App.py`:
    ```python
    client = MongoClient('your-atlas-mongodb-connection-string')
    ```

4. **Run the Flask Application:**
    Run the application locally by executing:
    ```bash
    python App.py
    ```

    The application will be available at `http://127.0.0.1:5000` or `http://localhost:5000`.

## Application Workflow

1. **Form Submission:**
    Users fill out the form located in `index.html`. The fields include:
    - Age
    - Gender
    - Income
    - Utilities
    - Entertainment
    - School Fees
    - Shopping
    - Healthcare

2. **Data Processing:**
    When the form is submitted:
    - The `submit()` function in `App.py` retrieves the form data.
    - The data is saved in two locations:
      - **CSV file**: Processed by `user_processing.py` and saved in `user_data.csv`.
      - **MongoDB**: Stored in the `survey_collection` in the `survey_db` database.

3. **MongoDB Structure:**
    The MongoDB stores user data with fields such as:
    ```json
    {
      "age": "23",
      "gender": "Female",
      "income": "4000",
      "utilities": "1000",
      "entertainment": "500",
      "school_fees": "200",
      "shopping": "300",
      "healthcare": "100"
    }
    ```

## Testing Locally

1. Open your browser and navigate to `http://127.0.0.1:5000`.
2. Fill out the form and submit it.
3. Verify that the data has been stored in:
    - The `user_data.csv` file.
    - The MongoDB collection (`survey_collection` in `survey_db`).

## Deploying to AWS Elastic Beanstalk

1. **Install AWS Elastic Beanstalk CLI:**
    Follow the [installation guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html).

2. **Initialize the Project with AWS EB:**
    ```bash
    eb init
    ```
    Follow the prompts to configure the AWS region and select the Python platform.

3. **Create an Elastic Beanstalk Environment:**
    ```bash
    eb create flask-env
    ```

4. **Deploy the Application:**
    ```bash
    eb deploy
    ```

5. **Check Application Status:**
    Verify the status of the environment:
    ```bash
    eb status
    ```

6. **Check Logs for Errors:**
    If there are issues, retrieve the logs:
    ```bash
    eb logs
    ```

## Procfile
The `Procfile` defines how the application should run on Elastic Beanstalk. The contents should be:
```bash
web: gunicorn App:app --bind 0.0.0.0:8080
```

## Troubleshooting

1. **MongoDB Connection Issues**: Ensure that MongoDB is properly running locally or Atlas is configured correctly. If using MongoDB Atlas, check that your IP is whitelisted and that the connection string is correct in `App.py`.

2. **Elastic Beanstalk Deployment Fails (502 Errors)**: If the health check returns a 502 error:
    - Check the `Procfile` to ensure it contains the correct Gunicorn command.
    - Review the logs by running `eb logs` to debug the issue.

3. **Data Not Saving to MongoDB**: Check that MongoDB is running and properly configured in `App.py`.

4. **CSV File Not Updating**: Ensure that the `user_processing.py` is correctly set up to handle the CSV file.

## Future Enhancements

1. **Form Validation**: Add form validation to ensure correct user input.
2. **Error Handling**: Add better error handling for MongoDB and file writing processes.
3. **Security**: Implement user authentication for secure data submissions.

## Conclusion

This project serves as a basic implementation of a survey application using Flask, MongoDB, and CSV for data storage. With options to enhance the form validation, error handling, and security, this application can be expanded further for real-world use. The current deployment method through AWS Elastic Beanstalk allows for scalability and efficient management of resources. By addressing potential troubleshooting issues, developers can ensure smooth operation of the application in various environments.
