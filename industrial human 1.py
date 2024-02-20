import io
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
import plotly.express as px
import json
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Load and concatenate dataframes
# Replace file paths with your actual file paths
# Read the CSV files
df1 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18_0800_NIC_FINAL_STATE_RAJASTHAN-2011.csv',
                  encoding='ISO-8859-1')
df2 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18_1200_NIC_FINAL_STATE_ARUNACHAL_PRADESH-2011.csv',
                  encoding='ISO-8859-1')
df3 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18_1400_NIC_FINAL_STATE_MANIPUR-2011.csv',
                  encoding='ISO-8859-1')
df4 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18_1500_NIC_FINAL_STATE_MIZORAM-2011.csv',
                  encoding='ISO-8859-1')
df5 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18_1900_NIC_FINAL_STATE_WEST_BENGAL-2011.csv',
                  encoding='ISO-8859-1')
df6 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_0700_NIC_FINAL_STATE_NCT_OF_DELHI-2011.csv',
                  encoding='ISO-8859-1')
df7 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_1600_NIC_FINAL_STATE_TRIPURA-2011.csv',
                  encoding='ISO-8859-1')
df8 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_2000_NIC_FINAL_STATE_JHARKHAND-2011.csv',
                  encoding='ISO-8859-1')
df9 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_2400_NIC_FINAL_STATE_GUJARAT-2011.csv',
                  encoding='ISO-8859-1')
df10 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_2700_NIC_FINAL_STATE_MAHARASHTRA-2011.csv',
                   encoding='ISO-8859-1')
df11 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_2900_NIC_FINAL_STATE_KARNATAKA-2011.csv',
                   encoding='ISO-8859-1')
df12 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_3000_NIC_FINAL_STATE_GOA-2011.csv',
                   encoding='ISO-8859-1')
df13 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_3200_NIC_FINAL_STATE_KERALA-2011.csv',
                   encoding='ISO-8859-1')
df14 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_3300_NIC_FINAL_STATE_TAMIL_NADU-2011.csv',
                   encoding='ISO-8859-1')
df15 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18sc_3400_NIC_FINAL_STATE_PUDUCHERRY-2011.csv',
                   encoding='ISO-8859-1')
df16 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18st_0200_NIC_FINAL_STATE_HIMACHAL_PRADESH-2011.csv',
                   encoding='ISO-8859-1')
df17 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18st_0500_NIC_FINAL_STATE_UTTARAKHAND-2011.csv',
                   encoding='ISO-8859-1')
df18 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18st_0900_NIC_FINAL_STATE_UTTAR_PRADESH-2011.csv',
                   encoding='ISO-8859-1')
df19 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18st_1000_NIC_FINAL_STATE_BIHAR-2011.csv',
                   encoding='ISO-8859-1')
df20 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18st_1100_NIC_FINAL_STATE_SIKKIM-2011.csv',
                   encoding='ISO-8859-1')
df21 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18st_1300_NIC_FINAL_STATE_NAGALAND-2011.csv',
                   encoding='ISO-8859-1')
df22 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18st_1800_NIC_FINAL_STATE_ASSAM-2011.csv',
                   encoding='ISO-8859-1')
df23 = pd.read_csv('C:\\Users\\M SWETHA\\Downloads\\DDW_B18st_2100_NIC_FINAL_STATE_ODISHA-2011.csv',
                   encoding='ISO-8859-1')

# Concatenate the dataframes
data = pd.concat(
    [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20,
     df21, df22, df23], ignore_index=True)


def load_data():
    # Replace 'your_data_file.csv' with the path to your dataset file
    data = pd.concat(
        [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20,
         df21, df22, df23], ignore_index=True)
    return data


# Ensure correct data types and handle missing values
# Make sure to replace 'your_column_name' with actual column names from your data
data['Main Workers - Total - Males'] = pd.to_numeric(data['Main Workers - Total - Males'], errors='coerce').fillna(0)
data['Main Workers - Total - Females'] = pd.to_numeric(data['Main Workers - Total - Females'], errors='coerce').fillna(
    0)


# Create an interactive map
def get_state_name(india_geojson, state_code):
    for feature in india_geojson['features']:
        if feature['properties']['state_code'] == state_code:
            return feature['properties']['st_nm']
    return 'Unknown'


