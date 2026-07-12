class SupplierDelayedRestockAlerterTriggerClient:
    def check_delay(self, transit_days: int) -> dict:
        return {"is_delayed": transit_days > 7}