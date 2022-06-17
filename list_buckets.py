from google.cloud import storage
if __name__ == '__main__':
    storage_client = storage.client()
    # bucket = storage_client.list_buckets("bwt-session-bucket")
    # bucket.storage_class ="COLDLINE"
    # new_bucket = storage_client.create_bucket(bucket,location="us")
