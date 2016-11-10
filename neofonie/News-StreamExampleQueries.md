----------

# News-Stream Example Queries

## Examples Fetching Data with Search Words


----------


#### Searchword "Hillary Clinton" - All Data

[Searchword: "Hillary Clinton"](https://nstr.neofonie.de/solr-dev/hackathon/select?q=Hillary+Clinton&rows=3&indent=on&wt=json "Fetching all data")


----------


#### Searchwords "Hillary Clinton AND Donald Trump" - All Data

[Searchword: "Hillary Clinton AND Donald Trump"](https://nstr.neofonie.de/solr-dev/hackathon/select?q=Hillary+Clinton+OR+Donals+Trump&rows=3&indent=on&=json "Fetching all data")


----------


#### Searchwords "Hillary Clinton AND Donald Trump" - Just title and text

[Searchword: "Hillary Clinton AND Donald Trump"](https://nstr.neofonie.de/solr-dev/hackathon/select?fl=title+AND+text&q=%22Hillary+Clinton%22+AND+%22Donald+Trump%22&rows=3&indent=on&wt=json "Just title and text")


----------
#### Searchword: "Hillary Clinton" AND "Donald Trump" -  Titles only for articles in english language.


[Searchword: "Hillary Clinton" AND "Donald Trump" -  Titles only for articles in english language](https://nstr.neofonie.de/solr-dev/hackathon/select?fl=title&q=%22Hillary+Clinton%22+AND+%22Donald+Trump%22&fq=language%3A+en+AND+sourceId%3Aneofonie&rows=10&sort=publicationDate+DESC&wt=json&indent=on "Only articles in English language")


----------


#### Using Meta Information and some semantics of Solr search queries

In the next queries we are setting the number of results to zero, because we are just interested in the meta information

For each of the following three examples we find a different number of results depending on the semantic of the seach query.

* In the first example the query string is OR'ed and we get all results containing any occurrence of the query tokens.
* In the second example the semantics of the query is interpreted by Solr ("text:hillary +text:clinton +text:donald text:trump").
* In the third query we are searching for exact matches of "Hillary Clinton" AND "Donald Trump".

Most of the time you want the third query for results which match both politicians.

[Searchword: 'Hillary Clinton Donald Trump'](https://nstr.neofonie.de/solr-dev/hackathon/select?rows=0&q=Hillary+Clinton+Donald+Trump&rows=3&indent=on&wt=json "Just 3 results")

[Searchword: 'Hillary Clinton AND Donald Trump'](https://nstr.neofonie.de/solr-dev/hackathon/select?rows=0&q=Hillary+Clinton+AND+Donald+Trump&rows=3&indent=on&wt=json "")

[Searchword: '"Hillary Clinton" AND "Donald Trump"'](https://nstr.neofonie.de/solr-dev/hackathon/select?rows=0&q=%22Hillary+Clinton%22+AND+%22Donald+Trump%22&rows=3&indent=on&wt=json "")


----------


#### Documents about "Washington" from Neofonie's news crawl not older than 24 hours


The following query returns results for all news articles containing the search term 'Washington'.

Results contain terms like 'Kamasi Washington', as 'Washington Redskins' etc.

[Searchword: Washington](https://nstr.neofonie.de/solr-dev/hackathon/select?q=Washington&fq=%2BsourceId%3Aneofonie+%2BpublicationDateNOW%2FHOUR-24HOUR+TO+NOW%2FHOUR%2B1HOUR&rows=3&indent=on&wt=json "Get all with Washingtons")

Whereas the following search narrows the search down to all articles containing the entity with label 'Washington', which might match your initial intention of searching for the american capital in news.
Please see the next chapter for more examples using named entities.

[Entity Search: Washington](https://nstr.neofonie.de/solr-dev/hackathon/select?q=entityLabels%3A+Washington&fq=%2BsourceId%3Aneofonie+%2BpublicationDateNOW%2FHOUR-24HOUR+TO+NOW%2FHOUR%2B1HOUR&rows=3&indent=on&wt=json "Just get Place Washington")


----------


#### Hourly Documents Count about "Hillary Clinton" from Neofonie's news crawl not older than 24 hours: 

[Hourly ordered documents for "Hillary Clinton"](https://nstr.neofonie.de/solr-dev/hackathon/select?facet.range.end=NOW%2FHOUR%2B1HOUR&facet.range.gap=%2B1HOUR&facet=true&facet.range=publicationDate&facet.range.start=NOW%2FHOUR-24HOUR&q=entityLabels%3A+Hillary+Clinton&fq=%2BpublicationDate%3A%5BNOW%2FHOUR-24HOUR+TO+NOW%2FHOUR%2B1HOUR%5D+%2BsourceId%3Aneofonie&rows=3&indent=on&wt=json "")


----------


## Examples fetching data based on named entities

#### Fetch Top 5 news with NER annotations for "Hillary Clinton" AND "Donald Trump"

[Top 5 news with "Hillary Clinton" AND "Donald Trump"](https://nstr.neofonie.de/solr-dev/hackathon/select?fl=neoUrl+AND+title+AND+entityLabels&sort=publicationDate+DESC&rows=5&q=entityLabels%3A+%22Hillary+Clinton%22+AND+entityLabels%3A+%22Donald+Trump%22&fq=%2BpublicationDate%3A%5BNOW%2FHOUR-24HOUR+TO+NOW%2FHOUR%2B1HOUR%5D+%2BsourceId%3Aneofonie&rows=3&indent=on&wt=json "Top 5 news ordered by publicationDate")


----------

#### Fetch Top 5 news for "Volkswagen"

[TOP 5 articles for "Volkswagen"](https://nstr.neofonie.de/solr-dev/hackathon/select?sort=publicationDate+DESC&rows=5&fq=%2BpublicationDate%3A%5BNOW%2FHOUR-24HOUR+TO+NOW%2FHOUR%2B1HOUR%5D+%2BsourceId%3Aneofonie&q=entityLabels%3A+Volkswagen&fl=title&indent=on&wt=json "Top 5 articles")

----------

#### Fetch Top 5 news for the last two hours with recognized Organisations

[Top 5 news with recognized organisations](https://nstr.neofonie.de/solr-dev/hackathon/select?sort=publicationDate+DESC&rows=5&fq=%2BpublicationDate%3A%5BNOW%2FHOUR-2HOUR+TO+NOW%2FHOUR%2B1HOUR%5D+%2BsourceId%3Aneofonie&q=entityTypes%3A+ORGANISATION&fl=neoUrl+title+entityRfc4180&indent=on&wt=json "Top 5 articles")

----------


#### Fetch Top 5 news for which CRF recognized persons that are not already known as named entities.

[TOP 5 news with CRF annotations](https://nstr.neofonie.de/solr-dev/hackathon/select?sort=publicationDate+DESC&rows=5&fq=%2BpublicationDate%3A%5BNOW%2FHOUR-2HOUR+TO+NOW%2FHOUR%2B1HOUR%5D+%2BsourceId%3Aneofonie&q=unknownTypes%3A+PERSON&fl=neoUrl+title+entityRfc4180&indent=on&wt=json "Top 5 articles")


----------


## Examples fetching data with facets

#### Counts of news per hour containing the search term "Hillary Clinton" in the last 24 hours.

[Counts of news per hour for "Hillary Clinton"](https://nstr.neofonie.de/solr-dev/hackathon/select?facet.range=publicationDate&facet.range.gap=%2B1HOUR&q=Hillary+Clinton&facet=true&fl=titles&rows=0&facet.range.start=NOW%2FHOUR-24HOUR&facet.range.end=NOW%2FHOUR%2B1HOUR&fq=%2BpublicationDate%3A%5BNOW%2FHOUR-24HOUR+TO+NOW%2FHOUR%2B1HOUR%5D+%2BsourceId%3Aneofonie&indent=on&wt=json "News Statistics")


----------


#### Count for news grouped by language for the search term "Hillary Clinton" OR "Donald Trump".

[Count for news grouped by language](https://nstr.neofonie.de/solr-dev/hackathon/select?f.language.facet.sort=count&facet.method=fcs&q=entityLabels%3A%22Hillary+Clinton%22+OR+entityLabels%3A%22Donald+Trump%22&facet=true&facet.missing=true&rows=0&facet.field=language&facet.limit=10&fq=publicationDate%3A%5BNOW%2FDAY-3DAY+TO+NOW%2FDAY%2B1DAY%5D&indent=on&wt=json "Language counts")


----------


#### Counting all occurences of named entities in news which contain NEs "Hillary Clinton" OR "Donald Trump"

[NER counts for NEs "Hillary Clinton" OR "Donald Trump"](https://nstr.neofonie.de/solr-dev/hackathon/select?facet.method=enum&f.knownSurfaceforms.facet.sort=count&q=entityLabels%3A%22Hillary+Clinton%22+OR+entityLabels%3A%22Donald+Trump%22&facet=true&facet.missing=true&rows=0&facet.field=knownSurfaceforms&facet.limit=10&fq=publicationDate%3A%5BNOW%2FDAY-3DAY+TO+NOW%2FDAY%2B1DAY%5D&indent=on&wt=json "NER counts")


----------


#### Counting all CRFs in news which contain NEs "Hillary Clinton" OR "Donald Trump"

[CRF Counts in News for NEs  "Hillary Clinton" OR "Donald Trump"](https://nstr.neofonie.de/solr-dev/hackathon/select?facet.method=enum&q=entityLabels%3A%22Hillary+Clinton%22+OR+entityLabels%3A%22Donald+Trump%22&f.unknownPersons.facet.sort=count&facet=true&facet.missing=true&rows=0&facet.field=unknownPersons&facet.limit=10&fq=publicationDate%3A%5BNOW%2FDAY-3DAY+TO+NOW%2FDAY%2B1DAY%5D&indent=on&wt=json "CRF Counts")


----------
