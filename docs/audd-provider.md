# AudD recognition provider

Musivex can use AudD for online song recognition. AudD's standard endpoint accepts a local file upload and returns structured artist/title/album information. The current standard endpoint has a 10 MB file limit and is intended for short recognition clips. urlAudD API documentationhttps://docs.audd.io/

Set `AUDD_API_TOKEN` in the environment. Never commit the token.

Recognition is optional: CI and the mock provider do not require network access or credentials.
