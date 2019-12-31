
def get_host_from_address(address):
    if not address:
        return None

    if address.lower().startswith("https://"):
        address = address[8:]
    if address.lower().startswith("http://"):
        address = address[7:]

    address = address.lstrip("/")
    if "/" in address:
        address = address.split("/")[0] or address
    if ":" in address:
        address = address.split(":")[0] or address

    return address
