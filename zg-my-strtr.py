#!/usr/bin/python3
# -*- coding: utf-8 -*-
# basic idea copied from here https://stackoverflow.com/questions/10931150/phps-strtr-for-python

import sys, getopt
import re

def strtr(s, repl):
  pattern = '|'.join(map(re.escape, sorted(repl, key=len, reverse=True)))
  return re.sub(pattern, lambda m: repl[m.group()], s)

# def returnkey(repl):
#     return repl

# def strtr_re(s, repl):
#   pattern = '|'.join(map(returnkey, sorted(repl, key=len, reverse=True)))
#   # print(pattern)
#   return re.sub(pattern, lambda m: m.group()[::-1], s)

## This is faster and more correct
def strtr_re(s, patterns):
  for pattern, repl in patterns.items():
    s = re.sub(pattern, repl, s)
  return s

# def strtr(strng, replace):
#     buf, i = [], 0
#     while i < len(strng):
#         for s, r in replace.items():
#             if strng[i:len(s)+i] == s:
#                 buf.append(r)
#                 i += len(s)
#                 break
#         else:
#             buf.append(strng[i])
#             i += 1
#     return ''.join(buf)

zguni = {'ဳ' : 'ု','ဴ' : 'ူ','္' : '်','်' : 'ျ','ျ' : 'ြ','ြ' : 'ွ','ွ' : 'ှ','ၚ' : 'ါ်','ၠ' : '္က','ၡ' : '္ခ','ၢ' : '္ဂ','ၣ' : '္ဃ','ၤ' : 'င်္','ၥ' : '္စ','ၦ' : '္ဆ','ၧ' : '္ဆ','ၨ' : '္ဇ','ၩ' : '္ဈ','ၪ' : 'ဉ','ၫ' : 'ည','ၬ' : '္ဋ','ၭ' : '္ဌ','ၮ' : 'ဍ္ဍ','ၯ' : 'ဍ္ဎ','ၰ' : '္ဏ','ၱ' : '္တ','ၲ' : '္တ','ၳ' : '္ထ','ၴ' : '္ထ','ၵ' : '္ဒ','ၶ' : '္ဓ','ၷ' : '္န','ၷ' : '္ပ','ၸ' : '္ပ','ၹ' : '္ဖ','ၺ' : '္ဗ','ၻ' : '္ဘ','ၼ' : '္မ','ၽ' : 'ျ','ၾ' : 'ြ','ၿ' : 'ြ','ႀ' : 'ြ','ႁ' : 'ြ','ႂ' : 'ြ','ႃ' : 'ြ','ႄ' : 'ြ','ႅ' : '္လ','ႆ' : 'ဿ','သ္သ' : 'ဿ','ႇ' : 'ှ','ႈ' : 'ှု','ႉ' : 'ှူ','ႊ' : 'ွှ','ႏ' : 'န','႐' : 'ရ','႑' : 'ဏ္ဍ','႒' : 'ဋ္ဌ','႓' : '္ဘ','႔' : '့','႕' : '့','႗' : 'ဋ္ဋ','၈ၤ':'ဂင်္','ဧ။္':'၏','ဧ၊္':'၏','၄​င္း':'၎င်း','၎':'၎င်း','၎င္း':'၎င်း','ေ၀' : 'ေဝ','ေ၇' : 'ေရ','ေ၈':'ေဂ','စ်':'ဈ','ဥ​ာ':'ဉာ​','ဥ​္':'ဉ်','ၾသ':'ဩ','ေၾသာ္':'ဪ'}
zgunicorrect = {'\\s+္':'္','([က-အ])(င်္)' : '\\2\\1','(ေ)([က-အ၀၈၇]{1}္[က-အ၀၈၇]{1})' : '\\2\\1','([ေြ]{1,2})([က-အ၀၈၇]{1})':'\\2\\1','(ေ)([ျြွှ]+)':'\\2\\1','(ှ)(ျ)':'\\2\\1','(ံ)([ုူ])':'\\2\\1','([ုူ])([ိီ])':'\\2\\1','(ော)(္[က-အ])':'\\2\\1'}

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('zg-my.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('zg-my.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         outputfile = "converted_" + inputfile
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   print('Input file is ', inputfile)
   print('Output file is ', outputfile)

   f = open(inputfile, "r")

   converted = strtr(f.read(), zguni)
   converted = strtr_re(converted, zgunicorrect)

   f.close()

   fo = open(outputfile, "w")
   fo.write(converted)
   fo.close()

if __name__ == "__main__":
   main(sys.argv[1:])
