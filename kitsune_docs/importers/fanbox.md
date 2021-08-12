# Fanbox Importer

The importer that is used when scraping from fanbox.cc

# Functions

## import_comment (user_id, post_id, import_id)

### Purpose

import a comment on Fanbox posts

### Parameters

user_id, str : ID of the creator

post_id, str : ID of the post

import_id, str : An Identifier for patreon post being imported


### Return Values
None

## import_comments (key, post_id, user_id, import_id, url)

### Purpose

Import all comments on Fabox posts

### Parameters

key, str : The patreon user access token used for authentication

post_id, str : ID of the post

user_id, str : ID of the creator

import_id, str : An Identifier for patreon post being imported

url, str : url to use for api requests, set None by default


### Return Values
None

## import_posts (import_id, key, url)

### Purpose

This gathers metadata and then uses that data to download the contents
of a specific creator using a valid token

### Parameters

import_id, str : An Identifier for patreon post being imported

key, str : The patreon user access token used for authentication

url, str : The url that will be used to retrieve the json data for extraction

### Return Values
None
