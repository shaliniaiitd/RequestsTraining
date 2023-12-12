import requests
import json
import xml
import xml.etree.ElementTree as ET
import xmltodict
import pytest


apiurl = "http://www.dneonline.com//calculator.asmx"
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
}
@pytest.mark.parametrize('int1, int2, result', [(4,4,'8'), (-2,-6,'-8'),(2,-6,'-4'),(5,-5,'0'),(2.5,5.6,'8.1')])
def test_add(int1,int2,result):
    headers['SOAPAction'] = 'http://tempuri.org/Add'
    soap1_input=f'''<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <Add xmlns="http://tempuri.org/">
          <intA>{int1}</intA>
          <intB>{int2}</intB>
        </Add>
      </soap:Body>
    </soap:Envelope>'''

    r1 = requests.post(apiurl, headers=headers, data=soap1_input)
    print(r1.status_code)
    xpars = xmltodict.parse(r1.text)
    print(xpars)

    assert (xpars["soap:Envelope"]["soap:Body"]["AddResponse"]["AddResult"]) == result

#Test Divide
@pytest.mark.parametrize('int1, int2, result', [(24,4,'6'), (24,-6,'-4'),(12,6,'2')])
def test_divide(int1,int2,result):
    headers['SOAPAction'] = 'http://tempuri.org/Divide'

    soap_input=f'''<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <Divide xmlns="http://tempuri.org/">
          <intA>{int1}</intA>
          <intB>{int2}</intB>
        </Divide>
      </soap:Body>
    </soap:Envelope>'''

    r1 = requests.post(apiurl, headers=headers, data= soap_input)

    xpars = xmltodict.parse(r1.text)
    print(xpars)

    assert (xpars["soap:Envelope"]["soap:Body"]["DivideResponse"]["DivideResult"]) == result

    #One defect is division by Zero error is not addressed.

#Test Multiply
@pytest.mark.parametrize('int1, int2, result', [(6,4,'24'), (-3,-6,'18'),(-2,6,'-12'),(0,7,'0')])
def test_multiply(int1,int2,result):
    headers['SOAPAction'] = 'http://tempuri.org/Multiply'

    soap_input=f'''<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <Multiply xmlns="http://tempuri.org/">
          <intA>{int1}</intA>
          <intB>{int2}</intB>
        </Multiply>
      </soap:Body>
    </soap:Envelope>'''

    r1 = requests.post(apiurl, headers=headers, data= soap_input)

    xpars = xmltodict.parse(r1.text)
    print(xpars)

    assert (xpars["soap:Envelope"]["soap:Body"]["MultiplyResponse"]["MultiplyResult"]) == result

#Test Subtract
@pytest.mark.parametrize('int1, int2, result', [(6,4,'2'), (4,-6,'10'),(2,6,'-4'),(3,0,'3')])
def test_subtract(int1,int2,result):
    headers['SOAPAction'] = 'http://tempuri.org/Subtract'

    soap_input=f'''<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <Subtract xmlns="http://tempuri.org/">
          <intA>{int1}</intA>
          <intB>{int2}</intB>
        </Subtract>
      </soap:Body>
    </soap:Envelope>'''

    r1 = requests.post(apiurl, headers=headers, data= soap_input)

    xpars = xmltodict.parse(r1.text)
    print(xpars)

    assert (xpars["soap:Envelope"]["soap:Body"]["SubtractResponse"]["SubtractResult"]) == result

