import json
import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/jxl,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Authorization': 'Bearer xx883b5583-07fb-416b-874b-77cce565d927',
    'Connection': 'keep-alive',
    'Content-Length': '9791',
    'Content-Type':	'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Host': 'platform.cloud.coveo.com',
    'Sec-Fetch-Dest':	'document',
    'Sec-Fetch-Mode':	'navigate',
    'Sec-Fetch-Site':	'none',
    'Sec-Fetch-User':	'?1',
    'Upgrade-Insecure-Requests':	'1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}

data = {
    'actionsHistory': '[]',
    'referrer': 'https://www.lcbo.com/en/products',
    'analytics': '{"clientId":"","documentLocation":"https://www.lcbo.com/en/products#t=clp-products&sort=relevancy&layout=card&f:@ec_category=[Beer%20%26%20Cider]","documentReferrer":"https://www.lcbo.com/en/products","pageId":""}',
    'isGuestUser': 'false',
    'aq': '@ec_category==Products',
    'searchHub': 'Web_Listing_EN',
    'tab': 'clp-products',
    'locale': 'en',
    'firstResult': '0',
    'numberOfResults': '10',
    'excerptLength': '200',
    'enableDidYouMean': 'true',
    'sortCriteria': 'relevancy',
    'queryFunctions': '[]',
    'rankingFunctions': '[]',
    'groupBy': '[{"field":"@lcbo_bintag_wine_sweetness","injectionDepth":10000,"computedFields":[{"field":"@lcbo_bintag_wine_sweetness","operation":"minimum"},{"field":"@lcbo_bintag_wine_sweetness","operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_bintag_wine_body","injectionDepth":10000,"computedFields":[{"field":"@lcbo_bintag_wine_body","operation":"minimum"},{"field":"@lcbo_bintag_wine_body","operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_bintag_wine_flavor_intensity","injectionDepth":10000,"computedFields":[{"field":"@lcbo_bintag_wine_flavor_intensity","operation":"minimum"},{"field":"@lcbo_bintag_wine_flavor_intensity","operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_bintag_wine_acidity","injectionDepth":10000,"computedFields":[{"field":"@lcbo_bintag_wine_acidity","operation":"minimum"},{"field":"@lcbo_bintag_wine_acidity","operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_bintag_wine_tannins","injectionDepth":10000,"computedFields":[{"field":"@lcbo_bintag_wine_tannins","operation":"minimum"},{"field":"@lcbo_bintag_wine_tannins","operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@ec_price","injectionDepth":10000,"computedFields":[{"field":"@ec_price","operation":"minimum"},{"field":"@ec_price","operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_total_volume","injectionDepth":10000,"computedFields":[{"field":"@lcbo_total_volume","operation":"minimum"},{"field":"@lcbo_total_volume","operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_alcohol_percent","injectionDepth":10000,"computedFields":[{"field":"@lcbo_alcohol_percent","operation":"minimum"},{"field":"@lcbo_alcohol_percent","operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_sugar_gm_per_ltr","injectionDepth":10000,"computedFields":[{"field":"@lcbo_sugar_gm_per_ltr","operation":"minimum"},{"field":"@lcbo_sugar_gm_per_ltr","operation":"maximum"}],"maximumNumberOfValues":1}]',
    'facets': '[{"facetId":"@ec_category","field":"ec_category","type":"hierarchical","injectionDepth":1000,"delimitingCharacter":"|","filterFacetCount":true,"basePath":["Products"],"filterByBasePath":false,"currentValues":[{"value":"Beer & Cider","state":"selected","children":[],"retrieveChildren":true,"retrieveCount":5}],"preventAutoSelect":true,"numberOfValues":1,"isFieldExpanded":false},{"facetId":"@lcbo_varietal_name","field":"lcbo_varietal_name","type":"specific","sortCriteria":"occurrences","injectionDepth":1000,"filterFacetCount":true,"currentValues":[{"value":"Chardonnay","state":"idle"},{"value":"Pinot Noir","state":"idle"},{"value":"Cabernet Sauvignon","state":"idle"},{"value":"Bordeaux","state":"idle"},{"value":"Shiraz/Syrah","state":"idle"}],"numberOfValues":5,"freezeCurrentValues":false,"preventAutoSelect":false,"isFieldExpanded":false},{"facetId":"@lcbo_vqa_code","field":"lcbo_vqa_code","type":"specific","injectionDepth":1000,"filterFacetCount":true,"currentValues":[{"value":"false","state":"idle"},{"value":"true","state":"idle"}],"numberOfValues":8,"freezeCurrentValues":false,"preventAutoSelect":false,"isFieldExpanded":false},{"facetId":"@country_of_manufacture","field":"country_of_manufacture","type":"specific","sortCriteria":"occurrences","injectionDepth":1000,"filterFacetCount":true,"currentValues":[{"value":"Canada","state":"idle"},{"value":"France","state":"idle"},{"value":"United States","state":"idle"},{"value":"Italy","state":"idle"},{"value":"United Kingdom","state":"idle"}],"numberOfValues":5,"freezeCurrentValues":false,"preventAutoSelect":false,"isFieldExpanded":false},{"facetId":"@lcbo_region_name","field":"lcbo_region_name","type":"specific","sortCriteria":"occurrences","injectionDepth":1000,"filterFacetCount":true,"currentValues":[{"value":"Ontario","state":"idle"},{"value":"California","state":"idle"},{"value":"Bordeaux","state":"idle"},{"value":"Burgundy","state":"idle"},{"value":"Tuscany","state":"idle"}],"numberOfValues":5,"freezeCurrentValues":false,"preventAutoSelect":false,"isFieldExpanded":false},{"facetId":"@lcbo_program","field":"lcbo_program","type":"specific","sortCriteria":"occurrences","injectionDepth":1000,"filterFacetCount":true,"currentValues":[{"value":"Vintages","state":"idle"},{"value":"Whisky Shop Collection","state":"idle"},{"value":"Online exclusive","state":"idle"},{"value":"Destination Collection","state":"idle"},{"value":"Gin Shop Collection","state":"idle"}],"numberOfValues":5,"freezeCurrentValues":false,"preventAutoSelect":false,"isFieldExpanded":false},{"facetId":"@lcbo_current_offer","field":"lcbo_current_offer","type":"specific","sortCriteria":"occurrences","injectionDepth":1000,"filterFacetCount":true,"currentValues":[{"value":"Clearance","state":"idle"},{"value":"On Sale","state":"idle"},{"value":"Aeroplan Offers","state":"idle"}],"numberOfValues":8,"freezeCurrentValues":false,"preventAutoSelect":false,"isFieldExpanded":false},{"facetId":"@stores_stock","field":"stores_stock","type":"specific","injectionDepth":1000,"filterFacetCount":true,"currentValues":[{"value":"false","state":"idle"},{"value":"true","state":"idle"}],"numberOfValues":8,"freezeCurrentValues":false,"preventAutoSelect":false,"isFieldExpanded":false},{"facetId":"@ec_rating","field":"ec_rating","type":"numericalRange","sortCriteria":"descending","injectionDepth":1000,"filterFacetCount":true,"currentValues":[{"start":5,"end":5,"endInclusive":true,"state":"idle"},{"start":4,"end":4.9,"endInclusive":true,"state":"idle"},{"start":3,"end":3.9,"endInclusive":true,"state":"idle"},{"start":2,"end":2.9,"endInclusive":true,"state":"idle"},{"start":1,"end":1.9,"endInclusive":true,"state":"idle"}],"numberOfValues":5,"freezeCurrentValues":false,"generateAutomaticRanges":false}]',
    'facetOptions': '{"freezeFacetOrder":true}',
    'categoryFacets': '[]',
    'retrieveFirstSentences': 'true',
    'timezone': 'America/Toronto',
    'enableQuerySyntax': 'false',
    'enableDuplicateFiltering': 'false',
    'enableCollaborativeRating': 'false',
    'debug': 'false',
    'allowQueriesWithoutKeywords': 'true',
    'dictionaryFieldContext': '{"stores_stock":"","stores_inventory":"212","stores_stock_combined":"212","stores_low_stock_combined":"212"}'
    }

# Get total number of entries in Beer & Cider Section
r = requests.post('https://platform.cloud.coveo.com/rest/search/v2?organizationId=lcboproductionx2kwygnc',
                 headers=headers, data=data)
result = r.json()
count = result['totalCount']
print(f'Count: {count}')

# Get entries 1000 at a time
start = 0
loop = 1
while count > 0:
    data['firstResult'] = start
    if count > 1000:
        data['numberOfResults'] = str(1000)
        #print(f'Start: {start}, Num Result: {data["numberOfResults"]}')
        r = requests.post('https://platform.cloud.coveo.com/rest/search/v2?organizationId=lcboproductionx2kwygnc',
                        headers=headers, data=data)
        result = r.json()
        start += 1000
        count -= 1000
        with open(f'data{loop}.json', 'w') as f:
            json.dump(result, f)
        loop += 1
    else:
        data['numberOfResults'] = str(count)
        #print(f'Start: {start}, Num Result: {data["numberOfResults"]}')
        r = requests.post('https://platform.cloud.coveo.com/rest/search/v2?organizationId=lcboproductionx2kwygnc',
                          headers=headers, data=data)
        result = r.json()
        with open(f'data{loop}.json', 'w') as f:
            json.dump(result, f)
        count -= 1000