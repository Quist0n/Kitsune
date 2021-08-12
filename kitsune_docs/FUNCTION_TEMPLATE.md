# Name
< Name is replaced for the name of the
component for the heading >
# Functions

## Functon Name(parameter list)
< Function Name is replaced for the name
of the function as it exists in the
source code>

### Purpose
A written purpose for what the function
exists for, what it is used for and why
it is used. A basic summary essentially

### Parameters

A list of parameters in the form
<parameter name, type> : <description>
One for each parameter

### Return Values
<condition for the values to be returned> :
        A list of parameters in the form
        <type> : <description>

Indent the output under its condition, omit conditions if there are
none

If data being returned is an array, list,
dictionary or some other method of
bundling the data together, just indent
them under the name of their parent. If
the data is in a list and therefore can't
be referenced like a Hashmap/Dictionary
would, just indent the same and state
what should be in that list.

E.g

If scraping site data is successful:

        list : List of imported post urls
                str : a string of the imported posts urls
