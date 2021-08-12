# Subscribestar Importer

The importer that is used when scraping from subscribstar.com

# Functions

## strip_tags (html)

### Purpose

This function strips the html tags from html text that is passed into it
### Parameters

html, str : the text that is to be stripped of its html tags

### Return Values

str : text that has been stripped of all html tags

## import_posts (import_id, key)

### Purpose

This function grabs the metadata required and then downloads the content of a specific subscribstar creator.

### Parameters

import_id, str : An Identifier for the subscribstar post being imported

key, str : The subscribstar user access token used for authentication

### Return Values

None
