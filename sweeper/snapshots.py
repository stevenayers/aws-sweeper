import boto3
from .common import display_results


def sweep_snapshots(ec2):
    orphan_results = find_orphan_snapshots()
    displaced_results = find_geographically_displaced_snapshots()
    display_results('snapshots', orphan_results + displaced_results)



def get_snapshots():
    return []


def find_orphan_snapshots():
    return []


def find_geographically_displaced_snapshots():
    return []








