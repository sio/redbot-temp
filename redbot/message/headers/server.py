from redbot.message import headers
from redbot.syntax import rfc7231


class server(headers.HttpHeader):
    canonical_name = "Server"
    description = """\
The `Server` header contains information about the software used by the origin server to handle the
request."""
    reference = f"{rfc7231.SPEC_URL}#header.server"
    syntax = rfc7231.Server
    list_header = True
    deprecated = False
    valid_in_requests = False
    valid_in_responses = True
