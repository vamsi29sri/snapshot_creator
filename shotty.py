import boto3
if __name=='__main__':
    session =boto3.Session(profile_name ='snapshoter')
    ec2=session.resource('ec2')
    for i in ec2.instances.all():
        print (i)
