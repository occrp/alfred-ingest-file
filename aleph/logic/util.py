from werkzeug.urls import url_join
from urlnormalizer import query_string

from aleph.core import settings, url_for


def ui_url(resource, id=None, _relative=False, **query):
    """Make a UI link."""
    if id is not None:
        resource = "%s/%s" % (resource, id)
    url = "/" if _relative else settings.APP_UI_URL
    url = url_join(url, resource)
    return url + query_string(list(query.items()))


def collection_url(collection_id=None, **query):
    return ui_url("datasets", id=collection_id, **query)


def entityset_url(entityset_id=None, **query):
    return ui_url("sets", id=entityset_id, **query)


def entity_url(entity_id=None, **query):
    return ui_url("entities", id=entity_id, **query)


def archive_url(authz, content_hash, file_name=None, mime_type=None, expire=None):
    """Create an access authorization link for an archive blob."""
    if content_hash is None:
        return None
    return url_for(
        "archive_api.retrieve",
        content_hash=content_hash,
        _authz=authz,
        _expire=expire,
        _query=[("file_name", file_name), ("mime_type", mime_type)],
    )
