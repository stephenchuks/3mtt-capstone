
# Local Containerization and Microservices Simulation



## Project Overview
This project is a simulation of a multi-service application in a local environment, demonstrating containerization and orchestration using Docker and Docker Compose as a requirement for completion of the 3mtt Nigeria Cloud Computing Track. It includes three primary services:
1. **Product Service** - Manages products in an e-commerce setting.
2. **Order Service** - Manages customer orders.
3. **User Service** - Manages user accounts.

## Prerequisites
- **Docker** and **Docker Compose** must be installed on your machine.

## Setup Instructions

### Step 1: Download and Install Docker
1. **Download Docker**: Go to [Docker’s official website](https://www.docker.com/products/docker-desktop) and download Docker Desktop for your operating system.
2. **Install Docker**: Follow the installation instructions specific to your OS. After installation, open Docker Desktop (for Windows and Mac) or start Docker (Linux).

   **Command-line Verification**:
   
   docker --version
   docker-compose --version


### Step 2: Clone the Repository
Download the project files from the repository.

git clone https://github.com/username/repo-name.git
cd repo-name


### Step 3: Build and Run Services
1. **Build Docker Images**:
   Build each service image and start the containers using Docker Compose.
   
   docker-compose up --build -d
   

2. **Check Running Containers**:
   Verify that all containers are up and running.
   
   docker ps


3. **View Networks and IP Addresses**:
   To see the network and IPs for each container:

   docker network ls               # List all networks
   docker network inspect <network_name>  # Inspect a specific network

## Adding Data from the Command Line

### Access the CLI of Each Service
Use the following commands to open a shell in any service container:

docker exec -it <container_name> /bin/bash

Replace `<container_name>` with the name of the container (e.g., `product-service`, `order-service`, `user-service`).

### Example Commands to Add New Data

1. **Add a New Product**:
   
   curl -X POST http://localhost:8001/products -H "Content-Type: application/json" -d '{"name": "New Product", "price": 20.00, "description": "A sample product description", "stock": 100}'
  

2. **Add a New Order**:
   
   curl -X POST http://localhost:8002/orders -H "Content-Type: application/json" -d '{"user_id": 1, "product_id": 1, "quantity": 2}'
  

3. **Add a New User**:
   
   curl -X POST http://localhost:8003/users -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'


## Viewing Data from the Command Line

1. **View All Products**:
   
   curl http://localhost:8002/products
  

2. **View All Orders**:
   
   curl http://localhost:8001/orders
  

3. **View All Users**:
   
   curl http://localhost:8003/users


## Future Feature Considerations

While the primary focus of this project is to simulate container orchestration using Docker Compose, here are a few additional features that could be implemented with more advanced setups:

1. **Authentication and Authorization**:
   - Currently, there is no user authentication or authorization. Implementing JWT (JSON Web Token) or OAuth2 would add secure access to each service.

2. **Database Optimization and Sharding**:
   - A single database is used for each service. In a large-scale deployment, consider database sharding, replication, and using managed databases for improved performance.

3. **Load Balancing and Auto-Scaling**:
   - In cloud deployments, tools like Kubernetes, along with load balancers, would manage traffic distribution and automatically scale services based on load.

4. **Centralized Logging and Monitoring**:
   - For local testing, logs are basic and stored within containers. Implementing centralized logging (e.g., using ELK stack) and monitoring tools (e.g., Prometheus and Grafana) would provide enhanced observability.

5. **Inter-Service Communication via Message Queues**:
   - Currently, each service communicates through HTTP requests. For a more resilient setup, use a message broker (e.g., RabbitMQ or Kafka) to handle asynchronous communication between services.



## Cleanup
To stop and remove all running containers:

docker-compose down

## Conclusion
This project offers a foundational setup for running a microservices-based application using Docker and Docker Compose in a local environment. Further refinements, such as advanced scaling, security, and performance optimizations, would be necessary for a production-ready cloud deployment.

