"""Small MusicBrainz-compatible provider implementation."""

import json
from urllib.parse import quote
from urllib.request import Request, urlopen

from .metadata_model import Metadata
from .provider_errors import ProviderUnavailable


class MusicBrainzProvider:
    def __init__(self, base_url: str = "https://musicbrainz.org/ws/2") -> None:
        self.base_url = base_url.rstrip("/")

    def search(self, *, title: str, artist: str | None = None) -> list[Metadata]:
        query = f'track:"{title}"'
        if artist:
            query += f' AND artist:"{artist}"'
        url = f"{self.base_url}/recording/?query={quote(query)}&fmt=json&limit=10"
        request = Request(url, headers={"User-Agent": "Musivex/0.1 (open-source project)"})
        try:
            with urlopen(request, timeout=10) as response:
                payload = json.load(response)
        except Exception as exc:
            raise ProviderUnavailable(str(exc)) from exc
        return [
            Metadata(title=item.get("title"), recording_id=item.get("id"))
            for item in payload.get("recordings", [])
        ]
