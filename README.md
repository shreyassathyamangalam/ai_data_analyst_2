# ai-data-analyst

![Project Logo](https://your-logo-url-here)  <!-- Replace with the logo URL if you have one -->

## Overview

`ai-data-analyst` is a Python-based application designed to facilitate data analysis tasks utilizing modern AI tools and techniques. This project leverages libraries such as LangChain and Streamlit to provide a user-friendly interface for interacting with datasets, performing analyses, and visualizing results.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Analyze data with AI-driven insights.
- Interactive frontend for visualizing and manipulating datasets.
- Automated database creation and configuration.
- Supports multiple data formats for seamless integration.

## Installation

To install the `ai-data-analyst` project, ensure you have Python 3.13 or higher installed. You can create a virtual environment for better dependency management:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt  # generate the requirements.txt file from pyproject.toml
```

Alternatively, you can install the dependencies directly via pip:

```bash
pip install langchain>=1.0.3 langchain-openai>=1.0.2 python-dotenv>=1.2.1 sqlalchemy>=2.0.44 streamlit>=1.51.0
```

## Usage

Once the installation is complete, you can run the application using the following command:

```bash
python main.py
```

This command will launch the application, allowing you to interact with the data analysis tools via your web browser.

## File Descriptions

- **.gitignore**: Specifies files and directories that should not be tracked by git.
- **.python-version**: Contains the Python version used for the project.
- **README.md**: Documentation file containing project information and instructions.
- **create_database.py**: Script responsible for setting up the SQLite database (`retail.db`).
- **frontend.py**: The main script that handles the UI rendering using Streamlit.
- **main.py**: Entry point for launching the application.
- **pyproject.toml**: Project metadata and dependency management file.
- **retail.db**: The SQLite database file that stores the data.
- **uv.lock**: A lock file managing project dependencies.

## Dependencies

This project depends on several Python libraries, as specified in the `pyproject.toml`:

- `langchain>=1.0.3`
- `langchain-openai>=1.0.2`
- `python-dotenv>=1.2.1`
- `sqlalchemy>=2.0.44`
- `streamlit>=1.51.0`

Make sure these libraries are installed to ensure the application runs smoothly.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (e.g., `feature-branch`).
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Submit a pull request with a description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to reach out if you have any questions or need assistance with the project!