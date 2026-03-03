def is_valid_url(url):
    # check for space
    if " " in url:
        return False
# check for ://
    if "://" not in url:
        return False

    parts = url.split("://")

    if len(parts) != 2:
        return False

    scheme = parts[0]
    rest = parts[1]
# check for http or https
    if scheme != "http" and scheme != "https":
        return False

    # get host (before first / if exists)
    host = rest.split("/")[0]
# check for .
    if "." not in host:
        return False

    return True