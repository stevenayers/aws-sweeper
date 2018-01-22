import boto3
from .common import display_results


def sweep_instances(ec2):
    orphan_results = find_orphan_instances()
    displaced_results = find_geographically_displaced_instances()
    display_results('instances', orphan_results + displaced_results)


def get_instances():
    return []


def find_orphan_instances():
    return []


def find_geographically_displaced_instances(good_regions, bad_regions):
    return []
