#!/usr/bin/env python3
from kscore.session import get_session
import sys


def add_health_check(slbClient, listener_id):
    slbClient.configure_health_check(
        **{'ListenerId': listener_id, 'HealthCheckState': 'start', 'HealthyThreshold': 5,
           'Interval': 5, 'Timeout': 4, 'UnhealthyThreshold': 4})


def register_k8s_instances(slbClient, listener_id, ip, port):
    slbClient.register_instances_with_listener(
        **{'ListenerId': listener_id, 'RealServerIp': ip, 'RealServerPort': port,
           'RealServerType': 'host', 'Weight': 20})


def create_listener(slbClient, lb_id, port):
    listenerResult = slbClient.create_listeners(
        **{'LoadBalancerId': lb_id, 'ListenerState': 'start', 'ListenerName': 'tcp_' + port,
           'ListenerProtocol': 'TCP', 'ListenerPort': port, 'Method': 'RoundRobin', 'SessionState': 'stop'})
    add_health_check(slbClient, listenerResult['ListenerId'])
    if port == '80':
        band_port = 80
    elif port == '443':
        band_port = 442
    else:
        band_port = int(port)
    register_k8s_instances(slbClient, listenerResult['ListenerId'], '10.1.10.15', band_port)
    register_k8s_instances(slbClient, listenerResult['ListenerId'], '10.1.9.36', band_port)
    register_k8s_instances(slbClient, listenerResult['ListenerId'], '10.1.9.19', band_port)


def create_and_build_eip(eipClient, lb_id):
    eipResult = eipClient.allocate_address(
        **{'LineId': '5fc2595f-1bfd-481b-bf64-2d08f116d800', 'BandWidth': 1, 'ChargeType': 'Daily'})
    public_ip = eipResult['PublicIp']
    print('the ip is:' + public_ip)
    eipClient.associate_address(
        **{'AllocationId': eipResult['AllocationId'], 'InstanceType': 'Slb', 'InstanceId': lb_id})


def create_lb(slbClient, name):
    lbResult = slbClient.create_load_balancer(
        **{'VpcId': '76403753-3fa0-4978-9096-4f68e06ea2f0', 'LoadBalancerName': name})
    return lbResult


def start_lb(slbClient, lb_id):
    slbClient.modify_load_balancer(**{'LoadBalancerId': lb_id, 'LoadBalancerState': 'start'})


def create_k8s_elb(name):
    s = get_session()

    region = 'cn-beijing-6'
    slbClient = s.create_client('slb', region)
    eipClient = s.create_client("eip", region)
    lbResult = create_lb(slbClient, name)
    lb_id = lbResult['LoadBalancerId']
    create_listener(slbClient, lb_id, '80')
    create_listener(slbClient, lb_id, '443')
    create_and_build_eip(eipClient, lb_id)
    start_lb(slbClient, lb_id)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('useage: %s orgName' % sys.argv[0])
    else:
        create_k8s_elb("lb-k8s-" + sys.argv[1])
