import os
import sys
from getpass import getpass
 
import gdata.docs.service
import gdata.spreadsheet.service
 
 
'''
    get user information from the command line argument and 
    pass it to the download method

'''
gdoc_id=[]
def get_gdoc_information():
    email = raw_input('Email address:')
    password = getpass('Password:')
    gdoc_id = ['1PqbLW7JQxQjKnNoxzmnhHYR9wfeOLrcpcI5ZYe4XloM#gid=0','15bTZEakMhVQEfIWTY-P8eBzQ0L-VkLn8sk3vebSyu4o#gid=1748450656','0AriNcwJlkyQSdDVXRDhBemNfcU9YcDNXcHV4VVdvMWc#gid=0','0Ahavvuz2mKl9dGF4RWo3MTBuSGpxRGROMmVkNl9tSUE#gid=1','0AkXVKeUYVfF3dHVlckdnbWNVUVNEMHJsc3pJUDRVX1E#gid=0']
    for doc_id in gdoc_id:
        try:
            download(doc_id, email, password)
        except Exception, e:
            raise e
    
#python gdoc.py 1m5F5TXAQ1ayVbDmUCyzXbpMQSYrP429K1FZigfD3bvk#gid=0
def download(doc_id, email, password, download_path=None, ):
    print "Downloading the CSV file with id %s" % doc_id
 
    gd_client = gdata.docs.service.DocsService()
 
    #auth using ClientLogin
    gs_client = gdata.spreadsheet.service.SpreadsheetsService()
    gs_client.ClientLogin(email, password)
 
    #getting the key(resource id and tab id from the ID)
    
    resource    = doc_id.split('#')[0]
    tab         = doc_id.split('#')[1].split('=')[1]
    resource_id = 'spreadsheet:'+resource

    if download_path is None:
        download_path = os.path.abspath(os.path.dirname(__file__))
    file_name = os.path.join(download_path, '%s.xls' % (gdoc_id))
    if doc_id =='0AriNcwJlkyQSdDVXRDhBemNfcU9YcDNXcHV4VVdvMWc&#gid=0':
        file_name =='Uptown Pre-Lease List'
    elif doc_id =='15bTZEakMhVQEfIWTY-P8eBzQ0L-VkLn8sk3vebSyu4o#gid=1748450656':
        file_name=='Realty Availability List Office 2015-2016 - Tower Realty'
    elif doc_id=='1PqbLW7JQxQjKnNoxzmnhHYR9wfeOLrcpcI5ZYe4XloM#gid=0':
        file_name=='Metro Realty--4-8-14'
    elif doc_id =='0AkXVKeUYVfF3dHVlckdnbWNVUVNEMHJsc3pJUDRVX1E&gid=0':
        file_name='_24th Street Realty & Lee Properties Pre-Lease and Current List-14-15_'

 
    print 'Downloading spreadsheet to %s...' % file_name
 
    docs_token = gd_client.GetClientLoginToken()
    gd_client.SetClientLoginToken(gs_client.GetClientLoginToken())
    gd_client.Export(resource_id, file_name, gid=tab)
    gd_client.SetClientLoginToken(docs_token)
 
    print "Download Completed!"
 

if __name__=='__main__':
    get_gdoc_information()