INVOICES = {1: {"owner": "alice", "total": 120}, 2: {"owner": "bob", "total": 980}}

def get_invoice(current_user: str, invoice_id: int) -> dict:
    # Flaw: no ownership check.
    return INVOICES[invoice_id]
