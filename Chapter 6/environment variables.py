import os
home_dir=os.getenv("TEMP")
print("Home Directory:",home_dir)

# set environment variables
os.environ['MY_VAR'] ="my_value"

# retrive the environment variables
value=os.environ['MY_VAR']
print("Value:",value)
# get all environment variables
env_vars=os.environ
print("Env Variables:",env_vars)
