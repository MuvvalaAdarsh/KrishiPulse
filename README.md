# **LOOM LINK 🔗**
https://www.loom.com/share/e2c0e9f4f32941c88ef6bad018d2dd3b


## **KrishiPulse – Agriculture & Climate Insight Tool**
KrishiPulse is a simple, practical prototype built for the Digital Bharat Internship – Challenge Samarth, focusing on generating insights from India’s agricultural production data and climate patterns.

The system connects crop production data with rainfall information and provides a clean UI to interactively compare states, crop trends, and climate influence.

### **Features**

- Compare crop production across two states

- Analyze rainfall vs crop trends

- Identify best & worst districts for a selected crop

- Policy support insights (drought-resistant vs water-intensive crops)

- Interactive visualizations

- Secure .env key handling

- Clean and easy Streamlit-based interface

_______________

## **Directory Structure**
```
Project_KrishiPulse/
│── app.py
│── crop_utils.py
│── visuals.py
│── requirements.txt
│── .env               
│── .gitignore
└── data/              
```
____________________

## **How to Run the Project**

1. Clone the repository

`git clone https://github.com/MuvvalaAdarsh/KrishiPulse.git`

2. Create a virtual environment

`python -m venv .venv`

3. Activate the environment

Windows:

`.venv\Scripts\activate`

Mac/Linux:

`source .venv/bin/activate`

4. Install dependencies

`pip install -r requirements.txt`

5. Add your .env file

Create a .env file inside the project:
```
API_KEY=your_api_key_here
RESOURCE_ID=resource_id_here
```

6. Run Streamlit

`streamlit run app.py`

The app will open in your browser at:

`http://localhost:8501`

___________________
## **Requirements**

The project uses:

- streamlit

- pandas

- numpy

- matplotlib

- python-dotenv

**All are included in requirements.txt**
_______________________________________

## **Notes**

- Dataset files are NOT pushed to GitHub (for security and size).

- API key is stored securely using .env.

- This is a prototype meant to demonstrate agricultural climate insights, not a full production system.
