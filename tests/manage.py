# tests/run_generate.py
import sys
import os
from pathlib import Path

# Step 2: Import the generate module (which will auto-run if it has top-level code)
from clio_api_model_generator import clio_manage
client_dir = Path(__file__).resolve().parent
clio_manage.generate_models(output_dir = client_dir, overwrite=False)