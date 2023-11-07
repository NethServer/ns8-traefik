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
