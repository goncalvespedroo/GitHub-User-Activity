# GitHub User Activity CLI 

A simple and efficient command-line interface (CLI) tool to fetch the recent activity of any GitHub user directly from your terminal.

This project was developed as part of a study on **Computational and Logical Thinking**, using the GitHub API to demonstrate real-time data consumption.

## Technologies Used

- **Python 3**
- **Requests:** For consuming the GitHub REST API  
- **Setuptools:** To package the script as a global CLI tool  
- **Pipx:** For installation in isolated environments (recommended for Linux)

## Installation

To install the tool globally on your machine, follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/goncalvespedroo/GitHub-User-Activity.git
   cd GitHub-User-Activity
   pipx install --editable .

Usage

After installation, you can use the githubactivity command followed by the username you want to query:

githubactivity goncalvespedroo

Example Output:
Name: PushEvent | Repository: goncalvespedroo/GitHub-User-Activity
Name: CreateEvent | Repository: goncalvespedroo/myNvim
Name: MemberEvent | Repository: DevMoitinho/MovieApp

📂 Project Structure
main.py: Contains the API consumption logic and the CLI entry point
setup.py: Packaging configuration and global command definition
