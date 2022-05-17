from ncclient import manager

m = manager.connect(
    host="10.128.207.132",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

yangModelsToCheck = [
    "Cisco-IOS-XE-voice",
    "Cisco-IOS-XE-cdp",
    "Cisco-IOS-XE-bgp",
    "Cisco-IOS-XE-crypto",
    "Cisco-IOS-XE-eigrp",
    "Cisco-IOS-XE-tunnel",
    "Test-Control",
]

print("# Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    supportedYangModel = capability.split('?')[-1].split("&")[0].split('=')[-1]
    if supportedYangModel in yangModelsToCheck:
        print("\t-", supportedYangModel)
