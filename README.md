# Summary
in this project, we try to get all the internal urls in a specific domain,
those urls that are valid will be stored in MongoDB, the purpose of this
project was to be used in information retrieval projects, specifically
, in something like search engine, in search engine, we should be able to get
all the urls in a domain, in order to, in the next stpes we could build
index based on their documents, each document is the content of an url,
that we get from reading the url, each document, represents, the content
of an url.
this program recursively find all the ursl, in this program specifying
depth is not mentioned, all the urls that have been referenced in any of
the internal urls will be fined.
# Attention
this program is not able to find orphan url, orphan urls are urls that in any
internal page/url, have not been referenced.
# Recommendations or suggestions for future work
1) implementing some sort of finger print for content of each url, in order to
detect, duplicate contents, that program has seen before, to reduce the size of
document that we want to build index based on, this feature, because of we use
this program, for a specific domain, is not so important, when this feature
become important, is when we remove restriction on domain, that means, no
longer we are obligated to just crawle one domain and its internal urls, that
we have specified in first place, in this situation, even external urls will be
crawled by the program, the important thing in this situation, when we lifted
the just one domain condition, is to specify, when our program shoud end, the
previous sentence is so important, we should know, when we shoud stop, because
this task of crawling even external urls, will lead to almost infinte loop of
crawlign urls, so if we decide to lift restrictions on domain, we should
specify the termination condition.
2) using robot.txt file if it is present in the root of the website, it gives
some important information about the website and domain that we want to crawle.
3) parallelize the task of crawling the specified domain, it could reduce the
time that we spend on this task.
# Usage
this program has been developed with python 3.9, for runnig this program just
write `python crawler.py` after pressing enter, the program will ask you the
domian you want to crawle, just keep in mind that the form of input should be
look like "https://www.digikala.com, anything except that would not work.


