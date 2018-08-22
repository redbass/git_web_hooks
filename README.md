# Git Web-Hooks

## Configuration
### Setup AWS credentials
If this is your first time configuring credentials for AWS you can follow these steps to quickly get started:

    mkdir ~/.aws
    cat >> ~/.aws/config
    
add this content

    [default]
    aws_access_key_id=YOUR_ACCESS_KEY_HERE
    aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
    region=YOUR_REGION (such as us-west-2, us-west-1, etc)
    
## Deploy
To deply just run

    chalice deploy