
# This file was generated by 'versioneer.py' (0.18) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

import json

version_json = '''
{
 "date": "2020-03-26T07:45:30-0400",
 "dirty": false,
 "error": null,
 "full-revisionid": "e132d81b6efb86665093cf2be2f501277ad84fc2",
 "version": "v0.4.4"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
