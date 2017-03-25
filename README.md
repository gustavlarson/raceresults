# raceresults
Create a list of top runners from a Neptron race

Download the results in a JSON format:

    curl http://results.neptron.se/webapi/sthtunnelruncitytunneln2017/results\?page\=0\&pageSize\=33251\&raceId\=99\&sortOrder\=Place > results.json
    
Print results

    ./resultparser.json
