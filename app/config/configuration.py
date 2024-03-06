import os
from dotenv import load_dotenv

load_dotenv()

STEPS = os.getenv("STEPS")
WINIUM_DRIVER = os.getenv("WINIUM_DRIVER")