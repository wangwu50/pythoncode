#!/usr/bin/env bash
aws elb describe-load-balancers |jq -r '.LoadBalancerDescriptions[].LoadBalancerName' |grep huami > huamielbname.txt
for line in `cat huamielbname.txt`
do
    aws elb add-tags --load-balancer-names $line --tags "Key=owner,Value=org-shouhuan"
done
rm huamielbname.txt