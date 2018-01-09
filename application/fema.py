import json
import ssl
import urllib.request

def disastersearch (state):

# disastersearch takes a two character state code as input and returns a sorted list of counties and # of disasters
# we do this by searching the OpenFEMA API for the input state and creating a histogram of the county & disaster count


    #Define a few variables & set HTTPS Context
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "GU" ]
    all_disaster_data = {}
    counties = {}
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    state=state.upper()
    if state not in states :
        lst=list()
        lst=[state, "Not a valid state"]
        return(lst)

    else:

        # FEMA API Documentation
        # https://www.fema.gov/openfema-api-documentation
        # FEMA Disaster Declarations Summaries API URL
        serviceurl = 'https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries?'

        # Pull the number of Disaster reports avialable out of the 'count' key in metadata from FEMA API
        # ALL option deletes state filter & Retrieves all disasters

        parameters = {'$inlinecount': 'allpages', '$filter': "state eq\'" + state + "\'"}
        #if get_all : parameters = {'$inlinecount': 'allpages'}

        url = serviceurl + urllib.parse.urlencode(parameters)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        all_disaster_data.update(json.loads(data))
        metadata = all_disaster_data['metadata']
        disaster_count = int(metadata['count'])

        # use metadata['count'] to determine how many records we need to pull
        # pulling 1000 at a time
        if (disaster_count % 1000):
            count = int((disaster_count / 1000) + 1)
        else:
            count = int(disaster_count / 1000)

        for i in range(count):
            # add $skip and $top to API request to iterate 1000/call up to metadata['count']
            parameters.update({'$skip': i * 1000, '$top': 1000})
            url = serviceurl + urllib.parse.urlencode(parameters)
            uh = urllib.request.urlopen(url, context=ctx)
            data = uh.read().decode()
            # Dump our JSON data into a dictionary - all_disaster_data
            all_disaster_data.update(json.loads(data))
            # pull Disaster Declarations Summaries into its own dictionary - disasters_dict
            disasters_dict = all_disaster_data['DisasterDeclarationsSummaries']

            # Create histogram of disasters_dict by "State Abbreviation - County Name" in dictionary counties
            # Useful if pulling all records by eliminating "state eq" in parameters dictionary

            for i in range(len(disasters_dict)):
                disaster_county = disasters_dict[i]['declaredCountyArea']
                disaster_state = disasters_dict[i]['state']
                if not disaster_county:
                #print(disasters_dict[i]['state'], disasters_dict[i]['id'], disasters_dict[i]['declarationDate'],
                #      disasters_dict[i]['incidentType'], disasters_dict[i]['title'], "No Declared County Area")
                    continue
                else:
                    counties[disaster_county] = counties.get(disaster_county,0) + 1

        # Dump our dictionary counties into lst, reverse sort them by value
        # then loop through the sorted list and print it out highest to lowest
        total_disasters = 0
        lst = list(counties.items())
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return(lst)