# Zawgyi - Unicode Converter
- Another zawgyi - unicode converter
- mimic php's strtr function, codes are copied from stackoverflow
- https://stackoverflow.com/questions/10931150/phps-strtr-for-python

## Rules are separated as 2 parts
- direct conversion using strtr function
- regular expression to correct character ordering

## Performance
- tested and converted within 10 seconds with Zawgyi xml (32MB wikipedia dump written in Zawgyi)
- 99% correctness guarrentee


## Instruction
```bash
python3 zg-my-strtr.py -i zawgyi.txt -o unicode.txt
```
