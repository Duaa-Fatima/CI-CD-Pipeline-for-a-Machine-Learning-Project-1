# CI/CD Pipeline for a Machine Learning Project

## Authors
- **Duaa Fatima** (21i-1667)
- **Syeda Mahum Raza** (21i-1662)
- **Section:** AI-B  
- **Assignment 1**

##  Introduction
This project implements a **CI/CD pipeline** for a machine learning application using **Jenkins, Docker, and GitHub Webhooks**. The pipeline ensures **automatic builds and deployments** whenever changes are pushed to the `dev` branch.

---

##  Flask Application Development
A Flask-based **diabetes prediction model** was developed. Key components include:

- **`app.py`** - Flask API for handling user inputs and returning predictions.
- **`model.py`** - Machine learning model logic (loading and training).
- **Flake8 Compliance** - Code was formatted according to **Flake8** standards to maintain code quality.

---

##  Jenkins Pipeline Configuration
A `Jenkinsfile` was created to automate the CI/CD pipeline. The pipeline consists of the following stages:

###  Checkout Code
- The pipeline pulls the latest code from the `dev` branch of the GitHub repository.

###  Flake8 Code Quality Check
- **Flake8** is installed and executed to check Python syntax errors and formatting issues.

###  Build Docker Image
- The application is packaged into a **Docker container** using the `Dockerfile`.
- The container image is tagged as `wthduaa/diabetes-predictor:latest`.

###  Push to Docker Hub
- The Docker image is **pushed to Docker Hub** using stored credentials.

###  Email Notification
- Upon successful pipeline execution, an **email notification** is sent to the team.

---

##  Repository Structure

```
├── app/
│   ├── app.py              # Flask API
│   ├── model.py            # Machine Learning Model
│   ├── requirements.txt    # Dependencies
├── docker/
│   ├── Dockerfile          # Docker Configuration
├── jenkins/
│   ├── Jenkinsfile         # CI/CD Pipeline Configuration
├── data/
│   ├── diabetes.csv        # Dataset
├── README.md               # Project Documentation
└── requirements.txt        # Required Python Libraries
```

---

##  Final Test and Deployment
To verify the pipeline:
1. A **test commit** was pushed to the `dev` branch.
2. **Jenkins automatically triggered** the pipeline build.
3. The pipeline successfully **built the Docker image, pushed it to Docker Hub, and sent an email notification**.

---

##  Conclusion
The CI/CD pipeline is now **fully automated**. Every time a developer pushes changes to the `dev` branch:

✔ **Jenkins builds the application.**  
✔ **Runs code quality checks.**  
✔ **Packages and uploads the image to Docker Hub.**  
✔ **Notifies the team via email.**  

---

##  Future Improvements
- Add **unit testing** to validate the model before deployment.
- Deploy the application to **AWS/GCP/Azure**.
- Implement **logging and monitoring** for better observability.

---

##  Contributing
Contributions are welcome! Feel free to **fork**, **submit issues**, or **create pull requests**.

---


