# Sanza parsing
Some rough and ready scripts for parsing with Stanza. 

## `stanza-parse`
`stanza-parse` calls `run-stanza.py`, which takes two arguments:
* The input string, either flagged by `-i` or `--input`, or just bare.
* The source language, flagged by `-l` or `--language`; if omited, defaults to English.
  * Currently has settings for `en`, `fr`, `it`, `de`, `nl` (which are at the moment minimally different anyway). 

Sample usage:
```
stanza-parse "Hello world!"
```
or equivalently
```
stanza-parse -i "Hellow world" -l en
```
The fist run of a new language will take a little time.

The output is a human-readable table, not the standard json-like object (I use this for checking things quickly on the command line, not running as part of a larger pipeline).

## More to come.
