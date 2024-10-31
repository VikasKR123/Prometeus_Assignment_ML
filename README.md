# Toxic Comment Classification Application with Prometheus and Grafana Monitoring
## Application Overview
I created an ML-based Flask application that collects a comment from the user and detects whether the comment is toxic. If it is toxic, the application classifies it as severe toxicity, insult, threat, or other categories using logistic regression. I also integrated MLflow for experiment tracking, and the model achieved an accuracy of 93%.

![toxic-comment-classification](https://github.com/user-attachments/assets/77d1967f-dbf6-4162-b6b5-340c19210354)

![toxic2](https://github.com/user-attachments/assets/ba97a0ba-09e8-4bf5-970a-6e3cde45d052)


# Prometheus Metrics Collection
## REQUEST_COUNT: Tracks the total number of requests.
## COMMENT_COUNT: Tracks the total number of comments submitted.


## Docker image is available at ``vikaskarbail/toxic-comment-classification.``

The Deployment file manages the deployment of the toxic comment classification application on Kubernetes. It specifies the Docker image, number of replicas, and the container settings needed for the application to run. The Service file creates a NodePort service that exposes the application outside of the Kubernetes cluster, allowing it to be accessed via the Minikube IP and a specified port. This setup ensures that the application can be scaled and accessed consistently while running in the Kubernetes environment.

# Step 2: Helm Chart - Installing Prometheus and Grafana
<pre>
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Install Prometheus
helm install prometheus prometheus-community/prometheus

# Install Grafana
helm install grafana grafana/grafana
</pre>

# Step 3: Configure Prometheus Scrape Configs
Customize the scrape configuration by editing the values.yaml file or by overriding during installation. Example scrape config:

<pre>
  - job_name: toxic-comment-classification
  static_configs:
    - targets: ["192.168.49.2:30000"]

</pre>

# Step 4: Accessing and Configuring Prometheus and Grafana in Minikube
To access the Prometheus UI, Grafana UI, and Toxic Comment Application UI, use the Minikube IP along with their respective NodePorts.

To add Prometheus as a data source in Grafana:
<pre>
  1. Navigate to Configuration > Data Sources.
  2. Click Add data source and select Prometheus.
  3. Set the URL to http://prometheus-server
</pre>


# Step 5: Create Dashboards in Grafana
To create dashboards in Grafana:

Go to Create > Dashboard.
Add panels to visualize key metrics such as Total HTTP Requests, Memory Usage, and CPU Usage.

# Snapshots
![Screenshot from 2024-10-31 13-46-12](https://github.com/user-attachments/assets/6d8b7aea-ce29-4d91-8c87-f0ae0ed1c802)

![prometeus-mlops](https://github.com/user-attachments/assets/6b5fbdc3-d7c1-47f0-b818-e830595659b0)


![Screenshot from 2024-10-31 14-51-41](https://github.com/user-attachments/assets/8f53bad9-cac0-4b9d-9f7d-306d22c54788)

![dashbord-mlops](https://github.com/user-attachments/assets/53160781-b6b7-4679-863e-52177af4c08a)
