import os
from dotenv import load_dotenv

load_dotenv()

"""
NOT IMPLEMENTED
background task template
"""

REDIS_URL = os.getenv()
QUEUES= ["emails","default"]

# emails is name of task
