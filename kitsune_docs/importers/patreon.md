# Patreon Importer

The importer that is used when scraping from patreon.com

# Functions

## get_ws_connection (url)

### Purpose
Get ids of campaigns with active pledge

### Parameters

url, str : url to make a WebSockets connection to

### Return Values


## get_active_campaign_ids (key, import_id)

### Purpose
Get ids of campaigns with active pledge

### Parameters

key, str: The patreon user access token used for authentication

import_id, str: An Identifier for the patreon post being imported


### Return Values

If there are HTTP errors when contacting patreon servers :
        set : an empty set

If there are cloudscraper issues :
        set : an empty set

If campaign ids can be scraped correctly :
        set : a set containing the ids of active campaigns


## get_cancelled_campaign_ids (key, import_id)

### Purpose
Get ids of campaigns with active pledge

### Parameters

key, str: The patreon user access token used for authentication

import_id, str: An Identifier for the patreon post being imported


### Return Values

If there are HTTP errors when contacting patreon servers :
        set : an empty set

If there are cloudscraper issues :
        set : an empty set

If campaign ids can be scraped correctly :
        set : a set containing the ids of calcelled campaigns


## get_campaign_ids (key, import_id)

### Purpose
Get ids of all campaigns

### Parameters

key, str: The patreon user access token used for authentication

import_id, str: An Identifier for the patreon post being imported


### Return Values
list : a list containing the ids of of campaigns, can be empty


## get_sendbird_token (key, import_id)

### Purpose
Get sendbird token

### Parameters

key, str: The patreon user access token used for authentication

import_id, str: An Identifier for the patreon post being imported


### Return Values
str : a list containing the ids of of campaigns, can be empty

If there are issues with the API or cloudscraper:
        None


## get_dm_campaigns (key, current_user_id, import_id)

### Purpose
Get a set containing all dm campaigns

### Parameters

key, str : The patreon user access token used for authentication

current_user_id, str : id of the patreon user currently being processed

import_id, str : An Identifier for the patreon post being imported


### Return Values
set : a set containing the ids of dm campaigns, can be empty

If there are issues with the API or cloudscraper:
        None


## get_current_user_id (key, import_id)

### Purpose
Get the current user id

### Parameters

key, str: The patreon user access token used for authentication

import_id, str: An Identifier for the patreon post being imported


### Return Values
str : the current user id

If there are issues with the API or cloudscraper:
        None

## import_channel (auth_token, url, import_id, current_user, contributor_id, timestamp)

### Purpose
Import the contents of Patreon channels

### Parameters

auth_token : token required for access to Patreon DMs

url : channel url

import_id, str : An Identifier for the patreon post being imported

current_user, str: Patreon User ID the current user

contributor_id, str : Patreon ID of the contributor

timestamp, str : ???

### Return Values
None


## import_channels (auth_token, current_user, campaigns, import_id, contributor_id, token)

### Purpose
Import the channels of Patreon DMs

### Parameters

auth_token : token required for access to Patreon DMs

current_user, str: Patreon User ID the current user

campaigns, set: set of campaigns that have been subscribed to

import_id, str : An Identifier for the patreon post being imported

contributor_id, str : Patreon ID of the contributor

token, str : ???

### Return Values
None


## import_dms (key, import_id, contributor_id)

### Purpose
Trigger import of all DMs from subscriptions

### Parameters

key, str: The patreon user access token used for authentication

import_id, str : An Identifier for the patreon post being imported

contributor_id, str : Patreon ID of the contributor

### Return Values
None


## import_comment (comment, user_id, import_id)

### Purpose
Import comments

### Parameters

comment, dict : comment data

user_id, str :

import_id, str : An Identifier for the patreon post being imported

### Return Values
None

## import_comments (url, post_id, user_id, import_id)

### Purpose
Import list of comments to pass then import the contents later

This function is recursive

### Parameters

url, str : url to patreon comment

key, str: The patreon user access token used for authentication

post_id, str : id of the post

user_id, str : id of the user

import_id, str : An Identifier for the patreon post being imported

### Return Values
None


## import_campaign_page (url, key, import_id)

### Purpose
import found patreon campaigns

This function is recursive

### Parameters

url, str : url to patreon comment

key, str: The patreon user access token used for authentication

import_id, str : An Identifier for the patreon post being imported

### Return Values
None


## import_posts (import_id, key, allowed_to_scrape_dms, contributor_id)

### Purpose

This function does precisely what one would think it does. It grabs the metadata required to then download the content of a specific patreon creator using a valid token via calling other functions

### Parameters

import_id, str : An Identifier for the patreon post being imported

key, str: The patreon user access token used for authentication

allowed_to_scrape_dms, bool : determines whether or not the contributor has given permission to scrape channels for the purposes of getting Patreon rewards which are sent in channels

contributor_id, str :

### Return Values

None
