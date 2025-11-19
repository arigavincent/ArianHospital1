from .models import ContactInfo


def site_contact(request):
    """Context processor that provides the top ContactInfo record as `site_contact`.

    Returns an empty dict if no ContactInfo instances exist.
    """
    try:
        contact = ContactInfo.objects.order_by('order').first()
    except Exception:
        # If the DB isn't ready or migrations haven't run yet, return nothing.
        return {}

    if not contact:
        return {}

    return {'site_contact': contact}
