# Dockerized GUI Text Editor

This repository demonstrates the use of Docker and x11docker for GUI application development and testing. It includes a sample Python-based text editor and the necessary Dockerfile for containerization.

## Prerequisites

Before proceeding, ensure the following are installed on your system:

- **Docker**: Install Docker by following the instructions on [Docker's official website](https://www.docker.com/).
- **x11docker**: Install x11docker from [x11docker GitHub page](https://github.com/mviereck/x11docker) to enable GUI support for Docker containers.

## Steps to Run the Application

1. **Clone the repository**  
   Clone this repository to your local system using the following command:
   ```bash
   git clone https://github.com/genesfidelt/Dockerized-Text-Editor.git

2. **Navigate to the project root directory**  
   Move into the root directory of the cloned repository:
   ```bash
   cd Dockerized-Text-Editor

3. **Build the Docker image**  
   Build the Docker image using the provided Dockerfile:
   ```bash
   docker build -t dockerized-text-editor .

4. **Run the application with x11docker**  
   Start the GUI application in a container using x11docker:
   ```bash
   x11docker dockerized-text-editor

5. **Access the text editor**  
   Once the container is running, the GUI-based text editor will be displayed, allowing you to test and use the application.
