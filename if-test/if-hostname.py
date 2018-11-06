#!/usr/bin/env python3
#hostname = 'MTG1'
hostname=input('key in the hostname: ')
if hostname.upper() == 'MTG':
	print('The hostname was found to be mtg','hostname matches expected config',sep='\n')
else:
	print('The hostname was not found to be mtg')
print('exiting the script')
