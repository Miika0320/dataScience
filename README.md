![download-compresskaru com](https://github.com/Miika0320/dataScience/assets/46465622/a697246c-fb08-49ab-b1bf-efe70986add6)
# SafeHouse


SafeHouse is a large-data capstone project for our group’s Fundamentals Of Data Science course at the University of Ottawa. Our project uses criminal and rental data to suggest safe living areas. It combines large datasets into Supabase DB and applies machine learning algorithms for analysis. The project aims to provide insights into neighborhood safety and assist in finding secure rental options.

## Features

- **Safety Ratings**: Generates safety ratings for neighborhoods based on criminal data trends.
- **Curated Rental Suggestions**: Offers rental suggestions by integrating safety ratings with rental data.
- **Comparative Analysis**: Utilizes Python scripts in the `/Utils` directory to perform comparative safety analysis across different areas.
- **Machine Learning Models**: Implements Decision Tree, Gradient Boosting, and Random Forest algorithms to analyze data and predict safety trends.


## Getting Started

To set up the project locally:

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/safehouse.git
```

2. **Navigate to the project directory**

```bash
cd safehouse
```

3. **Install Python dependencies**

Assuming you have Python and pip installed, install the project dependencies.

```bash
pip install -r requirements.txt
```

4. **Set up Supabase**

Ensure your Supabase account is set up with the necessary datasets for criminal offenses and rental listings. Configure your local environment with Supabase API keys.

5. **Run Python Scripts**

Navigate to the `/Utils` directory to run comparative analysis scripts.

```bash
cd Utils
python analysis_script.py
```

## Data Analysis

The project uses the following machine learning algorithms for analysis:

- **Decision Tree**: A model used to predict the safety of neighborhoods based on historical data.
- **Gradient Boosting**: Improves prediction accuracy by combining multiple weak models.
- **Random Forest**: Uses multiple decision trees to improve prediction reliability.

Analysis is performed using a train-then-test method to evaluate model performance.

## Contributing

This project welcomes contributions. Please feel free to fork the repository, make changes, and submit pull requests.

## Contact

For more information, please contact withsafehouse@gmail.com