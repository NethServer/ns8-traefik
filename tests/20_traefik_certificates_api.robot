*** Settings ***
Library    SSHLibrary
Resource          api.resource

*** Test Cases ***

Get default ACME server
    ${response} =  Run task    module/traefik1/get-acme-server    {}
    Should Be Equal As Strings    ${response['url']}        https://acme-v02.api.letsencrypt.org/directory


Set ACME server url to Let's Encrypt Staging
    ${response} =  Run task    module/traefik1/set-acme-server
    ...    {"url":"https://acme-staging-v02.api.letsencrypt.org/directory"}

Get configured ACME server
    ${response} =  Run task    module/traefik1/get-acme-server    {}
    Should Be Equal As Strings    ${response['url']}        https://acme-staging-v02.api.letsencrypt.org/directory

Request an invalid certificate
    ${response} =  Run task    module/traefik1/set-certificate
    ...    {"fqdn":"example.com"}
    Should Be Equal As Strings    ${response['obtained']}    False

Get invalid cerficate status
    ${response} =  Run task    module/traefik1/get-certificate    {"fqdn": "example.com"}
    Should Be Equal As Strings    ${response['fqdn']}        example.com
    Should Be Equal As Strings    ${response['obtained']}    False
    Should Be Equal As Strings    ${response['type']}    internal

Get certificate list
    ${response} =  Run task    module/traefik1/list-certificates    null
    Should Contain    ${response}    example.com

Get expanded certificate list
    ${response} =  Run task    module/traefik1/list-certificates    {"expand_list": true}
    Should Be Equal As Strings    ${response[0]['fqdn']}        example.com
    Should Be Equal As Strings    ${response[0]['obtained']}    False
    Should Be Equal As Strings    ${response[0]['type']}    internal

Delete certificate
    Run task    module/traefik1/delete-certificate   	 {"fqdn": "example.com"}

Get empty certificates list
    ${response} =  Run task    module/traefik1/list-certificates    null
    Should Be Empty    ${response}

Generate a custom private and public key
    ${plain_key} =    Execute Command    openssl genrsa 4096
    ${plain_csr} =    Execute Command    echo "${plain_key}" \| openssl req -key /dev/stdin -x509 -sha256 -days 3650 -nodes -subj "/CN=test.example.com"  -addext "subjectAltName=DNS:test.example.com"
    # base64 encode the key and csr
    ${encoded_key} =    Execute Command    echo "${plain_key}" \| base64 -w 0
    ${encoded_csr} =    Execute Command    echo "${plain_csr}" \| base64 -w 0
    Set Suite Variable    ${key}   ${encoded_key}
    Set Suite Variable    ${csr}   ${encoded_csr}

Upload a custom certificate
    ${response} =  Run task    module/traefik1/upload-certificate
    ...    {"keyFile": "${key}", "certFile": "${csr}"}
    ${response} =  Run task    module/traefik1/get-certificate    {"fqdn": "test.example.com"}
    Should Be Equal As Strings    ${response['fqdn']}        test.example.com
    Should Be Equal As Strings    ${response['obtained']}    True
    Should Be Equal As Strings    ${response['type']}    custom
    Run task    module/traefik1/delete-certificate   	 {"fqdn": "test.example.com"}

Upload custom certificate is no overriden by an internal certificate
    Run task    module/traefik1/upload-certificate
    ...    {"keyFile": "${key}", "certFile": "${csr}"}
    Run task    module/traefik1/set-certificate
    ...    {"fqdn":"test.example.com"}
    ${response} =  Run task    module/traefik1/get-certificate    {"fqdn": "test.example.com"}
    Should Be Equal As Strings    ${response['type']}    custom
    Run task    module/traefik1/delete-certificate   	 {"fqdn": "test.example.com"}
    ${response} =  Run task    module/traefik1/get-certificate    {"fqdn": "test.example.com"}
    Should Be Empty    ${response}

Requested internal certificate is overriden by an uploaded custom certificate
    Run task    module/traefik1/set-certificate   {"fqdn":"test.example.com"}
    Run task    module/traefik1/upload-certificate
    ...    {"keyFile": "${key}", "certFile": "${csr}"}
    ${response} =  Run task    module/traefik1/get-certificate    {"fqdn": "test.example.com"}
    Should Be Equal As Strings    ${response['type']}    custom
    Run task    module/traefik1/delete-certificate   	 {"fqdn": "test.example.com"}
    ${response} =  Run task    module/traefik1/get-certificate    {"fqdn": "test.example.com"}
    Should Be Empty    ${response}
     
The certificate must be listed only once
    Run task    module/traefik1/upload-certificate   {"keyFile": "${key}", "certFile": "${csr}"}
    Run task    module/traefik1/set-certificate   {"fqdn":"test.example.com"}
    ${response} =  Run task    module/traefik1/list-certificates    {"expand_list": true}
    Length Should Be    ${response}    1
    Should Be Equal As Strings    ${response[0]['type']}    custom

    Run task    module/traefik1/delete-certificate   	 {"fqdn": "test.example.com"}
    ${response} =  Run task    module/traefik1/get-certificate    {"fqdn": "test.example.com"}
    Should Be Empty    ${response}
    Run task    module/traefik1/set-certificate   {"fqdn":"test.example.com"}
    Run task    module/traefik1/upload-certificate   {"keyFile": "${key}", "certFile": "${csr}"}
    ${response} =  Run task    module/traefik1/list-certificates    {"expand_list": true}
    Length Should Be    ${response}    1

    Should Be Equal As Strings    ${response[0]['type']}    custom
    Run task    module/traefik1/delete-certificate   	 {"fqdn": "test.example.com"}
    ${response} =  Run task    module/traefik1/get-certificate    {"fqdn": "test.example.com"}
    Should Be Empty    ${response}
