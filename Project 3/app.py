from flask import Flask, render_template
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['flu']

national_data_collection = db['combined_national']
state_data_collection = db['combined_state']

@app.route('/')
def index():
    # Retrieve data from MongoDB collections
    national_data = pd.DataFrame(list(national_data_collection.find()))
    state_data = pd.DataFrame(list(state_data_collection.find()))

    # Pass the data to the template
    return render_template('app.html', national_data=national_data, state_data=state_data)

if __name__ == '__main__':
    app.run(debug=True)

