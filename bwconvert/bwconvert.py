#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Converter from Bitwarden json to csv for KeePassXC.

Artamonov Mikhail [https://github.com/maximalisimus]
maximalis171091@yandex.ru
# License: GPL3
"""

import json
import pathlib
import re
import codecs
import argparse
import sys

__author__ = 'Mikhail Artamonov'
__progname__ = str(pathlib.Path(sys.argv[0]).resolve().name)
__copyright__ = f"© The \"{__progname__}\". Copyright  by 2023."
__credits__ = ["Mikhail Artamonov"]
__license__ = "GPL3"
__version__ = "1.0.0"
__maintainer__ = "Mikhail Artamonov"
__email__ = "maximalis171091@yandex.ru"
__status__ = "Production"
__date__ = '02.10.2023'
__modifed__ = '12.10.2023'
__contact__ = 'VK: https://vk.com/shadow_imperator'

infromation = f"Author: {__author__}\nProgname: {__progname__}\nVersion: {__version__}\n" + \
			f"Date of creation: {__date__}\nLast modified date: {__modifed__}\n" + \
			f"License: {__license__}\nCopyright: {__copyright__}\nCredits: {__credits__}\n" + \
			f"Maintainer: {__maintainer__}\nStatus: {__status__}\n" + \
			f"E-Mail: {__email__}\nContacts: {__contact__}"

isuser = False

class Arguments:
	''' Class «Arguments».
	
		Info: A class designed to store command-line values 
				by entering parameters through the «Argparse» module.
		
		Variables: All parameters are entered using the «createParser()» 
					method.
		
		Methods: 
			__getattr__(self, attrname):
				Access to a non-existent variable.
				Used when trying to get a parameter that does not exist. 
				In this case, «None» is returned to the user, instead 
				of an error.
			
			__str__(self):
				For STR Function output paramters.
			
			__repr__(self):
				For Debug Function output paramters.
	'''
	
	__slots__ = ['__dict__']
	
	def __getattr__(self, attrname):
		''' Access to a non-existent variable. '''
		return None

	def __str__(self):
		''' For STR Function output paramters. '''
		except_list = ['']
		#return '\t' + '\n\t'.join(tuple(map(lambda x: f"{x}: {getattr(self, x)}" if not x in except_list else f"", tuple(filter( lambda x: '__' not in x, dir(self))))))
		return '\t' + '\n\t'.join(f"{x}: {getattr(self, x)}" for x in dir(self) if not x in except_list and '__' not in x)
	
	def __repr__(self):
		''' For Debug Function output paramters. '''
		except_list = ['']
		return f"{self.__class__}:\n\t" + \
				'\n\t'.join(f"{x}: {getattr(self, x)}" for x in dir(self) if not x in except_list and '__' not in x)
				#'\n\t'.join(tuple(map(lambda x: f"{x}: {getattr(self, x)}" if not x in except_list else f"", tuple(filter( lambda x: '__' not in x, dir(self))))))

def createParser():
	''' The function of creating a parser with a certain hierarchy 
		of calls. Returns the parser itself and the sub-parser, 
		as well as groups of parsers, if any. '''
	dict_parser = dict()
	parser = argparse.ArgumentParser(prog=__progname__,description='Converter from Bitwarden json to csv for KeePassXC.')
	parser.add_argument ('-v', '--version', action='version', version=f'{__progname__} {__version__}',  help='Version.')
	parser.add_argument ('-info', '--info', action='store_true', default=False, help='Information about the author.')
	parser.add_argument('json', metavar='JSON', type=str, default='', help='The input json file of the exported Bitwarden database.')#, required=True)
	parser.add_argument("-o", '--output', dest="output", metavar='OUTPUT', type=str, default='', help='The output csv file of the database for KeepasXC.')
	dict_parser['parser'] = parser
	
	return dict_parser

def read_write_json(jfile, typerw, data = dict(), indent: int = 2):
	''' The function of reading and writing JSON objects. '''
	with codecs.open(str(pathlib.Path(jfile).resolve()), typerw, 'utf8') as fp:
		if typerw == 'r':
			data = json.load(fp)
			return data
		else:
			json.dump(data, fp, indent=indent)

def read_write_text(onfile, typerw, data = ""):
	''' The function of reading and writing text files. '''
	with codecs.open(str(pathlib.Path(onfile).resolve()), typerw, 'utf8') as fp:
		if typerw == 'r':
			data = fp.read()
		else:
			fp.write(data)
	return data

def cleardata(obj_dict):
	obj_dict['group'].clear()
	obj_dict['title'] = ''
	obj_dict['username'] = ''
	obj_dict['password'] = ''
	obj_dict['url'].clear()
	obj_dict['notes'] = ''
	obj_dict['totp'] = ''
	obj_dict['icon'] = ''
	obj_dict['last'] = ''
	obj_dict['created'] = ''
	obj_dict['fields'] = ''

def normalize(obj_dict):
	obj_dict['notes'].replace('"','').replace('\'','').replace(',','').replace('\\','').replace('\\"','').strip()
	obj_dict['notes'] = re.sub('"','',obj_dict['notes'])
	obj_dict['notes'] = re.sub(',','',obj_dict['notes'])
	obj_dict['notes'] = re.sub('\'','',obj_dict['notes'])
	obj_dict['fields'].replace('"','').replace('\'','').replace(',','').replace('\\','').replace('\\"','').strip()
	obj_dict['fields'] = re.sub('"','',obj_dict['fields'])
	obj_dict['fields'] = re.sub(',','',obj_dict['fields'])
	obj_dict['fields'] = re.sub('\'','',obj_dict['fields'])
	obj_dict['title'].replace('"','').replace('\'','').replace(',','').replace('\\','').replace('\\"','').strip()
	obj_dict['title'] = re.sub('"','',obj_dict['title'])
	obj_dict['title'] = re.sub(',','',obj_dict['title'])
	obj_dict['title'] = re.sub('\'','',obj_dict['title'])
	for c in range(len(obj_dict['group'])):
		obj_dict['group'][c].replace('"','').replace('\'','').replace(',','').replace('\\','').replace('\\"','').strip()
		obj_dict['group'][c] = re.sub('"','',obj_dict['group'][c])
		obj_dict['group'][c] = re.sub(',','',obj_dict['group'][c])
		obj_dict['group'][c] = re.sub('\'','',obj_dict['group'][c])

def on_edit(elem, on_obj, on_org):
	global isuser
	
	cleardata(on_obj)
	
	if not isuser:
		for i in elem['collectionIds']:
			on_obj['group'].append(on_org[str(i)])
	else:
		on_obj['group'].append(on_org[elem['folderId']])
	
	on_obj['title'] = elem['name']
	on_obj['notes'] = elem['notes'] if elem['notes'] != None else 'None'
	on_obj['notes'].replace('"','').replace('\'','').replace(',','').replace('\\','').replace('\\"','').strip()
	if 'login' in elem.keys():
		if 'uris' in elem['login']:
			for j in elem['login']['uris']:
				on_obj['url'].append(j['uri'])
		on_obj['username'] = elem['login']['username'] if elem['login']['username'] != None else ''
		on_obj['password'] = elem['login']['password'] if elem['login']['password'] != None else ''
		on_obj['totp'] = elem['login']['totp'] if elem['login']['totp'] != None else ''
	if 'fields' in elem.keys():
		for i in elem['fields']:
			on_obj['fields'] = f"{on_obj['fields']}\n{i['name']}: {i['value']}"
	if 'card' in elem.keys():
		temp = elem['card']['cardholderName']
		on_obj['fields'] = f"{on_obj['fields']}\n\nБанковская карта.\nНаименование: {temp if temp != None else 'None'}"
		temp = elem['card']['brand']
		on_obj['fields'] = f"{on_obj['fields']}\nМарка: {temp if temp != None else 'None'}"
		temp = elem['card']['number']
		on_obj['fields'] = f"{on_obj['fields']}\nНомер карты: {temp if temp != None else 'None'}"
		temp = elem['card']['expMonth']
		on_obj['fields'] = f"{on_obj['fields']}\nМесяц окончания: {temp if temp != None else 'None'}"
		temp = elem['card']['expYear']
		on_obj['fields'] = f"{on_obj['fields']}\nГод окончания: {temp if temp != None else 'None'}"
		temp = elem['card']['code']
		on_obj['fields'] = f"{on_obj['fields']}\ncvv код: {temp if temp != None else 'None'}\n"
	if 'identity' in elem.keys():
		on_obj['fields'] = f"{on_obj['fields']}\n\nИдентификация.\n"
		for k, v in elem['identity'].items():
			on_obj['fields'] = f"{on_obj['fields']}\n{k}: {v if v != None else 'None'}"
	normalize(on_obj)

def main(*argv):
	''' The main cycle of the program. '''
	global infromation, isuser
	
	parser_dict = createParser()
	args = Arguments()
	if len(argv) > 0:
		parser_dict['parser'].parse_args(args=argv, namespace=Arguments)
	else:
		parser_dict['parser'].parse_args(namespace=Arguments)
	
	if args.info:
		print(infromation)
		sys.exit(0)
	
	if args.json != '':
		args.json = pathlib.Path(args.json).resolve()
	else:
		parser_dict['parser'].parse_args(['-h'])
		sys.exit(0)
	
	if args.output != '':
		out_file_name = args.output.replace(''.join(pathlib.Path(args.output).suffixes), '')
		args.output = pathlib.Path(f"{out_file_name}.csv").resolve()
	else:
		args.output = pathlib.Path(str(args.json).replace('.json','.csv')).resolve()
	
	arr = read_write_json(str(args.json),'r')
	org = dict()
	
	if 'collections' in arr.keys():
		isuser = False
	else:
		isuser = True
	
	if not isuser:	
		for i in arr['collections']:
			org[str(i['id'])] = i['name']
	else:
		for i in arr['folders']:
			org[str(i['id'])] = i['name']
	
	output_str = '"Group","Title","Username","Password","URL","Notes","TOTP","Icon","Last Modified","Created"'
	
	output_dict = dict()
	
	output_dict['group'] = list()
	output_dict['title'] = ''
	output_dict['username'] = ''
	output_dict['password'] = ''
	output_dict['url'] = list()
	output_dict['notes'] = ''
	output_dict['totp'] = ''
	output_dict['icon'] = ''
	output_dict['last'] = ''
	output_dict['created'] = ''
	output_dict['fields'] = ''
	
	counter = 0
	
	for i in arr['items']:
		on_edit(i, output_dict, org)
		counter+=1
		for l in output_dict['group']:
			output_str = f"{output_str}\n\"{l}\",\"{output_dict['title']}\""
			output_str = f"{output_str},\"{output_dict['username']}\",\"{output_dict['password']}\""
			
			on_url = ''
			for p in output_dict['url']:
				on_url += '\n' + str(p).replace('"','').replace('\'','').replace(',','').replace('\\','').replace('\\"','').strip()
				on_url = re.sub('"','',on_url)
				on_url = re.sub(',','',on_url)
				on_url = re.sub('\'','',on_url)
			
			if len(output_dict['url']) > 0:
				output_str = f"{output_str},\"{output_dict['url'][0]}\""
				output_dict['fields'] = f"{on_url}\n{output_dict['fields']}"
			else:
				output_str = f"{output_str},\"\""
			
			output_dict['notes'] = f"{output_dict['notes']}\n\n{output_dict['fields']}"
			output_str = f"{output_str},\"{output_dict['notes']}\""
			output_str = f"{output_str},\"{output_dict['totp']}\""
			output_str = f"{output_str},\"{output_dict['icon']}\""
			output_str = f"{output_str},\"{output_dict['last']}\""
			output_str = f"{output_str},\"{output_dict['created']}\""
	
	read_write_text(str(args.output), 'w', output_str.strip())
	print(counter)

if __name__ == '__main__':
	main()
else:
	main()
