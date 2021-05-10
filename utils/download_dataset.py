import logging
import os
import shutil
import urllib3
from configurations.config import Config


def download_dataset(LOCAL_FILE_NAME, url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    c = urllib3.PoolManager()
    with c.request("GET", url, preload_content=False) as res, open(
        LOCAL_FILE_NAME, "wb"
    ) as out_file:
        shutil.copyfileobj(res, out_file)
    logging.info("Download completed.")


def get_folder():
    path = os.getcwd()
    while True:
        path, ref = os.path.split(path)
        if ref == Config.PROJECT_NAME:
            path = os.path.join(path, ref)
            break
        if path == '':
            raise Exception('Check Wheather project name set correctly')
    return path


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    logging.info("Started download script")

    path = get_folder()
    LOCAL_FILE_NAME = os.path.join(path, "data", 'dataset1', "consumer_complaints_with_narrative.csv")
    download_dataset(LOCAL_FILE_NAME, Config.DATASET_URL)

    logging.info("Finished download script")
