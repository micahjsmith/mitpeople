# mitpeople

Simple python client for the [MIT People API](https://developer.mit.edu/api-people).

Full API documentation is available
[here](https://anypoint.mulesoft.com/exchange/portals/mit-5/9ddddac0-4fef-400a-8144-7b537fc0e936/mit-people/1.0.0/console/summary/).

Don't need programmatic access? Then just use the online [MIT People Directory](http://web.mit.edu/people.html) (some additional limitations present).

## usage

Create a `config.ini` file. Credentials are requested directly from the API service. Note
that some endpoints may be restricted; in particular, unless you believe otherwise, you will
only have access to the `people` and `person` endpoints.

``` ini
[credentials]
client_id = abcetc
client_secret = abcetc
```

### python library usage

Create a client object:

``` python
from mitpeople import Client
client = Client()
```

Try to fetch a result:

``` python
>>> from mitpeople import Client
>>> client = Client()
>>> client.person('micahs')
{'item': {'kerberosId': 'micahs', 'givenName': 'Micah', 'familyName': 'Smith', 'middleName': None, 'displayName': 'Micah Jacob Smith', 'email': 'micahs@mit.edu', 'phoneNumber': None, 'website': None, 'affiliations': [{'type': 'student', 'classYear': 'G', 'departments': [{'code': '6', 'name': 'Electrical Eng & Computer Sci'}], 'courses': [{'departmentCode': '6', 'courseOption': 'D', 'name': 'Electrical Engineering and Computer Science'}]}]}}
```

### CLI usage

Alternatively, use the command-line interface (requires `pip install fire`):

``` shell
$ ./mitpeople.py -- --help
Type:           Client
File:           mitpeople.py
Init docstring: MIT People API client object

Args:
    client_id (str)
    client_secret (str)

Usage:          mitpeople.py 
                mitpeople.py faculty
                mitpeople.py graduateStudents
                mitpeople.py people
                mitpeople.py person
                mitpeople.py postdocs
                mitpeople.py staff
                mitpeople.py students
                mitpeople.py undergraduateStudents
```

Example:
``` shell
$ ./mitpeople.py person micahs
item: {"kerberosId": "micahs", "givenName": "Micah", "familyName": "Smith", "middleName": null, "displayName": "Micah Jacob Smith", "email": "micahs@mit.edu", "phoneNumber": null, "website": null, "affiliations": [{"type": "student", "classYear": "G", "departments": [{"code": "6", "name": "Electrical Eng & Computer Sci"}], "courses": [{"departmentCode": "6", "courseOption": "D", "name": "Electrical Engineering and Computer Science"}]}]}
```

## notes

see also
- http://kb.mit.edu/confluence/pages/viewpage.action?pageId=3907064#HowdoIadministeranAthena%28Moira%29listorgroup%3F-listmaint
- https://debathena.mit.edu/manpages/www/manpages/hardy/man8/mrtest.8.html
- https://stuff.mit.edu/afs/sipb/project/doc/guide/guide/node26.html
- https://github.com/mit-athena/moira/blob/736a7c2a1f43346a67dbdd11970961f44254c5be/doc/queries.tex
