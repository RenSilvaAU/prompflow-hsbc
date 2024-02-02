from promptflow import tool
import requests
import json
import time
from promptflow.connections import CustomConnection

# url = "https://gocai-uat.apse1.dgt.np-api.fwd.com/cm-uat-gec/chat/message"

@tool
def call_service(question: str):

    url = "https://hsbc-ai-qayex.australiaeast.inference.ml.azure.com/score";
    token = "0xiTMtvt3kg4kcdZtUmZkT9df9FjSIe2"

    headers = {
      'Authorization': f'Bearer {token}',
      'Content-Type': 'application/json'
    }

    payload = json.dumps({
        "topic":   question
    })

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text
