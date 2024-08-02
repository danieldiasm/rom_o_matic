# Data Downloader File
# This module is responsible for downloading files from a pointed URL.
import threading
import queue
import requests
import sys
import time

class Downloader():

    def __init__(self) -> None:
        self.download_list = []
        self.status_queue = queue.Queue()

    def download_file(url, file_path, max_retries=5, backoff_factor=0.5):
        retry_count = 0

        while retry_count < max_retries:
            try:
                with open(file_path, mode="wb") as file:
                    resp = requests.get(url, stream=True)
                    resp.raise_for_status()  # Raise an error for bad status codes
                    if resp.status_code == 200:

                        total_size = int(resp.headers.get('content-length', 0))
                        chunk_size = 1024
                        downloaded_size = 0

                        for chunk in resp.iter_content(chunk_size=chunk_size):
                            file.write(chunk)
                            downloaded_size += len(chunk)
                            progress = int(50 * downloaded_size / total_size)
                            sys.stdout.write(f'\r[{"█" * progress}{"." * (50 - progress)} {downloaded_size} of {total_size}]')
                            sys.stdout.flush()
                        print("\nDownload complete!")
                    else:
                        print("Status code is not 200! Download Failed...")
                    return  # Exit the function if the download is successful

            except requests.RequestException as e:
                retry_count += 1
                wait_time = backoff_factor * (2 ** (retry_count - 1))
                print(f"\nDownload failed: {e}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            except ZeroDivisionError as e:
                print("FAILED - Code is 200, but file size is zero, link should be expired.")
                sys.exit(1)

        print("\nDownload failed after multiple attempts.")
