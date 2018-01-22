import argparse
import sweeper
import boto3


def argument_handler():
    description = "Searches AWS account for possibly unwanted and unused EC2 instances, volumes & snapshots."
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-a', '--all', action='store_true', help='Sweeps insances, snapshots, and volumes')
    parser.add_argument('-i', '--instances', action='store_true', help='Sweeps volumes')
    parser.add_argument('-s', '--snapshots',  action='store_true', help='Sweeps snapshots')
    parser.add_argument('-v', '--volumes',  action='store_true', help='Sweeps volumes')
    return parser.parse_args()


def initialise_client():
    """Set up EC2 resource"""
    resource = boto3.resource('ec2')
    return resource


def main():
    ec2 = initialise_client()
    args = argument_handler()

    if args.all is True:
        sweeper.sweep_instances(ec2)
        sweeper.sweep_snapshots(ec2)
        sweeper.sweep_volumes(ec2)
    else:
        if args.instances is True:
            sweeper.sweep_instances(ec2)
        if args.snapshots is True:
            sweeper.sweep_snapshots(ec2)
        if args.volumes is True:
            sweeper.sweep_volumes(ec2)


if __name__ == '__main__':
    main()


