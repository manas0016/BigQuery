from google.cloud import bigquery

def load_to_bigquery(file_path, table_id):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV, autodetect=True)

    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)
        job.result()
        print(f"Loaded {file_path} into {table_id}")
