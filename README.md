# House_price_prediction-
A beginner-friendly Python &amp; Flask project for predicting house prices

## Features
- Enter property details: Overall Quality, Living Area (sq ft), Garage Capacity, Year Built
- Get instant estimated house price
- Clean, responsive, and user-friendly web interface

## Dataset
This project uses the **House Prices dataset** from [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).  
Download `train.csv` and place it in the project folder before training the model.

## Setup Instructions
1. **Clone the repository**
```bash
git clone https://github.com/Deekshithakandrathi/House_price_prediction-.git
cd house-price-prediction
##Create & activate virtual environment

python -m venv venv
venv\Scripts\activate      # Windows Command Prompt
# OR
.\venv\Scripts\Activate    # Windows PowerShell
##Install dependencies

pip install -r requirements.txt
#Train the model

python model.py


#Run the web app

python app.py


##Open http://127.0.0.1:5000/ in your browser and use the form to predict house prices.

##Project Structure
house_price_prediction/
│-- app.py
│-- model.py
│-- templates/
│   └-- index.html
│-- requirements.txt
│-- README.md
│-- train.csv
│-- .gitignore

##Dependencies

Flask

pandas

numpy

scikit-learn

Optional: matplotlib, seaborn for visualization.

##GitHub Notes

.gitignore includes:

venv/
__pycache__/
*.pyc
house_price_model.pkl



