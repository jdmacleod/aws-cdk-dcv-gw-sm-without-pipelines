# AWS CDK Nice DCV Connection Gateway and Session Manager - Linux

Part of deploying examples of Amazon / Nice DCV running on EC2 instances.

<https://aws.amazon.com/blogs/desktop-and-application-streaming/automating-foundational-nice-dcv-infrastructure/>

## Setup

Create the project directory.

```bash
mkdir aws-cdk-dcv-gw-sm-without-pipelines
cd aws-cdk-dcv-gw-sm-without-pipelines
```

Initialize the CDK project.

```bash
cdk init app --language=python
```

Activate the Python virtual environment and install the Python dependencies.

```bash
source ./venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

Set the Node.js version to the LTS version.

```bash
nvm use --lts
```

Check the role being used by the AWS CLI.

```bash
aws sts get-caller-identity
```

Bootstrap the AWS CDK environment for the region, if has not already been done once. This step needs to run with Administrator privileges.

```bash
cdk --profile admin bootstrap
```

## DCV Gateway + Session Manager without Pipelines

This AWS CDK sample provisions the foundational infrastructure for a DCV Connection Gateway with DCV Session Manager environment. Both DCV Session Manager and DCV Connection Gateway are configured with bootstrap scripts so that can you utilize base AMIs. This deployment is intended to be deployed with Amazon Linux 2, but you can also deploy using other supported operating systems

See the AWS example on GitHub - <https://github.com/aws-samples/dcv-samples/tree/main/cdk/dcv-gw-sm-without-pipelines>

### Identify AMI ID's to use

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html>

We'll use the latest ARM-based Amazon Linux 2 AMI in the region (us-west-2).

Harder than it sounds, with many, many choices.

One way to do this:

<https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/>

```bash
aws ssm get-parameters-by-path --path "/aws/service/ami-amazon-linux-latest" --region us-west-2
```

From the list for the region, entries look like this:

```bash
PARAMETERS	arn:aws:ssm:us-west-2::parameter/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-arm64	text	2025-03-26T15:57:46.434000-07:00	/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-arm64	String	ami-03be73a6c76012d9f	114
```

This can also be done in the AWS Console.

```bash
aws ec2 describe-images --owners amazon --filters "Name=name,Values=amzn*" --query 'sort_by(Images, &CreationDate)[].Name'
```

From the Console->EC2->AMI Catalog, region us-west-2 (Oregon), this choice for the Amazon Linux 2 AMI, 64-bit Arm looks good.

`ami-0e0ae53798f2e021e`

### Set up Key Pairs for SSH Access to EC2

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html>

You can list available key pairs with this AWS CLI command:

```bash
aws ec2 describe-key-pairs --query 'KeyPairs[*].KeyName' --output table
```

Create a new key pair with the below command:

```bash
aws ec2 create-key-pair --key-name dcv-key-pair --output text > dcv-key-pair.pem
```

Confirm the key pair exists in the AWS Console->EC2-Key Pairs.

Verify there are no errors with the project using `cdk synth`.

### Check project with Synth

```bash
cdk synth --all
```

### Deploy Infrastructure stack

Deploy the project to AWS.

```bash
cdk deploy
```

## Reference

See the [boilerplate CDK Read Me](./REFERENCE.md) for reference.
