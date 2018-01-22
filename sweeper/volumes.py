import boto3
from .common import display_results


def sweep_volumes(ec2):
    orphan_results = find_orphan_volumes()
    displaced_results = find_geographically_displaced_volumes()
    display_results('volumes', orphan_results + displaced_results)


def get_volumes():
    return []


def find_orphan_volumes():
    return []


def find_geographically_displaced_volumes():
    return []
