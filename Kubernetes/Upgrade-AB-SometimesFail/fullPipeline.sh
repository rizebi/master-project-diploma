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
  date
  echo "Start version 1"
  kubectl apply -f deployment-version1.yml -f service-version1.yml -f ingress-version1.yml
  if [[ "x$1" == "xfull" ]]; then
    sleep 300
  fi
fi

if [[ "x$1" == "xfull" || "x$1" == "xv2" ]]; then
  date
  echo "Start version 2"
  kubectl apply -f deployment-version2.yml -f service-version2.yml
  sleep 70 # to start new version
  nohup kubectl apply -f ingress-version2.yml &
  if [[ "x$1" == "xfull" ]]; then
    sleep 230
  fi
fi

if [[ "x$1" == "xfull" || "x$1" == "xrollback" ]]; then
  date
  echo "Rollback to only version 1"
  nohup kubectl apply -f ingress-version1.yml &
  nohup kubectl delete -f deployment-version2.yml -f service-version2.yml &  if [[ "x$1" == "xfull" ]]; then
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
