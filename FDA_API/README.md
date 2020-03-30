# FDA_API
U.S. Food and Drug Administration provides almost 10 kinds of APIs that enable users to extract information about drugs, medical devices, food, etc. The website for developer is https://open.fda.gov, which is also very useful and user-friendly for journalists to find information, including product recalls and adverse events, out of public interest.   

In my case, I chose its Food Recall Enforcement Reports API, which returns data from the FDA Recall Enterprise System.


## Before query:
Before we dive into data, there are some API limitations that we need to be aware of, which is the key.

* With no API key: 40 requests per minute, per IP address. 1000 requests per day, per IP address.
* With an API key: 240 requests per minute, per key. 120000 requests per day, per key.

In my case, I didn’t apply for an API key since I don’t request a lot from the website and the connection is already stable and speedy. Of course, you can apply for a key if necessary. Here is a detailed [guidance](https://open.fda.gov/apis/authentication/) on how to get an API key.

### Using your API key

Your API key should be passed to the API as the value of the api_key parameter. Include it before other parameters, such as the search parameter. For example:

```
https://api_basics.fda.gov/drug/event.json?api_key=yourAPIKeyHere&search=...
```

## Query 1
For the first query, I want to see how many recalls have been initiated in 2019 regarding milk-related food. Here is the query:

```
https://api.fda.gov/food/enforcement.json?search=reason_for_recall:"milk"+AND+classification:"Class+I"+AND+report_date:[20190101+TO+20191231]&count=recalling_firm.exact&limit=5
```

For the first query, I’ve set five parameters:

* `Reason_for_recall = milk` means the recall has something to do with milk. You can change `milk` to any other types of food like `chips` or `ice+cream`.

* There are three classifications, where `Class+I` is the most serious one, which FDA defines as “dangerous or defective products that predictably could cause serious health problems or death.” The other two possible values are `Class+II` and `Class+III`.

* Report date is easy to understand, which means we perfectly collect all the recall reports in 2019. The correct format is `[yyyymmdd+TO+yyyymmdd]`, where `y`, `m` and `d` are all digits.

* `Count` means how we group the data. Here we want to have the number of recalls initiated by each company related, so we use set `count` equal to `recalling_firm.exact`.

* `Limit` means how many entries of result we want the query to return. Here we pick the top five companies in terms of number of recalls.

Here’s the [result](https://github.com/dingzhangyu/FDA_API/blob/master/milk_recall_response.json):
```
"results": [
    {
      "term": "Wismettac Asian Foods, INC",
      "count": 8
    },
    {
      "term": "Probar LLC",
      "count": 6
    },
    {
      "term": "Rong Shing Trading Inc.",
      "count": 3
    },
    {
      "term": "Surtidoras Bakery Inc",
      "count": 3
    },
    {
      "term": "Whole Foods Market",
      "count": 3
    }
  ]
```

It’s clear that Wismettac Asian Foods, INC ranked first on milk-related product recalling last year, with eight items recalled. Out of curiosity, I googled “wismettac Asian foods recall” and the following article popped out: [Wismettac Asian Foods Recalls Fish Cakes Due to Undeclared Allergens](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/wismettac-asian-foods-recalls-fish-cakes-due-undeclared-allergens).

In this official report, we can see the company is “recalling for eight types of Shirakiku brand imported fish cake products because of the possible contamination of some allergens (Milk, Egg and Crustacean shellfish).”

The announcement indicates that this is a voluntary recall initiated by the company and no illnesses have been reported yet.

Sounds not that bad.

## Query 2

```
https://api.fda.gov/food/enforcement.json?search=recalling_firm:"Wismettac+Asian+Foods,+INC"+AND+report_date:[20190101+TO+20191231]&limit=15
```

After our finding from the first query, I want to dive more into the Wismettac Asian Foods. Therefore, I changed the search parameter to the name of the company and kept the time constraint. I set the result limit to 15 entries to avoid too-long result.

Here is part of the [result](https://github.com/dingzhangyu/FDA_API/blob/master/Wismettac_Asian_Food.json):
```
"results": {
      "skip": 0,
      "limit": 15,
      "total": 18
    }
"results": [
    {
      "country": "United States",
      "city": "Santa Fe Springs",
      "reason_for_recall": "Fish Cake items contain possible contaminating undeclared egg, milk and shellfish.",
      "address_1": "13409 Orden Dr",
      "address_2": "",
      "code_info": "Item number #92525,",
      "product_quantity": "20,101 packages",
      "center_classification_date": "20190807",
      "distribution_pattern": "AK, AL, AR, AZ, CA, CO, CT, DC, FL, GA, HI, IL, IN, KS, KY, LA, MA, MD, MI, MN, MO, MS, NC, NE, NJ, NV, NY, OH, OK, OR, PA, RI, SC, TN, TX, UT, VA, WA",
      "state": "CA",
      "product_description": "Shirakiku FISH CAKE BOUTEN SK F  20/ 150G, Net Wt. 5.29 oz.  Keep Frozen, 7 pcs.  UPC 074410925253    Distributed by Wismettac Asian Foods, Inc. Santa Fe Springs, CA",
      "report_date": "20190814",
      "classification": "Class I",
      "openfda": {},
      "recall_number": "F-1973-2019",
      "recalling_firm": "Wismettac Asian Foods, INC",
      "initial_firm_notification": "Letter",
      "event_id": "83325",
      "product_type": "Food",
      "recall_initiation_date": "20190711",
      "postal_code": "90670-6336",
      "voluntary_mandated": "Voluntary: Firm initiated",
      "status": "Ongoing"
}
```

In the first part of the result, which I colored red, it shows we have 18 entries in total, which means the company had in total 18 food items recalled last year. But since we have a limit of 15, it only shows 15 entries.

Next, the second part is the 15 entries. In order to keep it short, here I only present the first entry, which is exactly one of the eight items we found in the first query. There is more information here about the recall, and I found the parameters not hard to understand. No elaboration here.

## Query 3a
```
https://api.fda.gov/food/enforcement.json?search=reason_for_recall:"milk"+AND+report_date:[20100101+TO+20191231]&count=voluntary_mandated.exact
```
After the queries above, I found most of the recall reports are initiated by companies, voluntarily, which tempted me to look for some recalls mandated by FDA. Therefore, I changed the reason back to `milk`, time period from `2010 to 2019` and sorted by `types of recall`.

Here comes the [result](https://github.com/dingzhangyu/FDA_API/blob/master/type_of_recall.json):
```
"results": [
    {
      "term": "Voluntary: Firm initiated",
      "count": 1495
    },
    {
      "term": "Voluntary: Firm Initiated",
      "count": 889
    },
    {
      "term": "FDA Mandated",
      "count": 1
    }
  ]
```
There is only one mandated recall related to milk product, initiated by FDA over the past decade! A bit staggering, right? But we are also curious about what the recalled item is and what the reasons may have been.

## Query 3b
```
https://api.fda.gov/food/enforcement.json?search=reason_for_recall:"milk"+AND+report_date:[20100101+TO+20191231]+AND+voluntary_mandated:"FDA+Mandated"
```
I tweaked the query parameter a little bit: instead of counting the number of FDA Mandated, I chose to search for the single case.

Here’s the final [answer](https://github.com/dingzhangyu/FDA_API/blob/master/Milk_Mandated.json):
```
"results": [
    {
      "country": "United States",
      "city": "Newport Beach",
      "reason_for_recall": "Graceleigh, Inc. dba Sammy\u0019s Milk is recalling certain lots of Sammy\u0019s Milk (Baby Food) because of possible presence of Cronobacter, a bacteria that can cause severe and sometimes fatal bloom infections or meningitis in infants (under 12 months of age) and it may not provide adequate nutritional levels of iron.",
      "address_1": "3419 Via Lido",
      "address_2": "",
      "code_info": "all lots:    AA141103  AB141103  AC141103  AD141103  AE141103  AF141103  AG141103  AA160526  AA160606A  AA160606B  AA160606C  AA160606D  AA160606E  AA160606F  AA160606G  AA160606H  AA160606I  AA160606J  AA160606K",
      "product_quantity": "20,008 units",
      "center_classification_date": "20170324",
      "distribution_pattern": "US",
      "state": "CA",
      "product_description": "Sammy's Milk (Baby Food), Net Wt. 12.84 oz (364 g), 6 containers per case",
      "report_date": "20170405",
      "classification": "Class I",
      "openfda": {},
      "recall_number": "F-1724-2017",
      "recalling_firm": "Sammy's Milk",
      "initial_firm_notification": "Press Release",
      "event_id": "75333",
      "product_type": "Food",
      "termination_date": "20170328",
      "more_code_info": null,
      "recall_initiation_date": "20160930",
      "postal_code": "92663-3908",
      "voluntary_mandated": "FDA Mandated",
      "status": "Terminated"
    }
  ]
```

There are many other usages of this API. Feel free to check this link to the official documentation that helps you get familiar with more parameters and syntax: https://open.fda.gov/apis/food/enforcement/
