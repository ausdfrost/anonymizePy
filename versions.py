import os
import glob
import random
import numpy as np
import pandas as pd
import regex as re
import spacy
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import logging

print(f"os: {os.__version__ if hasattr(os, '__version__') else 'built-in module, no version'}")
print(f"glob: {glob.__version__ if hasattr(glob, '__version__') else 'built-in module, no version'}")
print(f"random: {random.__version__ if hasattr(random, '__version__') else 'built-in module, no version'}")
print(f"numpy: {np.__version__}")
print(f"pandas: {pd.__version__}")
print(f"regex: {re.__version__}")
print(f"spacy: {spacy.__version__}")
print(f"scikit-learn: {accuracy_score.__module__.split('.')[0]}: {accuracy_score.__module__.split('.')[1]}")
print(f"logging: {logging.__version__ if hasattr(logging, '__version__') else 'built-in module, no version'}")