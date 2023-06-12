An example of how to configure dagster graphs at runtime using a python script to create a yaml file

# Create a virtual environment and install requirements with

- 'python3 -m venv venv'
- 'pip3 install -r requirements.txt'

# run a job

using ui:

- 'dagster dev -f hello.py'

locally:

- 'python3 hello.py'
