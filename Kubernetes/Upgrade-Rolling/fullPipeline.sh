# /bin/bash

date
echo "Clean All"
kubectl -n dizertatie-minikube-24349559-canary delete all --all
kubectl -n dizertatie-minikube-24349559-canary delete ingress --all
kubectl -n dizertatie-minikube-24349559-canary delete IngressRoute --all
echo "Done cleaning"
sleep 60
date
echo "Start version 1"
kubectl -n dizertatie-minikube-24349559-canary apply -f deployment-version1.yml -f service.yml -f ingress.yml
sleep 300
date
echo "Start version 2"
kubectl -n dizertatie-minikube-24349559-canary apply -f deployment-version2.yml
sleep 70 # to start new version
echo "Scale down version1"
kubectl -n dizertatie-minikube-24349559-canary apply -f deployment-version1-scaled-down.yml

sleep 300
date
echo "Rollback to only version 1"
kubectl -n dizertatie-minikube-24349559-canary delete -f deployment-version2.yml
echo "Scale up version 1"
kubectl -n dizertatie-minikube-24349559-canary apply -f deployment-version1.yml
sleep 300
date
echo "Delete all"
kubectl -n dizertatie-minikube-24349559-canary delete all --all
kubectl -n dizertatie-minikube-24349559-canary delete ingress --all
kubectl -n dizertatie-minikube-24349559-canary delete IngressRoute --all