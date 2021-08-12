
# Logger

# Functions

## log (log_id, msg, level, to_client)

### Purpose

log an event

### Parameters

log_id, str : ID for the log entry

msg, str : Log message contents

level, str : level of importance of the log message, 'debug' by default

to_client, bool : Push to redis backend for logging purposes, set to False to disable when handling more sensitive data, True by default

### Return Values
None


## get_logs (log_id)

### Purpose

Get a log entry

### Parameters

log_id, str : ID for the log entry

### Return Values
list : contains the logs that are requested, empty if there are none
