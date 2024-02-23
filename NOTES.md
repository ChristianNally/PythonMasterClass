# Prep

Python: [Python in 100 Seconds](https://www.youtube.com/watch?v=x7X9w_GIm1s)

Side by Side Comparison between TensorFlow and PyTorch:
[I built the same model with TensorFlow and PyTorch | Which Framework is better?](https://www.youtube.com/watch?v=ay1E1f8VqP8)

# Python Issues

Question: What is the real difference between async await and 'normal' function definitions in a FastAPI app?

[Answer](https://stackoverflow.com/questions/71516140/fastapi-runs-api-calls-in-serial-instead-of-parallel-fashion/71517830#71517830)



# Deployments (RAM, Disk Space and CPU all cost $ MONEY)

There is a wide variety of possibilities when it comes to deployments, from
- a preconfigured Jupyter Notebook on a fixed/provided/ugly URL

through to 

- your own custom UI on a custom domain name with outputs in the format most natural to your end-users

[Introduction to FastAPI](https://www.youtube.com/watch?v=SORiTsvnU28)

## platform.sh pricing
- Free 30-day trial.
- No credit card required to start.
- Development environments only = $12.00/Month
- Essential 0.65 vCPU & 0.65 GB RAM = $27.00/Month

## porter
- https://docs.porter.run/introduction
- deploys to AWS, Azure, or Google Cloud
- "If you’d like to learn more, contact us for a demo and pricing."

## coherence
- [100 builds per month for free*](https://docs.withcoherence.com/docs/overview/pricing#platform-fee)
- You'll need an EC2 or GCP "free" account (which has limits you might blow over!)

## EC2 Instances

## SageMaker Studio

... is a local program that manages your SageMaker instances. It sits in front of EC2.

It gives end-users access to a Notebook.

Administrator creates a studio and then shares the domain with developers. Developers won't need to interact with anything other than the notebooks, usually.

In the studio environment, you'll often see 'root'. e.g. in /root/ you can clone git repos and they'll show up in Studio.

