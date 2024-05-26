import os
import shutil
import boto3

def list_files_with_prefix(directory, prefix):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter files that start with the specified prefix
    matching_files = [file for file in files if file.startswith(prefix)]
    
    print("Matching files:")
    for file in matching_files:
        print(file)

def move_files_with_prefix(directory, prefix, destination_folder, sns_topic_arn=None):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter files that start with the specified prefix
    matching_files = [file for file in files if file.startswith(prefix)]
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder '{destination_folder}'")

    # Move each matching file to the destination folder and delete from source folder
    for file in matching_files:
        source_path = os.path.join(directory, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(f"Moved file '{source_path}' to '{destination_path}'")
        

        # Delete the file from the source folder
        os.remove(source_path)
        print(f"Deleted file '{source_path}'")
        
if sns_topic_arn and matching_files:
        sns_client = boto3.client('sns')
        message = "Files have been moved to another folder and deleted from the recent folder."
        sns_client.publish(TopicArn=sns_topic_arn, Message=message)
        print("Notification sent via SNS.")



if __name__ == "__main__":
    directory = '/home/ec2-user/'
    prefix = 'sr1_'
    destination_folder = '/home/ec2-user/sr1/'
    sns_topic_arn = 'fils with prefix sr1_'  
    
    list_files_with_prefix(directory, prefix)
    move_files_with_prefix(directory, prefix, destination_folder, sns_topic_arn)
