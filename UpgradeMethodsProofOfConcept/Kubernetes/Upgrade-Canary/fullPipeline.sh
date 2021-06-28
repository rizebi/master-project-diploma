# /bin/bash

if [[ "x$1" == "xfull" || "x$1" == "xdelete" || "x$1" == "xv1" ]]; then
  date
  echo "Clean All"
  kubectl delete all --all
  kubectl delete ingress --all
  kubectl delete IngressRoute --all
  echo "Done cleaning"
  if [[ "x$1" == "xfull" ]]; then
    sleep 60
  fi
fi

if [[ "x$1" == "xfull" || "x$1" == "xv1" ]]; then
  echo "Start DB"
  kubectl apply -f deployment-db.yml -f service-db.yml
  sleep 60
  date
  echo "Start version 1"
  kubectl apply -f deployment-version1.yml -f service-version1.yml -f ingress-version1.yml
  sleep 10
  kubectl -n dizertatie-minikube-24349559-canary exec $(kubectl -n dizertatie-minikube-24349559-canary get pods | grep production | grep -v "production-db" | head -1 | tr -s " " | cut -d " " -f 1) python3 populateTables.py

  if [[ "x$1" == "xfull" ]]; then
    sleep 290
  fi
fi

if [[ "x$1" == "xfull" || "x$1" == "xv2" ]]; then
  date
  echo "Start canary"
  kubectl apply -f deployment-version2.yml -f service-version2.yml -f ingress-version2.yml
  if [[ "x$1" == "xfull" ]]; then
    sleep 300
  fi
fi

if [[ "x$1" == "xfull" || "x$1" == "xrollback" ]]; then
  date
  echo "Rollback to only version 1"
  kubectl delete -f deployment-version2.yml -f service-version2.yml -f ingress-version2.yml
  if [[ "x$1" == "xfull" ]]; then
    sleep 300
  fi
fi

if [[ "x$1" == "xfull"]]; then
  date
  echo "Delete all"
  kubectl delete all --all
  kubectl delete ingress --all
  kubectl delete IngressRoute --all
fi