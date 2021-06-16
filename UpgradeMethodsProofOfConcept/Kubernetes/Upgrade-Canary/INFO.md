kubectl create ns canary-de-mana
kubectl -n canary-de-mana apply -f deployment-version1.yml -f service-version1.yml -f ingress-version1.yml
kubectl delete ns canary-de-mana
kubectl -n canary-de-mana delete all --all
kubectl -n canary-de-mana get all
kubectl -n canary-de-mana get ingress

kubectl -n canary-de-mana apply -f deployment-db.yml -f service-db.yml


kubectl -n canary-de-mana apply -f ../../Kubernetes-SimpleApp/Upgrade-Canary/deployment-version1.yml


mysql.canary-de-mana.svc.cluster.local

dizertatie-service-db.canary-de-mana.svc.cluster.local

/etc/hosts
192.168.64.2 dizertatie.com

BUILD:
cd /Users/eusebiu.rizescu/Data/Git/dizertatie-minikube/UpgradeMethodsProofOfConcept/DockerImages/Web-Version1
docker build -t dizertatie:webversion1 .
docker tag dizertatie:webversion1 ebieusebiu/dizertatie:webversion1
docker push ebieusebiu/dizertatie:webversion1

cd /Users/eusebiu.rizescu/Data/Git/dizertatie-minikube/UpgradeMethodsProofOfConcept/DockerImages/Web-Version2
docker build -t dizertatie:webversion2 .
docker tag dizertatie:webversion2 ebieusebiu/dizertatie:webversion2
docker push ebieusebiu/dizertatie:webversion2
