# British Airways Job Simulation

## 📌 Overview

This project was completed as part of the **British Airways Virtual Experience Program** on Forage.  
It focuses on web scraping, data cleaning, exploratory data analysis (EDA), and insight generation based on airline customer reviews.

## 📂 Project Structure

```
├── BA_Data_Scraping.py               # Python script for scraping customer reviews
├── British_Airways_Task1.ipynb        # Notebook for data scraping and cleaning
├── British_Airways_Task2.ipynb        # Notebook for EDA and visualizations
├── British_Airways_Data.csv           # Scraped and cleaned customer reviews data
├── customer_booking.csv               # Provided dataset with customer booking details
├── British_Airways_Task1.pptx         # Presentation for Task 1 (Scraping & Cleaning)
├── British_Airways_Task2.pptx         # Presentation for Task 2 (Analysis & Insights)
├── README.md                          # Project documentation
```

## 📊 Datasets

The project utilizes two primary datasets:

1. **British_Airways_Data.csv**  
   - Scraped customer reviews from Skytrax.
   - Contains fields like Name, Location, Date, Review Title, Full Review Text, Rating, and Service Attributes.

2. **customer_booking.csv**  
   - Provided customer data including:
     - **Booking Details**
     - **Revenue Information**
     - **Customer Behavior Attributes**

## 🚀 Installation

### 1️⃣ Clone the repository:

```bash
git clone https://github.com/27abhishek27/British-Airways-Job-Simulation.git
cd British-Airways-Job-Simulation
```

### 2️⃣ Install dependencies:

Ensure you have the following Python packages installed:

- `requests`
- `beautifulsoup4`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `wordcloud`
- `scikit-learn` *(optional for deeper analysis)*

Install them with:

```bash
pip install requests beautifulsoup4 pandas numpy matplotlib seaborn wordcloud scikit-learn
```

## 🔍 Methodology

### 1. **Web Scraping**

- **Target Website**: Skytrax Airline Quality Reviews.
- **Scraping Details**: Customer name, location, review title, full review, ratings, verification status, and service quality parameters.

### 2. **Data Cleaning**

- **Handling Missing Data**: Identified and removed/replaced missing values.
- **Feature Engineering**: Extracted and structured fields like Travel Class, Type of Traveller, Seat Type, etc.

### 3. **Exploratory Data Analysis (EDA)**

- **Review Sentiment Analysis**: Analyzed review text to understand customer sentiment trends.
- **Ratings Distribution**: Explored how different customer ratings are distributed.
- **Top Complaints & Praise**: Word clouds and frequency analysis of key themes.
- **Class of Travel Analysis**: Studied ratings across Economy, Premium Economy, Business, and First Class.

### 4. **Presentation**

- Summarized findings into two clear PowerPoint presentations:
  - Task 1: Data Scraping & Cleaning
  - Task 2: Insights & Recommendations

## 📊 Visualizations

Some visualizations generated during the analysis include:

![alt text](https://github.com/27abhishek27/British-Airways-Job-Simulation/blob/main/British_Airways_Task1_png/histogram.png)
![alt text](https://github.com/27abhishek27/British-Airways-Job-Simulation/blob/main/British_Airways_Task1_png/Rating.png)
![alt text](https://github.com/27abhishek27/British-Airways-Job-Simulation/blob/main/British_Airways_Task1_png/full%20reviewpng.png)
![alt text](https://github.com/27abhishek27/British-Airways-Job-Simulation/blob/main/British_Airways_Task1_png/recommended.png)

*(Presentations contain detailed visuals.)*

## 🛠️ Technologies Used

- **Python**
- **BeautifulSoup & Requests** (for web scraping)
- **Pandas & NumPy** (for data manipulation)
- **Matplotlib & Seaborn** (for visualization)
- **WordCloud** (for textual analysis)
- **Jupyter Notebook**

## 📌 Future Improvements

- **Sentiment Modeling**: Build machine learning models to predict customer satisfaction.
- **Dynamic Scraping**: Use Selenium or Playwright to scrape dynamically loaded content.
- **Dashboarding**: Develop interactive dashboards using Tableau, Power BI, or Plotly Dash for management reporting.
