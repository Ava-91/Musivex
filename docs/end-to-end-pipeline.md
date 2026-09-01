# End-to-end recognition pipeline

The safe path is:

1. recognize the recording;
2. normalize provider data;
3. compare local audio with the reference when available;
4. classify transformations;
5. enrich metadata/artwork;
6. apply the confidence/review decision;
7. write only approved metadata.

The mock provider makes this pipeline deterministic in CI. A real provider is optional and configured outside source control.
