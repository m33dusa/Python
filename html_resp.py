#Copyright 2022 July 27 
#Author Zainab Jalloh
#Title Guess the HTML Protocol 

import html
import random 
import sys, ast, json

def main():
    with open('protocols.txt', "wt") as file:
        html_protocols = dict({
            'Continue': 100,
            'Protocol Switch': 101,
            'Processing': 102,
            'Early Hint': 103,
            'ok': 200,
            'created': 201,
            'Accepted': 202,
            'Non-Authoritative Information': 203,
            'No Content': 204,
            'Reset Content': 205,
            'Partial Content': 206,
            'Multi-Status': 207,
            'Already Reported': 208,
            'IM Used': 226,
            #Redirection Messages
            'Multiple Choices': 300,
            'permanent redirect': 301,
            'Found': 302,
            'See Other': 303,
            'Not Modified': 304,
            'Use Proxy': 305,
            'Unused': 306,
            'Temporary Redirect': 307,
            'Permanent Redirect': 308,
            #Client error responses
            'Bad Request': 400,
            'Unauthorized': 401,
            'Payment Required': 402,
            'Forbidden': 403,
            'Not Found': 404,
            'Method Not Allowed': 405,
            'Not Acceptable': 406,
            'Proxy Authentication Required': 407,
            'Request Timeout': 408,
            'Conflict': 409,
            'Gone': 410,
            'Length Required': 411,
            'Precondition Failed': 412,
            'Payload Too Large': 413,
            'URI Too Long': 414,
            'Unsuported Media Type': 415,
            'Range Not Satisfiable': 416,
            'Exception Failed': 417,
            'Im a Teapot': 418,
            'Misdirected Request': 421,
            'Unprocessable Entity': 422,
            'Locked': 423,
            'Failed Dependency': 424,
            'Too Early': 425,
            'Upgrade Required': 426,
            'Precondition Required': 428,
            'Too Many Requests': 429,
            'Request Header Fields Too Large': 431,
            'Unavailable For Legal Reasons': 451,
            #Server Error Responses
            'Internal Server Error': 500,
            'Not Implemented': 501,    
            'Bad Gateway': 502,
            'Service Unavailable': 503,
            'Gateway Timeout': 504,
            'HTTP Version Not Supported': 505,
            'Variant Also Negotiates': 506,
            'Insufficient Storage': 507,
            'Loop Detected': 508,
            'Not Extended': 510,
            'Network Authentication Required': 511
        })
        for key, value in html_protocols.items():
            file.write('%s: %s\n' %(key, value))
        file.close()
    
    keys = random_html_protocol_generator()
    print(keys)

#randomly generates an HTML protocol 
def random_html_protocol_generator():
   with open('protocols.txt', 'r') as file:
    html_protocols_r = file.read().split('\n')
    html_protocols_dictionary = {}
    for i in range (len(html_protocols_r)):
        m = 0
        while( m<len(html_protocols_r)):
            html_protocols_dictionary = dict({
                (html_protocols_r[m].split(':')[0], html_protocols_r[m].split(':')[1])
            })
            print(html_protocols_dictionary)
            m +=1

if __name__=='__main__':main()

