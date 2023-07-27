from celery import shared_task
import requests


# @shared_task(bind=True)
# def test_func(self):
#     url = "http://127.0.0.1:8000/final/"
#     requests.get(url)
#     return "Done"
