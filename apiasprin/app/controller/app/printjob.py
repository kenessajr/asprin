from ...model.models import User
import arrow
from ..pdfalgo.size import humansize


def printJobBusiness(json_jobs):
    data = {'storage':0,'percentage':0,'PrintJob':[]}
    storage = 0
    for item in json_jobs:
        user = User.query.get(item['user_id'])
        storage += int(item['size'])
        item['names'] = user.names
        item['size'] = humansize(item['size'])
        date = arrow.get(item['regDate'])
        item['regDate'] = date.to('Africa/Kigali').humanize()
        data['PrintJob'].append(item)
        item['price'] = int(float(item['price']))
        item['tot_price'] = item['price'] + int(round(item['taxes'],0)) + int(round(item['commission'],0))



    data['storage']= humansize(round(storage))
    data['percentage'] = round(((float(data['storage'].split(" ")[0]) * 100)/1000),2)
    return data