from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

table_id = "backendstarterproject-361103.dataset1.table1"

def insert_input_to_bq(x: str):
    rows_to_insert = [
        {"input": x}
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
