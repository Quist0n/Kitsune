
# Gumroad Importer

The importer that is used when scraping from gumroad.com

# Functions

## import_posts (import_id, key, offset)

### Purpose

This function does precisely what one would think it does. It grabs the metadata required to then download the content of a specific gumroad creator.

### Parameters

import_id, str : An Identifier for gumroad post being imported

key, str : The gumroad user access token used for authentication

offset, int : The offset of the data that should be collected, used in the url when downloading information. default value is 1

### Return Values

None
