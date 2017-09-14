import sys
import logging
from ncclient import manager

log = logging.getLogger(__name__)

# Various IOS Snippets

CREATE_VRF = """
<config>
        <cli-config-data>
            <cmd>ip routing</cmd>
            <cmd>ip vrf %s</cmd>
        </cli-config-data>
</config>
"""


REMOVE_VRF = """
<config>
        <cli-config-data>
            <cmd>ip routing</cmd>
            <cmd>no ip vrf %s</cmd>
        </cli-config-data>
</config>
"""

CREATE_SUBINTERFACE = """
<config>
        <cli-config-data>
            <cmd>interface %s</cmd>
            <cmd>encapsulation dot1Q %s</cmd>
            <cmd>ip vrf forwarding %s</cmd>
            <cmd>ip address %s %s</cmd>
        </cli-config-data>
</config>
"""

REMOVE_SUBINTERFACE = """
<config>
        <cli-config-data>
            <cmd>no interface %s</cmd>
        </cli-config-data>
</config>
"""


def csr_connect(host, port, user, password):
    return manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           device_params={'name': "csr"},
                           timeout=30
            )


def create_vrf(conn, vrf_name):
    try:
        confstr = CREATE_VRF % vrf_name
        rpc_obj = conn.edit_config(target='running', config=confstr)
        _check_response(rpc_obj, "CREATE_VRF")
    except Exception:
        log.exception("Exception in creating VRF %s" % vrf_name)


def create_subinterface(conn, subinterface, vlan_id, vrf_name, ip, mask):
    try:
        confstr = CREATE_SUBINTERFACE % (subinterface, vlan_id,
                                         vrf_name, ip, mask)
        rpc_obj = conn.edit_config(target='running', config=confstr)
        _check_response(rpc_obj, 'CREATE_SUBINTERFACE')
    except Exception:
        log.exception("Exception in creating subinterface %s" % subinterface)


def remove_vrf(conn, vrf_name):
    try:
        confstr = REMOVE_VRF % vrf_name
        rpc_obj = conn.edit_config(target='running', config=confstr)
        _check_response(rpc_obj, "REMOVE_VRF")
    except Exception:
        log.exception("Exception in removing VRF %s" % vrf_name)


def remove_subinterface(conn, subinterface):
    try:
        confstr = REMOVE_SUBINTERFACE % (subinterface)
        rpc_obj = conn.edit_config(target='running', config=confstr)
        _check_response(rpc_obj, 'REMOVE_SUBINTERFACE')
    except Exception:
        log.exception("Exception in removing subinterface %s" % subinterface)


def _check_response(rpc_obj, snippet_name):
    log.debug("RPCReply for %s is %s" % (snippet_name, rpc_obj.xml))
    xml_str = rpc_obj.xml
    if "<ok />" in xml_str:
        log.info("%s successful" % snippet_name)
    else:
        log.error("Cannot successfully execute: %s" % snippet_name)


def test_csr(host, user, password):
    with csr_connect(host, port=22, user=user, password=password) as m:
        create_vrf(m, "test_vrf")
        create_subinterface(m, "GigabitEthernet 1.500",
                            '500', 'test_vrf',
                            '192.168.0.1', '255.255.255.0')
        #Optional
        remove_vrf(m, "test_vrf")
        remove_subinterface(m, "GigabitEthernet 1.500")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test_csr(sys.argv[1], sys.argv[2], sys.argv[3])
