INVOICES = {1: {"owner": "alice", "total": 120}, 2: {"owner": "bob", "total": 980}}

class NotFound(Exception):
    pass

def get_invoice(current_user: str, invoice_id: int) -> dict:
    # Fix: ownership enforced; no hint whether the ID exists.
    inv = INVOICES.get(invoice_id)
    if inv is None or inv["owner"] != current_user:
        raise NotFound()
    return inv
