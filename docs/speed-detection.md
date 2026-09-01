# Speed transformation detection

Speed detection compares the recognized recording against the local audio instead of trusting filenames. A ratio below 1 indicates a slowed candidate; a ratio above 1 indicates a sped-up candidate. A configurable tolerance prevents tiny timing differences from being labeled as transformations.