# Sidebar for navigation
with st.sidebar:
    selected = option_menu("Main Menu",
                           ["Data Exploration", "Data Cleaning", "Statistical Metrics", "Feature Engineering",
                            "Data Visualization"], icons=['search', 'brush', 'calculator', 'gear', 'graph-up'],
                           default_index=0)

# Main app
if selected == "Data Exploration":
    st.title("Data Exploration")

    State_data = data.groupby('State Code').agg({
        'Main Workers - Total -  Persons': 'sum',
        'Main Workers - Total - Males': 'sum',
        'Main Workers - Total - Females': 'sum'
    }).reset_index()


    def load_data():
        # Your code to load and return the DataFrame
        return State_data


    st.subheader("Loaded Dataset")
    st.dataframe(data)
    st.subheader("Main Workers Total Persons State Wise")
    st.dataframe(State_data)
    st.subheader("Identify Numerical Columns")
    numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
    numerical_cols
    plt.figure(figsize=(8, 6))
    sns.histplot(data['State Code'], kde=True)
    plt.title('Distribution of Your Numerical Column')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.xticks(rotation=45)
    plt.xlabel('Sate Code')
    plt.ylabel('Frequency')
    st.pyplot()

    data = load_data()
elif selected == "Data Cleaning":
    st.title("Data Cleaning")


    def main(data):
        st.subheader("Data Overview")
        # Display the first few rows of the DataFrame
        st.subheader("First Few Rows of the Dataset")
        st.write(data.head())
        st.dataframe(data)
        # Display a concise summary of the DataFrame
        st.subheader("Dataframe Summary")
        buffer = io.StringIO()
        data.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

        # Display descriptive statistics
        st.subheader("Descriptive Statistics")
        st.write(data.describe())

        data.fillna(data.mean(numeric_only=True), inplace=True)  # For numerical columns
        data.fillna('Unknown', inplace=True)  # For categorical columns

        # Remove duplicates
        data['State Code'] = data['State Code'].str.replace('`', '').astype(int)
        # Normalize data (Example: Min-Max scaling)
        scaler = MinMaxScaler()
        data[['Main Workers - Total -  Persons']] = scaler.fit_transform(data[['Main Workers - Total -  Persons']])
        # Convert categorical data to numerical (Example: One-hot encoding)
        data = pd.get_dummies(data, columns=['State Code'])

        # Split data
        from sklearn.model_selection import train_test_split
        # X_train, X_test, y_train, y_test = train_test_split(df.drop('Main Workers - Total - Persons', axis=1), df['Main Workers - Total - Persons'], test_size=0.2, random_state=42)
        X = data.drop('Main Workers - Total -  Persons', axis=1)
        y = data['Main Workers - Total -  Persons']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Visualize distribution
        st.subheader("Categorical Data Consistency")
        categorical_columns = ['State Code', 'District Code', 'India/States Division Group', 'Class', 'NIC Name']
        for col in categorical_columns:
            if col in data:
                st.text(f"Unique values in {col}:")
                st.write(data[col].unique())

            # Show effect of One-Hot Encoding
        if st.checkbox("Show One-Hot Encoded Data"):
            st.write("### One-Hot Encoded Data")
            st.write(data)

            # Group the data by industry division and sum up the number of main workers for each division
            industry_division_totals = data.groupby('Division')['Main Workers - Total -  Persons'].sum().sort_values(
                ascending=False)
            fig, ax = plt.subplots()
            industry_division_totals.plot(kind='bar', color='skyblue', ax=ax)
            ax.set_title('Total Main Workers by Industry Division')
            ax.set_xlabel('Industry Division')
            ax.set_ylabel('Number of Main Workers')
            ax.legend(['Main Workers'])
            plt.xticks(rotation=90)
            plt.tight_layout()

            # Display the Matplotlib plot in Streamlit
            st.pyplot(fig)


    if __name__ == "__main__":
        main(data)

        # Show statistics of numerical columns
    data = load_data()

