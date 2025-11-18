import hvac
import os

client = hvac.Client(
    url=os.getenv("VAULT_ADDR", "http://127.0.0.1:8200"),
    token=os.getenv("VAULT_TOKEN")
)

secret = client.secrets.kv.read_secret_version(path="myapp")
print("Vault secret:", secret["data"]["data"]["API_KEY"])
