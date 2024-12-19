# **Microservices-Based Application on Kubernetes (KIND)**

This project demonstrates a sample **microservices-based application** deployed on a **Kubernetes** cluster using **KIND (Kubernetes IN Docker)**. The application consists of two frontend services, a backend service, and a database, showcasing a modern, scalable architecture.

---

## 🚀 **Project Architecture**

- **Frontend 1**: Accepts user input data (e.g., name and value).
- **Frontend 2**: Displays the data submitted via Frontend 1.
- **Backend**: A Django-based API that handles requests and communicates with the database.
- **Database**: MySQL database for storing persistent data.

### **Architecture Overview**
1. Frontend 1 → Backend → Database → Frontend 2
2. Communication between services is facilitated using Kubernetes services (`ClusterIP`, `NodePort`).

---

## 🛠️ **Technologies Used**

- **Kubernetes**: Orchestrated the deployment of all services.
- **KIND (Kubernetes IN Docker)**: Lightweight Kubernetes cluster for local testing.
- **Docker**: Containerized all components.
- **Django**: Backend API framework.
- **MySQL**: Database for persistent storage.
- **NGINX**: Frontend web server.

---

## 📂 **Project Structure**

```bash
├── backend/
│   ├── Dockerfile           # Backend Dockerfile
│   ├── requirements.txt     # Backend dependencies
│   └── ...                  # Backend Django project files
├── frontend1/
│   ├── Dockerfile           # Frontend1 Dockerfile
│   └── ...                  # Frontend1 application files
├── frontend2/
│   ├── Dockerfile           # Frontend2 Dockerfile
│   └── ...                  # Frontend2 application files
├── mysql-deployment.yaml    # MySQL Deployment and Service
├── mysql-pv.yaml    # MySQL Deployment and Service
├── mysql-service.yaml    # MySQL Deployment and Service
├── backend-deployment.yaml  # Backend Deployment and Service
├── backend-service.yaml     # Backend Deployment and Service
├── frontend1-deployment.yaml # Frontend1 Deployment and Service
├── frontend2-deployment.yaml # Frontend2 Deployment and Service
└── README.md                # Project Documentation
```
backend-service.yaml
---

## ⚙️ **Setup and Deployment**

### Prerequisites

1. **Docker**: Install [Docker](https://docs.docker.com/get-docker/).
2. **KIND**: Install [KIND](https://kind.sigs.k8s.io/docs/user/quick-start/).
3. **kubectl**: Install [kubectl](https://kubernetes.io/docs/tasks/tools/).

### Step 1: Start a KIND Cluster

```bash
kind create cluster --name microservice
```

### Step 2: Build and Load Docker Images

```bash
# Build Docker images
docker build -t backend:latest ./backend
docker build -t frontend1:latest ./frontend1
docker build -t frontend2:latest ./frontend2

# Load images into KIND cluster
kind load docker-image backend:latest --name microservice
kind load docker-image frontend1:latest --name microservice
kind load docker-image frontend2:latest --name microservice
```

### Step 3: Apply Kubernetes Manifests

```bash
kubectl apply -f mysql-deployment.yaml
kubectl apply -f mysql-service.yaml
kubectl apply -f mysql-pv.yaml
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
kubectl apply -f frontend1-deployment.yaml
kubectl apply -f frontend2-deployment.yaml
```

### Step 4: Verify Deployment

```bash
# Check all pods are running
kubectl get pods

# Check all services
kubectl get svc
```

---

## 🌐 **Access the Application**

1. **Frontend 1**:
   - Access the data input frontend at `http://localhost:30001`.
   - Submit data (e.g., name and value).

2. **Frontend 2**:
   - Access the data display frontend at `http://localhost:30002`.
   - Verify the submitted data is displayed correctly.

3. **Backend**:
   - Interacts internally with Frontend 1 and the database.

---

## 📚 **Key Features**

- **Kubernetes Deployments**: Manages replicas for each service.
- **NodePort Services**: Exposes frontend services for external access.
- **ClusterIP Service**: Connects the backend and database internally.
- **Configuration Maps and Secrets**: Secures database credentials.

---

## 🐛 **Troubleshooting**

1. **Pod Not Starting**:
   - Check pod logs:
     ```bash
     kubectl logs <pod-name>
     ```

2. **Service Not Accessible**:
   - Verify services are running:
     ```bash
     kubectl get svc
     ```
   - Ensure the correct NodePort is used in your browser.

3. **Database Connection Issues**:
   - Verify database environment variables are correctly set in `backend-deployment.yaml`.

---

## 📜 **Future Improvements**

- Add an **Ingress Controller** for simplified service access.
- Use a **LoadBalancer Service** for production-grade deployments.
- Integrate CI/CD pipelines for automated deployments.

---

## 🧑‍💻 **Contributors**

- **Abdul Rehman**

Feel free to contribute or provide feedback!

---

## 📄 **License**

This project is licensed under the [MIT License](LICENSE).
