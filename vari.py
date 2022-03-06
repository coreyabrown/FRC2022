from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import tbapy

def setapikey():
    global apikey
    apikey = 'fWFSAeNa3VxZUdVJhaXgAXjnM9mfLBmbw1bbOrviglJBtJxmcUTANIMpECdWSSwU'
    return apikey

tba = tbapy.TBA(setapikey())
year = 2022
red = "red"
blue = "blue"
teamKeys = "team_keys"