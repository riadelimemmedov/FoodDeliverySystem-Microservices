# Food Delivery System - Microservices

<img width="85%" src="design_docs/order_container_diagram.png" alt=""/>

<hr/>

This repository contains the source code for a microservices-based food delivery system. The system is composed of several independent services that work together to provide a complete food ordering and delivery experience.

## Services

The food delivery system consists of the following microservices:

1. **Order Service**: Handles the creation, management, and tracking of food orders.
2. **Payment Service**: Processes payments for the placed orders.
3. **Kitchen Service**: Manages the preparation of food orders in the kitchen.
4. **Delivery Service**: Coordinates the delivery of completed orders to customers.

Each service is designed to be self-contained, scalable, and easily maintainable. They communicate with each other using a messaging system or RESTful APIs.

## Architecture

The food delivery system follows a microservices architecture, which provides several benefits:

- **Scalability**: Each service can be scaled independently based on its specific resource requirements.
- **Flexibility**: New services can be added or existing services can be modified without affecting the entire system.
- **Fault Tolerance**: If one service fails, the others can continue to operate, ensuring the overall system's reliability.
- **Technology Diversity**: Different services can be implemented using the most appropriate technologies for their specific requirements.

## Used Technologies

- **FastAPI**: For creating async and resilience rest api.
- **Redis**: For managing cache and data consistency and for caching of Orders and Microservice URLs.
- **Vault**: Managing secret values on docker side container.
- **Prism CLI**: For mocking the behavior of several of my Microservices.
- **Docker Desktop**: To manage the external components below.
- **MongoDB**: Store data durable on key:value format.
- **RabbitMQ**: Using as a message broker in event driven architecture system.
- **Https**: Keep the communication between web services encrypted.
- **API-key**: Authentication for the web service end points.

## Architectural Patterns and Design Principles

- **Hexagonal Architecture (Ports and Adapters)**: The system is designed using the Hexagonal Architecture pattern, which separates the core business logic from the infrastructure and external dependencies. This allows for better testability and flexibility in adapting to changes.
- **Dependency Injection**: The project utilizes Dependency Injection to manage the dependencies between the various components and services. This promotes modularity, testability, and flexibility in the system.
- **Repository Design Pattern**: The project uses the Repository design pattern to abstract the data access logic from the business logic. This separates the concerns and makes the codebase more maintainable and testable.
- **Unit of Work**: The Unit of Work pattern is used to manage database transactions and ensure data consistency across multiple operations.
- **Facade Pattern**: The Facade pattern is employed to provide a simplified interface to the complex underlying systems, making it easier for the clients to interact with the system.

The overall architecture of the system is depicted in the following diagram:
