# Sanza parsing
Some rough and ready scripts for parsing with Stanza. 

* `stanza-parse` calls `run-stanza.py`, which takes two arguments:
  * The input string, either flagged by `-i` or `--input`, or just bare.
  * The source language, flagged by `-l` or `--language`; if omited, defaults to English.

 ```
stanza-parse "Hello world!"
```
or equivalently
```
stanza-parse -i "Hellow world" -l en
```
