# 0x09. Web Infractructure Design
<img align="center" alt="Web infrastructure Design"  src="https://app.eraser.io/workspace/HHPR0Ok9FUSTD119dtRP?elements=Qi75AuKZLZxTSwoB5S5zPA" />

## Resources:

### Read or watch:

-  Network basics concept page
- Server concept page
-  Web server concept page
- DNS concept page
- Load balancer concept page
- Monitoring concept page

- [What is a database](https://intranet.alxswe.com/rltoken/n3CdS3EA5l5psDDKbEhApA)
-  [What’s the difference between a web server and an app server?](https://intranet.alxswe.com/rltoken/0as4wDlFqyhLhf0f_gedcw)
- [DNS record types](https://intranet.alxswe.com/rltoken/Pl3UoEfAO7K_jUKRLMmnAQ)
- [Single point of failure](https://intranet.alxswe.com/rltoken/uxpx2YhXs10TFLIDg78chA)
- [How to avoid downtime when deploying new code](https://intranet.alxswe.com/rltoken/4ansLu2gtHnoFrNThqyObA)
- [High availability cluster (active-active/active-passive)](https://intranet.alxswe.com/rltoken/TAJeVYy9U9iLaEDd6XkbRA)
- [What is HTTPS](https://intranet.alxswe.com/rltoken/c0zs2MxrmxFLsCPOizxq6g)
- [What is a firewall](https://intranet.alxswe.com/rltoken/j6idMcUTyNEDj1oYDQFmUw)


# TASK-0 : Simple Web Stack
<img align="center" alt="Simple Web Stack"  src="https://app.eraser.io/workspace/HHPR0Ok9FUSTD119dtRP?elements=HVlZb6-CEYaeDDm1v_Dw3Q" />

## **Components:**

1. **Server:** A server is a powerful computer that provides resources, data, services, or programs to other computers, known as clients, over a network.

2. **Domain Name:** A domain name is a unique identifier for a website on the internet. It acts as an address that users can type into a web browser to find and access 
a website.

3. **IP Address:** An IP address, or Internet Protocol address, is a unique numerical identifier assigned to every device on the internet.

4. **DNS Record:** A DNS record, or Domain Name System record, is an entry in a DNS database that maps a domain name to an IP address. 

5. **Web Server:** A web server is a program that delivers web pages to users' web browsers.

6. **Application Server:** An application server is a program that runs the application logic and handles user requests.

7. **Database:** A database is a structured collection of data that is organized and stored for easy retrieval and management.

## **Understanding the Infrastructure:**

1. **Server:** The server acts as the central point for hosting and delivering the application and its associated data.

2. **Domain Name:** The domain name "[﻿foobar.com](https://foobar.com/)" is configured with a "www" record that points to the server's IP address 8.8.8.8.

3. **DNS Record:** The "www" record associates the domain name "[﻿foobar.com](https://foobar.com/)" with the IP address 8.8.8.8, allowing users to access the websites using the familiar domain name rather than the direct IP address.

4. **Web Server:** A web server, such as Nginx, is responsible for receiving the request from the user's browser, retrieving the appropriate web pages from the application server, and sending them back to the browser.

5. **Application Server:** The application server is responsible for processing user interactions, accessing the database, and generating dynamic content for the web server to deliver.

6. **Database:** The database, such as MySQL, Stores the application data, such as user profile, product information, and the order details.

## **Communication Between Server and User Computer:**
The server communicates with the user's computer using the Hypertext Transfer Protocol (HTTP), a standardized protocol for exchanging information between web servers and web browsers. When a user requests a web page from the website, their browser sends HTTP request to the server's IP address. The server processes the request, retrieves the requested web page from the application server, and sends back an HTTP response containing the webpage content.



## **Potential Issues with the Infrastructure:**

1. **Single Point of Failure (SPOF):** The reliance on a single server for hosting both the web server and application server creates a single point of failure (SPOF). If the server goes down, the entire website becomes unavailable, causing downtime and disrupting user access.

2. **Downtime during Maintenance:** When maintenance is needed, such as deploying new code, the web server needs to be restarted, causing downtime for the website. This can disrupt user access and potentially impact business operations.

3. **Scalability Limitations:** The infrastructure's ability to handle increasing traffic is limited due to its reliance on a single server. As traffic grows, the server may become overloaded, leading to slow performance and potential crashes.

## **TASK-1 : **Distributed web infrastructure
<img align="center" alt="Distributed Web Infrastructure"  src="https://app.eraser.io/workspace/HHPR0Ok9FUSTD119dtRP?elements=CSq651S86YxX8iC4aSeCsA" />

## **Components and Explanations:**

1. **Load Balancer (HAproxy):** A load balancer distributes incoming traffic across multiple servers, ensuring efficient resource utilization and preventing overloading of any single server. It acts as a single entry point for client requests, directing traffic to the most appropriate server based on load balancing algorithms.

2. **Distribution Algorithm:** In this setup, the load balancer is configured with a Round Robin (RR) algorithm, which evenly distributes incoming requests among the available servers in a circular fashion. This ensures that no single server is overwhelmed with traffic, maintaining optimal performance and responsiveness. 

3. **Active-Active vs. Active-Passive Setup:** In this infrastructure, an active-active setup is recommended to maximize availability and responsiveness.
    - **Active-Active:** In an active-active setup, both servers are actively handling client requests simultaneously. This configuration provides the highest level of availability, as if one server fails, the other can immediately take over without any downtime.
    - **Active-Passive:** In an active-passive setup, only one server is actively handling requests at a time, while the other server remains passive as a standby. The passive server is synchronized with the active server's data, ensuring seamless failover when the active server fails.

4. **Web Server (Nginx):** The web server receives requests from the load balancer, retrieves the requested web pages or static content from the application server, and sends them back to the client's browser. It acts as an intermediary between the client and the application server, handling HTTP requests and delivering web content efficiently.

5. **Application Server:** The application server hosts the application's code and handles dynamic content generation. It receives requests from the web server, processes user interactions, retrieves data from the database, and generates dynamic web pages to be sent back to the client. It is the core of the application logic and business operations.

6. **Database (MySQL):** The database stores the application's data, such as user profiles, product information, and order details. It provides a structured and organized data storage system, enabling the application to access and manage its data efficiently.
**Addressing Potential Issues:**

1. **SPOFs:**
    - **Load Balancer:** The load balancer is a potential SPOF, as its failure would disrupt traffic distribution and potentially bring down the entire website. To mitigate this risk, consider implementing a redundant load balancer configuration.
    - **Database:** The database is a potential SPOF, as its failure would prevent the application from accessing its data. To mitigate this risk, consider implementing a database Primary-Replica (Master-Slave) cluster.
2. **Security Issues:**
    - **Firewall:** The absence of a firewall leaves the network vulnerable to unauthorized access and cyberattacks. Implement a firewall to filter incoming and outgoing traffic, protecting the infrastructure from malicious activities.
    - **HTTPS:** The absence of HTTPS means that data transmission is unencrypted, exposing sensitive information to interception. Implement HTTPS to encrypt data communication between the web server and the client's browser, ensuring data confidentiality and integrity.
3. **Monitoring:** The lack of monitoring makes it difficult to identify and resolve potential issues promptly. Implement monitoring tools to track server performance, resource utilization, and application health, enabling proactive identification and resolution of problems.

# **TASK-2 : ** Secured and monitored web infrastructure
<img align="center" alt="Secured and monitored web infrastructure"  src="https://app.eraser.io/workspace/HHPR0Ok9FUSTD119dtRP?elements=2Bta41GI6SZ4Fgpm-R0RVg" />

## Additional Components and Explanations:

1. **Firewalls:** Firewalls act as gatekeepers, filtering incoming and outgoing network traffic based on predefined rules and security policies. They protect the infrastructure from unauthorized access, malicious attacks, and data breaches.
    - **Front-End Firewall:** The front-end firewall protects the load balancer and web server from external threats. It filters incoming traffic, blocks suspicious connections, and prevents unauthorized access attempts.
    - **Application Firewall:** The application firewall protects the application server from application-level attacks, such as SQL injection and cross-site scripting (XSS). It monitors application-specific traffic patterns and blocks malicious requests.
    - **Database Firewall:** The database firewall protects the database from unauthorized access and data manipulation. It controls access to the database and restricts database queries based on security policies.

2. **SSL Certificate:** An SSL certificate, or Secure Sockets Layer certificate, enables HTTPS encryption, securing communication between the web server and the client's browser. It encrypts data transmission, protecting sensitive information, such as login credentials and financial data, from interception and eavesdropping.

3. **Monitoring Clients:** Monitoring clients, or data collectors, gather performance and health data from the servers and infrastructure components. They provide real-time insights into system performance, resource utilization, and application health, enabling proactive problem detection and resolution.
**Monitoring QPS (Queries Per Second):**

To monitor QPS (Queries Per Second) for the web server, you can use a monitoring client that collects metrics related to HTTP requests and response times. By analyzing these metrics, you can identify trends, potential bottlenecks, and performance issues related to the web server's handling of requests.

**Potential Issues:**

1. **SSL Termination at Load Balancer:** While terminating SSL at the load balancer offloads encryption from the web servers, it can introduce a single point of failure (SPOF) if the load balancer fails. Consider using a hardware load balancer with dedicated SSL acceleration capabilities to mitigate this risk.

2. **Single MySQL Write Server:** Having only one MySQL server capable of accepting writes creates a potential SPOF and limits scalability. Implement a database Primary-Replica (Master-Slave) cluster to enable write operations on multiple servers, enhancing availability and scalability.

3. **Identical Server Components:** Having servers with all the same components (database, web server, and application server) can make it challenging to scale components independently. Consider using a containerized environment, such as Docker, to package each component separately, allowing for flexible scaling of individual components.

# **TASK-3 : ** Scale up
<img align="center" alt="Scale up"  src="https://app.eraser.io/workspace/HHPR0Ok9FUSTD119dtRP?elements=_V1lIxBwtB4h1ZOV_lSRSg" />

## **Additional Components and Explanations:**

1. **Additional Load Balancer (HAproxy):** Introducing a second load balancer configured as a cluster with the existing one provides redundancy and enhances fault tolerance. If one load balancer fails, the other can take over without disrupting traffic flow, ensuring high availability.

2. **Dedicated Web Servers:** Separating the web server function onto dedicated servers allows for independent scaling of web resources, enabling you to allocate more resources to the web server layer if traffic demands increase.

3. **Dedicated Application Servers:** Isolating the application server function onto dedicated servers provides a clear separation of concerns and allows for independent scaling of application logic. You can scale up application servers to handle increased application workload without affecting other components.

4. **Database Replication (Master-Slave Cluster):** Implementing a database replication setup using a Master-Slave cluster eliminates the single point of failure associated with a single MySQL write server. The Master node handles write operations, while the Slave nodes replicate data and can take over as the Master if needed.

**Benefits of the Updated Infrastructure:**

- **Enhanced Availability:** The redundant load balancers, database replication cluster, and dedicated servers with independent scaling capabilities significantly improve overall infrastructure availability, minimizing downtime and ensuring continuous service delivery.

- **Scalability:** The separation of components allows for flexible scaling of each layer based on specific demands. You can scale up web servers to handle increased traffic, application servers to handle more complex processing, and database replicas to accommodate growing data volumes.

- **Improved Performance:** By distributing load across multiple servers, you can optimize performance and reduce response times, ensuring a smooth user experience even under heavy traffic conditions.

- **Fault Tolerance:** The redundancy and isolation of components provide greater resilience to failures. If one component fails, the others can continue operating, minimizing disruption and ensuring the overall health of the infrastructure.