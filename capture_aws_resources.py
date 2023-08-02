import csv
import boto3

# List of AWS regions you want to capture resources from
regions = ["us-east-1", "us-west-2", "eu-west-1", "ap-south-1"]

# CSV file to store the results
output_file = "aws_resources.csv"

# Initialize the AWS clients
ec2_client = boto3.client("ec2")
s3_client = boto3.client("s3")
# efs_client = boto3.client("efs")
# rds_client = boto3.client("rds")

# Open the CSV file and write the header row
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Region", "ResourceType", "ResourceId"])

    for region in regions:
        # Capture EC2 instances
        ec2_response = ec2_client.describe_instances()
        for reservation in ec2_response["Reservations"]:
            for instance in reservation["Instances"]:
                writer.writerow([region, "EC2", instance["InstanceId"]])

        # Capture S3 buckets
        s3_response = s3_client.list_buckets()
        for bucket in s3_response["Buckets"]:
            writer.writerow([region, "S3", bucket["Name"]])

        # # Capture EFS filesystems
        # efs_response = efs_client.describe_file_systems()
        # for filesystem in efs_response["FileSystems"]:
        #     writer.writerow([region, "EFS", filesystem["FileSystemId"]])

        # # Capture RDS instances
        # rds_response = rds_client.describe_db_instances()
        # for db_instance in rds_response["DBInstances"]:
        #     writer.writerow([region, "RDS", db_instance["DBInstanceIdentifier"]])
