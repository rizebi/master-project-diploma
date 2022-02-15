# Bachelor's degree diploma project

In few words, this is a "framework" created by me in order to compare different method of upgrade in Kubernetes. During upgrade a script will simulate traffic, Prometheus will scrape the metrics, and in Grafana we can see the graphs and draw conclusions.

Unfortunately the documentation for it is not in English. The file can be find in Documentation/Final/EusebiuRizescu.pdf 

Note that this repository is copied form Gitlab. We can si a Gitlab CI file and also there is an integration in scripts with Gitlab Kubernetes cluster.

# Longer description
An important aspect when an application is used by customers is that the upgrade of it to a new version, should have the least impact felt by users. Customers expect the application to be available at all times and developers want to upgrade as often as possible to test and improve the new code as soon as possible. There are several upgrade strategies that will be discussed in this document. To validate and test them, an application upgrade was simulated in several ways, on the Kuberenetes infrastructure.
