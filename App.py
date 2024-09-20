from flask import Flask, render_template, request
from pymongo import MongoClient
from user_processing import User

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db']
collection = db['survey_collection']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    age = request.form['age']
    gender = request.form['gender']
    income = request.form['income']
    utilities = request.form['utilities']
    entertainment = request.form['entertainment']
    school_fees = request.form['school_fees']
    shopping = request.form['shopping']
    healthcare = request.form['healthcare']
    
    # Create user and save to CSV
    user = User(age, gender, income, utilities, entertainment, school_fees, shopping, healthcare)
    user.save_to_csv()

    # Save to MongoDB
    user_data = {
        'age': age,
        'gender': gender,
        'income': income,
        'utilities': utilities,
        'entertainment': entertainment,
        'school_fees': school_fees,
        'shopping': shopping,
        'healthcare': healthcare
    }
    collection.insert_one(user_data)

    return 'Data Submitted Successfully!'

if __name__ == '__main__':
    app.run(debug=True)
