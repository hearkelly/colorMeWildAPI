import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv()
QUEUES= ["emails","default"]

# emails is name of task