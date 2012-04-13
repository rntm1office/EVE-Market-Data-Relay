from emdr.core.serialization.eve_marketeer import history, orders

def parse_from_payload(payload):
    """
    Given an EVE Marketeer message, parse the contents and return a
    MarketOrderList or MarketHistory instance.

    :param dict payload: An EVE Marketeer payload dict from the gateway.
    :rtype: MarketOrderList or MarketHistory
    """
    if payload['upload_type'] == 'orders':
        return orders.parse_from_payload(payload)
    else:
        return history.parse_from_payload(payload)