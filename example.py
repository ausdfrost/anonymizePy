# # anonymizePy Data Anonymization Example

# import data anonymization methods
from anonymizePy import PIIGenerator, DataAnonymizer, ModelEvaluator

# Specify data paths
labeled_datapath = "call_data.csv"  # labeled input
unanonymized_datapath = "call_data_With_Identifiers.csv"  # original input with faux PII
anonymized_datapath = "call_data_Anonymized.csv"  # anonymized output

# 1. Insert randomly generated PII into data
pii_generator = PIIGenerator()
pii_generator.insert_pii(labeled_datapath, unanonymized_datapath)

# 2. Deploy the case anonymizer
data_anonymizer = DataAnonymizer()
data_anonymizer.anonymizer(unanonymized_datapath, anonymized_datapath, use_ner=True, use_regex=True, use_resources=False, ignore_columns=["Assessment", "Homeless", "Gender", "Call Sign"])

# 3. Evaluate the model performance
evaluator = ModelEvaluator()
evaluator.evaluate_model(labeled_datapath, unanonymized_datapath, anonymized_datapath)