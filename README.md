minikube start

kubectl proxy --port=19970 --address 0.0.0.0 --accept-hosts '.*' &

cd /Users/eusebiu.rizescu/Data/Git/dizertatie-minikube/UpgradeMethodsProofOfConcept/Scripts
python3 loadTest.oy

Start V1 from Gitlab

kubectl -n dizertatie-minikube-24349559-canary-web exec $(kubectl -n dizertatie-minikube-24349559-canary-web get pods | grep production | grep -v "production-db" | head -1 | tr -s " " | cut -d " " -f 1) python3 populateTables.py

Start Both from Gitlab