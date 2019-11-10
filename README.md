FEMAWeb

FEMAWeb is a test of:
* Learning Python (Python 3)
* Building an OpenShift Application
* Consuming OpenFEMA Data as a Web Service

Documentation

FEMA API Documentation
https://www.fema.gov/openfema-api-documentation

FEMA Disaster Declarations Summaries API URL

serviceurl = 'https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries?'

Pull requests gleefully accepted - running application available at
http://femaweb-femaweb.7e14.starter-us-west-2.openshiftapps.com/

Updated 11/10/2019
Modify function names to make FEMAWeb compatible with OpenFaas, renaming fema.py to handler.py and disastersearch function to handle
added error checking in function handle to check state is equal to 2 char 
