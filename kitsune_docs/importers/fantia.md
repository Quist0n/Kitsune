
# fantia Importer

The importer that is used when scraping from fantia.jp

# Functions

## enable_adult_mode (import_id, jar)

### Purpose

This function enables the viewing and downloading of adult rated content on a fantia account

### Parameters

import_id, str : ID of the imported post

jar, requests.cookies.RequestsCookieJar : object containing HTTP cookie information

### Return Values

If enabling viewing of adult content is successful:
       boolean: This will be set to True
Otherwise:
        boolean: This will be set to False

## disable_adult_mode (import_id, jar)

### Purpose

Used for disabling the ability to view adult content for a fantia account

### Parameters

import_id, str : ID of the imported post

jar, requests.cookies.RequestsCookieJar : object containing cookie information

### Return Values

None

## import_fanclub (fanclub_id, import_id, jar, page)

### Purpose

Parses data on the fantia fanclub pages and downloads and saves the contents

This function is recursive

### Parameters

fanclub_id, str : ID of the Fantia fanclub the user is subscribed to

import_id, str : ID of the imported post

jar, requests.cookies.RequestsCookieJar : object containing cookie information

page, int : The number of the page to import the contents of

### Return Values

None


## import_posts (import_id, key)

### Purpose

Manage the import via the usage of import_fanclub, enable_adult_mode and disable_adult_mode

### Parameters

import_id, str : ID of the imported post

key, str : user access token used for authentication

### Return Values

None
