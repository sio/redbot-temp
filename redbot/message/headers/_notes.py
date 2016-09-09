#!/usr/bin/env python

"""
Common header-related Notes.
"""

from redbot.speak import Note, categories, levels


class SINGLE_HEADER_REPEAT(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u"Only one %(field_name)s header is allowed in a response."
    text = u"""\
This header is designed to only occur once in a message. When it occurs more than once, a receiver
needs to choose the one to use, which can lead to interoperability problems, since different
implementations may make different choices.

For the purposes of its tests, RED uses the last instance of the header that is present; other
implementations may behave differently."""

class FIELD_NAME_BAD_SYNTAX(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u'"%(field_name)s" is not a valid header field-name.'
    text = u"""\
Header names are limited to the TOKEN production in HTTP; i.e., they can't contain parenthesis,
angle brackes (<>), ampersands (@), commas, semicolons, colons, backslashes (\\), forward
slashes (/), quotes, square brackets ([]), question marks, equals signs (=), curly brackets ({})
spaces or tabs."""

class BAD_SYNTAX(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u"The %(field_name)s header's syntax isn't valid."
    text = u"""\
The value for this header doesn't conform to its specified syntax; see [its
definition](%(ref_uri)s) for more information."""

class PARAM_STAR_QUOTED(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u"The '%(param)s' parameter's value cannot be quoted."
    text = u"""\
Parameter values that end in '*' have a specific format, defined in
[RFC5987](http://tools.ietf.org/html/rfc5987), to allow non-ASCII text.

The `%(param)s` parameter on the `%(field_name)s` header has double-quotes around it, which is not
valid."""

class PARAM_STAR_ERROR(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u"The %(param)s parameter's value is invalid."
    text = u"""\
Parameter values that end in '*' have a specific format, defined in
[RFC5987](http://tools.ietf.org/html/rfc5987), to allow non-ASCII text.

 The `%(param)s` parameter on the `%(field_name)s` header is not valid; it needs to have three
parts, separated by single quotes (')."""

class PARAM_STAR_BAD(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u"The %(param)s* parameter isn't allowed on the %(field_name)s header."
    text = u"""\
Parameter values that end in '*' are reserved for non-ascii text, as explained in
[RFC5987](http://tools.ietf.org/html/rfc5987).

The `%(param)s` parameter on the `%(field_name)s` does not allow this; you should use %(param)s
without the "*" on the end (and without the associated encoding).

RED ignores the content of this parameter.
     """

class PARAM_STAR_NOCHARSET(Note):
    category = categories.GENERAL
    level = levels.WARN
    summary = u"The %(param)s parameter's value doesn't define an encoding."
    text = u"""\
Parameter values that end in '*' have a specific format, defined in
[RFC5987](http://tools.ietf.org/html/rfc5987), to allow non-ASCII text.

The `%(param)s` parameter on the `%(field_name)s` header doesn't declare its character encoding,
which means that recipients can't understand it. It should be `UTF-8`."""

class PARAM_STAR_CHARSET(Note):
    category = categories.GENERAL
    level = levels.WARN
    summary = u"The %(param)s parameter's value uses an encoding other than UTF-8."
    text = u"""\
Parameter values that end in '*' have a specific format, defined in
[RFC5987](http://tools.ietf.org/html/rfc5987), to allow non-ASCII text.

The `%(param)s` parameter on the `%(field_name)s` header uses the `'%(enc)s` encoding, which has
interoperability issues on some browsers. It should be `UTF-8`."""

class PARAM_REPEATS(Note):
    category = categories.GENERAL
    level = levels.WARN
    summary = u"The '%(param)s' parameter repeats in the %(field_name)s header."
    text = u"""\
Parameters on the %(field_name)s header should not repeat; implementations may handle them
differently."""

class PARAM_SINGLE_QUOTED(Note):
    category = categories.GENERAL
    level = levels.WARN
    summary = u"The '%(param)s' parameter on the %(field_name)s header is single-quoted."
    text = u"""\
The `%(param)s`'s value on the %(field_name)s header start and ends with a single quote (').
However, single quotes don't mean anything there.

This means that the value will be interpreted as `%(param_val)s`, **not**
`%(param_val_unquoted)s`. If you intend the latter, drop the single quotes."""

class BAD_DATE_SYNTAX(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u"The %(field_name)s header's value isn't a valid date."
    text = u"""\
HTTP dates have very specific syntax, and sending an invalid date can cause a number of problems,
especially around caching. Common problems include sending "1 May" instead of "01 May" (the month
is a fixed-width field), and sending a date in a timezone other than GMT. See [the HTTP
specification](http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.3) for more
information."""

class HEADER_TOO_LARGE(Note):
    category = categories.GENERAL
    level = levels.WARN
    summary = u"The %(header_name)s header is very large (%(header_size)s)."
    text = u"""\
Some implementations limit the size of any single header line."""

class HEADER_NAME_ENCODING(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u"The %(header_name)s header's name contains non-ASCII characters."
    text = u"""\
HTTP header field-names can only contain ASCII characters. RED has detected (and possibly removed)
non-ASCII characters in this header name."""

class HEADER_VALUE_ENCODING(Note):
    category = categories.GENERAL
    level = levels.WARN
    summary = u"The %(header_name)s header's value contains non-ASCII characters."
    text = u"""\
HTTP headers use the ISO-8859-1 character set, but in most cases are pure ASCII (a subset of this
encoding).

This header has non-ASCII characters, which RED has interpreted as being encoded in
ISO-8859-1. If another encoding is used (e.g., UTF-8), the results may be unpredictable."""

class REQUEST_HDR_IN_RESPONSE(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u'"%(field_name)s" is a request header.'
    text = u"""\
%(field_name)s isn't defined to have any meaning in responses, so RED has ignored it."""

class RESPONSE_HDR_IN_REQUEST(Note):
    category = categories.GENERAL
    level = levels.BAD
    summary = u'"%(field_name)s" is a request header.'
    text = u"""\
%(field_name)s isn't defined to have any meaning in reqeusts, so RED has ignored it."""

class HEADER_DEPRECATED(Note):
    category = categories.GENERAL
    level = levels.WARN
    summary = u"The %(header_name)s header is deprecated."
    text = u"""\
This header field is no longer recommended for use, because of interoperability problems and/or
lack of use. See [the deprecation notice](%(deprecation_ref)s) for more information."""
