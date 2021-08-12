
# Discord Importer

# Functions

## import_channel (channel_id, import_id, key)

### Purpose

Get channel info and data in preparation for downloading

### Parameters

channel_id, str : ID of the Discord channel

import_id, str : import id

key, str : discord session token


### Return Values
None


## process_channel (channel_id, server_id, import_id, key, before)

### Purpose

Scrape Discord channel content

### Parameters

channel_id, str : ID of the Discord channel

server_id, str : ID of the Discord server

import_id, str : import id

key, str : discord session token

before, str : look for posts before the ID specified here, default = None


### Return Values
If API or CloudScraper error occur, aka critical error:
        False
If scraping is successful:
        True


## import_posts (import_id, channel_id_str, key)

### Purpose

Uses import_channel to begin the scraping process

### Parameters

import_id, str : import id

channel_id_str, str : comma separated list of discord channel IDs

key, str : discord session token

### Return Values
None
