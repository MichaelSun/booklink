
# Create your models here.
#class Poll(models.Model):
#    question = models.CharField(max_length=200)
#    name = models.CharField(max_length=200)

import sae.storage

accessKey = 'jy32j2mj4n'
secretKey = '0ilmw2ll5l5kh3m212y45x3hwiykmxxij42myh4m'

def try_save_file(domain, filename, data):
    if domain != None:
        s = sae.storage.Client(accesskey=accessKey, secretkey=secretKey)
        if s != None:
            domains = s.list_domain()
            if domains != None and domain in domains:
                ob = sae.storage.Object(data)
                url = s.put(domain, filename, ob)
                return url
    return None


def try_get_data(domain, filename):
    if domain != None:
        s = sae.storage.Client(accesskey=accessKey, secretkey=secretKey)
        if s != None:
            obj = s.get(domain, filename)
            if obj != None:
                return obj.data

    return None

def try_list_file(domain):
    if domain != None:
        s = sae.storage.Client(accesskey=accessKey, secretkey=secretKey)
        if s != None:
            return s.list(domain)

    return None



def listDomain():
    s = sae.storage.Client(accesskey=accessKey, secretkey=secretKey)
    return s.list_domain()


