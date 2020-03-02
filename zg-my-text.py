#!/usr/bin/python3
# -*- coding: utf-8 -*-
# basic idea copied from here https://stackoverflow.com/questions/10931150/phps-strtr-for-python

import sys, getopt
import re

def strtr(s, repl):
  pattern = '|'.join(map(re.escape, sorted(repl, key=len, reverse=True)))
  return re.sub(pattern, lambda m: repl[m.group()], s)

## This is faster and more correct
def strtr_re(s, patterns):
  for pattern, repl in patterns.items():
    s = re.sub(pattern, repl, s)
  return s


zguni = {'ဳ' : 'ု','ဴ' : 'ူ','္' : '်','်' : 'ျ','ျ' : 'ြ','ြ' : 'ွ','ွ' : 'ှ','ၚ' : 'ါ်','ၠ' : '္က','ၡ' : '္ခ','ၢ' : '္ဂ','ၣ' : '္ဃ','ၤ' : 'င်္','ၥ' : '္စ','ၦ' : '္ဆ','ၧ' : '္ဆ','ၨ' : '္ဇ','ၩ' : '္ဈ','ၪ' : 'ဉ','ၫ' : 'ည','ၬ' : '္ဋ','ၭ' : '္ဌ','ၮ' : 'ဍ္ဍ','ၯ' : 'ဍ္ဎ','ၰ' : '္ဏ','ၱ' : '္တ','ၲ' : '္တ','ၳ' : '္ထ','ၴ' : '္ထ','ၵ' : '္ဒ','ၶ' : '္ဓ','ၷ' : '္န','ၷ' : '္ပ','ၸ' : '္ပ','ၹ' : '္ဖ','ၺ' : '္ဗ','ၻ' : '္ဘ','ၼ' : '္မ','ၽ' : 'ျ','ၾ' : 'ြ','ၿ' : 'ြ','ႀ' : 'ြ','ႁ' : 'ြ','ႂ' : 'ြ','ႃ' : 'ြ','ႄ' : 'ြ','ႅ' : '္လ','ႆ' : 'ဿ','သ္သ' : 'ဿ','ႇ' : 'ှ','ႈ' : 'ှု','ႉ' : 'ှူ','ႊ' : 'ွှ','ႏ' : 'န','႐' : 'ရ','႑' : 'ဏ္ဍ','႒' : 'ဋ္ဌ','႓' : '္ဘ','႔' : '့','႕' : '့','႗' : 'ဋ္ဋ','၈ၤ':'ဂင်္','ဧ။္':'၏','ဧ၊္':'၏','၄င္း':'၎င်း','၎':'၎င်း','၎င္း':'၎င်း','ေ၀' : 'ေဝ','ေ၇' : 'ေရ','ေ၈':'ေဂ','စ်':'ဈ','ဥာ':'ဉာ','ဥ္':'ဉ်','ၾသ':'ဩ','ေၾသာ္':'ဪ'}
zgunicorrect = {'\\s+္':'္','([က-အ])(င်္)' : '\\2\\1','(ေ)([က-အ၀၈၇]{1}္[က-အ၀၈၇]{1})' : '\\2\\1','([ေြ]{1,2})([က-အ၀၈၇]{1})':'\\2\\1','(ေ)([ျြွှ]+)':'\\2\\1','(ှ)(ျ)':'\\2\\1','(ံ)([ုူ])':'\\2\\1','([ုူ])([ိီ])':'\\2\\1','(ော)(္[က-အ])':'\\2\\1','(ဲ)(ွ)':'\\2\\1'}

def main(argv):
   inputdata = ''

   try:
      opts, args = getopt.getopt(argv,"hi:",["input="])
   except getopt.GetoptError:
      print('zg-my.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('zg-my.py -i <input>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputdata = arg

   converted = strtr(inputdata, zguni)
   converted = strtr_re(converted, zgunicorrect)

   print('converted from ', inputdata, ' to ', converted)

if __name__ == "__main__":
   main(sys.argv[1:])
