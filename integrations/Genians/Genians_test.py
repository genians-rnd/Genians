import demistomock as demisto
import CommonServerPython
import pytest
import json
import requests_mock


integration_params = {
    'server_ip': '172.29.62.26',
    'apikey': '98e7ab23-5078-49ff-bd8e-153a90f3f328',
    'tag_name': 'THREAT',
    'insecure': True
}

mock_demisto_args = {
    'ip': '172.29.62.3'
}


@pytest.fixture(autouse=True)
def init_tests(mocker):
    mocker.patch.object(demisto, 'params', return_value=integration_params)
    mocker.patch.object(demisto, 'args', return_value=mock_demisto_args)


def test_get_ip_nodeid(mocker):
    '''Genians-Genian-NAC-get-ip-nodeid'''
    from Genians import get_ip_nodeid
    
    res = get_ip_nodeid(mock_demisto_args['ip'])
    assert res == result_data_get_ip_nodeid


def test_get_tag_list(mocker):
    '''Genians-Genian-NAC-get-tag-list'''
    from Genians import get_tag_list
    
    res = get_tag_list()
    assert res == result_data_get_tag_list
    
  
result_data_get_ip_nodeid = [
    {
        "nl_nodeid": "66af6c34-4871-103a-8002-2cf05d0cf498-c9cd139d",
        "nl_ipstr": "172.29.62.3",
        "nl_mac": "2C:F0:5D:0C:F4:98",
        "nl_sensornid": "455eba44-4871-103a-8001-08002746dd06-326ef817",
        "nl_genidev": 20
    }
]

result_data_get_tag_list = {
    "result": [
        {
            "NP_NAME": "THREAT",
            "NP_PERIOD": "0h",
            "NP_STATIC": 0,
            "NP_PERIODEXPIRE": "0h",
            "NP_PERIODTYPE": 0,
            "NP_COLOR": "ff0000",
            "NP_DESC": "Anomaly",
            "NP_IDX": 3
        }
    ],
    "total": 1,
    "pageSize": 30,
    "page": 1
}
