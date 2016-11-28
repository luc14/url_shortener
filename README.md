# url_shortener
This project is for practicing programming design and flask.  

The user interface is a long url as the input and a short url as the output. The short url will redicrect the request to where the long url directs to. 

I created two types of storage: dictionary in memory and pickle file on disk. It wouldn't work in production because it cannot handle multiple processes or threads. (Also dictionary storage loses everything after shutting down the app.)
