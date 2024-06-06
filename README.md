# SQL to Neo4j Pipeline

This project provides a Python-based pipeline for extracting data from a SQL database, transforming it, and loading it into a Neo4j graph database.

## Prerequisites

- Python 3.6 or later
- A SQL database (e.g., PostgreSQL, MySQL, SQLite)
- Neo4j graph database

## Installation

1. Clone the repository:
 ```bash 
 git clone https://github.com/your-username/sql_neo4j_pipeline.git
 ```
2. Navigate to the project directory:
 ```bash
 cd sql_neo4j_pipeline
 ```
3. Create a virtual environment (optional but recommended):
```bash 

python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

```
4. Install the required dependencies:
```bash 
pip install -r requirements.txt
```

## Configuration

Before running the pipeline, you need to configure the database connections and other settings in the `sql_neo4j_pipeline/config.py` file.

## Usage

To run the pipeline, execute the following command:
```bash
python scripts/run_pipeline.py
```
This will trigger the following steps:

1. **Extract**: Data is extracted from the configured SQL database.
2. **Transform**: The extracted data is transformed into a format suitable for the Neo4j graph database.
3. **Load**: The transformed data is loaded into the Neo4j graph database.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).