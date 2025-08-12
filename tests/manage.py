import sys
import os
from pathlib import Path

from clio_api_model_generator import clio_manage
client_dir = Path(__file__).resolve().parent
clio_manage.generate_models(output_dir = client_dir, overwrite=False)