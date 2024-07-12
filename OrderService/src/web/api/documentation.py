from fastapi import Path

# Local modules
from ...config.setup import config

order_id_documentation = Path(
    ...,
    description="**Order ID**: *Example `dbb86c27-2eed-410d-881e-ad47487dd228`*. "
    "A unique identifier for an existing Order.",
)
""" OpenAPI order ID documentation. """

health_example = {
    "status": True,
    "cert_remaining_days": 820,
    "version": f"{config.version}",
    "name": f"{config.service_name}",
    "resources": [
        {"name": "Certificate.valid", "status": True},
        {"name": "MongoDb", "status": True},
        {"name": "RabbitMq", "status": True},
        {"name": "PaymentService", "status": True},
        {"name": "KitchenService", "status": True},
        {"name": "DeliveryService", "status": True},
        {"name": "CustomerService", "status": True},
    ],
}
""" OpenAPI health response documentation. """

resource_example = {
    "status": True,
    "cert_remaining_days": 820,
    "version": f"{config.version}",
    "name": f"{config.service_name}",
    "resources": [
        {"name": "Certificate.valid", "status": True},
        {"name": "MongoDb", "status": True},
        {"name": "RabbitMq", "status": True},
        {"name": "PaymentService", "status": True},
        {"name": "KitchenService", "status": True},
        {"name": "DeliveryService", "status": True},
        {"name": "CustomerService", "status": True},
    ],
}
""" OpenAPI health response documentation. """

tags_metadata = [
    {
        "name": "Orders",
        "description": f"The ***{config.service_name}*** handle Orders for the Fictitious Company.",
    }
]
""" OpenAPI Orders endpoint documentation. """

license_info = {
    "name": "License: Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
}
""" OpenAPI license documentation. """

servers = [
    {
        "url": "https://127.0.0.1:8000",
        "description": "URL for local development and testing",
    },
    {
        "url": "https://coffeemesh-staging.com",
        "description": "staging server for testing purposes only",
    },
    {"url": "https://coffeemesh.com", "description": "main production server"},
]
""" OpenAPI API platform servers. """

description = """
<img width="65%" align="right" src="/static/order_container_diagram.png"/>
**An example on how to use FastAPI and RabbitMQ asynchronously to create a RESTful API for responses that 
takes a bit more time to process.** 

This service implements a Facade pattern to simplify the complexity between the MicroServices in the system 
and the WEB GUI program (it only has to work against one API).

The OrderService handles multiple status updates from several services during the lifecycle of an Order. These 
responses are asynchronous events spread out over time and to be able to handle this type of dynamic the RabbitMQ 
message broker is used. The RabbitMQ queue routing technique is used since it is designed to scale with the growing 
needs of the service.

The key to this design is that a metadata structure is part of every message that is sent between the services in 
the system. This `MetaDataSchema` structure is described in the Schemas section for the 
[PaymentService](https://127.0.0.1:8001/docs). 

<br>**The following HTTP status codes are returned:**
  * `200:` Successful GET response.
  * `202:` Successful POST response.
  * `204:` Successful DELETE response.
  * `400:` Failed updating Order in DB.
  * `404:` Order not found in DB.
  * `422:` Validation error, supplied parameter(s) are incorrect.
  * `500:` Failed to connect to internal MicroService.
  * `500:` Failed Health response.
<br><br>
---
"""
""" OpenAPI main Order documentation. """
