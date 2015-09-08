import ceph.ceph_rest_client.client as client
import ceph.ceph_rest_client.exceptions as exceptions


class CephWrapper(client.CephClient):

    def __init__(self, **params):

        super(CephWrapper, self).__init__(**params)
        self.user_agent = 'python-cephclient-wrapper'

    ###
    # Cluster GET calls
    ###
    def df(self, **kwargs):
        return self.get('cluster/df/', **kwargs)

    def fsid(self, **kwargs):
        return self.get('cluster/fsid/', **kwargs)

    def health(self, **kwargs):
        return self.get('cluster/health/', **kwargs)

    def status(self, **kwargs):
        return self.get('cluster/status/', **kwargs)

    def fs(self, **kwargs):
        return self.get('cluster/fs/', **kwargs)

    def performance(self, **kwargs):
        return self.get('cluster/performance/', **kwargs)

    ###
    # root PUT calls
    ###
    def compact(self, **kwargs):
        return self.put('compact', **kwargs)

    def heap(self, heapcmd, **kwargs):
        return self.put('heap?heapcmd={0}'
                        .format(heapcmd), **kwargs)







