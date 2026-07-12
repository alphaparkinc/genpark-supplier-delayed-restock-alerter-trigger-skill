from client import SupplierDelayedRestockAlerterTriggerClient
client = SupplierDelayedRestockAlerterTriggerClient()
print(client.check_delay(10))