elif selected == "Statistical Metrics":
    st.title("Statistical Metrics")


    def plot_missing_values_heatmap(data):
        plt.figure(figsize=(12, 6))
        sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
        plt.title("Heatmap of Missing Values in the Dataset")
        return plt


    null_counts = data.isnull().sum()

    # Display the result in Streamlit
    st.subheader("Count of Null Values in Each Column")
    st.write(null_counts)

    # In your Streamlit app
    if st.button("Show Missing Values Heatmap"):
        plt = plot_missing_values_heatmap(data)
        st.pyplot(plt)

    st.title("Mean Values")
    mean_values = data.mean(numeric_only=True)
    numeric_data = data.select_dtypes(include=['number'])
    mean_values = numeric_data.mean()
    mean_values
    st.title("Mean of Each Column")
    fig, ax = plt.subplots()
    sns.barplot(x=mean_values.index, y=mean_values.values, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set_ylabel("Mean Value")
    st.pyplot(fig)
    st.title("Median Values")
    median_values = data.median(numeric_only=True)
    median_values
    st.title("Median of Each Column")
    fig, ax = plt.subplots()
    sns.barplot(x=median_values.index, y=median_values.values, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set_ylabel("Median Value")
    st.pyplot(fig)
    st.title("Standard deviation")

    data = data.apply(pd.to_numeric, errors='coerce')
    numeric_data = data.select_dtypes(include=[np.number])

    data.fillna(data.mean(), inplace=True)
    std_dev = numeric_data.std()
    std_dev = data.std()
    std_dev

    st.title("To calculate quantiles")
    quantiles = data.quantile([0.25, 0.5, 0.75])
    quantiles
    st.title("correlation matrix")
    correlation_matrix = data.corr()

    plt.figure(figsize=(25, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    correlation_matrix
    plt.tight_layout()
    st.pyplot()

    st.title("Skewness")
    skewness = data.skew()
    skewness


elif selected == "Feature Engineering":
    st.title("Feature Engineering")
    st.subheader('Visualize the distribution of a numerical variable')
    data_info = data.info()

    # Selecting features and target variable for the regression model
    # Assuming we want to predict 'Main Workers - Total - Persons'
    target = 'Main Workers - Total -  Persons'
    features = data.columns.drop(target)

    # For simplicity, let's select only numerical features for now
    # In a real-world scenario, you would also want to consider categorical variables and potentially encode them
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns.drop(target)

    # Fill missing values with the mean (simple imputation)
    data[numerical_features] = data[numerical_features].fillna(data[numerical_features].mean())

    # Splitting the dataset into training and testing sets
    X = data[numerical_features]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardizing the numerical features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Linear Regression Model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Predictions
    y_pred = model.predict(X_test_scaled)

    # Evaluating the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    mse, r2
    sns.set_style("whitegrid")
    try:
        data = pd.read_table(data, encoding='ISO-8859-1')
    except Exception as e:
        error_message = str(e)

    # Check if the data is loaded successfully or not
    if 'data' in locals():
        success = True
        preview = data.head()
    else:
        success = False
        preview = None

    success, preview

    st.write("Model Evaluation Metrics:")
    st.metric(label="Mean Squared Error (MSE)", value=mse)
    st.metric(label="R-squared (R2)", value=r2)
    grouped_data = data.groupby('State Code')['Main Workers - Total -  Persons'].sum()

    fig, ax = plt.subplots()
    grouped_data.plot(kind='bar', ax=ax)
    ax.set_title('Total Main Workers by State')
    ax.set_xlabel('State Code')
    ax.set_ylabel('Main Workers - Total -  Persons')

    # Displaying the plot in Streamlit
    st.pyplot(fig)

elif selected == "Data Visualization":
    st.title("Data Visualization")


    def plot_histogram(column):
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        st.pyplot()


    # Function to plot a bar chart
    def plot_bar_chart(column):
        plt.figure(figsize=(10, 6))
        data[column].value_counts().plot(kind='bar')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        st.pyplot()


    # Select a column to visualize
    column = st.selectbox("Select a column for visualization", data.columns)

    # Select a type of plot
    plot_type = st.selectbox("Select the type of plot", ["Histogram", "Bar Chart"])

    # Display the selected plot
    if plot_type == "Histogram":
        plot_histogram(column)
    elif plot_type == "Bar Chart":
        plot_bar_chart(column)

