# Slash Phase 6 - Installation Guide

Welcome to the Slash Phase 6 project! This guide will walk you through the setup process to install and run the application.

---

## Prerequisites

Ensure the following are installed on your machine:

- **Python 3.10+**
- **Git**
- **pip** (Python package manager)
- PostgreSQL

## Installation Steps

1. **Clone the Repository**
    
    ```bash
    git clone <https://github.com/DFY-NCSU/slash-phase6.git>
    cd slash-phase6
    ```
    
2. **Set Up Virtual Environment** (recommended)
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
    ```
    
3. **Install Dependencies**
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Configure Database**:
    
    Ensure that PostgreSQL is installed. In the `src/database.py` file, update the database connection settings with your PostgreSQL username and password.
    
    Start the SQL with this command
    
    - For Windows
    
    ```bash
    pg_ctl -D your_path start
    ```
    
    - For Mac
    
    ```bash
    brew services start postgresql
    ```
    
    - For Linux
    
    ```bash
    sudo systemctl start postgresql
    ```
    

## Running the Application

1. **Run the Web Application**
    
    ```bash
    streamlit run src/slash_user_interface.py
    ```
    
2. Run the Backend Service:
    
    Navigate to the `src` directory and start the backend service:
    

```bash
cd src
python main.py
```

1. **Access the Application**
    - Open your browser and navigate to `http://localhost:xxxx` to start using the app.

---

## Usage

- Use the search functionality to find deals from popular e-commerce websites.
- Filter, sort, and compare results from multiple platforms.

---

## Troubleshooting

- If you encounter errors during installation, make sure all prerequisites are correctly installed.
- Ensure all dependencies in `requirements.txt` are installed without issues.

---

Enjoy using Slash Phase 6 to find the best deals online!

---