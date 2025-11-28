# Git Commit Extractor

## About
 - A simple project for extracting all your commits with metadata from specified **LOCAL** repositories

## Getting started
 - Make sure you have `Python` installed, preferably version `3.13` or newer
   - Download here: https://www.python.org/downloads/latest/python3.13/
   - Or use the Python Version Manager `pyenv`: https://github.com/pyenv/pyenv
 - Create virtual environment: `python3 -m venv .venv`
 - Install poetry, see https://python-poetry.org/docs/basic-usage/
 - Install dependencies: `poetry install`
 - **COPY and RENAME** `_config.toml` to `config.toml`
 - Run the main.py

## Configuration
 - Configuration is managed in the `config.toml` file
 - You can set there
   - `output_path`
     - Output path for the json with commits
   - `repo_paths`
     - Repository paths to search
   - `user_names`
     - User names to filter commits
