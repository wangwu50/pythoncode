#!/usr/bin/env bash

sed -i 's|cluster-domain=cluster.local|cluster-domain=cluster.local --pod-infra-container-image=gcr.io/google_containers/pause-amd64:3.1|g' /etc/kubernetes/kubelet
#sed '12d' /etc/systemd/system/kubelet.service
systemctl daemon-reload
systemctl restart kubelet