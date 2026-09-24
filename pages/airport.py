# Master Hub Page — Airport
# Author: Mohamed · M3
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# page config managed by Master Hub
import os
exec(open(os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "airport_dashboard.py")).read())
