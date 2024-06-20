# SQL Query Generator with Generative AI

Welcome to the SQL Query Generator project! This application leverages the Gemini AI model to simplify the process of writing SQL queries. Users can input natural language prompts to generate SQL queries, along with explanations and expected outputs. Built with Streamlit, the app provides a user-friendly web interface for interacting with the AI model.

## Features

- **Natural Language Input**: Type in prompts describing your desired SQL query.
- **SQL Query Generation**: Automatically generate SQL queries based on your prompts.
- **Expected Output**: View sample outputs for the generated SQL queries.
- **Query Explanation**: Get clear explanations for the generated SQL queries.

## Technologies Used

- **Streamlit**: A web application framework for creating interactive applications.
- **Google Generative AI (Gemini API)**: An API for generating human-like text based on prompts.
- **Python**: The primary programming language used.
- **Pandas**: For handling and displaying tabular data.
- **SQLite**: For in-memory database operations during query generation.

## Setup and Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Google Generative AI (Gemini API) key

### Installation Steps

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/sql-query-generator.git
    cd sql-query-generator
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the project root directory and add your Gemini API key:
      ```env
      GEMINI_KEY=your_gemini_api_key
      ```

5. **Run the application**:
    ```sh
    streamlit run app.py
    ```

## Usage

1. **Enter Prompt**:
   - In the text area provided, enter a natural language prompt describing the SQL query you need.
   - Example: "I want people whose first name starts with S".

2. **Generate SQL Query**:
   - Click the "Generate SQL Query" button to generate the SQL query.
   - The application will display the generated SQL query, an expected output, and a simple explanation of the query.

### Example

1. **Input Prompt**:
   ```
   I want people whose first name starts with S
   ```

2. **Generated SQL Query**:
   ```sql
   SELECT *
   FROM your_table
   WHERE First_Name LIKE 'S%';
   ```

3. **Expected Output**:
   ```
   | First_Name | Last_Name | Age | ...
   |------------|-----------|-----| ...
   | Sarah      | Connor    | 35  | ...
   | Steve      | Rogers    | 99  | ...
   ```

4. **Explanation**:
   ```
   This SQL query selects all columns from the table named `your_table` where the `First_Name` column starts with the letter 'S'. The `LIKE 'S%'` clause is used to find matches where the first character of the `First_Name` is 'S'.
   ```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Google Generative AI** for providing the powerful AI model.
- **Streamlit** for the easy-to-use web application framework.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).

---

Thank you for using the SQL Query Generator! We hope it makes your SQL querying process simpler and more efficient.
