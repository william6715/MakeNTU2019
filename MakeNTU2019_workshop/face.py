import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '7aa79720d4a5449ba782f6fdc8e066c5',
}

params = urllib.parse.urlencode({
    'mode': 'Printed',
})

try:
    conn=http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "https://westus.api.cognitive.microsoft.com/vision/v2.0/recognizeText?mode=Printed" , {"url":"https://www.vedfolnir.com/images/2016/03/TaiwanP1991-100Yuan-20002001_a.jpg"}, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
